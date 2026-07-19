# DataHub Sample Datasets

Pre-built SQLite databases with realistic schemas, lineage, and metadata — ready for ingestion into DataHub.

Each dataset simulates a real-world data pipeline with tables, views (for lineage), tags, glossary terms, and ownership. Some include deliberately planted data quality issues for testing monitoring, auditing, and automation workflows.

---

## Available Datasets

| Dataset | What It Simulates | Pipeline Shape | .db Files | Size |
|---|---|---|---|---|
| [nyc-taxi](./nyc-taxi/) | 3-stage data pipeline with freshness tracking | raw → staging → mart (linear) | `nyc_taxi.db` + `nyc_taxi_pipeline.db` | ~85MB each |
| [healthcare](./healthcare/) | Forking pipeline with data quality issues | raw → staging → billing + demographics (fork) | `healthcare.db` (quality issues planted) | ~2MB |
| [fiction-retail](./fiction-retail/) | Synthetic global retail — orders, fulfillment, returns | 10 flat tables (no views) | `fiction-retail.db` | ~95MB |

### When to Use What

**Testing freshness monitoring, staleness detection, or pipeline health?**
→ Use **nyc-taxi** (`nyc_taxi.db` + generate `nyc_taxi_pipeline.db`). A 3-stage pipeline where staging silently falls 3 days behind raw. Invisible in metadata — only detectable by querying actual timestamps.

**Testing quality monitoring, circuit breaking, or selective pipeline halting?**
→ Use **healthcare** (`healthcare.db`). A forking pipeline where bad data in the source (negative billing, invalid ages) propagates to two downstream marts with different severity. The challenge: halt billing but let demographics continue.

**Exploring a flat, wide-table retail schema with no planted issues?**
→ Use **fiction-retail** (`fiction-retail.db`). 10 clean, interconnected tables covering customers, orders, products, suppliers, inventory, warehouses, shipments, returns, and promotions. Good baseline for schema exploration, join traversal, or building demos from scratch.

**Building something else entirely?**
→ Any of the above. Each dataset is a complete, realistic data environment. Pick the one whose schema and pipeline shape best fits your idea.

---

## Quick Start

```bash
# Prerequisites
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
# DataHub running locally: https://datahubproject.io/docs/quickstart

# Pick a dataset and run 3 commands
cd datasets/healthcare                    # (or nyc-taxi, fiction-retail)
datahub ingest -c ingest.yaml             # load tables + views into DataHub
python add_lineage.py                      # connect the pipeline stages
python add_metadata.py                     # add tags, glossary, ownership
```

---

## What's in Each Dataset

### nyc-taxi

NYC Yellow Taxi trip records from the [NYC TLC](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) — ~500k trips loaded as a 3-stage pipeline.

**Committed .db files:**
- `nyc_taxi.db` — Clean pipeline: raw_trips → staging_trips → mart_daily_summary. All stages in sync.

**Generated via `create_db.py --pipeline-from-existing` (not committed):**
- `nyc_taxi_pipeline.db` — Same pipeline with planted staleness: staging/mart are 3 days behind raw, plus one "empty load" day where the pipeline ran but loaded 0 rows.

**Metadata:** Tags (daily_refresh, time_series, pii, pipeline_stage), glossary (freshness_sla, empty_load, pipeline_stage), ownership (data_platform_team).

### fiction-retail

Fully synthetic global retail dataset — 10 interconnected tables covering the complete order lifecycle across 50k customers, 150k orders, 5k products, 500 suppliers, and 15 warehouses.

**Committed .db files:**
- `fiction-retail.db` — Single clean database. No planted issues. All foreign keys present in the data.

**No additional variants.** This dataset has no ETL pipeline stages or views — it's a flat analytical schema intended as a clean foundation.

**Key tables:** `customers`, `orders`, `order_items`, `products`, `suppliers`, `inventory`, `warehouses`, `shipments`, `returns`, `promotions`

**Metadata:** Tags (pii, financial, transactional, reference_data), glossary (order_status, customer_segment, discount_pct, reorder_threshold, return_reason_code, shipment_state), ownership (customer_team, commerce_team, catalog_team, logistics_team, marketing_team, finance_team).

**Source:** [Kaggle — Fiction Retail E-Commerce Dataset](https://www.kaggle.com/datasets/nasalakshay/fiction-retail-e-commerce-dataset) | License: CC0 1.0 (Public Domain)

### healthcare

Synthetic patient records from [Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) — ~55k records loaded as a forking pipeline with quality issues planted.

**Committed .db files:**
- `healthcare.db` — Forking pipeline: raw_patients → staging_patients → mart_billing + mart_demographics. Quality issues planted in raw propagate to both marts.

**No additional variants.** Quality issues are always present — they are the dataset's purpose.

**Planted issues:** ~2% negative billing, ~1% NULL names, ~1.5% invalid ages, ~0.5% admission-after-discharge date swaps.

**Metadata:** Tags (pii, critical, internal, quality_monitored, pipeline_stage), glossary (billing_amount, admission_date, length_of_stay), ownership (clinical_team, finance_team, research_team).

---

## How It Works

### Lineage via add_lineage.py

DataHub's SQLite connector has a known URN mismatch when parsing view definitions for lineage. All ingestion recipes set `include_view_lineage: false`, and each dataset includes an `add_lineage.py` script that auto-discovers actual URNs from DataHub's API and emits lineage with the correct format. Zero hardcoded URNs — works regardless of DataHub version or configuration.

### Metadata via add_metadata.py

Each dataset's `add_metadata.py` creates tags and glossary terms with full descriptions, then attaches them to datasets. All tags and glossary terms for a given table are collected first and emitted in a single API call (emitting one at a time would overwrite previous assignments).

### Pipeline Stages

Some datasets simulate multi-stage data pipelines by creating separate tables for each stage (raw, staging, mart) plus views that define the transformation logic. This gives DataHub both the table-to-table lineage (the pipeline flow) and the view definitions (how each transformation works).

---

## Repository Structure

```
datasets/
├── README.md                        ← You are here
├── .gitignore
├── nyc-taxi/
│   ├── README.md
│   ├── create_db.py
│   ├── nyc_taxi.db                  ← committed
│   ├── ingest.yaml
│   ├── ingest_pipeline.yaml
│   ├── add_lineage.py
│   └── add_metadata.py
├── healthcare/
│   ├── README.md
│   ├── create_db.py
│   ├── healthcare.db                ← committed
│   ├── ingest.yaml
│   ├── add_lineage.py
│   └── add_metadata.py
└── fiction-retail/
    ├── README.md
    ├── fiction-retail.db            ← committed
    ├── ingest.yaml
    ├── add_lineage.py
    └── add_metadata.py
```

---

## Data Sources & Licenses

These datasets are derived from publicly available sources. DataHub does not own or claim ownership of any underlying data.

| Dataset | Original Source | License |
|---|---|---|
| NYC Taxi Trip Records | [Kaggle](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) — NYC TLC | Public Domain |
| Healthcare Dataset | [Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) — Prasad22 | CC0 1.0 (Public Domain) |
| Fiction Retail | [Kaggle](https://www.kaggle.com/datasets/nasalakshay/fiction-retail-e-commerce-dataset) — nasalakshay | CC0 1.0 (Public Domain) |

### What We Modified

Original CSV data is loaded as-is into the base tables. The following additions are ours:

- **SQL views** — for DataHub lineage visualization
- **Pipeline stages** — staging and mart tables computed from raw data
- **Planted issues** — data quality problems and staleness gaps (documented in each dataset's README)
- **Metadata scripts** — tags, glossary terms, ownership emitted via DataHub SDK

---

## Prerequisites

```bash
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
```

DataHub must be running locally. See [DataHub Quickstart](https://datahubproject.io/docs/quickstart).