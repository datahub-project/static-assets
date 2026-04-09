#!/usr/bin/env python3
"""
Create NYC Taxi Trip SQLite databases from Kaggle CSV files.

Simulates a 3-stage data pipeline (raw → staging → mart) for testing
freshness auditing and pipeline monitoring.

Usage:
    1. Download from: https://kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data
    2. Extract the ZIP (you'll get multiple monthly CSV files)
    3. Run:

    python create_db.py /path/to/csvs --all           # Both variants
    python create_db.py /path/to/csvs --source         # Clean pipeline only
    python create_db.py /path/to/csvs --pipeline       # Staleness planted
    python create_db.py --pipeline-from-existing       # From committed .db (no CSV needed)

Output files:
    nyc_taxi.db            Clean 3-stage pipeline (~500k trip subset)
    nyc_taxi_pipeline.db   Same pipeline with planted staleness (staging/mart lag behind raw)
"""

import csv
import os
import random
import shutil
import sqlite3
import sys
from datetime import datetime, timedelta

random.seed(42)

# ─── Auto-detect pickup datetime column ───
PICKUP_DATETIME_CANDIDATES = [
    "tpep_pickup_datetime",
    "pickup_datetime",
    "lpep_pickup_datetime",
    "Trip_Pickup_DateTime",
]

DROPOFF_DATETIME_CANDIDATES = [
    "tpep_dropoff_datetime",
    "dropoff_datetime",
    "lpep_dropoff_datetime",
    "Trip_Dropoff_DateTime",
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CSV Loading
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def find_csvs(csv_dir):
    """Find all CSV files in the directory, sorted by name."""
    csvs = []
    for f in sorted(os.listdir(csv_dir)):
        if f.lower().endswith(".csv"):
            csvs.append(os.path.join(csv_dir, f))
    return csvs


def detect_datetime_columns(headers):
    """Auto-detect the pickup and dropoff datetime column names."""
    headers_lower = {h.lower().strip(): h.strip() for h in headers}
    pickup_col, dropoff_col = None, None

    for candidate in PICKUP_DATETIME_CANDIDATES:
        if candidate.lower() in headers_lower:
            pickup_col = headers_lower[candidate.lower()]
            break
    for candidate in DROPOFF_DATETIME_CANDIDATES:
        if candidate.lower() in headers_lower:
            dropoff_col = headers_lower[candidate.lower()]
            break

    return pickup_col, dropoff_col


def load_csv_subset(conn, csv_paths, max_rows=250_000):
    """Load a subset of rows from one or more CSV files into raw_trips.

    Distributes rows evenly across all files to get good date coverage.
    The full Kaggle dataset is 1.8GB+ compressed — we only need a fraction.

    Default is 250k rows (~85MB .db). To load more data, increase max_rows.
    Note: GitHub rejects files over 100MB, so keep max_rows under ~300k.
    """
    rows_per_file = max_rows // len(csv_paths)
    print(f"  Loading {len(csv_paths)} file(s), ~{rows_per_file:,} rows each, {max_rows:,} total cap")

    # Read headers from first file
    with open(csv_paths[0], "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = [h.strip() for h in next(reader)]

    pickup_col, dropoff_col = detect_datetime_columns(headers)
    if not pickup_col:
        print(f"  ✗ Cannot find pickup datetime column in: {headers}")
        print(f"    Expected one of: {PICKUP_DATETIME_CANDIDATES}")
        sys.exit(1)

    print(f"  Detected: pickup={pickup_col}, dropoff={dropoff_col}")

    # Create table
    col_defs = ", ".join(f'"{h}" TEXT' for h in headers)
    conn.execute("DROP TABLE IF EXISTS raw_trips")
    conn.execute(f"CREATE TABLE raw_trips ({col_defs})")

    placeholders = ", ".join("?" for _ in headers)
    grand_total = 0

    for csv_path in csv_paths:
        file_name = os.path.basename(csv_path)
        batch, file_total = [], 0

        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            file_headers = [h.strip() for h in next(reader)]

            if len(file_headers) != len(headers):
                print(f"    ⚠ {file_name}: column count mismatch, skipped")
                continue

            for row in reader:
                if file_total >= rows_per_file or grand_total >= max_rows:
                    break
                batch.append(row)
                if len(batch) >= 10000:
                    conn.executemany(f"INSERT INTO raw_trips VALUES ({placeholders})", batch)
                    file_total += len(batch)
                    grand_total += len(batch)
                    batch = []
            if batch:
                conn.executemany(f"INSERT INTO raw_trips VALUES ({placeholders})", batch)
                file_total += len(batch)
                grand_total += len(batch)

        print(f"    ✓ {file_name}: {file_total:,} rows")

    conn.commit()
    print(f"    Total raw_trips: {grand_total:,} rows, {len(headers)} columns")

    min_date = conn.execute(f'SELECT MIN("{pickup_col}") FROM raw_trips WHERE "{pickup_col}" IS NOT NULL').fetchone()[0]
    max_date = conn.execute(f'SELECT MAX("{pickup_col}") FROM raw_trips WHERE "{pickup_col}" IS NOT NULL').fetchone()[0]
    print(f"    Date range: {min_date} → {max_date}")

    return headers, pickup_col, dropoff_col, grand_total


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Pipeline stage creation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def create_staging_table(conn, pickup_col, dropoff_col):
    """Create staging_trips — cleaned and enriched version of raw_trips."""
    conn.execute("DROP TABLE IF EXISTS staging_trips")

    if dropoff_col:
        duration_expr = f'ROUND((JULIANDAY("{dropoff_col}") - JULIANDAY("{pickup_col}")) * 24 * 60, 1) AS trip_duration_min,'
    else:
        duration_expr = "NULL AS trip_duration_min,"

    conn.execute(f"""
        CREATE TABLE staging_trips AS
        SELECT
            *,
            DATE("{pickup_col}") AS trip_date,
            {duration_expr}
            'staged' AS pipeline_status
        FROM raw_trips
        WHERE "{pickup_col}" IS NOT NULL
          AND CAST(trip_distance AS REAL) > 0
          AND CAST(fare_amount AS REAL) > 0
    """)

    count = conn.execute("SELECT COUNT(*) FROM staging_trips").fetchone()[0]
    max_date = conn.execute("SELECT MAX(trip_date) FROM staging_trips").fetchone()[0]
    print(f"    ✓ staging_trips: {count:,} rows (latest: {max_date})")
    return count, max_date


def create_mart_table(conn):
    """Create mart_daily_summary — daily aggregation from staging."""
    conn.execute("DROP TABLE IF EXISTS mart_daily_summary")
    conn.execute("""
        CREATE TABLE mart_daily_summary AS
        SELECT
            trip_date,
            COUNT(*) AS trip_count,
            ROUND(SUM(CAST(fare_amount AS REAL)), 2) AS total_fare,
            ROUND(SUM(CAST(total_amount AS REAL)), 2) AS total_revenue,
            ROUND(AVG(CAST(fare_amount AS REAL)), 2) AS avg_fare,
            ROUND(AVG(CAST(trip_distance AS REAL)), 2) AS avg_distance,
            ROUND(AVG(CAST(passenger_count AS REAL)), 1) AS avg_passengers,
            ROUND(AVG(trip_duration_min), 1) AS avg_duration_min
        FROM staging_trips
        GROUP BY trip_date
        ORDER BY trip_date
    """)
    count = conn.execute("SELECT COUNT(*) FROM mart_daily_summary").fetchone()[0]
    print(f"    ✓ mart_daily_summary: {count} days")
    return count


def create_views(conn, pickup_col, dropoff_col):
    """Create views for lineage in DataHub."""
    if dropoff_col:
        duration_expr = f'ROUND((JULIANDAY("{dropoff_col}") - JULIANDAY("{pickup_col}")) * 24 * 60, 1) AS trip_duration_min,'
    else:
        duration_expr = "NULL AS trip_duration_min,"

    conn.execute(f"""
        CREATE VIEW IF NOT EXISTS v_staging_from_raw AS
        SELECT *, DATE("{pickup_col}") AS trip_date,
            {duration_expr}
            'staged' AS pipeline_status
        FROM raw_trips
        WHERE "{pickup_col}" IS NOT NULL
          AND CAST(trip_distance AS REAL) > 0
          AND CAST(fare_amount AS REAL) > 0
    """)
    print(f"    ✓ v_staging_from_raw")

    conn.execute("""
        CREATE VIEW IF NOT EXISTS v_daily_from_staging AS
        SELECT
            trip_date,
            COUNT(*) AS trip_count,
            ROUND(SUM(CAST(fare_amount AS REAL)), 2) AS total_fare,
            ROUND(SUM(CAST(total_amount AS REAL)), 2) AS total_revenue,
            ROUND(AVG(CAST(fare_amount AS REAL)), 2) AS avg_fare,
            ROUND(AVG(CAST(trip_distance AS REAL)), 2) AS avg_distance,
            ROUND(AVG(CAST(passenger_count AS REAL)), 1) AS avg_passengers,
            ROUND(AVG(trip_duration_min), 1) AS avg_duration_min
        FROM staging_trips
        GROUP BY trip_date
    """)
    print(f"    ✓ v_daily_from_staging")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Staleness planting
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def plant_staleness(conn):
    """Plant freshness issues into the pipeline.

    The core trick: raw_trips has data through the latest date,
    but staging_trips and mart_daily_summary stop 3 days earlier.

    This simulates a pipeline that ran successfully (DataHub shows
    "ingested now") but didn't actually process new data.
    """
    max_raw = conn.execute("SELECT MAX(trip_date) FROM staging_trips").fetchone()[0]
    if not max_raw:
        print("    ✗ Cannot determine max date — skipping")
        return

    cutoff_date = (datetime.strptime(max_raw, "%Y-%m-%d") - timedelta(days=3)).strftime("%Y-%m-%d")
    print(f"    Raw data through: {max_raw}")
    print(f"    Staging/mart cutoff: {cutoff_date} (3 days stale)")

    # Remove recent rows from staging
    before = conn.execute("SELECT COUNT(*) FROM staging_trips").fetchone()[0]
    conn.execute(f"DELETE FROM staging_trips WHERE trip_date > '{cutoff_date}'")
    after = conn.execute("SELECT COUNT(*) FROM staging_trips").fetchone()[0]
    print(f"    ✓ staging_trips: removed {before - after:,} recent rows")

    # Remove recent days from mart
    before_m = conn.execute("SELECT COUNT(*) FROM mart_daily_summary").fetchone()[0]
    conn.execute(f"DELETE FROM mart_daily_summary WHERE trip_date > '{cutoff_date}'")
    after_m = conn.execute("SELECT COUNT(*) FROM mart_daily_summary").fetchone()[0]
    print(f"    ✓ mart_daily_summary: removed {before_m - after_m} recent days")

    # Plant one "empty load" day (pipeline ran, loaded nothing)
    mid_date = (datetime.strptime(cutoff_date, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
    conn.execute(f"""
        UPDATE mart_daily_summary
        SET trip_count = 0, total_fare = 0, total_revenue = 0,
            avg_fare = 0, avg_distance = 0, avg_passengers = 0, avg_duration_min = 0
        WHERE trip_date = '{mid_date}'
    """)
    affected = conn.execute("SELECT changes()").fetchone()[0]
    if affected > 0:
        print(f"    ✓ Empty load: {mid_date} shows 0 trips (pipeline ran but loaded nothing)")
    else:
        print(f"    ⚠ Empty load: {mid_date} not found in mart (skipped)")

    conn.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Build helpers
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def build_base_db(csv_paths, db_path):
    """Build the clean pipeline database from CSV files."""
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)

    print("  Loading CSVs (subset)...")
    headers, pickup_col, dropoff_col, _ = load_csv_subset(conn, csv_paths)

    print("  Creating staging table...")
    create_staging_table(conn, pickup_col, dropoff_col)

    print("  Creating mart table...")
    create_mart_table(conn)

    print("  Creating views...")
    create_views(conn, pickup_col, dropoff_col)

    conn.commit()
    conn.close()
    return pickup_col, dropoff_col


def verify_db(db_path, label):
    """Verify a database variant."""
    conn = sqlite3.connect(db_path)

    raw = conn.execute("SELECT COUNT(*) FROM raw_trips").fetchone()[0]
    staging = conn.execute("SELECT COUNT(*) FROM staging_trips").fetchone()[0]
    mart = conn.execute("SELECT COUNT(*) FROM mart_daily_summary").fetchone()[0]

    staging_max = conn.execute("SELECT MAX(trip_date) FROM staging_trips").fetchone()
    mart_max = conn.execute("SELECT MAX(trip_date) FROM mart_daily_summary").fetchone()

    print(f"\n  [{label}] {os.path.basename(db_path)}")
    print(f"    raw_trips: {raw:,} rows")
    print(f"    staging_trips: {staging:,} rows (max date: {staging_max[0] if staging_max else 'N/A'})")
    print(f"    mart_daily_summary: {mart} days (max date: {mart_max[0] if mart_max else 'N/A'})")

    empty_days = conn.execute("SELECT COUNT(*) FROM mart_daily_summary WHERE trip_count = 0").fetchone()[0]
    if empty_days > 0:
        print(f"    Empty load days in mart: {empty_days}")

    size_mb = os.path.getsize(db_path) / (1024 * 1024)
    tables = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
    views = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='view'").fetchone()[0]
    print(f"    Size: {size_mb:.1f} MB | {tables} tables, {views} views")

    conn.close()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VARIANTS = {
    "--source":   ("nyc_taxi.db",          "Clean 3-stage pipeline"),
    "--pipeline": ("nyc_taxi_pipeline.db", "Pipeline with planted staleness"),
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # ── Help ──
    if not args and "--pipeline-from-existing" not in flags:
        print("Usage: python create_db.py /path/to/csv/directory [OPTIONS]")
        print()
        print("Options:")
        print("  --all                    Create all database variants")
        print("  --source                 Create nyc_taxi.db (clean pipeline)")
        print("  --pipeline               Create nyc_taxi_pipeline.db (staleness planted)")
        print("  --pipeline-from-existing Create pipeline variant from existing nyc_taxi.db")
        print("                           (no CSV download needed)")
        print()
        print("If you already have nyc_taxi.db (committed to repo), just run:")
        print("  python create_db.py --pipeline-from-existing")
        sys.exit(1)

    # ── Shortcut: build pipeline from existing .db ──
    if "--pipeline-from-existing" in flags:
        base_db = os.path.join(script_dir, "nyc_taxi.db")
        if not os.path.exists(base_db):
            print(f"✗ nyc_taxi.db not found in {script_dir}")
            sys.exit(1)

        db_path = os.path.join(script_dir, "nyc_taxi_pipeline.db")
        print(f"{'='*60}")
        print(f"Building pipeline variant from existing nyc_taxi.db")
        print(f"{'='*60}")
        if os.path.exists(db_path):
            os.remove(db_path)
        shutil.copy2(base_db, db_path)
        conn = sqlite3.connect(db_path)
        print("  Planting staleness...")
        plant_staleness(conn)
        conn.close()
        verify_db(db_path, "Pipeline with planted staleness")
        return

    # ── Normal: build from CSVs ──
    csv_dir = os.path.abspath(args[0])

    csv_paths = find_csvs(csv_dir)
    if not csv_paths:
        print(f"✗ No CSV files found in: {csv_dir}")
        sys.exit(1)

    print(f"Found {len(csv_paths)} CSV file(s):")
    for p in csv_paths:
        size_mb = os.path.getsize(p) / (1024 * 1024)
        print(f"  {os.path.basename(p)} ({size_mb:.1f} MB)")

    if "--all" in flags:
        flags = {"--source", "--pipeline"}

    variant_flags = flags & set(VARIANTS.keys())
    if not variant_flags:
        variant_flags = {"--source"}

    # Build clean base
    base_db = os.path.join(script_dir, "nyc_taxi.db")
    print(f"\n{'='*60}")
    print(f"Building clean pipeline: nyc_taxi.db")
    print(f"{'='*60}")
    build_base_db(csv_paths, base_db)

    created = []

    if "--source" in variant_flags:
        created.append(("nyc_taxi.db", "Clean 3-stage pipeline"))

    if "--pipeline" in variant_flags:
        db_path = os.path.join(script_dir, "nyc_taxi_pipeline.db")
        print(f"\n{'='*60}")
        print(f"Building variant: nyc_taxi_pipeline.db")
        print(f"{'='*60}")
        if os.path.exists(db_path):
            os.remove(db_path)
        shutil.copy2(base_db, db_path)
        conn = sqlite3.connect(db_path)
        print("  Planting staleness...")
        plant_staleness(conn)
        conn.close()
        created.append(("nyc_taxi_pipeline.db", "Pipeline with planted staleness"))

    if "--source" not in variant_flags:
        os.remove(base_db)

    # Verify
    print(f"\n{'='*60}")
    print(f"Verification")
    print(f"{'='*60}")
    for db_name, label in created:
        verify_db(os.path.join(script_dir, db_name), label)

    print(f"\n{'='*60}")
    print(f"Next steps:")
    print(f"  datahub ingest -c ingest.yaml")
    print(f"  python add_lineage.py")
    print(f"  python add_metadata.py")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()