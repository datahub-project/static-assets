#!/usr/bin/env python3
"""
Add lineage for the fiction-retail dataset in DataHub.

Run AFTER ingestion:
    datahub ingest -c ingest.yaml
    python add_lineage.py

Supports: --dry-run

This dataset has no ETL pipeline stages. Lineage here reflects the natural
data relationships in a retail operation — which tables depend on which
reference/dimension tables to be meaningful. For example, order_items is only
interpretable in combination with orders and products; shipments depend on
orders and warehouses.
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

DATAHUB_SERVER = "http://localhost:8080"
PLATFORM = "sqlite"
DEFAULT_INSTANCE = "fiction-retail"

# Lineage: downstream → [upstreams]
# Reflects which tables a given table draws meaning from (FK dependencies).
TABLE_LINEAGE = {
    # orders reference customers and promotions
    "orders": ["customers", "promotions"],
    # order_items are line items that join orders and products
    "order_items": ["orders", "products"],
    # products are supplied by suppliers
    "products": ["suppliers"],
    # inventory tracks product stock levels per warehouse
    "inventory": ["products", "warehouses"],
    # shipments fulfil orders and ship from a warehouse
    "shipments": ["orders", "warehouses"],
    # returns reference a completed order and the specific product returned
    "returns": ["orders", "products"],
}


def discover_urns(graph, platform_instance):
    query = f"""
    {{ search(input: {{type: DATASET, query: "{platform_instance}", start: 0, count: 100}}) {{
        searchResults {{ entity {{ urn ... on Dataset {{ name platform {{ name }} }} }} }}
    }} }}
    """
    result = graph.execute_graphql(query)
    urn_map = {}
    for item in result.get("search", {}).get("searchResults", []):
        entity = item.get("entity", {})
        if entity.get("platform", {}).get("name", "") != PLATFORM:
            continue
        if f",{platform_instance}." not in entity.get("urn", ""):
            continue
        name = entity.get("name", "")
        simple = name.split(".")[-1] if "." in name else name
        urn_map[simple] = entity["urn"]
    return urn_map


def emit_lineage(emitter, urn_map, dry_run=False):
    count = 0
    for downstream, upstream_names in TABLE_LINEAGE.items():
        if downstream not in urn_map:
            print(f"    ✗ {downstream}: not found in DataHub (run ingestion first)")
            continue

        upstreams = [urn_map[t] for t in upstream_names if t in urn_map]
        missing = [t for t in upstream_names if t not in urn_map]
        if missing:
            print(f"    ⚠ {downstream}: upstream(s) not found — {', '.join(missing)}")
        if not upstreams:
            continue

        if dry_run:
            print(f"    → {downstream} ← {', '.join(upstream_names)}")
            count += 1
            continue

        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=urn_map[downstream],
            aspect=UpstreamLineageClass(
                upstreams=[
                    UpstreamClass(dataset=u, type=DatasetLineageTypeClass.TRANSFORMED)
                    for u in upstreams
                ]
            ),
        ))
        print(f"    ✓ {downstream} ← {', '.join(upstream_names)}")
        count += 1

    return count


def main():
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg == "--help":
            print("Usage: python add_lineage.py [--dry-run]")
            return
        else:
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")
    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)

    print(f"\n  Instance: {DEFAULT_INSTANCE}")
    urn_map = discover_urns(graph, DEFAULT_INSTANCE)
    if not urn_map:
        print("  No datasets found — run ingestion first.")
        sys.exit(1)

    print(f"  Found {len(urn_map)} datasets: {', '.join(sorted(urn_map))}")
    count = emit_lineage(emitter, urn_map, dry_run=dry_run)

    print(f"\n{'='*50}")
    if dry_run:
        print(f"DRY RUN — {count} lineage edges would be created")
    else:
        print(f"✅ Lineage added: {count} relationships")
        print(f"   customers → orders → order_items")
        print(f"   products  → order_items, inventory, returns")
        print(f"   suppliers → products")
        print(f"   warehouses → inventory, shipments")
        print(f"   promotions → orders")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
