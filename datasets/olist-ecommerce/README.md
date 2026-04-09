# Olist E-Commerce Dataset for DataHub

A ready-to-ingest SQLite dataset built from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 100k real orders across 9 interconnected tables covering orders, customers, products, sellers, payments, reviews, and geolocation.

This package provides pre-built SQLite databases, DataHub ingestion recipes, and scripts to add lineage, tags, glossary terms, and ownership — everything needed to explore DataHub's metadata capabilities with real-world data.

---

## What's Included

```
olist-ecommerce/
├── olist.db                  ← Clean database, all original data (committed)
├── olist_dirty.db            ← Same data + planted quality issues (committed)
├── create_db.py              ← Generates all .db variants from source CSVs
├── ingest_source.yaml        ← Ingests olist.db into DataHub
├── ingest_dirty.yaml         ← Ingests olist_dirty.db into DataHub
├── ingest_warehouse.yaml     ← Ingests olist_warehouse.db into DataHub
├── ingest_analytics.yaml     ← Ingests olist_analytics.db into DataHub
├── add_lineage.py            ← Adds view→table lineage (auto-discovers URNs)
├── add_metadata.py           ← Adds tags, glossary terms, ownership
└── README.md                 ← You are here
```

> **Note:** Only `olist.db` and `olist_dirty.db` are committed to this repo. The warehouse and analytics variants can be generated locally using `create_db.py` (see [Generate Additional Variants](#generate-additional-variants)).

---

## Quick Start

### Prerequisites

```bash
# DataHub running locally
# See: https://datahubproject.io/docs/quickstart

# Install the DataHub CLI with SQLAlchemy support
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
```

### 3 Commands to Get Started

```bash
# 1. Ingest tables + views into DataHub
datahub ingest -c ingest_source.yaml

# 2. Add lineage (view→table relationships)
python add_lineage.py

# 3. Add metadata (tags, glossary terms, ownership)
python add_metadata.py
```

Open DataHub at [http://localhost:9002](http://localhost:9002) and search for "olist" — you'll see 9 tables, 5 views, lineage edges, tags, glossary terms, and team ownership.

---

## What's in Each Database

### `olist.db` — Clean Base (Source of Truth)

The original Kaggle dataset loaded as-is into SQLite. All joins match 100%. No modifications to the data.

**9 tables:**

| Table | Rows | Description |
|---|---|---|
| `olist_customers` | 99,441 | Customer profiles — ID, unique ID, city, state, zip code |
| `olist_orders` | 99,441 | Orders — status, purchase/approval/delivery timestamps |
| `olist_order_items` | 112,650 | Line items — product, seller, price, freight per item |
| `olist_products` | 32,951 | Product catalog — category (Portuguese), dimensions, weight |
| `olist_sellers` | 3,095 | Seller profiles — ID, city, state, zip code |
| `olist_order_payments` | 103,886 | Payments — type (credit/boleto/voucher), installments, value |
| `olist_order_reviews` | 99,224 | Reviews — score (1–5), free-text title and comment |
| `olist_geolocation` | 1,000,163 | Zip code → latitude/longitude mapping (multiple per zip) |
| `product_category_name_translation` | 71 | Portuguese → English category name lookup |

**5 views (these create lineage in DataHub):**

| View | Upstream Tables | What It Joins |
|---|---|---|
| `v_order_details` | orders + customers + order_items | Full order context with customer location and line items |
| `v_order_payments` | orders + payments | Payment breakdown per order |
| `v_order_reviews` | orders + reviews | Customer satisfaction scores per order |
| `v_seller_performance` | order_items + sellers + products + reviews | Seller metrics with product categories and ratings |
| `v_product_sales` | order_items + products + category_translation | Product sales with English category names |

**Lineage graph:**

```
olist_customers ───────┐
olist_orders ──────────┼──→ v_order_details
olist_order_items ─────┤
                       ├──→ v_order_payments ←── olist_order_payments
                       └──→ v_order_reviews  ←── olist_order_reviews

olist_order_items ─────┐
olist_sellers ─────────┼──→ v_seller_performance ←── olist_order_reviews
olist_products ────────┘

olist_order_items ─────┐
olist_products ────────┼──→ v_product_sales
product_category_name  │
  _translation ────────┘

olist_geolocation ─── (standalone, no views reference it)
```

---

### `olist_dirty.db` — Planted Data Quality Issues

Identical structure to `olist.db` but with 3 deliberately introduced data quality problems. These simulate real-world issues commonly found in production data pipelines.

| Issue | What Was Done | Affected Rows | How to Detect |
|---|---|---|---|
| Orphan customers | ~8% of customers deleted from `olist_customers` | ~7,955 rows removed | `LEFT JOIN orders↔customers` produces NULLs where `INNER JOIN` drops rows |
| Seller ID mismatch | ~5% of `seller_id` values in `olist_order_items` truncated by 1 character | ~5,632 rows modified | Seller lookup against `olist_sellers` returns no match for truncated IDs |
| NULL categories | ~3% of `product_category_name` in `olist_products` set to NULL | ~988 rows modified | Category translation join returns NULL; `WHERE category IS NULL` finds them |

All planted issues use `random.seed(42)` for reproducibility — you get identical results every time.

---

## Ingestion Details

Each `.db` file ingests as a separate **platform instance** in DataHub. This means `olist_source.olist_orders` and `olist_dirty.olist_orders` appear as independent datasets — same table names, different sources.

| Recipe | Database | Platform Instance | Use Case |
|---|---|---|---|
| `ingest_source.yaml` | `olist.db` | `olist_source` | Clean data exploration, reconciliation baseline |
| `ingest_dirty.yaml` | `olist_dirty.db` | `olist_dirty` | Data quality testing, join validation |
| `ingest_warehouse.yaml` | `olist_warehouse.db` | `olist_warehouse` | Reconciliation (ETL drift) |
| `ingest_analytics.yaml` | `olist_analytics.db` | `olist_analytics` | Reconciliation (aggregation drift) |

### Ingest One Variant

```bash
datahub ingest -c ingest_source.yaml
python add_lineage.py
python add_metadata.py
```

### Ingest Multiple Variants

```bash
datahub ingest -c ingest_source.yaml
datahub ingest -c ingest_dirty.yaml

python add_lineage.py --all
python add_metadata.py --all
```

The `--all` flag loops through all 4 instances, skipping any that haven't been ingested. Always safe to use.

### Ingest a Specific Variant

```bash
datahub ingest -c ingest_dirty.yaml
python add_lineage.py --instance=olist_dirty
python add_metadata.py --instance=olist_dirty
```

---

## Metadata Added by `add_metadata.py`

### Tags

Tags are created with descriptions and attached to datasets.

| Tag | Description | Attached To |
|---|---|---|
| `pii` | Contains personally identifiable information | customers, geolocation, reviews |
| `identifier` | Contains primary or foreign key columns | customers, orders, order_items, products, sellers |
| `financial` | Contains monetary values | payments, order_items |

View in DataHub: click any dataset → **Tags** section.

### Glossary Terms

Terms are created with full definitions in DataHub's glossary, then linked to relevant datasets.

| Term | Definition | Attached To |
|---|---|---|
| Order Status | Lifecycle state of an order. Values: created, approved, invoiced, processing, shipped, delivered, unavailable, canceled. | `olist_orders` |
| Customer Identity | Olist uses two customer IDs. `customer_id` is unique per order (changes each purchase). `customer_unique_id` is stable across orders (the real person). Joining on the wrong one produces incorrect results. | `olist_customers` |

View in DataHub: top menu → **Govern → Glossary**.

### Ownership

| Team | Owns |
|---|---|
| `logistics_team` | sellers, geolocation, order_items |
| `finance_team` | payments |
| `customer_experience_team` | reviews, customers |
| `product_team` | products, category_translation |
| `data_platform_team` | orders |

View in DataHub: click any dataset → **Owners** section.

---

## Generate Additional Variants

Only `olist.db` and `olist_dirty.db` are committed to this repo. Two additional variants for reconciliation testing can be generated locally.

### Prerequisites

Download the original CSVs from Kaggle:
- **Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Extract the ZIP — you'll get 9 CSV files

### Generate All Variants

```bash
python create_db.py /path/to/extracted/csvs --all
```

### Generate Specific Variants

```bash
python create_db.py /path/to/csvs --source       # → olist.db (clean)
python create_db.py /path/to/csvs --dirty         # → olist_dirty.db (quality issues)
python create_db.py /path/to/csvs --warehouse     # → olist_warehouse.db (ETL drift)
python create_db.py /path/to/csvs --analytics     # → olist_analytics.db (aggregation drift)
```

### Warehouse Variant (`olist_warehouse.db`)

Simulates a warehouse that received data through a flawed ETL pipeline:

| Drift | What Happened | Impact |
|---|---|---|
| ~3% orders dropped | Random orders deleted | Row count lower than source |
| Precision loss | `payment_value` rounded to 0 decimal places | Value sums differ from source |
| Regional gap | All São Paulo (SP) customers deleted | Entire state missing (~42k rows) |

### Analytics Variant (`olist_analytics.db`)

Simulates an analytics layer with aggregation and normalization bugs:

| Drift | What Happened | Impact |
|---|---|---|
| ~4% duplicate orders | Delivered orders inserted twice | Row count higher than source |
| Freight zeroed | `freight_value` set to 0 for Minas Gerais (MG) sellers | Revenue calculations wrong |
| Score shift | `review_score` incremented by 1, capped at 5 | Average ratings skewed upward |

### Using Reconciliation Variants

Ingest all three to see the same data in three different "systems":

```bash
datahub ingest -c ingest_source.yaml       # source of truth
datahub ingest -c ingest_warehouse.yaml    # ETL copy with drift
datahub ingest -c ingest_analytics.yaml    # analytics copy with drift

python add_lineage.py --all
python add_metadata.py --all
```

---

## How Lineage Works

### Why `add_lineage.py` is Needed

DataHub's SQLAlchemy source can parse view definitions to auto-generate lineage. However, with SQLite, the URN format generated by the view parser doesn't match the URN format of the ingested tables (a known limitation of the generic SQLAlchemy connector with SQLite). This causes lineage references to appear as "entity does not exist" ghost links.

To solve this, view lineage is **disabled** in the ingestion recipes (`include_view_lineage: false`), and `add_lineage.py` handles lineage separately by:

1. Querying DataHub's API to discover the actual URNs of ingested tables and views
2. Emitting lineage using those exact URNs

This approach is fully automatic — no hardcoded URNs, no manual configuration. It works regardless of how DataHub generates URN formats.

### Preview Without Emitting

```bash
python add_lineage.py --dry-run
```

---

## Data Characteristics

### Natural (present in original Kaggle data)

- **Geolocation is many-to-one** — 1,000,163 rows for ~20k unique zip codes. Multiple lat/lng entries per zip.
- **Two customer ID columns** — `customer_id` (unique per order, changes each purchase) vs `customer_unique_id` (stable across orders, identifies the actual person). Using the wrong one in joins produces silently incorrect results.
- **Portuguese category names** — The `product_category_name_translation` table maps Portuguese names to English, but a few categories have no translation.
- **Multiple payment methods per order** — A single order can have multiple rows in `olist_order_payments` (e.g., credit card + voucher).

### Planted (introduced by `create_db.py`, NOT in original data)

All planted issues are deterministic (`random.seed(42)`) and only present in variant databases, never in `olist.db`.

---

## Original Data Source

| | |
|---|---|
| **Dataset** | [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| **Author** | Olist / André Sionek |
| **License** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Published** | 2018, Kaggle |
| **Records** | ~100k orders from 2016–2018 |

> **License terms:** This dataset is available for non-commercial use. If you redistribute it, you must provide attribution and use the same license. The data has been anonymized by Olist — company and partner names in reviews are replaced with Game of Thrones house names.

### What We Modified

The original CSV data is loaded **as-is** into `olist.db`. We did not alter, clean, or transform any original values. The following additions are ours:

- **SQL views** — 5 views created inside the SQLite database to establish join relationships
- **Variant databases** — `olist_dirty.db`, `olist_warehouse.db`, `olist_analytics.db` contain deliberately planted data quality issues (documented above)
- **Metadata scripts** — Tags, glossary terms, ownership, and lineage are added to DataHub via Python scripts, not embedded in the data

---

## Troubleshooting

### Ingestion shows 0 tables

The `.db` path in the YAML recipe is relative to where you run the command. Make sure you're in the `olist-ecommerce/` directory:

```bash
cd datasets/olist-ecommerce
datahub ingest -c ingest_source.yaml
```

### Lineage links show "entity does not exist"

You likely ran ingestion with `include_view_lineage: true` (an older version of the recipe). This creates ghost entities with mismatched URNs. Fix:

1. Delete the ingestion source in DataHub UI
2. Re-ingest with the current recipe (which has `include_view_lineage: false`)
3. Run `python add_lineage.py`

### add_lineage.py or add_metadata.py finds 0 datasets

The scripts search DataHub for datasets matching the platform instance name. If nothing is found:

- Verify ingestion succeeded: search "olist" in DataHub UI
- Check that the instance name matches: `--instance=olist_source` (not `olist`)
- Wait a few seconds after ingestion for DataHub's search index to update

### add_metadata.py says "table not found (skipped)"

The script auto-discovers URNs by searching DataHub. If a table was ingested but the script can't find it, DataHub's search index may not have updated yet. Wait 10 seconds and retry.

### .db file is too large to commit to GitHub

The `olist_geolocation` table has 1M+ rows. We cap it at 500k rows to keep .db files under GitHub's 100MB limit. To load the full table, open `create_db.py` and change one line:

```python
GEOLOCATION_MAX_ROWS = 500_000  # ← change to None for all 1M+ rows
```

Then regenerate: `python create_db.py ./csvs --all`

### create_db.py fails with encoding errors

The script uses `utf-8-sig` encoding to handle CSV files with BOM (byte order mark). If you still get encoding errors, verify your CSV files are the original Kaggle download and haven't been re-saved with a different encoding.

---

## All Available Commands

```bash
# ── Database generation ──
python create_db.py /path/to/csvs --all              # All 4 variants
python create_db.py /path/to/csvs --source            # Clean only
python create_db.py /path/to/csvs --dirty             # Quality issues only
python create_db.py /path/to/csvs --warehouse         # ETL drift only
python create_db.py /path/to/csvs --analytics         # Aggregation drift only

# ── Ingestion ──
datahub ingest -c ingest_source.yaml                   # Ingest clean
datahub ingest -c ingest_dirty.yaml                    # Ingest dirty
datahub ingest -c ingest_warehouse.yaml                # Ingest warehouse
datahub ingest -c ingest_analytics.yaml                # Ingest analytics

# ── Lineage ──
python add_lineage.py                                  # Default: olist_source
python add_lineage.py --instance=olist_dirty           # Specific instance
python add_lineage.py --all                            # All ingested instances
python add_lineage.py --dry-run                        # Preview only

# ── Metadata ──
python add_metadata.py                                 # Default: olist_source
python add_metadata.py --instance=olist_dirty          # Specific instance
python add_metadata.py --all                           # All ingested instances
python add_metadata.py --dry-run                       # Preview only
```