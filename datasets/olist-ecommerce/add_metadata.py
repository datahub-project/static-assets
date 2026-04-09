#!/usr/bin/env python3
"""
Add metadata (tags, glossary terms, ownership) to Olist dataset in DataHub.

Run AFTER ingestion + lineage:
    1. datahub ingest -c ingest_source.yaml
    2. python add_lineage.py
    3. python add_metadata.py

For other variants:
    python add_metadata.py --instance=olist_dirty
    python add_metadata.py --instance=olist_warehouse
    python add_metadata.py --instance=olist_analytics
    python add_metadata.py --dry-run

Prerequisites:
    pip install 'acryl-datahub[datahub-rest]'
    DataHub running at http://localhost:8080

What this adds:
    - Tags: pii, identifier, financial (created + attached)
    - Glossary terms: order_status, customer_identity (created with definitions + attached)
    - Ownership: logistics_team, finance_team, customer_experience_team, product_team
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

# ─── Configuration ───
DATAHUB_SERVER = "http://localhost:8080"
PLATFORM = "sqlite"
DEFAULT_INSTANCE = "olist_source"
VALID_INSTANCES = ["olist_source", "olist_dirty", "olist_warehouse", "olist_analytics"]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Tag definitions (created + attached)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TAG_DEFINITIONS = {
    "pii": {
        "description": "Contains personally identifiable information (names, locations, coordinates, free text)",
    },
    "identifier": {
        "description": "Contains primary or foreign key columns used for joining tables",
    },
    "financial": {
        "description": "Contains monetary values (prices, payments, freight costs)",
    },
}

TAG_ASSIGNMENTS = {
    "pii": [
        "olist_customers",
        "olist_geolocation",
        "olist_order_reviews",
    ],
    "identifier": [
        "olist_customers",
        "olist_orders",
        "olist_order_items",
        "olist_products",
        "olist_sellers",
    ],
    "financial": [
        "olist_order_payments",
        "olist_order_items",
    ],
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Glossary term definitions (created + attached)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 1: Terms are CREATED with name + definition in DataHub
# Step 2: Terms are ATTACHED to specific datasets
# Without Step 1, you get empty ghost terms with no description.

GLOSSARY_DEFINITIONS = {
    "order_status": {
        "name": "Order Status",
        "definition": "Lifecycle state of an order. Values: created, approved, invoiced, processing, shipped, delivered, unavailable, canceled. Critical for filtering and reporting.",
    },
    "customer_identity": {
        "name": "Customer Identity",
        "definition": "Olist uses two customer IDs. customer_id is unique per order (changes each purchase). customer_unique_id is stable across orders (the real person). Joining on the wrong one produces incorrect results.",
    },
}

GLOSSARY_ASSIGNMENTS = {
    "order_status": [
        "olist_orders",
    ],
    "customer_identity": [
        "olist_customers",
    ],
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Ownership assignments
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OWNERSHIP_ASSIGNMENTS = {
    "logistics_team": [
        "olist_sellers",
        "olist_geolocation",
        "olist_order_items",
    ],
    "finance_team": [
        "olist_order_payments",
    ],
    "customer_experience_team": [
        "olist_order_reviews",
        "olist_customers",
    ],
    "product_team": [
        "olist_products",
        "product_category_name_translation",
    ],
    "data_platform_team": [
        "olist_orders",
    ],
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# URN auto-discovery (same approach as add_lineage.py)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def discover_urns(graph: DataHubGraph, platform_instance: str) -> dict:
    """Auto-discover dataset URNs from DataHub. Returns {simple_name: urn}."""
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
        platform_name = entity.get("platform", {}).get("name", "")

        if platform_name != PLATFORM:
            continue
        if platform_instance not in urn:
            continue

        simple_name = name.split(".")[-1] if "." in name else name
        urn_map[simple_name] = urn

    return urn_map


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Emission functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def create_tags(emitter: DatahubRestEmitter) -> int:
    """Create tag entities with descriptions."""
    count = 0
    for tag_name, info in TAG_DEFINITIONS.items():
        tag_urn = f"urn:li:tag:{tag_name}"
        mcp = MetadataChangeProposalWrapper(
            entityUrn=tag_urn,
            aspect=TagPropertiesClass(
                name=tag_name,
                description=info["description"],
            ),
        )
        emitter.emit(mcp)
        print(f"  ✓ Created tag: {tag_name}")
        count += 1
    return count


def attach_tags(emitter: DatahubRestEmitter, urn_map: dict) -> int:
    """Attach tags to datasets. Collects ALL tags per table, emits once."""
    table_tags = {}
    for tag_name, tables in TAG_ASSIGNMENTS.items():
        for table in tables:
            if table not in urn_map:
                continue
            if table not in table_tags:
                table_tags[table] = []
            table_tags[table].append(f"urn:li:tag:{tag_name}")

    count = 0
    for table, tag_urns in table_tags.items():
        mcp = MetadataChangeProposalWrapper(
            entityUrn=urn_map[table],
            aspect=GlobalTagsClass(
                tags=[TagAssociationClass(tag=u) for u in tag_urns]
            ),
        )
        emitter.emit(mcp)
        tag_names = [u.split(":")[-1] for u in tag_urns]
        print(f"    ✓ {table} ← tags: {', '.join(tag_names)}")
        count += 1
    return count


def create_glossary_terms(emitter: DatahubRestEmitter) -> int:
    """Create glossary term entities with names and definitions.

    This is the step the old version had that we were missing.
    Without this, terms exist as empty entities with no description.
    """
    count = 0
    for term_key, info in GLOSSARY_DEFINITIONS.items():
        term_urn = f"urn:li:glossaryTerm:{term_key}"
        mcp = MetadataChangeProposalWrapper(
            entityUrn=term_urn,
            aspect=GlossaryTermInfoClass(
                name=info["name"],
                definition=info["definition"],
                termSource="INTERNAL",
            ),
        )
        emitter.emit(mcp)
        print(f"  ✓ Created glossary term: {info['name']}")
        count += 1
    return count


def attach_glossary_terms(emitter: DatahubRestEmitter, urn_map: dict) -> int:
    """Attach glossary terms to datasets. Collects ALL terms per table, emits once."""
    now_ms = int(time.time() * 1000)
    table_terms = {}
    for term_key, tables in GLOSSARY_ASSIGNMENTS.items():
        for table in tables:
            if table not in urn_map:
                continue
            if table not in table_terms:
                table_terms[table] = []
            table_terms[table].append(f"urn:li:glossaryTerm:{term_key}")

    count = 0
    for table, term_urns in table_terms.items():
        mcp = MetadataChangeProposalWrapper(
            entityUrn=urn_map[table],
            aspect=GlossaryTermsClass(
                terms=[GlossaryTermAssociationClass(urn=u) for u in term_urns],
                auditStamp=AuditStampClass(
                    time=now_ms,
                    actor="urn:li:corpuser:datahub",
                ),
            ),
        )
        emitter.emit(mcp)
        term_names = [u.split(":")[-1] for u in term_urns]
        print(f"    ✓ {table} ← terms: {', '.join(term_names)}")
        count += 1
    return count


def emit_ownership(emitter: DatahubRestEmitter, urn_map: dict) -> int:
    """Add ownership to datasets."""
    count = 0
    for owner_name, tables in OWNERSHIP_ASSIGNMENTS.items():
        owner_urn = f"urn:li:corpGroup:{owner_name}"
        for table in tables:
            if table not in urn_map:
                print(f"  ⚠ {table} not found in DataHub (skipped)")
                continue
            mcp = MetadataChangeProposalWrapper(
                entityUrn=urn_map[table],
                aspect=OwnershipClass(
                    owners=[
                        OwnerClass(
                            owner=owner_urn,
                            type=OwnershipTypeClass.DATAOWNER,
                        )
                    ]
                ),
            )
            emitter.emit(mcp)
            print(f"  ✓ owner:{owner_name} → {table}")
            count += 1
    return count


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def main():
    # Parse arguments
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
            print("Usage: python add_metadata.py [--instance=INSTANCE] [--all] [--dry-run]")
            print(f"  --instance=X   Target one instance (default: {DEFAULT_INSTANCE})")
            print(f"  --all          Target all instances: {', '.join(VALID_INSTANCES)}")
            print(f"  --dry-run      Preview URNs without emitting")
            return
        elif arg.startswith("--"):
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    for inst in instances:
        if inst not in VALID_INSTANCES:
            print(f"Unknown instance: {inst}")
            print(f"Valid: {', '.join(VALID_INSTANCES)}")
            sys.exit(1)

    # Connect
    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")

    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)

    # Step 1: Create tags and glossary terms (only once, shared across instances)
    if not dry_run:
        print(f"\nCreating tags...")
        create_tags(emitter)

        print(f"\nCreating glossary terms...")
        create_glossary_terms(emitter)

    # Step 2: For each instance, discover URNs and attach metadata
    for instance in instances:
        print(f"\n{'='*60}")
        print(f"Instance: {instance}")
        print(f"{'='*60}")

        urn_map = discover_urns(graph, instance)

        if not urn_map:
            print(f"  ✗ No datasets found for '{instance}' (skipped)")
            continue

        print(f"  Found {len(urn_map)} datasets")

        if dry_run:
            print(f"\n  DRY RUN — URNs that would be used:")
            for name in sorted(urn_map.keys()):
                print(f"    {name}: {urn_map[name]}")
            continue

        print(f"\n  Attaching tags...")
        tag_count = attach_tags(emitter, urn_map)

        print(f"\n  Attaching glossary terms...")
        glossary_count = attach_glossary_terms(emitter, urn_map)

        print(f"\n  Adding ownership...")
        ownership_count = emit_ownership(emitter, urn_map)

        print(f"\n  Done: {tag_count} tags, {glossary_count} glossary, {ownership_count} ownership")

    print(f"\n{'='*60}")
    print(f"✅ Metadata complete")
    print(f"   View tags/owners: click any dataset")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()