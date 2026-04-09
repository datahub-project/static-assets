#!/usr/bin/env python3
"""
Add lineage relationships between tables and views in DataHub.

Run AFTER ingestion:
    1. datahub ingest -c ingest_source.yaml
    2. python add_lineage.py

For other variants:
    python add_lineage.py --instance=olist_dirty
    python add_lineage.py --instance=olist_warehouse
    python add_lineage.py --instance=olist_analytics
    python add_lineage.py --dry-run

Why this script exists:
    DataHub's view lineage parser generates URNs that don't match the
    ingested table URNs (different path format). This script auto-discovers
    the actual URNs from DataHub and emits lineage using the correct format.

Prerequisites:
    pip install 'acryl-datahub[datahub-rest]'
    DataHub running at http://localhost:8080
    Tables already ingested via ingest_*.yaml
"""

import sys

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DatahubClientConfig
from datahub.metadata.schema_classes import (
    DatasetLineageTypeClass,
    UpstreamClass,
    UpstreamLineageClass,
)

# ─── Configuration ───
DATAHUB_SERVER = "http://localhost:8080"
PLATFORM = "sqlite"
DEFAULT_INSTANCE = "olist_source"
VALID_INSTANCES = ["olist_source", "olist_dirty", "olist_warehouse", "olist_analytics"]


# ─── Lineage definitions ───
# Map of: view_name → [upstream_table_names]
# These match the views created in create_db.py

VIEW_LINEAGE = {
    "v_order_details": [
        "olist_orders",
        "olist_customers",
        "olist_order_items",
    ],
    "v_order_payments": [
        "olist_orders",
        "olist_order_payments",
    ],
    "v_order_reviews": [
        "olist_orders",
        "olist_order_reviews",
    ],
    "v_seller_performance": [
        "olist_order_items",
        "olist_sellers",
        "olist_products",
        "olist_order_reviews",
    ],
    "v_product_sales": [
        "olist_order_items",
        "olist_products",
        "product_category_name_translation",
    ],
}


def discover_urns(graph: DataHubGraph, platform_instance: str) -> dict:
    """Auto-discover actual dataset URNs from DataHub.

    Queries DataHub for all datasets in the given platform instance
    and builds a name → URN lookup table.

    Returns:
        dict: {"olist_orders": "urn:li:dataset:(...)", "v_order_details": "urn:li:dataset:(...)", ...}
    """
    query = f"""
    {{
        search(
            input: {{
                type: DATASET,
                query: "{platform_instance}",
                start: 0,
                count: 200
            }}
        ) {{
            searchResults {{
                entity {{
                    urn
                    ... on Dataset {{
                        name
                        platform {{
                            name
                        }}
                    }}
                }}
            }}
        }}
    }}
    """

    result = graph.execute_graphql(query)
    urn_map = {}

    for item in result.get("search", {}).get("searchResults", []):
        entity = item.get("entity", {})
        urn = entity.get("urn", "")
        name = entity.get("name", "")

        # Only include datasets from our platform
        platform_name = entity.get("platform", {}).get("name", "")
        if platform_name != PLATFORM:
            continue

        # Only include datasets from our platform instance
        if platform_instance not in urn:
            continue

        # Extract the simple table/view name from the full qualified name
        # Name could be like "olist_source.olist.db.main.olist_orders"
        # We want just "olist_orders"
        simple_name = name.split(".")[-1] if "." in name else name
        urn_map[simple_name] = urn

    return urn_map


def emit_lineage(emitter: DatahubRestEmitter, urn_map: dict, dry_run: bool = False) -> int:
    """Emit lineage relationships using discovered URNs."""
    count = 0

    for view_name, upstream_names in VIEW_LINEAGE.items():
        # Find the view URN
        if view_name not in urn_map:
            print(f"  ✗ {view_name}: not found in DataHub (skipped)")
            continue

        view_urn = urn_map[view_name]

        # Find upstream URNs
        upstreams = []
        missing = []
        for table_name in upstream_names:
            if table_name in urn_map:
                upstreams.append(urn_map[table_name])
            else:
                missing.append(table_name)

        if missing:
            print(f"  ⚠ {view_name}: missing upstream(s): {', '.join(missing)}")

        if not upstreams:
            print(f"  ✗ {view_name}: no upstreams found (skipped)")
            continue

        if dry_run:
            print(f"  → {view_name}")
            print(f"    URN: {view_urn}")
            for u_name, u_urn in zip(upstream_names, upstreams):
                print(f"    ← {u_name}: {u_urn}")
            count += 1
            continue

        # Emit lineage
        lineage = UpstreamLineageClass(
            upstreams=[
                UpstreamClass(
                    dataset=upstream_urn,
                    type=DatasetLineageTypeClass.TRANSFORMED,
                )
                for upstream_urn in upstreams
            ]
        )

        mcp = MetadataChangeProposalWrapper(
            entityUrn=view_urn,
            aspect=lineage,
        )
        emitter.emit(mcp)
        print(f"  ✓ {view_name} ← {', '.join(upstream_names)}")
        count += 1

    return count


def main():
    # Parse arguments
    instance = DEFAULT_INSTANCE
    instances = [DEFAULT_INSTANCE]
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg == "--all":
            instances = list(VALID_INSTANCES)
        elif arg.startswith("--instance="):
            instances = [arg.split("=", 1)[1]]
        elif arg == "--help":
            print("Usage: python add_lineage.py [--instance=INSTANCE] [--all] [--dry-run]")
            print(f"  --instance=X   Target one instance (default: {DEFAULT_INSTANCE})")
            print(f"  --all          Target all instances: {', '.join(VALID_INSTANCES)}")
            print(f"  --dry-run      Preview without emitting")
            return
        elif arg.startswith("--"):
            print(f"Unknown flag: {arg}")
            print(f"Usage: python add_lineage.py [--instance=INSTANCE] [--all] [--dry-run]")
            sys.exit(1)

    for instance in instances:
        if instance not in VALID_INSTANCES:
            print(f"Unknown instance: {instance}")
            print(f"Valid: {', '.join(VALID_INSTANCES)}")
            sys.exit(1)

    # Connect to DataHub
    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")

    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        print(f"  Make sure DataHub is running: curl {DATAHUB_SERVER}/config")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)
    total_count = 0

    for instance in instances:
        print(f"\n{'='*60}")
        print(f"Instance: {instance}")
        print(f"{'='*60}")

        # Discover actual URNs
        print(f"  Discovering datasets...")
        urn_map = discover_urns(graph, instance)

        if not urn_map:
            print(f"  ✗ No datasets found for '{instance}' (skipped)")
            continue

        print(f"  Found {len(urn_map)} datasets")

        # Emit lineage
        action = "DRY RUN — would add" if dry_run else "Adding"
        print(f"  {action} lineage...")

        count = emit_lineage(emitter, urn_map, dry_run=dry_run)
        total_count += count

    print(f"\n{'='*60}")
    if dry_run:
        print(f"DRY RUN complete — {total_count} lineage edges would be created")
    else:
        print(f"✅ Lineage added: {total_count} view→table relationships")
        print(f"   Check DataHub UI → click any view → Lineage tab")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()