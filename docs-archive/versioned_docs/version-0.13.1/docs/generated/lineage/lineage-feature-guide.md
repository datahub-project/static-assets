---
title: About DataHub Lineage
sidebar_label: Lineage
slug: /generated/lineage/lineage-feature-guide
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/lineage/lineage-feature-guide.md
---
import FeatureAvailability from '@site/src/components/FeatureAvailability';

# About DataHub Lineage

<FeatureAvailability/>

Lineage is used to capture data dependencies within an organization. It allows you to track the inputs from which a data asset is derived, along with the data assets that depend on it downstream.

## Viewing Lineage

You can view lineage under **Lineage** tab or **Lineage Visualization** screen.

<p align="center">
<img width="70%" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/lineage-tab.png" />
</p>

The UI shows the latest version of the lineage. The time picker can be used to filter out edges within the latest version to exclude those that were last updated outside of the time window. Selecting time windows in the patch will not show you historical lineages. It will only filter the view of the latest version of the lineage.

<p align="center">
<img width="70%" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/lineage-view.png" />
</p>


:::tip The Lineage Tab is greyed out - why can’t I click on it?
This means you have not yet ingested lineage metadata for that entity. Please ingest lineage to proceed.

:::

## Adding Lineage

### Ingestion Source

If you're using an ingestion source that supports extraction of Lineage (e.g. **Table Lineage Capability**), then lineage information can be extracted automatically.
For detailed instructions, refer to the [source documentation](/integrations) for the source you are using.

### UI

As of `v0.9.5`, DataHub supports the manual editing of lineage between entities. Data experts are free to add or remove upstream and downstream lineage edges in both the Lineage Visualization screen as well as the Lineage tab on entity pages. Use this feature to supplement automatic lineage extraction or establish important entity relationships in sources that do not support automatic extraction. Editing lineage by hand is supported for Datasets, Charts, Dashboards, and Data Jobs.
Please refer to our [UI Guides on Lineage](../../features/feature-guides/ui-lineage.md) for more information.

:::caution Recommendation on UI-based lineage

Lineage added by hand and programmatically may conflict with one another to cause unwanted overwrites.
It is strongly recommend that lineage is edited manually in cases where lineage information is not also extracted in automated fashion, e.g. by running an ingestion source.

:::

### API

If you are not using a Lineage-support ingestion source, you can programmatically emit lineage edges between entities via API.
Please refer to [API Guides on Lineage](../../api/tutorials/lineage.md) for more information.


## Lineage Support

### Automatic Lineage Extraction Support

This is a summary of automatic lineage extraciton support in our data source. Please refer to the **Important Capabilities** table in the source documentation. Note that even if the source does not support automatic extraction, you can still add lineage manually using our API & SDKs.

| Source | Table-Level Lineage | Column-Level Lineage | Related Configs |
| ---------- | ------ | ----- |----- |
| [Athena](../../generated/ingestion/sources/athena.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage|
| [BigQuery](../../generated/ingestion/sources/bigquery.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- lineage_use_sql_parser<br />- lineage_parse_view_ddl<br />- lineage_sql_parser_use_raw_names<br />- extract_column_lineage<br />- extract_lineage_from_catalog<br />- include_table_lineage<br />- upstream_lineage_in_report|
| [Business Glossary](../../generated/ingestion/sources/business-glossary.md) | ❌ | ❌ | |
| [ClickHouse `clickhouse`](../../generated/ingestion/sources/clickhouse.md) | ❌ | ❌ | |
| [ClickHouse `clickhouse-usage`](../../generated/ingestion/sources/clickhouse.md) | ❌ | ❌ | |
| [Databricks](../../generated/ingestion/sources/databricks.md) | ✅ | ✅ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage<br />- include_external_lineage<br />- include_column_lineage<br />- column_lineage_column_limit|
| [DataHub](../../generated/ingestion/sources/datahub.md) | ❌ | ❌ | |
| [DataHubGc](../../generated/ingestion/sources/datahubgc.md) | ❌ | ❌ | |
| [dbt `dbt`](../../generated/ingestion/sources/dbt.md) | ✅ | ✅ | - incremental_lineage<br />- skip_sources_in_lineage<br />- include_column_lineage|
| [dbt `dbt-cloud`](../../generated/ingestion/sources/dbt.md) | ✅ | ✅ | - incremental_lineage<br />- skip_sources_in_lineage<br />- include_column_lineage|
| [Delta Lake](../../generated/ingestion/sources/delta-lake.md) | ❌ | ❌ | |
| [Druid](../../generated/ingestion/sources/druid.md) | ❌ | ❌ | |
| [Elasticsearch](../../generated/ingestion/sources/elasticsearch.md) | ❌ | ❌ | |
| [Feast](../../generated/ingestion/sources/feast.md) | ✅ | ❌ | |
| [File](../../generated/ingestion/sources/file.md) | ❌ | ❌ | |
| [File Based Lineage](../../generated/ingestion/sources/file-based-lineage.md) | ✅ | ✅ | |
| [Fivetran](../../generated/ingestion/sources/fivetran.md) | ❌ | ✅ | - include_column_lineage|
| [Glue](../../generated/ingestion/sources/glue.md) | ✅ | ❌ | - emit_s3_lineage<br />- glue_s3_lineage_direction|
| [Google Cloud Storage](../../generated/ingestion/sources/gcs.md) | ❌ | ❌ | |
| [Hive](../../generated/ingestion/sources/hive.md) | ❌ | ❌ | |
| [Kafka](../../generated/ingestion/sources/kafka.md) | ❌ | ❌ | |
| [Kafka Connect](../../generated/ingestion/sources/kafka-connect.md) | ✅ | ❌ | - convert_lineage_urns_to_lowercase|
| [Looker `looker`](../../generated/ingestion/sources/looker.md) | ✅ | ✅ | - extract_column_level_lineage|
| [Looker `lookml`](../../generated/ingestion/sources/looker.md) | ✅ | ✅ | - extract_column_level_lineage|
| [MariaDB](../../generated/ingestion/sources/mariadb.md) | ❌ | ❌ | |
| [Metabase](../../generated/ingestion/sources/metabase.md) | ✅ | ❌ | |
| [Microsoft SQL Server](../../generated/ingestion/sources/mssql.md) | ❌ | ❌ | |
| [MLflow](../../generated/ingestion/sources/mlflow.md) | ❌ | ❌ | |
| [Mode](../../generated/ingestion/sources/mode.md) | ✅ | ❌ | |
| [MongoDB](../../generated/ingestion/sources/mongodb.md) | ❌ | ❌ | |
| [MySQL](../../generated/ingestion/sources/mysql.md) | ❌ | ❌ | |
| [NiFi](../../generated/ingestion/sources/nifi.md) | ✅ | ❌ | |
| [Okta](../../generated/ingestion/sources/okta.md) | ❌ | ❌ | |
| [Oracle](../../generated/ingestion/sources/oracle.md) | ❌ | ❌ | |
| [Postgres](../../generated/ingestion/sources/postgres.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage|
| [PowerBI `powerbi`](../../generated/ingestion/sources/powerbi.md) | ✅ | ✅ | - extract_lineage<br />- convert_lineage_urns_to_lowercase<br />- enable_advance_lineage_sql_construct<br />- extract_column_level_lineage|
| [PowerBI `powerbi-report-server`](../../generated/ingestion/sources/powerbi.md) | ❌ | ❌ | |
| [Presto](../../generated/ingestion/sources/presto.md) | ❌ | ❌ | |
| [Presto on Hive](../../generated/ingestion/sources/presto-on-hive.md) | ❌ | ❌ | |
| [Qlik Sense](../../generated/ingestion/sources/qlik-sense.md) | ❌ | ❌ | |
| [Redash](../../generated/ingestion/sources/redash.md) | ❌ | ❌ | |
| [Redshift](../../generated/ingestion/sources/redshift.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- s3_lineage_config<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- use_lineage_v2<br />- lineage_v2_generate_queries<br />- include_table_lineage<br />- include_copy_lineage<br />- include_unload_lineage<br />- include_table_rename_lineage<br />- table_lineage_mode<br />- extract_column_level_lineage<br />- resolve_temp_table_in_lineage|
| [S3 Data Lake](../../generated/ingestion/sources/s3.md) | ❌ | ❌ | |
| [SageMaker](../../generated/ingestion/sources/sagemaker.md) | ✅ | ❌ | |
| [Salesforce](../../generated/ingestion/sources/salesforce.md) | ❌ | ❌ | |
| [SAP HANA](../../generated/ingestion/sources/hana.md) | ❌ | ❌ | |
| [Slack](../../generated/ingestion/sources/slack.md) | ❌ | ❌ | |
| [Snowflake](../../generated/ingestion/sources/snowflake.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage<br />- ignore_start_time_lineage<br />- upstream_lineage_in_report<br />- include_column_lineage|
| [SQL Queries](../../generated/ingestion/sources/sql-queries.md) | ✅ | ✅ | |
| [Superset](../../generated/ingestion/sources/superset.md) | ✅ | ❌ | |
| [Tableau](../../generated/ingestion/sources/tableau.md) | ✅ | ✅ | - extract_column_level_lineage<br />- lineage_overrides<br />- extract_lineage_from_unsupported_custom_sql_queries<br />- force_extraction_of_lineage_from_custom_sql_queries|
| [Teradata](../../generated/ingestion/sources/teradata.md) | ✅ | ✅ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage|
| [Trino `trino`](../../generated/ingestion/sources/trino.md) | ❌ | ❌ | |
| [Trino `starburst-trino-usage`](../../generated/ingestion/sources/trino.md) | ❌ | ❌ | |
| [Vertica](../../generated/ingestion/sources/vertica.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_projection_lineage|


### Types of Lineage Connections

Types of lineage connections supported in DataHub and the example codes are as follows.

| Connection          | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | A.K.A           |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Dataset to Dataset  | - [lineage_emitter_mcpw_rest.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_mcpw_rest.py) <br /> - [lineage_emitter_rest.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_rest.py) <br /> - [lineage_emitter_kafka.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_kafka.py) <br /> - [lineage_emitter_dataset_finegrained.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_dataset_finegrained.py) <br /> - [Datahub BigQuery Lineage](https://github.com/datahub-project/datahub/blob/a1bf95307b040074c8d65ebb86b5eb177fdcd591/metadata-ingestion/src/datahub/ingestion/source/sql/bigquery.py#L229) <br /> - [Datahub Snowflake Lineage](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/sql/snowflake.py#L249) |
| DataJob to DataFlow | - [lineage_job_dataflow.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_job_dataflow.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |    |
| DataJob to Dataset  | - [lineage_dataset_job_dataset.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_dataset_job_dataset.py) <br /> | Pipeline Lineage |
| Chart to Dashboard  | - [lineage_chart_dashboard.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_chart_dashboard.py)  |  |
| Chart to Dataset    | - [lineage_dataset_chart.py](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_dataset_chart.py)  |  |


:::tip Our Roadmap
We're actively working on expanding lineage support for new data sources.
Visit our [Official Roadmap](https://feature-requests.datahubproject.io/roadmap) for upcoming updates!
:::

## References

- [DataHub Basics: Lineage 101](https://www.youtube.com/watch?v=rONGpsndzRw&t=1s)
- [DataHub November 2022 Town Hall](https://www.youtube.com/watch?v=BlCLhG8lGoY&t=1s) - Including Manual Lineage Demo
- [Acryl Data introduces lineage support and automated propagation of governance information for Snowflake in DataHub](https://blog.datahubproject.io/acryl-data-introduces-lineage-support-and-automated-propagation-of-governance-information-for-339c99536561)
- [Data in Context: Lineage Explorer in DataHub](https://blog.datahubproject.io/data-in-context-lineage-explorer-in-datahub-a53a9a476dc4)
- [Harnessing the Power of Data Lineage with DataHub](https://blog.datahubproject.io/harnessing-the-power-of-data-lineage-with-datahub-ad086358dec4)
- [DataHub Lineage Impact Analysis](../../act-on-metadata/impact-analysis.md)
                        
