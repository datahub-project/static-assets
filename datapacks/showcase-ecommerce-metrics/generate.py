"""Build showcase-ecommerce-metrics MCPs.

Regenerate 01-data.json (from a DataHub checkout with the metrics SDK)::

    /path/to/datahub-fork/metadata-ingestion/venv/bin/python generate.py \\
        --output 01-data.json

Physical tables, Looker charts, and the Order Entry dashboard come from
showcase-ecommerce / showcase-ecommerce-databricks. This overlay adds semantic
models, metrics, column lineage, and ``upstreamMetrics`` on those consumers.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List

from datahub.emitter.mce_builder import make_data_platform_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.ingestion.sink.file import write_metadata_file
from datahub.metadata.schema_classes import (
    AiContextClass,
    AuditStampClass,
    DataPlatformInstanceClass,
    DatasetPropertiesClass,
    DerivedMetricInputClass,
    DialectClass,
    DialectExpressionClass,
    EdgeClass,
    ERModelRelationshipCardinalityClass,
    MetricExpressionClass,
    MetricInfoClass,
    MetricRelationshipsClass,
    MetricUpstreamsClass,
    SemanticFieldTypeClass,
    StatusClass,
    UpstreamMetricsClass,
)
from datahub.metadata.urns import MetricUrn, SchemaFieldUrn
from datahub.sdk import (
    AiContextInput,
    Dataset,
    DialectExpressionInput,
    Metric,
    SemanticFieldInput,
    SemanticModel,
    SemanticModelDataset,
    SemanticModelRelationshipInput,
)
from datahub.sdk.entity import Entity

ECOMMERCE_DOMAIN = "urn:li:domain:b2fd91.d4f24004-fb54-4e3c-8dea-2b7e209230b0"
ACTOR = "urn:li:corpuser:datahub"
# Fixed so regenerating 01-data.json does not churn audit stamps.
NOW_MS = 1770000000000
STAMP = AuditStampClass(time=NOW_MS, actor=ACTOR)
SAMPLE_METADATA = {"properties": {"sampleData": "true"}}

SF_ORDERS = "urn:li:dataset:(urn:li:dataPlatform:snowflake,b2fd91.order_entry_db.order_entry.orders,PROD)"
SF_CUSTOMERS = "urn:li:dataset:(urn:li:dataPlatform:snowflake,b2fd91.order_entry_db.order_entry.customers,PROD)"
SF_PROMOTIONS = "urn:li:dataset:(urn:li:dataPlatform:snowflake,b2fd91.order_entry_db.order_entry.promotions,PROD)"
DBX_ORDER_ITEMS = "urn:li:dataset:(urn:li:dataPlatform:databricks,order_entry_db.order_entry.order_items,PROD)"

CHART_ORDERS_BY_DAY = "urn:li:chart:(looker,b2fd91.dashboard_elements.224)"
CHART_PROMOTIONS = "urn:li:chart:(looker,b2fd91.dashboard_elements.222)"
DASH_ORDER_ENTRY = "urn:li:dashboard:(looker,b2fd91.dashboards.53)"


def dim(path: str, typ: str = "varchar", **kw) -> SemanticFieldInput:
    return SemanticFieldInput(
        field_path=path, type=typ, semantic_type=SemanticFieldTypeClass.DIMENSION, **kw
    )


def measure(path: str, agg: str, typ: str = "number", **kw) -> SemanticFieldInput:
    return SemanticFieldInput(
        field_path=path,
        type=typ,
        semantic_type=SemanticFieldTypeClass.MEASURE,
        aggregation_function=agg,
        **kw,
    )


def upstream_metrics_mcp(entity_urn: str, metric_urns: List[str]) -> MetadataChangeProposalWrapper:
    return MetadataChangeProposalWrapper(
        entityUrn=entity_urn,
        aspect=UpstreamMetricsClass(
            metrics=[EdgeClass(destinationUrn=u, created=STAMP, lastModified=STAMP) for u in metric_urns]
        ),
    )


def standalone_metric(
    *,
    platform: str,
    path: str,
    metric_id: str,
    name: str,
    description: str,
    expression: str,
    dialect: str,
    dataset_upstreams: List[str],
    field_upstreams: List[str] | None = None,
    derived_from: List[str] | None = None,
    synonyms: List[str] | None = None,
    domain: str | None = None,
) -> List[MetadataChangeProposalWrapper]:
    urn = MetricUrn(platform=platform, path=path, id=metric_id).urn()
    mcps: List[MetadataChangeProposalWrapper] = [
        MetadataChangeProposalWrapper(entityUrn=urn, aspect=StatusClass(removed=False)),
        MetadataChangeProposalWrapper(
            entityUrn=urn,
            aspect=DataPlatformInstanceClass(platform=make_data_platform_urn(platform)),
        ),
        MetadataChangeProposalWrapper(
            entityUrn=urn,
            aspect=MetricInfoClass(
                name=name,
                description=description,
                created=STAMP,
                lastModified=STAMP,
                expression=MetricExpressionClass(
                    dialects=[DialectExpressionClass(dialect=dialect, expression=expression)]
                ),
            ),
        ),
        MetadataChangeProposalWrapper(
            entityUrn=urn,
            aspect=MetricRelationshipsClass(
                derivedFrom=[DerivedMetricInputClass(destinationUrn=d) for d in (derived_from or [])]
            ),
        ),
        MetadataChangeProposalWrapper(
            entityUrn=urn,
            aspect=MetricUpstreamsClass(
                datasetUpstreams=[EdgeClass(destinationUrn=d) for d in dataset_upstreams],
                fieldUpstreams=[EdgeClass(destinationUrn=f) for f in (field_upstreams or [])],
            ),
        ),
    ]
    if synonyms:
        mcps.append(
            MetadataChangeProposalWrapper(entityUrn=urn, aspect=AiContextClass(synonyms=synonyms))
        )
    if domain:
        from datahub.metadata.schema_classes import DomainsClass

        mcps.append(MetadataChangeProposalWrapper(entityUrn=urn, aspect=DomainsClass(domains=[domain])))
    return mcps


def build() -> tuple[List[Entity], List[MetadataChangeProposalWrapper]]:
    entities: List[Entity] = []
    mcps: List[MetadataChangeProposalWrapper] = []

    # ------------------------------------------------------------------ Sales Model (Snowflake)
    sales_model = SemanticModel(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="sales_model",
        name="Sales Model",
        description="Semantic model over showcase order_entry orders and customers.",
        native_definition=(
            "CREATE SEMANTIC VIEW order_entry_db.analytics.sales_model\n"
            "  TABLES (orders PRIMARY KEY (order_id), customers PRIMARY KEY (customer_id))\n"
            "  RELATIONSHIPS (orders(customer_id) REFERENCES customers)\n"
            "  METRICS (orders.total_order_revenue AS SUM(order_total));"
        ),
        ai_context=AiContextInput(
            synonyms=["sales", "orders model"],
            instructions="Use for order revenue, volume, and customer count questions.",
        ),
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    sales_orders = SemanticModelDataset(
        platform="snowflake",
        name="b2fd91.order_entry_db.analytics.sales_model.orders",
        semantic_model=sales_model.urn,
        alias="ORDERS",
        description="Logical orders view of the Sales Model.",
        extra_aspects=[DatasetPropertiesClass(name="orders (Sales Model)")],
        schema=[
            dim("order_id", "number", is_part_of_key=True),
            dim("customer_id", "number"),
            dim("order_date", "timestamp", is_time_dimension=True),
            dim("order_status"),
            measure(
                "order_total",
                "SUM",
                expression=DialectExpressionInput(
                    expression="SUM(order_total)", dialect=DialectClass.SNOWFLAKE
                ),
                ai_context=AiContextInput(synonyms=["revenue"]),
            ),
        ],
        upstreams={
            SF_ORDERS: {
                "order_id": ["order_id"],
                "customer_id": ["customer_id"],
                "order_date": ["order_date"],
                "order_status": ["order_status"],
                "order_total": ["order_total"],
            }
        },
        domain=ECOMMERCE_DOMAIN,
    )
    sales_customers = SemanticModelDataset(
        platform="snowflake",
        name="b2fd91.order_entry_db.analytics.sales_model.customers",
        semantic_model=sales_model.urn,
        alias="CUSTOMERS",
        description="Logical customers view of the Sales Model.",
        extra_aspects=[DatasetPropertiesClass(name="customers (Sales Model)")],
        schema=[
            dim("customer_id", "number", is_part_of_key=True),
            dim("cust_first_name"),
            dim("cust_last_name"),
            dim("customer_class"),
        ],
        upstreams={
            SF_CUSTOMERS: {
                "customer_id": ["customer_id"],
                "cust_first_name": ["cust_first_name"],
                "cust_last_name": ["cust_last_name"],
                "customer_class": ["customer_class"],
            }
        },
        domain=ECOMMERCE_DOMAIN,
    )
    sales_model.set_datasets([sales_orders, sales_customers])
    sales_model.set_relationships(
        [
            SemanticModelRelationshipInput(
                from_alias="ORDERS",
                from_columns=["customer_id"],
                to_alias="CUSTOMERS",
                to_columns=["customer_id"],
                name="orders_to_customers",
                cardinality=ERModelRelationshipCardinalityClass.N_ONE,
            )
        ]
    )

    total_order_revenue = Metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="total_order_revenue",
        semantic_model=sales_model.urn,
        name="Total Order Revenue",
        description="Sum of order_total across showcase orders.",
        expression=DialectExpressionInput(
            expression="SUM(ORDERS.order_total)", dialect=DialectClass.SNOWFLAKE
        ),
        upstream_datasets=[sales_orders.urn],
        ai_context=AiContextInput(synonyms=["revenue", "order total"]),
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    total_order_revenue._ensure_metric_upstreams().fieldUpstreams = [
        EdgeClass(destinationUrn=SchemaFieldUrn(str(sales_orders.urn), "order_total").urn())
    ]
    order_count = Metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="order_count",
        semantic_model=sales_model.urn,
        name="Order Count",
        description="Number of distinct orders.",
        expression=DialectExpressionInput(
            expression="COUNT(DISTINCT ORDERS.order_id)", dialect=DialectClass.SNOWFLAKE
        ),
        upstream_datasets=[sales_orders.urn],
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    customer_count = Metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="customer_count",
        semantic_model=sales_model.urn,
        name="Customer Count",
        description="Number of distinct customers.",
        expression=DialectExpressionInput(
            expression="COUNT(DISTINCT CUSTOMERS.customer_id)", dialect=DialectClass.SNOWFLAKE
        ),
        upstream_datasets=[sales_customers.urn],
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    average_order_value = Metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="average_order_value",
        semantic_model=sales_model.urn,
        name="Average Order Value",
        description="Total order revenue divided by order count.",
        expression="total_order_revenue / order_count",
        derived_from=[total_order_revenue.urn, order_count.urn],
        upstream_datasets=[sales_orders.urn],
        ai_context=AiContextInput(synonyms=["AOV"]),
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    revenue_per_customer = Metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.analytics",
        id="revenue_per_customer",
        semantic_model=sales_model.urn,
        name="Revenue per Customer",
        description="Total order revenue divided by customer count.",
        expression="total_order_revenue / customer_count",
        derived_from=[total_order_revenue.urn, customer_count.urn],
        upstream_datasets=[sales_orders.urn, sales_customers.urn],
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    entities += [
        sales_model,
        sales_orders,
        sales_customers,
        total_order_revenue,
        order_count,
        customer_count,
        average_order_value,
        revenue_per_customer,
    ]

    # ------------------------------------------------------------------ Line Items Model (Databricks)
    line_items_model = SemanticModel(
        platform="databricks",
        path="order_entry_db.analytics",
        id="line_items_model",
        name="Line Items Model",
        description="Semantic model over Databricks order_items.",
        ai_context=AiContextInput(synonyms=["line items", "order lines"]),
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    line_items_ds = SemanticModelDataset(
        platform="databricks",
        name="order_entry_db.analytics.line_items_model.order_items",
        semantic_model=line_items_model.urn,
        alias="ORDER_ITEMS",
        description="Logical order_items view of the Line Items Model.",
        extra_aspects=[DatasetPropertiesClass(name="order_items (Line Items Model)")],
        schema=[
            dim("order_id", "number", is_part_of_key=True),
            dim("line_item_id", "number", is_part_of_key=True),
            dim("product_id", "number"),
            measure("unit_price", "SUM"),
            measure("quantity", "SUM"),
        ],
        upstreams={
            DBX_ORDER_ITEMS: {
                "order_id": ["order_id"],
                "line_item_id": ["line_item_id"],
                "product_id": ["product_id"],
                "unit_price": ["unit_price"],
                "quantity": ["quantity"],
            }
        },
        domain=ECOMMERCE_DOMAIN,
    )
    line_items_model.set_datasets([line_items_ds])
    line_revenue = Metric(
        platform="databricks",
        path="order_entry_db.analytics",
        id="line_revenue",
        semantic_model=line_items_model.urn,
        name="Line Revenue",
        description="Sum of unit_price * quantity across Databricks order_items.",
        expression=DialectExpressionInput(
            expression="SUM(ORDER_ITEMS.unit_price * ORDER_ITEMS.quantity)",
            dialect=DialectClass.DATABRICKS,
        ),
        upstream_datasets=[line_items_ds.urn],
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    line_revenue._ensure_metric_upstreams().fieldUpstreams = [
        EdgeClass(destinationUrn=SchemaFieldUrn(str(line_items_ds.urn), "unit_price").urn()),
        EdgeClass(destinationUrn=SchemaFieldUrn(str(line_items_ds.urn), "quantity").urn()),
    ]
    units_sold = Metric(
        platform="databricks",
        path="order_entry_db.analytics",
        id="units_sold",
        semantic_model=line_items_model.urn,
        name="Units Sold",
        description="Sum of line-item quantities.",
        expression=DialectExpressionInput(
            expression="SUM(ORDER_ITEMS.quantity)", dialect=DialectClass.DATABRICKS
        ),
        upstream_datasets=[line_items_ds.urn],
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    entities += [line_items_model, line_items_ds, line_revenue, units_sold]

    # ------------------------------------------------------------------ Standalone metrics (PROMOTIONS, no SM)
    promo_spend_urn = MetricUrn(
        platform="snowflake", path="b2fd91.order_entry_db.standalone", id="promotion_spend"
    ).urn()
    active_promos_urn = MetricUrn(
        platform="snowflake", path="b2fd91.order_entry_db.standalone", id="active_promotions"
    ).urn()
    mcps += standalone_metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.standalone",
        metric_id="promotion_spend",
        name="Promotion Spend",
        description="Standalone metric (no semantic model). Sum of promotion_cost.",
        expression="SUM(promotion_cost)",
        dialect=DialectClass.SNOWFLAKE,
        dataset_upstreams=[SF_PROMOTIONS],
        field_upstreams=[SchemaFieldUrn(SF_PROMOTIONS, "promotion_cost").urn()],
        synonyms=["promo spend", "campaign cost"],
        domain=ECOMMERCE_DOMAIN,
    )
    mcps += standalone_metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.standalone",
        metric_id="active_promotions",
        name="Active Promotions",
        description="Standalone metric (no semantic model). Count of promotions.",
        expression="COUNT(*)",
        dialect=DialectClass.SNOWFLAKE,
        dataset_upstreams=[SF_PROMOTIONS],
        domain=ECOMMERCE_DOMAIN,
    )
    mcps += standalone_metric(
        platform="snowflake",
        path="b2fd91.order_entry_db.standalone",
        metric_id="promotion_cost_per_order",
        name="Promotion Cost per Order",
        description="Standalone derived metric. Promotion spend divided by order count.",
        expression="promotion_spend / order_count",
        dialect=DialectClass.SNOWFLAKE,
        dataset_upstreams=[SF_PROMOTIONS],
        derived_from=[promo_spend_urn, str(order_count.urn)],
        synonyms=["promo CAC"],
        domain=ECOMMERCE_DOMAIN,
    )

    # ------------------------------------------------------------------ New marts (dataset downstream)
    daily_order_kpis = Dataset(
        platform="snowflake",
        name="b2fd91.order_entry_db.analytics.daily_order_kpis",
        display_name="daily_order_kpis",
        description="Daily order KPIs consuming Sales Model metrics.",
        schema=[
            ("as_of_date", "date"),
            ("total_order_revenue", "number"),
            ("order_count", "number"),
            ("average_order_value", "number"),
        ],
        subtype="Table",
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    line_item_kpis = Dataset(
        platform="databricks",
        name="order_entry_db.analytics.line_item_kpis",
        display_name="line_item_kpis",
        description="Line-item KPIs consuming Line Items Model metrics.",
        schema=[("as_of_date", "date"), ("line_revenue", "number"), ("units_sold", "number")],
        subtype="Table",
        owners=[ACTOR],
        domain=ECOMMERCE_DOMAIN,
    )
    entities += [daily_order_kpis, line_item_kpis]
    mcps.append(
        upstream_metrics_mcp(
            str(daily_order_kpis.urn),
            [str(total_order_revenue.urn), str(order_count.urn), str(average_order_value.urn)],
        )
    )
    mcps.append(
        upstream_metrics_mcp(str(line_item_kpis.urn), [str(line_revenue.urn), str(units_sold.urn)])
    )

    # ------------------------------------------------------------------ Existing Looker consumers
    mcps.append(
        upstream_metrics_mcp(
            CHART_ORDERS_BY_DAY,
            [str(total_order_revenue.urn), str(order_count.urn)],
        )
    )
    mcps.append(upstream_metrics_mcp(CHART_PROMOTIONS, [promo_spend_urn, active_promos_urn]))
    mcps.append(
        upstream_metrics_mcp(
            DASH_ORDER_ENTRY,
            [str(total_order_revenue.urn), promo_spend_urn, str(line_revenue.urn)],
        )
    )

    return entities, mcps


def collect_mcps() -> List[MetadataChangeProposalWrapper]:
    entities, extra_mcps = build()
    all_mcps: List[MetadataChangeProposalWrapper] = []
    for entity in entities:
        all_mcps.extend(entity.as_mcps())
    all_mcps.extend(extra_mcps)
    return all_mcps


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(Path(__file__).resolve().parent / "01-data.json"),
        help="Write MCP JSON here (default: 01-data.json next to this script).",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    all_mcps = collect_mcps()
    print(f"Built {len(all_mcps)} MCPs")
    if args.dry_run:
        from collections import Counter

        counts = Counter((m.entityType, m.aspectName) for m in all_mcps)
        for key, count in sorted(counts.items()):
            print(f"  {key[0]:>14}.{key[1]:<28} {count}")
        return

    out = Path(args.output)
    write_metadata_file(out, all_mcps)
    records = json.loads(out.read_text())
    for record in records:
        record["systemMetadata"] = SAMPLE_METADATA
    out.write_text(json.dumps(records, indent=4) + "\n")
    print(f"Wrote {len(records)} MCPs to {out}")


if __name__ == "__main__":
    sys.exit(main())
