# DataHub Sample Datasets

Pre-built SQLite databases with realistic schemas, lineage, and metadata — ready for ingestion into DataHub.

Each dataset simulates a real-world data pipeline with tables, views (for lineage), tags, glossary terms, and ownership. Some include deliberately planted data quality issues for testing monitoring, auditing, and automation workflows.

---

## Available Datasets

| Dataset | What It Simulates | Pipeline Shape | .db Files | Size |
|---|---|---|---|---|
| [olist-ecommerce](./olist-ecommerce/) | Multi-table e-commerce with join relationships | 9 tables + 5 cross-table join views | `olist.db` (clean) + `olist_dirty.db` (broken joins) | ~90MB each |
| [nyc-taxi](./nyc-taxi/) | 3-stage data pipeline with freshness tracking | raw → staging → mart (linear) | `nyc_taxi.db` + `nyc_taxi_pipeline.db` | ~85MB each |
| [healthcare](./healthcare/) | Forking pipeline with data quality issues | raw → staging → billing + demographics (fork) | `healthcare.db` (quality issues planted) | ~2MB |

### When to Use What

**Testing join validation, schema matching, or cross-source discovery?**
→ Use **olist-ecommerce** (`olist_dirty.db`). 8 interconnected tables with planted orphan keys, ID format mismatches, and NULL categories. Also includes clean + warehouse + analytics variants for reconciliation testing.

**Testing freshness monitoring, staleness detection, or pipeline health?**
→ Use **nyc-taxi** (`nyc_taxi.db` + generate `nyc_taxi_pipeline.db`). A 3-stage pipeline where staging silently falls 3 days behind raw. Invisible in metadata — only detectable by querying actual timestamps.

**Testing quality monitoring, circuit breaking, or selective pipeline halting?**
→ Use **healthcare** (`healthcare.db`). A forking pipeline where bad data in the source (negative billing, invalid ages) propagates to two downstream marts with different severity. The challenge: halt billing but let demographics continue.

**Testing data reconciliation or cross-system consistency?**
→ Use **olist-ecommerce** (`olist.db` + `olist_warehouse.db` + `olist_analytics.db`). Same source data in three "systems" — each with different drift. Warehouse has missing rows and precision loss. Analytics has daily rollups with inflated counts and missing days.

**Building something else entirely?**
→ Any of the above. Each dataset is a complete, realistic data environment. Pick the one whose schema and pipeline shape best fits your idea.

---

## Quick Start

```bash
# Prerequisites
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
# DataHub running locally: https://datahubproject.io/docs/quickstart

# Pick a dataset and run 3 commands
cd datasets/healthcare                    # (or olist-ecommerce, nyc-taxi)
datahub ingest -c ingest.yaml             # load tables + views into DataHub
python add_lineage.py                      # connect the pipeline stages
python add_metadata.py                     # add tags, glossary, ownership
```

---

## What's in Each Dataset

### olist-ecommerce

Brazilian e-commerce data from [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 100k orders across 9 interconnected tables (orders, customers, products, sellers, payments, reviews, geolocation).

**Committed .db files:**
- `olist.db` — Clean source of truth. All joins match 100%.
- `olist_dirty.db` — ~8% orphan customers, ~5% seller ID mismatches, ~3% NULL categories.

**Generated via `create_db.py` (not committed):**
- `olist_warehouse.db` — Same table structure with ETL drift: dropped rows, duplicated records, precision loss.
- `olist_analytics.db` — Different structure: daily rollup tables with inflated counts, freight reduction, missing days.

**Metadata:** Tags (pii, identifier, financial), glossary (order_status, customer_identity), ownership (logistics, finance, customer experience, product, platform teams).

### nyc-taxi

NYC Yellow Taxi trip records from the [NYC TLC](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) — ~500k trips loaded as a 3-stage pipeline.

**Committed .db files:**
- `nyc_taxi.db` — Clean pipeline: raw_trips → staging_trips → mart_daily_summary. All stages in sync.

**Generated via `create_db.py --pipeline-from-existing` (not committed):**
- `nyc_taxi_pipeline.db` — Same pipeline with planted staleness: staging/mart are 3 days behind raw, plus one "empty load" day where the pipeline ran but loaded 0 rows.

**Metadata:** Tags (daily_refresh, time_series, pii, pipeline_stage), glossary (freshness_sla, empty_load, pipeline_stage), ownership (data_platform_team).

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
├── olist-ecommerce/
│   ├── README.md
│   ├── create_db.py
│   ├── olist.db                     ← committed
│   ├── olist_dirty.db               ← committed
│   ├── ingest_source.yaml
│   ├── ingest_dirty.yaml
│   ├── ingest_warehouse.yaml
│   ├── ingest_analytics.yaml
│   ├── add_lineage.py
│   └── add_metadata.py
├── nyc-taxi/
│   ├── README.md
│   ├── create_db.py
│   ├── nyc_taxi.db                  ← committed
│   ├── ingest.yaml
│   ├── ingest_pipeline.yaml
│   ├── add_lineage.py
│   └── add_metadata.py
└── healthcare/
    ├── README.md
    ├── create_db.py
    ├── healthcare.db                ← committed
    ├── ingest.yaml
    ├── add_lineage.py
    └── add_metadata.py
```

---

## Data Sources & Licenses

These datasets are derived from publicly available sources. DataHub does not own or claim ownership of any underlying data.

| Dataset | Original Source | License |
|---|---|---|
| Brazilian E-Commerce (Olist) | [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — Olist / André Sionek | CC BY-NC-SA 4.0 |
| NYC Taxi Trip Records | [Kaggle](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) — NYC TLC | Public Domain |
| Healthcare Dataset | [Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) — Prasad22 | CC0 1.0 (Public Domain) |

### What We Modified

Original CSV data is loaded as-is into the base tables. The following additions are ours:

- **SQL views** — for DataHub lineage visualization
- **Pipeline stages** — staging and mart tables computed from raw data
- **Planted issues** — data quality problems, staleness gaps, and cross-copy drift (documented in each dataset's README)
- **Metadata scripts** — tags, glossary terms, ownership emitted via DataHub SDK

---

## Prerequisites

```bash
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
```

DataHub must be running locally. See [DataHub Quickstart](https://datahubproject.io/docs/quickstart).