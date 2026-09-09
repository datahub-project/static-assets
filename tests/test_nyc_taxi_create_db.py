import importlib.util
import sqlite3
import unittest
from pathlib import Path


CREATE_DB_PATH = (
    Path(__file__).resolve().parents[1] / "datasets" / "nyc-taxi" / "create_db.py"
)
SPEC = importlib.util.spec_from_file_location("nyc_taxi_create_db", CREATE_DB_PATH)
assert SPEC is not None and SPEC.loader is not None
CREATE_DB = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CREATE_DB)


class PlantStalenessTest(unittest.TestCase):
    def make_pipeline(self):
        conn = sqlite3.connect(":memory:")
        self.addCleanup(conn.close)
        conn.executescript(
            """
            CREATE TABLE raw_trips (tpep_pickup_datetime TEXT);
            CREATE TABLE staging_trips (trip_date TEXT);
            CREATE TABLE mart_daily_summary (
                trip_date TEXT,
                trip_count INTEGER,
                total_fare REAL,
                total_revenue REAL,
                avg_fare REAL,
                avg_distance REAL,
                avg_passengers REAL,
                avg_duration_min REAL
            );
            """
        )

        raw_dates = [f"2026-01-{day:02d} 12:00:00" for day in range(1, 11)]
        staging_dates = [f"2026-01-{day:02d}" for day in range(1, 10)]
        conn.executemany("INSERT INTO raw_trips VALUES (?)", [(d,) for d in raw_dates])
        conn.executemany("INSERT INTO staging_trips VALUES (?)", [(d,) for d in staging_dates])
        conn.executemany(
            "INSERT INTO mart_daily_summary VALUES (?, 10, 1, 1, 1, 1, 1, 1)",
            [(d,) for d in staging_dates],
        )
        return conn

    def test_cutoff_uses_raw_business_date(self):
        conn = self.make_pipeline()

        CREATE_DB.plant_staleness(conn)

        raw_max = conn.execute(
            "SELECT MAX(DATE(tpep_pickup_datetime)) FROM raw_trips"
        ).fetchone()[0]
        staging_max = conn.execute(
            "SELECT MAX(trip_date) FROM staging_trips"
        ).fetchone()[0]
        mart_max = conn.execute(
            "SELECT MAX(trip_date) FROM mart_daily_summary"
        ).fetchone()[0]
        self.assertEqual(raw_max, "2026-01-10")
        self.assertEqual(staging_max, "2026-01-07")
        self.assertEqual(mart_max, "2026-01-07")

    def test_empty_load_uses_an_existing_mart_date(self):
        conn = self.make_pipeline()

        CREATE_DB.plant_staleness(conn)

        empty_days = conn.execute(
            "SELECT COUNT(*) FROM mart_daily_summary WHERE trip_count = 0"
        ).fetchone()[0]
        self.assertEqual(empty_days, 1)


if __name__ == "__main__":
    unittest.main()
