#!/usr/bin/env python3
"""
Add metadata (tags, glossary terms, ownership) to NYC Taxi dataset in DataHub.

Run AFTER ingestion + lineage:
    datahub ingest -c ingest.yaml
    python add_lineage.py
    python add_metadata.py

Supports: --instance=nyc_taxi_pipeline, --all, --dry-run
"""

import sys
import time

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DatahubClientConfig
from datahub.metadata.schema_classes import (
    AuditStampClass,
    GlobalTagsClass,
    GlossaryTermAssociationClass,
    GlossaryTermInfoClass,
    GlossaryTermsClass,
    OwnerClass,
    OwnershipClass,
    OwnershipTypeClass,
    TagAssociationClass,
    TagPropertiesClass,
)

DATAHUB_SERVER = "http://localhost:8080"
PLATFORM = "sqlite"
DEFAULT_INSTANCE = "nyc_taxi"
VALID_INSTANCES = ["nyc_taxi", "nyc_taxi_pipeline"]


# ─── Tag definitions ───
TAG_DEFINITIONS = {
    "daily_refresh": {
        "description": "Table expected to receive new data daily. Staleness beyond 24 hours indicates a pipeline issue.",
    },
    "time_series": {
        "description": "Contains timestamped records forming a time series. Each row has a specific date/time.",
    },
    "pii": {
        "description": "Contains personally identifiable information (pickup/dropoff locations).",
    },
    "pipeline_stage": {
        "description": "Part of a multi-stage data pipeline (raw → staging → mart).",
    },
}

TAG_ASSIGNMENTS = {
    "daily_refresh": ["raw_trips", "staging_trips", "mart_daily_summary"],
    "time_series": ["raw_trips", "staging_trips"],
    "pii": ["raw_trips", "staging_trips"],
    "pipeline_stage": ["raw_trips", "staging_trips", "mart_daily_summary"],
}


# ─── Glossary terms ───
GLOSSARY_DEFINITIONS = {
    "freshness_sla": {
        "name": "Freshness SLA",
        "definition": "Expected update frequency for a table. A table is stale when MAX(timestamp) falls behind the expected refresh cadence. For daily tables, data more than 24 hours old violates the SLA.",
    },
    "empty_load": {
        "name": "Empty Load",
        "definition": "A pipeline execution that completes successfully but loads zero new rows. The pipeline status shows 'success' and the table timestamp updates, but MAX(data_date) doesn't change. Undetectable from pipeline metadata alone.",
    },
    "pipeline_stage": {
        "name": "Pipeline Stage",
        "definition": "A step in a multi-stage data pipeline. Raw data is ingested, staging cleans and filters, mart aggregates for consumption. Each stage depends on its upstream — staleness propagates downstream.",
    },
}

GLOSSARY_ASSIGNMENTS = {
    "freshness_sla": ["raw_trips", "staging_trips", "mart_daily_summary"],
    "empty_load": ["mart_daily_summary"],
    "pipeline_stage": ["raw_trips", "staging_trips", "mart_daily_summary"],
}


# ─── Ownership ───
OWNERSHIP_ASSIGNMENTS = {
    "data_platform_team": ["raw_trips", "staging_trips", "mart_daily_summary"],
}


# ─── URN discovery ───
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
        if platform_instance not in entity.get("urn", ""):
            continue
        name = entity.get("name", "")
        simple = name.split(".")[-1] if "." in name else name
        urn_map[simple] = entity["urn"]
    return urn_map


# ─── Emission ───
def create_tags(emitter):
    for name, info in TAG_DEFINITIONS.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=f"urn:li:tag:{name}",
            aspect=TagPropertiesClass(name=name, description=info["description"]),
        ))
        print(f"    ✓ Created tag: {name}")


def attach_tags(emitter, urn_map):
    count = 0
    for tag, tables in TAG_ASSIGNMENTS.items():
        for t in tables:
            if t not in urn_map:
                continue
            emitter.emit(MetadataChangeProposalWrapper(
                entityUrn=urn_map[t],
                aspect=GlobalTagsClass(tags=[TagAssociationClass(tag=f"urn:li:tag:{tag}")]),
            ))
            print(f"    ✓ tag:{tag} → {t}")
            count += 1
    return count


def create_glossary(emitter):
    for key, info in GLOSSARY_DEFINITIONS.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=f"urn:li:glossaryTerm:{key}",
            aspect=GlossaryTermInfoClass(
                name=info["name"], definition=info["definition"], termSource="INTERNAL",
            ),
        ))
        print(f"    ✓ Created term: {info['name']}")


def attach_glossary(emitter, urn_map):
    now_ms = int(time.time() * 1000)
    count = 0
    for key, tables in GLOSSARY_ASSIGNMENTS.items():
        for t in tables:
            if t not in urn_map:
                continue
            emitter.emit(MetadataChangeProposalWrapper(
                entityUrn=urn_map[t],
                aspect=GlossaryTermsClass(
                    terms=[GlossaryTermAssociationClass(urn=f"urn:li:glossaryTerm:{key}")],
                    auditStamp=AuditStampClass(time=now_ms, actor="urn:li:corpuser:datahub"),
                ),
            ))
            print(f"    ✓ glossary:{key} → {t}")
            count += 1
    return count


def emit_ownership(emitter, urn_map):
    count = 0
    for owner, tables in OWNERSHIP_ASSIGNMENTS.items():
        for t in tables:
            if t not in urn_map:
                continue
            emitter.emit(MetadataChangeProposalWrapper(
                entityUrn=urn_map[t],
                aspect=OwnershipClass(owners=[
                    OwnerClass(owner=f"urn:li:corpGroup:{owner}", type=OwnershipTypeClass.DATAOWNER)
                ]),
            ))
            print(f"    ✓ owner:{owner} → {t}")
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
            print(f"Usage: python add_metadata.py [--instance=X] [--all] [--dry-run]")
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

    if not dry_run:
        print(f"\n  Creating tags...")
        create_tags(emitter)
        print(f"\n  Creating glossary terms...")
        create_glossary(emitter)

    for instance in instances:
        print(f"\n{'='*50}")
        print(f"  Instance: {instance}")
        print(f"{'='*50}")

        urn_map = discover_urns(graph, instance)
        if not urn_map:
            print(f"    No datasets found (skipped)")
            continue

        print(f"    Found {len(urn_map)} datasets")

        if dry_run:
            for name in sorted(urn_map.keys()):
                print(f"      {name}: {urn_map[name]}")
            continue

        print(f"\n    Attaching tags...")
        attach_tags(emitter, urn_map)
        print(f"\n    Attaching glossary terms...")
        attach_glossary(emitter, urn_map)
        print(f"\n    Adding ownership...")
        emit_ownership(emitter, urn_map)

    print(f"\n{'='*50}")
    print(f"✅ Metadata complete")
    print(f"   Glossary: DataHub UI → Govern → Glossary")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()