#!/usr/bin/env python3
"""
Add lineage for the healthcare forking pipeline in DataHub.

Run AFTER ingestion:
    datahub ingest -c ingest.yaml
    python add_lineage.py

Supports: --dry-run

The pipeline forks: raw → staging → billing mart + demographics mart
Both table-to-table and view-to-table lineage are emitted.
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
DEFAULT_INSTANCE = "healthcare"
VALID_INSTANCES = ["healthcare"]

# View lineage
VIEW_LINEAGE = {
    "v_staging_from_raw": ["raw_patients"],
    "v_billing_from_staging": ["staging_patients"],
    "v_demographics_from_staging": ["staging_patients"],
}

# Table-to-table lineage (the forking pipeline)
TABLE_LINEAGE = {
    "staging_patients": ["raw_patients"],
    "mart_billing": ["staging_patients"],
    "mart_demographics": ["staging_patients"],
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
    all_lineage = {**VIEW_LINEAGE, **TABLE_LINEAGE}

    for downstream, upstream_names in all_lineage.items():
        if downstream not in urn_map:
            print(f"    ✗ {downstream}: not found (skipped)")
            continue

        upstreams = [urn_map[t] for t in upstream_names if t in urn_map]
        if not upstreams:
            continue

        if dry_run:
            print(f"    → {downstream} ← {', '.join(upstream_names)}")
            count += 1
            continue

        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=urn_map[downstream],
            aspect=UpstreamLineageClass(
                upstreams=[UpstreamClass(dataset=u, type=DatasetLineageTypeClass.TRANSFORMED) for u in upstreams]
            ),
        ))
        print(f"    ✓ {downstream} ← {', '.join(upstream_names)}")
        count += 1

    return count


def main():
    instance = DEFAULT_INSTANCE
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg == "--help":
            print(f"Usage: python add_lineage.py [--dry-run]")
            return
        elif arg.startswith("--"):
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")
    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)

    print(f"\n  Instance: {instance}")
    urn_map = discover_urns(graph, instance)
    if not urn_map:
        print(f"    No datasets found (run ingestion first)")
        sys.exit(1)

    print(f"    Found {len(urn_map)} datasets")
    count = emit_lineage(emitter, urn_map, dry_run=dry_run)

    print(f"\n{'='*50}")
    if dry_run:
        print(f"DRY RUN — {count} lineage edges would be created")
    else:
        print(f"✅ Lineage added: {count} relationships")
        print(f"   Pipeline: raw_patients → staging_patients → mart_billing + mart_demographics")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()