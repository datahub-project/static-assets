#!/usr/bin/env python3
"""
Add lineage relationships between pipeline stages in DataHub.

Run AFTER ingestion:
    datahub ingest -c ingest.yaml
    python add_lineage.py

For other variants:
    python add_lineage.py --instance=nyc_taxi_pipeline
    python add_lineage.py --all
    python add_lineage.py --dry-run

Auto-discovers actual URNs from DataHub — no hardcoded URNs.
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
DEFAULT_INSTANCE = "nyc_taxi"
VALID_INSTANCES = ["nyc_taxi", "nyc_taxi_pipeline"]

# Pipeline lineage: downstream → [upstream tables]
# Both view lineage AND table-to-table lineage

VIEW_LINEAGE = {
    "v_staging_from_raw": ["raw_trips"],
    "v_daily_from_staging": ["staging_trips"],
}

TABLE_LINEAGE = {
    "staging_trips": ["raw_trips"],
    "mart_daily_summary": ["staging_trips"],
}


def discover_urns(graph, platform_instance):
    """Auto-discover dataset URNs from DataHub."""
    query = f"""
    {{
        search(
            input: {{
                type: DATASET,
                query: "{platform_instance}",
                start: 0,
                count: 100
            }}
        ) {{
            searchResults {{
                entity {{
                    urn
                    ... on Dataset {{
                        name
                        platform {{ name }}
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
        if entity.get("platform", {}).get("name", "") != PLATFORM:
            continue
        if platform_instance not in urn:
            continue
        simple_name = name.split(".")[-1] if "." in name else name
        urn_map[simple_name] = urn
    return urn_map


def emit_lineage(emitter, urn_map, dry_run=False):
    """Emit lineage using discovered URNs."""
    count = 0
    all_lineage = {**VIEW_LINEAGE, **TABLE_LINEAGE}

    for downstream, upstream_names in all_lineage.items():
        if downstream not in urn_map:
            print(f"    ✗ {downstream}: not found (skipped)")
            continue

        upstreams = []
        for t in upstream_names:
            if t in urn_map:
                upstreams.append(urn_map[t])
            else:
                print(f"    ⚠ {t} not found")

        if not upstreams:
            continue

        if dry_run:
            print(f"    → {downstream} ← {', '.join(upstream_names)}")
            count += 1
            continue

        mcp = MetadataChangeProposalWrapper(
            entityUrn=urn_map[downstream],
            aspect=UpstreamLineageClass(
                upstreams=[
                    UpstreamClass(dataset=u, type=DatasetLineageTypeClass.TRANSFORMED)
                    for u in upstreams
                ]
            ),
        )
        emitter.emit(mcp)
        print(f"    ✓ {downstream} ← {', '.join(upstream_names)}")
        count += 1

    return count


def main():
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
            print(f"Usage: python add_lineage.py [--instance=X] [--all] [--dry-run]")
            print(f"  Instances: {', '.join(VALID_INSTANCES)}")
            return
        elif arg.startswith("--"):
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    for inst in instances:
        if inst not in VALID_INSTANCES:
            print(f"Unknown instance: {inst}")
            sys.exit(1)

    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")
    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)
    total = 0

    for instance in instances:
        print(f"\n  Instance: {instance}")
        urn_map = discover_urns(graph, instance)
        if not urn_map:
            print(f"    No datasets found (skipped)")
            continue
        print(f"    Found {len(urn_map)} datasets")
        total += emit_lineage(emitter, urn_map, dry_run=dry_run)

    print(f"\n{'='*50}")
    if dry_run:
        print(f"DRY RUN — {total} lineage edges would be created")
    else:
        print(f"✅ Lineage added: {total} relationships")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()