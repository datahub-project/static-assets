#!/usr/bin/env python3
"""
Add metadata (tags, glossary terms, ownership) to the fiction-retail dataset in DataHub.

Run AFTER ingestion + lineage:
    datahub ingest -c ingest.yaml
    python add_lineage.py
    python add_metadata.py

Supports: --dry-run
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
DEFAULT_INSTANCE = "fiction-retail"

# ─── Tags ───────────────────────────────────────────────────────────────────

TAG_DEFINITIONS = {
    "pii": {
        "description": "Contains personally identifiable information (customer names, emails, phone numbers, location data).",
    },
    "financial": {
        "description": "Contains monetary values (order totals, unit prices, discounts, refunds). Treat with appropriate access controls.",
    },
    "transactional": {
        "description": "Records individual business transactions (orders, purchases, shipments, returns). High row volume, append-heavy.",
    },
    "reference_data": {
        "description": "Slowly changing lookup data (products, suppliers, warehouses, promotions). Low row count, read-heavy.",
    },
}

TAG_ASSIGNMENTS = {
    "pii": ["customers"],
    "financial": ["orders", "order_items", "returns"],
    "transactional": ["orders", "order_items", "shipments", "returns"],
    "reference_data": ["products", "suppliers", "warehouses", "promotions"],
}

# ─── Glossary ────────────────────────────────────────────────────────────────

GLOSSARY_DEFINITIONS = {
    "order_status": {
        "name": "Order Status",
        "definition": "Lifecycle state of an order. Typical values: Pending, Processing, Shipped, Delivered, Cancelled, Returned. Used to filter active vs completed vs failed orders in reporting.",
    },
    "customer_segment": {
        "name": "Customer Segment",
        "definition": "Classification of a customer by purchasing behaviour or account type (e.g. Retail, Wholesale, VIP). Used to personalise pricing, promotions, and reporting cohorts.",
    },
    "discount_pct": {
        "name": "Discount Percentage",
        "definition": "Percentage reduction applied to a line item's unit price at time of purchase. Ranges from 0.0 (no discount) to 1.0 (100% off). Used to calculate net revenue and measure promotional effectiveness.",
    },
    "reorder_threshold": {
        "name": "Reorder Threshold",
        "definition": "The quantity_on_hand level at which a restock should be triggered for a given product in a given warehouse. When quantity_on_hand drops at or below this value, a purchase order should be raised.",
    },
    "return_reason_code": {
        "name": "Return Reason Code",
        "definition": "Standardised code describing why a product was returned (e.g. Defective, Wrong Item, Changed Mind, Damaged in Transit). Used to categorise return volume and identify quality or fulfilment issues.",
    },
    "shipment_state": {
        "name": "Shipment State",
        "definition": "Current status of a shipment in the carrier's pipeline (e.g. Label Created, In Transit, Out for Delivery, Delivered, Failed). Distinct from order_status — an order can be Delivered while its shipment shows a carrier exception.",
    },
}

GLOSSARY_ASSIGNMENTS = {
    "order_status": ["orders"],
    "customer_segment": ["customers"],
    "discount_pct": ["order_items"],
    "reorder_threshold": ["inventory"],
    "return_reason_code": ["returns"],
    "shipment_state": ["shipments"],
}

# ─── Ownership ───────────────────────────────────────────────────────────────

OWNERSHIP_ASSIGNMENTS = {
    "customer_team": ["customers"],
    "commerce_team": ["orders", "order_items"],
    "catalog_team": ["products", "suppliers"],
    "logistics_team": ["shipments", "warehouses", "inventory"],
    "marketing_team": ["promotions"],
    "finance_team": ["returns"],
}


# ─── URN discovery ───────────────────────────────────────────────────────────

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


# ─── Emission (batch pattern: collect all per table, emit once) ───────────────

def create_tags(emitter):
    for name, info in TAG_DEFINITIONS.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=f"urn:li:tag:{name}",
            aspect=TagPropertiesClass(name=name, description=info["description"]),
        ))
        print(f"    ✓ Created tag: {name}")


def attach_tags(emitter, urn_map):
    table_tags = {}
    for tag, tables in TAG_ASSIGNMENTS.items():
        for t in tables:
            if t not in urn_map:
                continue
            table_tags.setdefault(t, []).append(f"urn:li:tag:{tag}")

    count = 0
    for table, tag_urns in table_tags.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=urn_map[table],
            aspect=GlobalTagsClass(tags=[TagAssociationClass(tag=u) for u in tag_urns]),
        ))
        names = [u.split(":")[-1] for u in tag_urns]
        print(f"    ✓ {table} ← tags: {', '.join(names)}")
        count += 1
    return count


def create_glossary(emitter):
    for key, info in GLOSSARY_DEFINITIONS.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=f"urn:li:glossaryTerm:{key}",
            aspect=GlossaryTermInfoClass(
                name=info["name"],
                definition=info["definition"],
                termSource="INTERNAL",
            ),
        ))
        print(f"    ✓ Created term: {info['name']}")


def attach_glossary(emitter, urn_map):
    now_ms = int(time.time() * 1000)
    table_terms = {}
    for key, tables in GLOSSARY_ASSIGNMENTS.items():
        for t in tables:
            if t not in urn_map:
                continue
            table_terms.setdefault(t, []).append(f"urn:li:glossaryTerm:{key}")

    count = 0
    for table, term_urns in table_terms.items():
        emitter.emit(MetadataChangeProposalWrapper(
            entityUrn=urn_map[table],
            aspect=GlossaryTermsClass(
                terms=[GlossaryTermAssociationClass(urn=u) for u in term_urns],
                auditStamp=AuditStampClass(time=now_ms, actor="urn:li:corpuser:datahub"),
            ),
        ))
        names = [u.split(":")[-1] for u in term_urns]
        print(f"    ✓ {table} ← terms: {', '.join(names)}")
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
                    OwnerClass(
                        owner=f"urn:li:corpGroup:{owner}",
                        type=OwnershipTypeClass.DATAOWNER,
                    )
                ]),
            ))
            print(f"    ✓ owner:{owner} → {t}")
            count += 1
    return count


def main():
    dry_run = "--dry-run" in sys.argv

    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")
    try:
        graph = DataHubGraph(DatahubClientConfig(server=DATAHUB_SERVER))
    except Exception as e:
        print(f"  ✗ Cannot connect: {e}")
        sys.exit(1)

    emitter = DatahubRestEmitter(DATAHUB_SERVER)

    urn_map = discover_urns(graph, DEFAULT_INSTANCE)
    if not urn_map:
        print(f"  No datasets found for '{DEFAULT_INSTANCE}'. Run ingestion first.")
        sys.exit(1)

    print(f"  Found {len(urn_map)} datasets: {', '.join(sorted(urn_map))}")

    if dry_run:
        print("\n  Tags to create:", list(TAG_DEFINITIONS))
        print("  Glossary terms to create:", [v["name"] for v in GLOSSARY_DEFINITIONS.values()])
        print("  Owners:", list(OWNERSHIP_ASSIGNMENTS))
        return

    print(f"\n  Creating tags...")
    create_tags(emitter)
    print(f"\n  Creating glossary terms...")
    create_glossary(emitter)

    print(f"\n  Attaching tags...")
    attach_tags(emitter, urn_map)
    print(f"\n  Attaching glossary terms...")
    attach_glossary(emitter, urn_map)
    print(f"\n  Adding ownership...")
    emit_ownership(emitter, urn_map)

    print(f"\n{'='*50}")
    print(f"✅ Metadata complete")
    print(f"   Tags: pii, financial, transactional, reference_data")
    print(f"   Glossary: Order Status, Customer Segment, Discount Percentage,")
    print(f"             Reorder Threshold, Return Reason Code, Shipment State")
    print(f"   Owners: customer_team, commerce_team, catalog_team,")
    print(f"           logistics_team, marketing_team, finance_team")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
