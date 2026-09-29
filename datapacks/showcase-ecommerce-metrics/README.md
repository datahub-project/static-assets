# showcase-ecommerce-metrics

Overlay pack: semantic models and metrics on top of the ecommerce catalogs.
Does not replace `showcase-ecommerce` or `showcase-ecommerce-databricks`.

**Requires:** DataHub Cloud >= 2.3.0 or DataHub OSS >= 1.7.0 (`metricsEnabled`).

## Load order

1. `showcase-ecommerce`
2. `showcase-ecommerce-databricks` (needed for Line Items Model / Databricks `order_items`)
3. this pack

Until this directory is on `static-assets` main, load by URL:

```bash
datahub datapack load showcase-ecommerce \
  --url https://raw.githubusercontent.com/datahub-project/static-assets/feat/showcase-ecommerce-add-databricks/datapacks/showcase-ecommerce/index.json \
  --trust-custom --no-time-shift
datahub datapack load showcase-ecommerce-databricks \
  --url https://raw.githubusercontent.com/datahub-project/static-assets/feat/showcase-ecommerce-add-databricks/datapacks/showcase-ecommerce-databricks/index.json \
  --trust-custom --no-time-shift
datahub datapack load showcase-ecommerce-metrics \
  --url https://raw.githubusercontent.com/datahub-project/static-assets/feat/showcase-ecommerce-metrics/datapacks/showcase-ecommerce-metrics/index.json \
  --trust-custom --no-time-shift
```

A Snowflake-only load still creates the Sales Model and standalone promotion metrics.
Line Revenue / Units Sold point at Databricks `order_items`; those edges stay dangling
until `showcase-ecommerce-databricks` is loaded.

Standalone metrics (no semantic model) do not appear in the default Metrics sidebar
tree. Use sidebar search or group by Platform.

## Contents

- **Sales Model** (Snowflake) over pack `ORDERS` / `CUSTOMERS`, with column lineage
- Metrics: Total Order Revenue, Order Count, Customer Count, Average Order Value, Revenue per Customer
- **Line Items Model** (Databricks) over pack `order_items`: Line Revenue, Units Sold
- **Standalone** (no semantic model): Promotion Spend, Active Promotions, Promotion Cost per Order
- Downstream `upstreamMetrics` on Looker Orders by Day, Promotions, and Order Entry Dashboard
- Marts: `daily_order_kpis` (Snowflake), `line_item_kpis` (Databricks)

## Regenerate `01-data.json`

Needs a DataHub checkout whose Python SDK includes `datahub.sdk.Metric` / `SemanticModel`:

```bash
/path/to/datahub-fork/metadata-ingestion/venv/bin/python generate.py --output 01-data.json
```
