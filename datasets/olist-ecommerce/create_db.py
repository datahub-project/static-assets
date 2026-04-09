#!/usr/bin/env python3
"""
Create Olist E-Commerce SQLite databases from Kaggle CSV files.

One script creates ALL database variants needed for different problems.

Usage:
    1. Download from: https://kaggle.com/datasets/olistbr/brazilian-ecommerce
    2. Extract the ZIP (you'll get 9 CSV files)
    3. Run:

    # Create all variants at once
    python create_db.py /path/to/csvs --all

    # Or create specific variants
    python create_db.py /path/to/csvs --source           → olist.db
    python create_db.py /path/to/csvs --dirty             → olist_dirty.db
    python create_db.py /path/to/csvs --warehouse         → olist_warehouse.db
    python create_db.py /path/to/csvs --analytics         → olist_analytics.db

Output files:
    olist.db               Clean base (source of truth)
    olist_dirty.db         Data quality issues planted (orphans, ID mismatch, NULL categories)
    olist_warehouse.db     Reconciliation: rows dropped, precision truncated
    olist_analytics.db     Reconciliation: duplicates, regional data zeroed
"""

import csv
import os
import random
import shutil
import sqlite3
import sys

# Seed for reproducibility — same issues every time
random.seed(42)

# ─── CSV file → SQLite table name mapping ───
CSV_TABLE_MAP = {
    "olist_customers_dataset.csv": "olist_customers",
    "olist_orders_dataset.csv": "olist_orders",
    "olist_order_items_dataset.csv": "olist_order_items",
    "olist_products_dataset.csv": "olist_products",
    "olist_sellers_dataset.csv": "olist_sellers",
    "olist_order_payments_dataset.csv": "olist_order_payments",
    "olist_order_reviews_dataset.csv": "olist_order_reviews",
    "olist_geolocation_dataset.csv": "olist_geolocation",
    "product_category_name_translation.csv": "product_category_name_translation",
}


# ─── Views that establish lineage in DataHub ───
# DataHub's sqlalchemy source parses view SQL to create lineage edges.

GEOLOCATION_MAX_ROWS = 500_000

VIEWS = [
    (
        "v_order_details",
        """
        CREATE VIEW IF NOT EXISTS v_order_details AS
        SELECT
            o.order_id,
            o.order_status,
            o.order_purchase_timestamp,
            o.order_approved_at,
            o.order_delivered_carrier_date,
            o.order_delivered_customer_date,
            o.order_estimated_delivery_date,
            c.customer_unique_id,
            c.customer_city,
            c.customer_state,
            c.customer_zip_code_prefix,
            oi.order_item_id,
            oi.product_id,
            oi.seller_id,
            oi.price,
            oi.freight_value,
            oi.shipping_limit_date
        FROM olist_orders o
        JOIN olist_customers c ON o.customer_id = c.customer_id
        JOIN olist_order_items oi ON o.order_id = oi.order_id
        """,
    ),
    (
        "v_order_payments",
        """
        CREATE VIEW IF NOT EXISTS v_order_payments AS
        SELECT
            o.order_id,
            o.order_status,
            o.order_purchase_timestamp,
            o.customer_id,
            p.payment_sequential,
            p.payment_type,
            p.payment_installments,
            p.payment_value
        FROM olist_orders o
        JOIN olist_order_payments p ON o.order_id = p.order_id
        """,
    ),
    (
        "v_order_reviews",
        """
        CREATE VIEW IF NOT EXISTS v_order_reviews AS
        SELECT
            o.order_id,
            o.order_status,
            o.order_purchase_timestamp,
            o.customer_id,
            r.review_id,
            r.review_score,
            r.review_comment_title,
            r.review_comment_message,
            r.review_creation_date,
            r.review_answer_timestamp
        FROM olist_orders o
        JOIN olist_order_reviews r ON o.order_id = r.order_id
        """,
    ),
    (
        "v_seller_performance",
        """
        CREATE VIEW IF NOT EXISTS v_seller_performance AS
        SELECT
            s.seller_id,
            s.seller_city,
            s.seller_state,
            s.seller_zip_code_prefix,
            p.product_id,
            p.product_category_name,
            oi.order_id,
            oi.price,
            oi.freight_value,
            r.review_score
        FROM olist_order_items oi
        JOIN olist_sellers s ON oi.seller_id = s.seller_id
        JOIN olist_products p ON oi.product_id = p.product_id
        LEFT JOIN olist_order_reviews r ON oi.order_id = r.order_id
        """,
    ),
    (
        "v_product_sales",
        """
        CREATE VIEW IF NOT EXISTS v_product_sales AS
        SELECT
            p.product_id,
            p.product_category_name,
            t.product_category_name_english,
            p.product_weight_g,
            p.product_length_cm,
            p.product_height_cm,
            p.product_width_cm,
            oi.order_id,
            oi.seller_id,
            oi.price,
            oi.freight_value
        FROM olist_order_items oi
        JOIN olist_products p ON oi.product_id = p.product_id
        LEFT JOIN product_category_name_translation t
            ON p.product_category_name = t.product_category_name
        """,
    ),
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CSV Loading
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def load_csv_to_sqlite(conn, csv_path, table_name, max_rows=None):
    """Load a CSV file into SQLite. All columns as TEXT to preserve data exactly."""
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = [h.strip() for h in next(reader)]

        col_defs = ", ".join(f'"{h}" TEXT' for h in headers)
        conn.execute(f'DROP TABLE IF EXISTS "{table_name}"')
        conn.execute(f'CREATE TABLE "{table_name}" ({col_defs})')

        placeholders = ", ".join("?" for _ in headers)
        batch, total = [], 0
        for row in reader:
            if max_rows and total >= max_rows:
                break
            batch.append(row)
            if len(batch) >= 10000:
                conn.executemany(
                    f'INSERT INTO "{table_name}" VALUES ({placeholders})', batch
                )
                total += len(batch)
                batch = []
        if batch:
            conn.executemany(
                f'INSERT INTO "{table_name}" VALUES ({placeholders})', batch
            )
            total += len(batch)

    suffix = f" (capped at {max_rows:,})" if max_rows and total >= max_rows else ""
    print(f"    ✓ {table_name}: {total:,} rows{suffix}")
    return total


def create_views(conn):
    """Create SQL views for lineage."""
    for name, sql in VIEWS:
        conn.execute(sql)
        count = conn.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
        print(f"    ✓ {name}: {count:,} rows")


def build_base_db(csv_dir, db_path):
    """Load CSVs + create views. Returns the connection (still open)."""
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)

    print("  Loading CSVs...")
    for csv_file, table_name in CSV_TABLE_MAP.items():
        csv_path = os.path.join(csv_dir, csv_file)
        # Cap geolocation to keep .db under GitHub's 100MB limit
        row_limit = GEOLOCATION_MAX_ROWS if table_name == "olist_geolocation" else None
        load_csv_to_sqlite(conn, csv_path, table_name, max_rows=row_limit)

    print("  Creating views...")
    create_views(conn)
    conn.commit()
    return conn


def copy_base_db(source_path, dest_path):
    """Copy a base .db to create a variant."""
    if os.path.exists(dest_path):
        os.remove(dest_path)
    shutil.copy2(source_path, dest_path)
    return sqlite3.connect(dest_path)


def print_db_summary(db_path, label):
    """Print summary of a .db file."""
    conn = sqlite3.connect(db_path)
    tables = conn.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
    ).fetchone()[0]
    views = conn.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='view'"
    ).fetchone()[0]
    size_mb = os.path.getsize(db_path) / (1024 * 1024)
    conn.close()
    print(f"  ✅ {os.path.basename(db_path):30s} {size_mb:6.1f} MB | {tables} tables, {views} views | {label}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Variant: Join Advisor (planted join quality issues)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def plant_join_quality_issues(conn):
    """Plant join quality issues into the clean dataset.

    Original data is perfectly clean — all joins match 100%.
    These issues simulate real-world problems commonly found in production:
    - Dimension table missing records (most common ETL failure)
    - ID format drift from type conversions
    - Incomplete upstream data
    """

    # Issue 1: ~8% orphan customer_ids
    # Delete customers → orders reference non-existent customer_ids
    total = conn.execute("SELECT COUNT(*) FROM olist_customers").fetchone()[0]
    delete_n = int(total * 0.08)
    conn.execute(f"""
        DELETE FROM olist_customers
        WHERE customer_id IN (
            SELECT customer_id FROM olist_customers
            ORDER BY customer_id
            LIMIT {delete_n}
        )
    """)
    print(f"    ✓ Orphan customers: deleted {delete_n:,}/{total:,} customers")

    # Issue 2: ~5% seller_id mismatch
    # Truncate seller_id in order_items → no match in sellers table
    total = conn.execute("SELECT COUNT(*) FROM olist_order_items").fetchone()[0]
    trunc_n = int(total * 0.05)
    conn.execute(f"""
        UPDATE olist_order_items
        SET seller_id = SUBSTR(seller_id, 1, LENGTH(seller_id) - 1)
        WHERE rowid IN (
            SELECT rowid FROM olist_order_items ORDER BY rowid LIMIT {trunc_n}
        )
    """)
    print(f"    ✓ Seller ID mismatch: truncated {trunc_n:,}/{total:,} order items")

    # Issue 3: ~3% NULL product categories
    # Breaks category translation join
    total = conn.execute("SELECT COUNT(*) FROM olist_products").fetchone()[0]
    null_n = int(total * 0.03)
    conn.execute(f"""
        UPDATE olist_products
        SET product_category_name = NULL
        WHERE product_id IN (
            SELECT product_id FROM olist_products
            WHERE product_category_name IS NOT NULL
            ORDER BY product_id LIMIT {null_n}
        )
    """)
    print(f"    ✓ NULL categories: nulled {null_n:,}/{total:,} products")

    conn.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Variant: Warehouse (reconciliation — ETL drift)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def plant_warehouse_drift(conn):
    """Plant warehouse-style drift into the dataset.

    The warehouse is the SAME table structure as source, but with
    realistic drift from pipeline issues:
    - Missing rows (failed batch loads)
    - Duplicate records (re-processed batches)
    - Precision differences (type conversions)

    Useful for testing data reconciliation between source and warehouse copies.
    """

    # Drift 1: ~3% of orders randomly dropped (failed ETL batch)
    total = conn.execute("SELECT COUNT(*) FROM olist_orders").fetchone()[0]
    drop_n = int(total * 0.03)
    conn.execute(f"""
        DELETE FROM olist_orders
        WHERE order_id IN (
            SELECT order_id FROM olist_orders
            ORDER BY RANDOM()
            LIMIT {drop_n}
        )
    """)
    print(f"    ✓ Missing rows: {drop_n:,}/{total:,} orders randomly dropped")

    # Drift 2: ~2% of order_items duplicated (re-processed batch)
    total_items = conn.execute("SELECT COUNT(*) FROM olist_order_items").fetchone()[0]
    dup_n = int(total_items * 0.02)
    conn.execute(f"""
        INSERT INTO olist_order_items
        SELECT * FROM olist_order_items
        WHERE rowid IN (
            SELECT rowid FROM olist_order_items
            ORDER BY RANDOM()
            LIMIT {dup_n}
        )
    """)
    actual_dup = conn.execute("SELECT changes()").fetchone()[0]
    print(f"    ✓ Duplicate records: {actual_dup:,} order_items duplicated")

    # Drift 3: Payment values rounded to 0 decimal places (precision loss)
    # Simulates warehouse using INT instead of DECIMAL for payment_value
    conn.execute("""
        UPDATE olist_order_payments
        SET payment_value = CAST(ROUND(CAST(payment_value AS REAL), 0) AS TEXT)
        WHERE payment_value IS NOT NULL
    """)
    affected = conn.execute("SELECT changes()").fetchone()[0]
    print(f"    ✓ Precision loss: payment_value rounded to 0 decimals ({affected:,} rows)")

    conn.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Variant: Analytics (reconciliation — aggregation/duplication drift)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def plant_analytics_drift(conn):
    """Create analytics-layer tables with aggregated daily rollups.

    Unlike source and warehouse (which have the SAME table structure),
    the analytics layer has DIFFERENT tables — daily rollups/aggregations.

    The reconciliation challenge:
      SUM(source.olist_order_items.price) for 2017-05-15
      should equal
      analytics_daily_revenue.total_revenue for 2017-05-15
    ...but it doesn't, because of planted drift in the rollups.

    Tables created (these REPLACE the raw tables):
      analytics_daily_orders     — date, order_count, avg_items_per_order
      analytics_daily_revenue    — date, total_revenue, total_freight, total_payment
      analytics_daily_sellers    — date, seller_state, active_sellers, items_sold
      analytics_daily_reviews    — date, review_count, avg_score

    Drift planted:
      - 5 random days have order_count inflated by 10-20% (overcounting bug)
      - total_freight is systematically 5% lower than source (rounding in ETL)
      - avg_score rounded to 1 decimal (precision loss vs source's exact values)
      - 3 random days completely missing from analytics_daily_revenue (gap)
    """

    # ── Step 1: Drop raw tables, create aggregation tables ──
    # Keep only the tables needed to compute rollups, then replace with rollups

    # -- Daily Orders --
    conn.execute("DROP TABLE IF EXISTS analytics_daily_orders")
    conn.execute("""
        CREATE TABLE analytics_daily_orders AS
        SELECT
            DATE(o.order_purchase_timestamp) AS order_date,
            COUNT(DISTINCT o.order_id) AS order_count,
            ROUND(
                CAST(COUNT(oi.order_item_id) AS REAL) / MAX(COUNT(DISTINCT o.order_id), 1),
                2
            ) AS avg_items_per_order
        FROM olist_orders o
        LEFT JOIN olist_order_items oi ON o.order_id = oi.order_id
        WHERE o.order_purchase_timestamp IS NOT NULL
        GROUP BY DATE(o.order_purchase_timestamp)
    """)
    days_orders = conn.execute("SELECT COUNT(*) FROM analytics_daily_orders").fetchone()[0]
    print(f"    ✓ Created analytics_daily_orders: {days_orders} days")

    # -- Daily Revenue --
    conn.execute("DROP TABLE IF EXISTS analytics_daily_revenue")
    conn.execute("""
        CREATE TABLE analytics_daily_revenue AS
        SELECT
            DATE(o.order_purchase_timestamp) AS order_date,
            ROUND(SUM(CAST(oi.price AS REAL)), 2) AS total_revenue,
            ROUND(SUM(CAST(oi.freight_value AS REAL)), 2) AS total_freight,
            ROUND(SUM(CAST(p.payment_value AS REAL)), 2) AS total_payment
        FROM olist_orders o
        JOIN olist_order_items oi ON o.order_id = oi.order_id
        JOIN olist_order_payments p ON o.order_id = p.order_id
        WHERE o.order_purchase_timestamp IS NOT NULL
        GROUP BY DATE(o.order_purchase_timestamp)
    """)
    days_revenue = conn.execute("SELECT COUNT(*) FROM analytics_daily_revenue").fetchone()[0]
    print(f"    ✓ Created analytics_daily_revenue: {days_revenue} days")

    # -- Daily Sellers --
    conn.execute("DROP TABLE IF EXISTS analytics_daily_sellers")
    conn.execute("""
        CREATE TABLE analytics_daily_sellers AS
        SELECT
            DATE(o.order_purchase_timestamp) AS order_date,
            s.seller_state,
            COUNT(DISTINCT s.seller_id) AS active_sellers,
            COUNT(oi.order_item_id) AS items_sold
        FROM olist_orders o
        JOIN olist_order_items oi ON o.order_id = oi.order_id
        JOIN olist_sellers s ON oi.seller_id = s.seller_id
        WHERE o.order_purchase_timestamp IS NOT NULL
        GROUP BY DATE(o.order_purchase_timestamp), s.seller_state
    """)
    rows_sellers = conn.execute("SELECT COUNT(*) FROM analytics_daily_sellers").fetchone()[0]
    print(f"    ✓ Created analytics_daily_sellers: {rows_sellers} rows")

    # -- Daily Reviews --
    conn.execute("DROP TABLE IF EXISTS analytics_daily_reviews")
    conn.execute("""
        CREATE TABLE analytics_daily_reviews AS
        SELECT
            DATE(r.review_creation_date) AS review_date,
            COUNT(*) AS review_count,
            ROUND(AVG(CAST(r.review_score AS REAL)), 2) AS avg_score
        FROM olist_order_reviews r
        WHERE r.review_creation_date IS NOT NULL
        GROUP BY DATE(r.review_creation_date)
    """)
    days_reviews = conn.execute("SELECT COUNT(*) FROM analytics_daily_reviews").fetchone()[0]
    print(f"    ✓ Created analytics_daily_reviews: {days_reviews} days")

    # ── Step 2: Drop the raw tables (analytics layer only has rollups) ──
    raw_tables = [
        "olist_customers", "olist_orders", "olist_order_items",
        "olist_products", "olist_sellers", "olist_order_payments",
        "olist_order_reviews", "olist_geolocation",
        "product_category_name_translation",
    ]
    # Also drop views that reference raw tables
    views = [v[0] for v in VIEWS]
    for view in views:
        conn.execute(f"DROP VIEW IF EXISTS {view}")
    for table in raw_tables:
        conn.execute(f"DROP TABLE IF EXISTS {table}")
    print(f"    ✓ Dropped raw tables and views (analytics has only rollups)")

    # ── Step 3: Plant drift in the rollups ──

    # Drift 1: Inflate order_count for 5 random days by 10-20%
    conn.execute("""
        UPDATE analytics_daily_orders
        SET order_count = CAST(order_count * (1.1 + (ABS(RANDOM()) % 10) * 0.01) AS INTEGER)
        WHERE order_date IN (
            SELECT order_date FROM analytics_daily_orders
            ORDER BY RANDOM()
            LIMIT 5
        )
    """)
    print(f"    ✓ Drift: order_count inflated on 5 random days (10-20% overcounting)")

    # Drift 2: Reduce total_freight by 5% across all days (systematic ETL rounding)
    conn.execute("""
        UPDATE analytics_daily_revenue
        SET total_freight = ROUND(total_freight * 0.95, 2)
    """)
    print(f"    ✓ Drift: total_freight reduced by 5% across all days")

    # Drift 3: Round avg_score to 1 decimal (precision loss)
    conn.execute("""
        UPDATE analytics_daily_reviews
        SET avg_score = ROUND(avg_score, 1)
    """)
    print(f"    ✓ Drift: avg_score rounded to 1 decimal")

    # Drift 4: Delete 3 random days from analytics_daily_revenue (gap)
    conn.execute("""
        DELETE FROM analytics_daily_revenue
        WHERE order_date IN (
            SELECT order_date FROM analytics_daily_revenue
            ORDER BY RANDOM()
            LIMIT 3
        )
    """)
    print(f"    ✓ Drift: 3 random days deleted from analytics_daily_revenue")

    conn.commit()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Verification
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def verify_db(db_path, label):
    """Run basic verification on a .db file."""
    conn = sqlite3.connect(db_path)

    tables = [t[0] for t in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()]
    views = [v[0] for v in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name"
    ).fetchall()]

    print(f"\n  [{label}] {os.path.basename(db_path)}")
    print(f"    Tables: {', '.join(tables)}")
    if views:
        print(f"    Views:  {', '.join(views)}")

    # Analytics variant has different tables — detect and verify accordingly
    if "analytics_daily_orders" in tables:
        # Analytics rollup verification
        days = conn.execute("SELECT COUNT(*) FROM analytics_daily_orders").fetchone()[0]
        revenue_days = conn.execute("SELECT COUNT(*) FROM analytics_daily_revenue").fetchone()[0]
        seller_rows = conn.execute("SELECT COUNT(*) FROM analytics_daily_sellers").fetchone()[0]
        review_days = conn.execute("SELECT COUNT(*) FROM analytics_daily_reviews").fetchone()[0]
        print(f"    Daily orders: {days} days | Daily revenue: {revenue_days} days")
        print(f"    Daily sellers: {seller_rows} rows | Daily reviews: {review_days} days")
    else:
        # Source/dirty/warehouse verification
        orders = conn.execute("SELECT COUNT(*) FROM olist_orders").fetchone()[0]
        customers = conn.execute("SELECT COUNT(*) FROM olist_customers").fetchone()[0]
        items = conn.execute("SELECT COUNT(*) FROM olist_order_items").fetchone()[0]
        payments = conn.execute("SELECT COUNT(*) FROM olist_order_payments").fetchone()[0]

        orphan_orders = conn.execute("""
            SELECT COUNT(*) FROM olist_orders o
            LEFT JOIN olist_customers c ON o.customer_id = c.customer_id
            WHERE c.customer_id IS NULL
        """).fetchone()[0]

        orphan_sellers = conn.execute("""
            SELECT COUNT(*) FROM olist_order_items oi
            LEFT JOIN olist_sellers s ON oi.seller_id = s.seller_id
            WHERE s.seller_id IS NULL
        """).fetchone()[0]

        print(f"    Orders: {orders:,} | Customers: {customers:,} | Items: {items:,} | Payments: {payments:,}")
        print(f"    Orphan orders→customers: {orphan_orders:,} | Orphan items→sellers: {orphan_sellers:,}")

    conn.close()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VARIANTS = {
    "--source":    ("olist.db",             "Clean base (source of truth)"),
    "--dirty":     ("olist_dirty.db",       "Planted data quality issues"),
    "--warehouse": ("olist_warehouse.db",   "Reconciliation: ETL drift"),
    "--analytics": ("olist_analytics.db",   "Reconciliation: aggregation drift"),
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}

    if not args:
        print("Usage: python create_db.py /path/to/csvs [OPTIONS]")
        print()
        print("Options:")
        print("  --all            Create all 4 database variants")
        print("  --source         Create olist.db (clean base)")
        print("  --dirty          Create olist_dirty.db (data quality issues planted)")
        print("  --warehouse      Create olist_warehouse.db (reconciliation: ETL drift)")
        print("  --analytics      Create olist_analytics.db (reconciliation: aggregation drift)")
        print()
        print("Examples:")
        print("  python create_db.py ./csvs --all                    # Everything")
        print("  python create_db.py ./csvs --source                 # Just the clean base")
        print("  python create_db.py ./csvs --dirty                  # Just the one with issues")
        print("  python create_db.py ./csvs --warehouse --analytics  # Just reconciliation pair")
        print()
        print("Download CSVs from:")
        print("  https://kaggle.com/datasets/olistbr/brazilian-ecommerce")
        print()
        print("Expected CSV files:")
        for f in sorted(CSV_TABLE_MAP.keys()):
            print(f"  - {f}")
        sys.exit(1)

    csv_dir = os.path.abspath(args[0])
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # If --all, enable all variants
    if "--all" in flags:
        flags = {"--source", "--dirty", "--warehouse", "--analytics"}

    # If no variant flag specified, default to --source
    variant_flags = flags & set(VARIANTS.keys())
    if not variant_flags:
        variant_flags = {"--source"}

    # Verify CSVs exist
    print(f"Checking CSVs in: {csv_dir}\n")
    missing = []
    for csv_file in CSV_TABLE_MAP:
        path = os.path.join(csv_dir, csv_file)
        if not os.path.exists(path):
            missing.append(csv_file)
            print(f"  ✗ {csv_file}")
        else:
            size = os.path.getsize(path) / (1024 * 1024)
            print(f"  ✓ {csv_file} ({size:.1f} MB)")

    if missing:
        print(f"\n❌ Missing {len(missing)} file(s).")
        print("   Download: https://kaggle.com/datasets/olistbr/brazilian-ecommerce")
        sys.exit(1)

    # ── Always build the clean base first ──
    base_db = os.path.join(script_dir, "olist.db")
    print(f"\n{'='*60}")
    print(f"Building clean base: olist.db")
    print(f"{'='*60}")
    conn = build_base_db(csv_dir, base_db)
    conn.close()

    # ── Build requested variants ──
    created = []

    if "--source" in variant_flags:
        # Base is already the source — just register it
        created.append(("olist.db", "Clean base (source of truth)"))

    if "--dirty" in variant_flags:
        db_path = os.path.join(script_dir, "olist_dirty.db")
        print(f"\n{'='*60}")
        print(f"Building variant: olist_dirty.db")
        print(f"{'='*60}")
        conn = copy_base_db(base_db, db_path)
        print("  Planting data quality issues...")
        plant_join_quality_issues(conn)
        conn.close()
        created.append(("olist_dirty.db", "Planted data quality issues"))

    if "--warehouse" in variant_flags:
        db_path = os.path.join(script_dir, "olist_warehouse.db")
        print(f"\n{'='*60}")
        print(f"Building variant: olist_warehouse.db")
        print(f"{'='*60}")
        conn = copy_base_db(base_db, db_path)
        print("  Planting warehouse drift...")
        plant_warehouse_drift(conn)
        conn.close()
        created.append(("olist_warehouse.db", "Reconciliation: ETL drift"))

    if "--analytics" in variant_flags:
        db_path = os.path.join(script_dir, "olist_analytics.db")
        print(f"\n{'='*60}")
        print(f"Building variant: olist_analytics.db")
        print(f"{'='*60}")
        conn = copy_base_db(base_db, db_path)
        print("  Planting analytics drift...")
        plant_analytics_drift(conn)
        conn.close()
        created.append(("olist_analytics.db", "Reconciliation: aggregation drift"))

    # If only variants were requested (no --source), remove the base
    if "--source" not in variant_flags:
        os.remove(base_db)

    # ── Verification ──
    print(f"\n{'='*60}")
    print(f"Verification")
    print(f"{'='*60}")
    for db_name, label in created:
        db_path = os.path.join(script_dir, db_name)
        verify_db(db_path, label)

    # ── Final summary ──
    print(f"\n{'='*60}")
    print(f"Summary")
    print(f"{'='*60}")
    for db_name, label in created:
        db_path = os.path.join(script_dir, db_name)
        print_db_summary(db_path, label)

    print(f"\nNext steps:")
    print(f"  datahub ingest -c ingest_<variant>.yaml")
    print(f"  python add_metadata.py")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()