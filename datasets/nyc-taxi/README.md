# NYC Taxi Trip Dataset for DataHub

NYC Yellow Taxi trip records loaded as a **3-stage data pipeline** (raw → staging → mart) for testing freshness auditing, pipeline monitoring, and staleness detection with DataHub.

Built from the [NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) on Kaggle (originally from the NYC Taxi & Limousine Commission).

---

## What's Included

```
nyc-taxi/
├── nyc_taxi.db               ← Clean 3-stage pipeline, ~500k trips (committed)
├── create_db.py              ← Generates .db variants from source CSV
├── ingest.yaml               ← Ingests nyc_taxi.db into DataHub
├── ingest_pipeline.yaml      ← Ingests nyc_taxi_pipeline.db into DataHub
├── add_lineage.py            ← Adds pipeline lineage (auto-discovers URNs)
├── add_metadata.py           ← Adds tags, glossary terms, ownership
└── README.md                 ← You are here
```

> **Note:** Only `nyc_taxi.db` and `nyc_taxi_pipeline.db` are committed (~85MB each, 250k trip subset). The full Kaggle dataset is 1.8GB+ compressed — you don't need to download it.

---

## Quick Start

```bash
# 1. Ingest into DataHub
datahub ingest -c ingest.yaml

# 2. Add pipeline lineage
python add_lineage.py

# 3. Add metadata
python add_metadata.py
```

---

## What's in Each Database

### `nyc_taxi.db` — Clean 3-Stage Pipeline

A working data pipeline where all stages are in sync. Data flows correctly from raw through staging to mart.

**Tables (3 pipeline stages):**

| Table | Description | Row Count |
|---|---|---|
| `raw_trips` | Original taxi trip data loaded from CSV (subset to ~250k rows) | ~250,000 |
| `staging_trips` | Cleaned: filtered nulls, zero-distance trips, invalid fares. Added `trip_date` and `trip_duration_min` | ~225,000 |
| `mart_daily_summary` | Daily aggregation: trip count, total revenue, avg fare, avg distance, avg passengers | ~30 days |

**Pipeline lineage (what you see in DataHub):**

```
raw_trips ──→ staging_trips ──→ mart_daily_summary
   (raw)         (cleaned)          (aggregated)
```

Additionally, views `v_staging_from_raw` and `v_daily_from_staging` show how each transformation works.

**Key columns in raw_trips:**

| Column | Description |
|---|---|
| `VendorID` | TPEP provider (1=CMT, 2=VeriFone) |
| `tpep_pickup_datetime` | Pickup timestamp |
| `tpep_dropoff_datetime` | Dropoff timestamp |
| `passenger_count` | Number of passengers |
| `trip_distance` | Trip distance in miles |
| `PULocationID` / `pickup_longitude` | Pickup location (format varies by dataset year) |
| `DOLocationID` / `dropoff_longitude` | Dropoff location |
| `payment_type` | Payment method (1=Credit, 2=Cash, 3=No charge, 4=Dispute) |
| `fare_amount` | Meter fare |
| `tip_amount` | Tip (auto-populated for credit card only) |
| `total_amount` | Total charged to passenger |

**Columns added in staging_trips:**

| Column | Description |
|---|---|
| `trip_date` | Extracted date from pickup datetime |
| `trip_duration_min` | Calculated trip duration in minutes |
| `pipeline_status` | Always 'staged' — marks this as processed data |

---

### `nyc_taxi_pipeline.db` — Planted Staleness

Same 3-stage pipeline structure, but with freshness issues planted:

| Issue | What's Planted | How to Detect |
|---|---|---|
| Stale staging | `staging_trips` stops 3 days before `raw_trips` max date | Compare `MAX(trip_date)` between raw and staging |
| Stale mart | `mart_daily_summary` reflects the staging gap | Last 3 days missing from daily summary |
| Empty load | One day in the mart shows 0 trips | `trip_count = 0` for that day — pipeline ran but loaded nothing |

**The core trick:** DataHub metadata shows all tables as "ingested now" (because they were all ingested at the same time). The staleness is invisible in metadata — you can only detect it by querying the actual data timestamps.

```
raw_trips:          data through Jan 31  ← looks fresh
staging_trips:      data through Jan 28  ← 3 days behind (stale!)
mart_daily_summary: data through Jan 28  ← also stale, plus one day shows 0 trips
```

---

## Ingestion Details

| Recipe | Database | Platform Instance |
|---|---|---|
| `ingest.yaml` | `nyc_taxi.db` | `nyc_taxi` |
| `ingest_pipeline.yaml` | `nyc_taxi_pipeline.db` | `nyc_taxi_pipeline` |

### Single variant

```bash
datahub ingest -c ingest.yaml
python add_lineage.py
python add_metadata.py
```

### Both variants

```bash
datahub ingest -c ingest.yaml
datahub ingest -c ingest_pipeline.yaml
python add_lineage.py --all
python add_metadata.py --all
```

---

## Metadata

### Tags

| Tag | Description | Attached To |
|---|---|---|
| `daily_refresh` | Expected to receive new data daily | raw_trips, staging_trips, mart_daily_summary |
| `time_series` | Contains timestamped records | raw_trips, staging_trips |
| `pii` | Contains pickup/dropoff locations | raw_trips, staging_trips |
| `pipeline_stage` | Part of a multi-stage pipeline | raw_trips, staging_trips, mart_daily_summary |

### Glossary Terms

| Term | Definition | Attached To |
|---|---|---|
| Freshness SLA | Expected update frequency. A table is stale when MAX(timestamp) falls behind the expected cadence. | All 3 tables |
| Empty Load | Pipeline completes successfully but loads zero new rows. Undetectable from metadata alone. | mart_daily_summary |
| Pipeline Stage | A step in raw → staging → mart. Staleness propagates downstream. | All 3 tables |

### Ownership

| Team | Owns |
|---|---|
| `data_platform_team` | All 3 tables |

---

## Generate the Staleness Variant

**From the committed .db (no Kaggle download needed):**

```bash
# Uses the committed nyc_taxi.db as base — copies it and plants staleness
python create_db.py --pipeline-from-existing
```

**From the original CSV (if you want to rebuild everything):**

```bash
# Download from: https://kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data
# WARNING: The Kaggle download is ~1.8GB compressed. You don't need it
# unless you want to rebuild from scratch.

python create_db.py /path/to/csvs --all       # Both variants
python create_db.py /path/to/csvs --pipeline   # Just the staleness variant
```

---

## How the Pipeline Simulation Works

This isn't just a raw CSV loaded into SQLite. The `create_db.py` script builds a realistic 3-stage pipeline:

1. **raw_trips** — CSV data loaded as-is (subset to first ~500k rows)
2. **staging_trips** — Materialized from raw with filters and computed columns:
   - Removes rows with NULL datetime, zero distance, or negative fares
   - Adds `trip_date` (extracted date) and `trip_duration_min` (calculated from pickup/dropoff)
3. **mart_daily_summary** — Aggregated from staging:
   - One row per day: trip count, total fare/revenue, averages for distance/passengers/duration

Views exist alongside the tables to show DataHub the lineage relationships between stages.

---

## How Lineage Works

`add_lineage.py` creates two types of lineage:

- **Table-to-table:** `raw_trips → staging_trips → mart_daily_summary` — this is the pipeline flow you see when clicking any table's Lineage tab
- **View-to-table:** `v_staging_from_raw ← raw_trips` and `v_daily_from_staging ← staging_trips` — shows how each transformation is defined

Both use auto-discovered URNs from DataHub's API. `include_view_lineage: false` in the ingest YAML because SQLite's SQLAlchemy connector generates mismatched URNs for view lineage.

---

## Original Data Source

| | |
|---|---|
| **Dataset** | [NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) |
| **Original Source** | [NYC Taxi & Limousine Commission (TLC)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **License** | Public Domain (NYC Open Data) |
| **Records** | Millions of trip records (we subset to ~500k) |

> The data was collected by technology providers authorized under the Taxicab Passenger Enhancement Program (TPEP). The TLC does not guarantee accuracy or completeness.

### What We Modified

- **Subset:** Only ~250k rows loaded (distributed across all monthly CSV files) to keep file size under GitHub's 100MB limit. The full Kaggle dataset is 1.8GB+ compressed.
- **Pipeline stages:** `staging_trips` and `mart_daily_summary` are computed from raw data, not in the original CSV
- **Views:** Created for DataHub lineage visualization
- **Staleness variant:** `nyc_taxi_pipeline.db` has deliberately planted freshness gaps (documented above)

---

## Troubleshooting

### create_db.py can't find the datetime column

The script auto-detects column names by looking for `tpep_pickup_datetime`, `pickup_datetime`, `lpep_pickup_datetime`, or `Trip_Pickup_DateTime`. If your CSV uses a different name, the script will list the actual headers and exit.

### .db file is too large

The script loads 250k rows by default (~85MB .db). To load more or fewer rows, open `create_db.py` and change one line:

```python
def load_csv_subset(conn, csv_paths, max_rows=250_000):  # ← change this number
```

Note: GitHub rejects files over 100MB, so keep `max_rows` under ~300k if you plan to commit the .db.

### Staleness is hard to see in DataHub

That's the point! The staleness is invisible in metadata. All tables show the same "last ingested" timestamp. You need to query `SELECT MAX(trip_date) FROM staging_trips` vs `SELECT MAX(trip_date) FROM raw_trips` to see the 3-day gap. This is exactly the problem a freshness auditor should detect.

---

## All Available Commands

```bash
# ── Database generation ──
python create_db.py --pipeline-from-existing    # From committed .db (no CSV needed)
python create_db.py /path/to/csvs --all         # Both variants from CSV
python create_db.py /path/to/csvs --source      # Clean pipeline only
python create_db.py /path/to/csvs --pipeline    # Staleness variant only

# ── Ingestion ──
datahub ingest -c ingest.yaml                   # Clean pipeline
datahub ingest -c ingest_pipeline.yaml          # Staleness variant

# ── Lineage ──
python add_lineage.py                           # Default: nyc_taxi
python add_lineage.py --instance=nyc_taxi_pipeline
python add_lineage.py --all
python add_lineage.py --dry-run

# ── Metadata ──
python add_metadata.py                          # Default: nyc_taxi
python add_metadata.py --instance=nyc_taxi_pipeline
python add_metadata.py --all
python add_metadata.py --dry-run
```