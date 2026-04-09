#!/usr/bin/env python3
"""
Create Healthcare SQLite database from Kaggle CSV.

Simulates a forking data pipeline (raw → staging → billing mart + demographics mart)
with planted data quality issues for testing quality monitoring and circuit breaking.

Usage:
    1. Download from: https://kaggle.com/datasets/prasad22/healthcare-dataset
    2. Extract the ZIP
    3. Run:  python create_db.py /path/to/csvs

Output: healthcare.db (single variant — quality issues are always planted)
"""

import csv
import os
import random
import sqlite3
import sys

random.seed(42)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CSV Loading
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def find_csv(csv_dir):
    """Find the healthcare CSV file."""
    for f in sorted(os.listdir(csv_dir)):
        if f.lower().endswith(".csv"):
            return os.path.join(csv_dir, f)
    return None


def load_csv(conn, csv_path):
    """Load CSV into raw_patients table. All columns as TEXT."""
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = [h.strip() for h in next(reader)]

    # Normalize column names for consistent SQL references
    clean_headers = [h.replace(" ", "_").lower() for h in headers]

    col_defs = ", ".join(f'"{h}" TEXT' for h in clean_headers)
    conn.execute("DROP TABLE IF EXISTS raw_patients")
    conn.execute(f"CREATE TABLE raw_patients ({col_defs})")

    placeholders = ", ".join("?" for _ in clean_headers)
    batch, total = [], 0

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            batch.append(row)
            if len(batch) >= 10000:
                conn.executemany(f"INSERT INTO raw_patients VALUES ({placeholders})", batch)
                total += len(batch)
                batch = []
        if batch:
            conn.executemany(f"INSERT INTO raw_patients VALUES ({placeholders})", batch)
            total += len(batch)

    conn.commit()
    print(f"    ✓ raw_patients: {total:,} rows, {len(clean_headers)} columns")
    print(f"    Columns: {', '.join(clean_headers)}")
    return clean_headers, total


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Quality issue planting
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def plant_quality_issues(conn):
    """Plant data quality issues into raw_patients.

    These simulate real-world data problems at the source stage:
    - Negative billing (data entry errors or system bugs)
    - NULL names (incomplete records from upstream)
    - Invalid ages (ETL type conversion failures)
    - Admission after discharge (timestamp ordering bugs)

    A quality circuit breaker should catch these BEFORE they propagate
    downstream to billing and demographics marts.
    """
    total = conn.execute("SELECT COUNT(*) FROM raw_patients").fetchone()[0]

    # Issue 1: ~2% negative billing amounts
    neg_n = int(total * 0.02)
    conn.execute(f"""
        UPDATE raw_patients
        SET billing_amount = CAST(-1 * ABS(CAST(billing_amount AS REAL)) AS TEXT)
        WHERE rowid IN (
            SELECT rowid FROM raw_patients ORDER BY RANDOM() LIMIT {neg_n}
        )
    """)
    print(f"    ✓ Negative billing: {neg_n:,} rows set to negative amounts")

    # Issue 2: ~1% NULL patient names
    null_n = int(total * 0.01)
    conn.execute(f"""
        UPDATE raw_patients
        SET name = NULL
        WHERE rowid IN (
            SELECT rowid FROM raw_patients
            WHERE name IS NOT NULL
            ORDER BY RANDOM() LIMIT {null_n}
        )
    """)
    print(f"    ✓ NULL names: {null_n:,} rows set to NULL")

    # Issue 3: ~1.5% invalid ages (< 0 or > 120)
    age_n = int(total * 0.015)
    half = age_n // 2
    # Half get negative ages
    conn.execute(f"""
        UPDATE raw_patients
        SET age = CAST(-1 * ABS(CAST(age AS INTEGER)) AS TEXT)
        WHERE rowid IN (
            SELECT rowid FROM raw_patients ORDER BY RANDOM() LIMIT {half}
        )
    """)
    # Half get ages > 120
    conn.execute(f"""
        UPDATE raw_patients
        SET age = CAST(200 + ABS(CAST(age AS INTEGER)) AS TEXT)
        WHERE rowid IN (
            SELECT rowid FROM raw_patients
            WHERE CAST(age AS INTEGER) > 0
            ORDER BY RANDOM() LIMIT {age_n - half}
        )
    """)
    print(f"    ✓ Invalid ages: {age_n:,} rows ({half} negative, {age_n - half} over 120)")

    # Issue 4: ~0.5% admission date after discharge date
    swap_n = int(total * 0.005)
    conn.execute(f"""
        UPDATE raw_patients
        SET date_of_admission = discharge_date,
            discharge_date = date_of_admission
        WHERE rowid IN (
            SELECT rowid FROM raw_patients
            WHERE date_of_admission < discharge_date
            ORDER BY RANDOM() LIMIT {swap_n}
        )
    """)
    print(f"    ✓ Date swap: {swap_n:,} rows have admission after discharge")

    conn.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Pipeline stage creation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def create_staging_table(conn):
    """Create staging_patients — standardized version of raw.

    Note: this does NOT filter out bad data. Quality issues propagate
    from raw through staging. A circuit breaker should catch them
    before they reach the marts.
    """
    conn.execute("DROP TABLE IF EXISTS staging_patients")
    conn.execute("""
        CREATE TABLE staging_patients AS
        SELECT
            *,
            LOWER(TRIM(gender)) AS gender_clean,
            LOWER(TRIM(blood_type)) AS blood_type_clean,
            LOWER(TRIM(medical_condition)) AS condition_clean,
            LOWER(TRIM(admission_type)) AS admission_type_clean,
            LOWER(TRIM(test_results)) AS test_results_clean,
            'staged' AS pipeline_status
        FROM raw_patients
    """)
    count = conn.execute("SELECT COUNT(*) FROM staging_patients").fetchone()[0]
    print(f"    ✓ staging_patients: {count:,} rows")
    return count


def create_mart_tables(conn):
    """Create two downstream marts — this is the FORK in the pipeline.

    mart_billing:      Financial data (billing, insurance, admission type)
    mart_demographics: Patient demographics (age, gender, blood type, condition)

    The circuit breaker challenge: bad data in raw_patients flows through
    staging into BOTH marts. But the impact is different:
    - mart_billing is directly affected by negative billing amounts
    - mart_demographics is affected by invalid ages and NULL names
    - A smart breaker should selectively halt based on which mart is impacted
    """
    # mart_billing
    conn.execute("DROP TABLE IF EXISTS mart_billing")
    conn.execute("""
        CREATE TABLE mart_billing AS
        SELECT
            name,
            hospital,
            insurance_provider,
            admission_type_clean AS admission_type,
            CAST(billing_amount AS REAL) AS billing_amount,
            date_of_admission,
            discharge_date,
            ROUND(
                JULIANDAY(discharge_date) - JULIANDAY(date_of_admission), 1
            ) AS length_of_stay_days,
            medication,
            pipeline_status
        FROM staging_patients
    """)
    billing_count = conn.execute("SELECT COUNT(*) FROM mart_billing").fetchone()[0]
    print(f"    ✓ mart_billing: {billing_count:,} rows")

    # mart_demographics
    conn.execute("DROP TABLE IF EXISTS mart_demographics")
    conn.execute("""
        CREATE TABLE mart_demographics AS
        SELECT
            name,
            CAST(age AS INTEGER) AS age,
            gender_clean AS gender,
            blood_type_clean AS blood_type,
            condition_clean AS medical_condition,
            hospital,
            test_results_clean AS test_results,
            pipeline_status
        FROM staging_patients
    """)
    demo_count = conn.execute("SELECT COUNT(*) FROM mart_demographics").fetchone()[0]
    print(f"    ✓ mart_demographics: {demo_count:,} rows")

    return billing_count, demo_count


def create_views(conn):
    """Create views for lineage in DataHub."""
    conn.execute("""
        CREATE VIEW IF NOT EXISTS v_staging_from_raw AS
        SELECT
            *,
            LOWER(TRIM(gender)) AS gender_clean,
            LOWER(TRIM(blood_type)) AS blood_type_clean,
            LOWER(TRIM(medical_condition)) AS condition_clean,
            LOWER(TRIM(admission_type)) AS admission_type_clean,
            LOWER(TRIM(test_results)) AS test_results_clean,
            'staged' AS pipeline_status
        FROM raw_patients
    """)
    print(f"    ✓ v_staging_from_raw")

    conn.execute("""
        CREATE VIEW IF NOT EXISTS v_billing_from_staging AS
        SELECT
            name,
            hospital,
            insurance_provider,
            admission_type_clean AS admission_type,
            CAST(billing_amount AS REAL) AS billing_amount,
            date_of_admission,
            discharge_date,
            ROUND(
                JULIANDAY(discharge_date) - JULIANDAY(date_of_admission), 1
            ) AS length_of_stay_days,
            medication,
            pipeline_status
        FROM staging_patients
    """)
    print(f"    ✓ v_billing_from_staging")

    conn.execute("""
        CREATE VIEW IF NOT EXISTS v_demographics_from_staging AS
        SELECT
            name,
            CAST(age AS INTEGER) AS age,
            gender_clean AS gender,
            blood_type_clean AS blood_type,
            condition_clean AS medical_condition,
            hospital,
            test_results_clean AS test_results,
            pipeline_status
        FROM staging_patients
    """)
    print(f"    ✓ v_demographics_from_staging")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Verification
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def verify_issues(conn):
    """Verify planted quality issues are detectable."""
    print("\n  Verifying quality issues...")

    neg_billing = conn.execute(
        "SELECT COUNT(*) FROM raw_patients WHERE CAST(billing_amount AS REAL) < 0"
    ).fetchone()[0]
    print(f"    → Negative billing amounts: {neg_billing:,}")

    null_names = conn.execute(
        "SELECT COUNT(*) FROM raw_patients WHERE name IS NULL"
    ).fetchone()[0]
    print(f"    → NULL patient names: {null_names:,}")

    bad_ages = conn.execute(
        "SELECT COUNT(*) FROM raw_patients WHERE CAST(age AS INTEGER) < 0 OR CAST(age AS INTEGER) > 120"
    ).fetchone()[0]
    print(f"    → Invalid ages (< 0 or > 120): {bad_ages:,}")

    date_swaps = conn.execute(
        "SELECT COUNT(*) FROM raw_patients WHERE date_of_admission > discharge_date"
    ).fetchone()[0]
    print(f"    → Admission after discharge: {date_swaps:,}")

    # Check propagation to marts
    neg_mart = conn.execute(
        "SELECT COUNT(*) FROM mart_billing WHERE billing_amount < 0"
    ).fetchone()[0]
    print(f"    → Negative billing in mart_billing: {neg_mart:,} (propagated!)")

    bad_age_mart = conn.execute(
        "SELECT COUNT(*) FROM mart_demographics WHERE age < 0 OR age > 120"
    ).fetchone()[0]
    print(f"    → Invalid ages in mart_demographics: {bad_age_mart:,} (propagated!)")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not args:
        print("Usage: python create_db.py /path/to/csv/directory")
        print()
        print("Download from: https://kaggle.com/datasets/prasad22/healthcare-dataset")
        sys.exit(1)

    csv_dir = os.path.abspath(args[0])
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "healthcare.db")

    csv_path = find_csv(csv_dir)
    if not csv_path:
        print(f"✗ No CSV file found in: {csv_dir}")
        sys.exit(1)

    size_mb = os.path.getsize(csv_path) / (1024 * 1024)
    print(f"Found: {os.path.basename(csv_path)} ({size_mb:.1f} MB)")

    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)

    # Step 1: Load CSV
    print(f"\n{'='*60}")
    print(f"Step 1: Loading CSV into raw_patients")
    print(f"{'='*60}")
    headers, total = load_csv(conn, csv_path)

    # Step 2: Plant quality issues
    print(f"\n{'='*60}")
    print(f"Step 2: Planting quality issues in raw_patients")
    print(f"{'='*60}")
    plant_quality_issues(conn)

    # Step 3: Create pipeline stages
    print(f"\n{'='*60}")
    print(f"Step 3: Creating pipeline stages")
    print(f"{'='*60}")
    create_staging_table(conn)
    create_mart_tables(conn)

    # Step 4: Create views
    print(f"\n{'='*60}")
    print(f"Step 4: Creating views (lineage)")
    print(f"{'='*60}")
    create_views(conn)
    conn.commit()

    # Step 5: Verify
    print(f"\n{'='*60}")
    print(f"Step 5: Verification")
    print(f"{'='*60}")
    verify_issues(conn)

    # Summary
    size_mb = os.path.getsize(db_path) / (1024 * 1024)
    tables = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
    views = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='view'").fetchone()[0]

    print(f"\n{'='*60}")
    print(f"✅ Created: {db_path}")
    print(f"   Size: {size_mb:.1f} MB | {tables} tables, {views} views")
    print(f"   Pipeline: raw_patients → staging_patients → mart_billing + mart_demographics")
    print(f"   Quality issues: 4 types planted (negative billing, NULL names, invalid ages, date swaps)")
    print(f"\nNext steps:")
    print(f"   datahub ingest -c ingest.yaml")
    print(f"   python add_lineage.py")
    print(f"   python add_metadata.py")
    print(f"{'='*60}")

    conn.close()


if __name__ == "__main__":
    main()