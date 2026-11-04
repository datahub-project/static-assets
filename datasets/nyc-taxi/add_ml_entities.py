#!/usr/bin/env python3
"""
Add ML entities on top of the nyc-taxi pipeline in DataHub.

Run AFTER ingestion and lineage:
    datahub ingest -c ingest.yaml
    python add_lineage.py
    python add_metadata.py
    python add_ml_entities.py

For other variants:
    python add_ml_entities.py --instance=nyc_taxi_pipeline
    python add_ml_entities.py --all
    python add_ml_entities.py --dry-run

Why this exists
---------------
None of the sample datasets in this repo ship ML entities, so there is nowhere to
exercise DataHub's ML metadata model against realistic data. Anyone demoing or testing
mlModel / mlFeature / mlFeatureTable currently has to invent their own fixtures first.

This builds the ML half of the taxi pipeline:

    staging_trips ──(DerivedFrom)──▶ mlFeature × 6
                                          │
                                    (Consumes)
                                          ▼
                            mlFeatureTable:taxi_features
                            mlModel:taxi_demand_forecast
                                          │
                                          ▼
                          mlModelDeployment:taxi-demand-prod

Paired with `nyc_taxi_pipeline.db`, this makes the repo's planted staleness reachable
from a model: the defect is upstream of a model's features, which is exactly the shape
of a silent ML failure and is not otherwise testable with the shipped fixtures.

URNs are constructed rather than searched
-----------------------------------------
`add_lineage.py` and `add_metadata.py` discover URNs via the search API. DataHub's
search index is populated asynchronously by the MAE consumer, so immediately after a
*successful* ingest those scripts can print "No datasets found (run ingestion first)".
This script builds dataset URNs from the platform instance and table name instead, so
it does not depend on index freshness.
"""

import sys

from datahub.emitter.mce_builder import (
    make_dataset_urn_with_platform_instance,
    make_ml_feature_table_urn,
    make_ml_feature_urn,
    make_ml_model_deployment_urn,
    make_ml_model_urn,
)
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.metadata.schema_classes import (
    MLFeatureDataTypeClass,
    MLFeaturePropertiesClass,
    MLFeatureTablePropertiesClass,
    MLModelDeploymentPropertiesClass,
    MLModelPropertiesClass,
)

DATAHUB_SERVER = "http://localhost:8080"
PLATFORM = "sqlite"
ML_PLATFORM = "science"
ENV = "PROD"
DEFAULT_INSTANCE = "nyc_taxi"
VALID_INSTANCES = ["nyc_taxi", "nyc_taxi_pipeline"]

SOURCE_TABLE = "staging_trips"
FEATURE_TABLE = "taxi_features"
MODEL_NAME = "taxi_demand_forecast"
DEPLOYMENT_NAME = "taxi-demand-prod"

# feature name -> (source column, description)
#
# Every column below exists in staging_trips, so the `sources` edges point at a table
# that is really there and the features describe data that is really present.
FEATURES = {
    "trips_7d": ("trip_date", "Rolling 7-day trip count"),
    "avg_fare_7d": ("fare_amount", "Rolling 7-day mean fare"),
    "avg_distance_7d": ("trip_distance", "Rolling 7-day mean trip distance"),
    "avg_duration_7d": ("trip_duration_min", "Rolling 7-day mean trip duration"),
    "passenger_mean_7d": ("passenger_count", "Rolling 7-day mean passenger count"),
    "revenue_7d": ("total_amount", "Rolling 7-day total revenue"),
}


def dataset_urn(platform_instance, table):
    """Build a dataset URN without touching the search index."""
    return make_dataset_urn_with_platform_instance(
        platform=PLATFORM,
        name=f"main.{table}",
        platform_instance=platform_instance,
        env=ENV,
    )


def build_mcps(platform_instance):
    """Every MCP for one instance's ML subgraph."""
    source = dataset_urn(platform_instance, SOURCE_TABLE)

    # Namespace by instance so nyc_taxi and nyc_taxi_pipeline do not collide.
    feature_table = f"{platform_instance}_{FEATURE_TABLE}"
    model = f"{platform_instance}_{MODEL_NAME}"
    deployment = f"{platform_instance}_{DEPLOYMENT_NAME}"

    feature_urns = [make_ml_feature_urn(feature_table, name) for name in FEATURES]
    mcps = []

    for name, (column, description) in FEATURES.items():
        mcps.append(
            MetadataChangeProposalWrapper(
                entityUrn=make_ml_feature_urn(feature_table, name),
                aspect=MLFeaturePropertiesClass(
                    description=f"{description}, derived from {SOURCE_TABLE}.{column}",
                    dataType=MLFeatureDataTypeClass.CONTINUOUS,
                    # NOTE: `sources` accepts dataset URNs only. Its relationship
                    # annotation is entityTypes:["dataset"], so a schemaField URN is
                    # rejected with "is not a valid destination". The originating
                    # column is recorded as a custom property instead.
                    sources=[source],
                    customProperties={"source_column": column, "source_table": SOURCE_TABLE},
                ),
            )
        )

    mcps.append(
        MetadataChangeProposalWrapper(
            entityUrn=make_ml_feature_table_urn(ML_PLATFORM, feature_table),
            aspect=MLFeatureTablePropertiesClass(
                description="Rolling 7-day demand features for NYC taxi forecasting.",
                mlFeatures=feature_urns,
            ),
        )
    )

    mcps.append(
        MetadataChangeProposalWrapper(
            entityUrn=make_ml_model_urn(ML_PLATFORM, model, ENV),
            aspect=MLModelPropertiesClass(
                description=(
                    "Forecasts daily taxi demand from rolling 7-day aggregates of "
                    f"{SOURCE_TABLE}."
                ),
                mlFeatures=feature_urns,
                deployments=[make_ml_model_deployment_urn(ML_PLATFORM, deployment, ENV)],
                customProperties={"framework": "scikit-learn", "task": "regression"},
            ),
        )
    )

    mcps.append(
        MetadataChangeProposalWrapper(
            entityUrn=make_ml_model_deployment_urn(ML_PLATFORM, deployment, ENV),
            aspect=MLModelDeploymentPropertiesClass(
                description="Production deployment of the taxi demand forecaster.",
                customProperties={"region": "us-east", "replicas": "3"},
            ),
        )
    )

    return mcps


def emit_ml_entities(emitter, platform_instance, dry_run=False):
    """Emit the ML subgraph for one instance."""
    mcps = build_mcps(platform_instance)

    if dry_run:
        print(f"    → {len(FEATURES)} features ← {SOURCE_TABLE}")
        print(f"    → 1 feature table, 1 model, 1 deployment")
        return len(mcps)

    for mcp in mcps:
        emitter.emit(mcp)

    print(f"    ✓ {len(FEATURES)} mlFeatures ← {SOURCE_TABLE}")
    print(f"    ✓ mlFeatureTable: {platform_instance}_{FEATURE_TABLE}")
    print(f"    ✓ mlModel: {platform_instance}_{MODEL_NAME}")
    print(f"    ✓ mlModelDeployment: {platform_instance}_{DEPLOYMENT_NAME}")
    return len(mcps)


def main():
    instances = [DEFAULT_INSTANCE]
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg == "--all":
            instances = list(VALID_INSTANCES)
        elif arg.startswith("--instance="):
            instances = [arg.split("=", 1)[1]]
        elif arg == "--help":
            print("Usage: python add_ml_entities.py [--instance=X] [--all] [--dry-run]")
            print(f"  Instances: {', '.join(VALID_INSTANCES)}")
            return
        elif arg.startswith("--"):
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    for inst in instances:
        if inst not in VALID_INSTANCES:
            print(f"Unknown instance: {inst}")
            sys.exit(1)

    print(f"Connecting to DataHub at {DATAHUB_SERVER}...")
    emitter = DatahubRestEmitter(DATAHUB_SERVER)
    total = 0

    for instance in instances:
        print(f"\n  Instance: {instance}")
        try:
            total += emit_ml_entities(emitter, instance, dry_run=dry_run)
        except Exception as e:
            print(f"    ✗ Failed: {e}")
            sys.exit(1)

    print(f"\n{'='*50}")
    if dry_run:
        print(f"DRY RUN — {total} aspects would be emitted")
    else:
        print(f"✅ ML entities added: {total} aspects")
        print("\nView the model in DataHub:")
        print(f"  http://localhost:9002/search?query={MODEL_NAME}")


if __name__ == "__main__":
    main()
