# ml-lineage

A small ML platform: a Snowflake warehouse pipeline with **column-level lineage**, a Feast
feature store, and three production MLflow models. Ingested via
`datahub datapack load ml-lineage`.

This is the only sample that contains `mlFeatureTable`, `mlFeature`, `mlModel` and
`mlModelGroup` entities, so it is the one to use when you need lineage that crosses from
tables into models.

## Contents

| File | Purpose | Aspects |
|------|---------|---------|
| `index.json` | Pack manifest (version, MCP file list) | — |
| `mcps/01-warehouse.json` | 7 Snowflake datasets: schemas and descriptions | 14 |
| `mcps/02-column-lineage.json` | `upstreamLineage`: 5 table edges, 21 `fineGrainedLineages` column mappings | 4 |
| `mcps/03-features.json` | 2 Feast feature tables, 6 features | 8 |
| `mcps/04-models.json` | 3 MLflow models in 3 model groups | 6 |

32 aspects, 15 entities. ~48 KB across four MCP files.

## The graph

```
                     column-level lineage                    entity-level
  ┌──────────────┐   ┌──────────────┐   ┌───────────────┐   ┌──────────┐   ┌──────────────┐
  │ raw_trips    │──▶│ stg_trips    │──▶│ trip_features │──▶│ 4        │──▶│ tip_predictor│
  │ raw_payments │──▶│ stg_payments │──▶│               │   │ features │   │ eta_predictor│
  │ raw_zones    │   │              │──▶│ zone_features │──▶│ 2        │──▶│ surge_pricing│
  └──────────────┘   └──────────────┘   └───────────────┘   │ features │   └──────────────┘
     snowflake          snowflake          snowflake            feast           mlflow
```

Relationship chain, all four hops traversable by impact analysis:

```
dataset --DownstreamOf--> dataset --DerivedFrom--> mlFeature --Consumes--> mlModel --MemberOf--> mlModelGroup
```

| Entity type | Platform | Count | Names |
|---|---|---|---|
| `dataset` | snowflake | 7 | `nyc_taxi.{raw_trips,raw_payments,raw_zones,stg_trips,stg_payments,trip_features,zone_features}` |
| `mlFeatureTable` | feast | 2 | `trip_features`, `zone_features` |
| `mlFeature` | — | 6 | `trip_features.{tip_rate,fare_per_mile,duration_min,distance_km}`, `zone_features.{avg_trip_duration,trips_per_hour}` |
| `mlModel` | mlflow | 3 | `tip_predictor_v3`, `eta_predictor_v2`, `surge_pricing_v1` |
| `mlModelGroup` | mlflow | 3 | `tip_predictor`, `eta_predictor`, `surge_pricing` |

## What makes it useful

**Column-level lineage that actually discriminates.** The 21 `fineGrainedLineages`
mappings are deliberately asymmetric, so table-level and column-level lineage give
different answers to the same question. Every row below was measured against a loaded
instance, not designed on paper:

| Change one column | Downstream datasets (table-level) | Columns affected | Models affected (column-precise) |
|---|---|---|---|
| `raw_payments.tip_amount` | 3 | 2 — `stg_payments.tip_amount`, `trip_features.tip_rate` | **1** — `tip_predictor_v3` |
| `raw_payments.payment_type` | 3 | 1 — `stg_payments.payment_type` | **0** — dead-ends before any feature |
| `raw_trips.trip_id` | 3 | 2 — `stg_trips.trip_id`, `zone_features.trips_per_hour` | **1** — `surge_pricing_v1` |
| `raw_trips.trip_distance` | 3 | 3 — `stg_trips.trip_distance`, `trip_features.distance_km`, `trip_features.fare_per_mile` | **3** — all of them |

Table-level lineage answers "3 models" to all four questions. Column-level lineage answers
1, 0, 1, 3. The pack is built so that spread exists, which makes it useful for testing
impact analysis, column-lineage UI, or alerting precision — anything that has to be judged
on false positives rather than recall.

Note the `payment_type` row: a column whose change genuinely affects nothing downstream is
as important a test case as one that affects everything, and it is the case flat lineage
fixtures cannot express.

**A fork and a join.** `stg_trips` feeds both feature tables; `trip_features` draws from
both `stg_payments` and `stg_trips`. Single-parent chains do not exercise multi-upstream
merge logic, and this one does.

**Multi-column derivations.** `duration_min` comes from
`FIELD_SET(pickup_datetime, dropoff_datetime)`, `tip_rate` from
`FIELD_SET(tip_amount, fare_amount)` — not just 1:1 renames.

## Load

Once the pack is in the registry:

```bash
datahub datapack load ml-lineage
```

Before the registry URL is published, or when working from a checkout:

```bash
datahub datapack load ml-lineage \
  --url "file://$(pwd)/datapacks/ml-lineage/index.json" \
  --trust-custom
```

To remove it again:

```bash
datahub datapack unload ml-lineage
```

## Try it

After loading, the whole chain is visible from a single call:

```graphql
query {
  searchAcrossLineage(input:{
    urn:"urn:li:dataset:(urn:li:dataPlatform:snowflake,nyc_taxi.raw_payments,PROD)",
    direction:DOWNSTREAM, query:"*", count:50
  }) {
    total
    searchResults { degree entity { urn type } }
  }
}
```

`total: 12`, and the results walk the whole chain:

```
degree=1  DATASET        nyc_taxi.stg_payments
degree=2  DATASET        nyc_taxi.trip_features
degree=3  MLFEATURE      trip_features.{tip_rate, fare_per_mile, duration_min, distance_km}
degree=4  MLMODEL        tip_predictor_v3, eta_predictor_v2, surge_pricing_v1
degree=5  MLMODEL_GROUP  tip_predictor, eta_predictor, surge_pricing
```

For the column-precise answer, read `upstreamLineage.fineGrainedLineages` off the
downstream dataset directly — lineage search from a `schemaField` URN terminates at the
dataset boundary and will not return `mlFeature` results.

## Regenerating

`generate.py` builds the MCP files from a single declaration of the graph, so the URNs
cannot drift out of sync:

```bash
pip install 'acryl-datahub[datahub-rest]'
python generate.py --out datapacks/ml-lineage
```

## Notes

- **No row data.** This is a metadata-only pack. `mlModel` and `mlFeature` have no SQL
  representation, so unlike `datasets/nyc-taxi` there is no SQLite database to ingest and
  no `create_db.py`. Schemas are emitted directly as `schemaMetadata`.
- **No timestamps.** Nothing in the pack carries an epoch-millis field, so
  `--reference-timestamp` time shifting is a no-op here.
- **`wait_for_completion`** is set on `01-warehouse.json` and `03-features.json` because
  the file that follows each references those URNs: features point at datasets, models
  point at features.
- **No tags, glossary terms, or ownership.** Deliberate — the pack is meant to be a
  minimal, readable ML-lineage reference, and the governance-heavy case is already
  covered by `showcase-ecommerce`. Easy to add if that is preferred.
- Table and column names follow the NYC TLC taxi schema so the pack reads alongside
  `datasets/nyc-taxi`, but the values are illustrative: no NYC TLC data is included or
  required.
