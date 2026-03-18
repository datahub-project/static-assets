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

Data lineage is a **map that shows how data flows through your organization.** It details where your data originates, how it travels, and where it ultimately ends up. 
This can happen within a single system (like data moving between Snowflake tables) or across various platforms.

With data lineage, you can
- Maintaining Data Integrity
- Simplify and Refine Complex Relationships
- Perform [Lineage Impact Analysis](../../act-on-metadata/impact-analysis.md)
- [Propagate Metadata](https://blog.datahubproject.io/acryl-data-introduces-lineage-support-and-automated-propagation-of-governance-information-for-339c99536561) Across Lineage


## Viewing Lineage

You can view lineage under **Lineage** tab or **Lineage Visualization** screen.


<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/lineage-tab.png" />
</p>

By default, The UI shows the latest version of the lineage. The time picker can be used to filter out edges within the latest version to exclude those that were last updated outside of the time window. Selecting time windows in the patch will not show you historical lineages. It will only filter the view of the latest version of the lineage.

<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/lineage-view.png" />
</p>

In this example, data flows from Airflow/BigQuery to Snowflake tables, then to the Hive dataset, and ultimately to the features of Machine Learning Models.


:::tip The Lineage Tab is greyed out - why can’t I click on it?
This means you have not yet ingested lineage metadata for that entity. Please ingest lineage to proceed.

:::

## Column Level Lineage Support

Column-level lineage **tracks changes and movements for each specific data column.** This approach is often contrasted with table-level lineage, which specifies lineage at the table level.
Below is how column-level lineage can be set with dbt and Postgres tables.

<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/column-level-lineage.png" />
</p>

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

DataHub supports **[automatic table- and column-level lineage detection](#automatic-lineage-extraction-support)** from BigQuery, Snowflake, dbt, Looker, PowerBI, and 20+ modern data tools. 
For data tools with limited native lineage tracking, **DataHub's SQL Parser** detects lineage with 97–99% accuracy, ensuring teams will have high quality lineage graphs across all corners of their data stack.

### Types of Lineage Connections

Types of lineage connections supported in DataHub and the example codes are as follows.

* Dataset to Dataset
    * [Dataset Lineage](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_rest.py)
    * [Finegrained Dataset Lineage](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_dataset_finegrained.py)
    * [Datahub BigQuery Lineage](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/sql/snowflake.py#L249)
    * [Dataset Lineage via MCPW REST Emitter](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_mcpw_rest.py)
    * [Dataset Lineage via Kafka Emitter](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_emitter_kafka.py)
* [DataJob to DataFlow](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_job_dataflow.py)
* [DataJob to Dataset](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_dataset_job_dataset.py)
* [Chart to Dashboard](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_chart_dashboard.py)
* [Chart to Dataset](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/lineage_dataset_chart.py)

### Automatic Lineage Extraction Support

This is a summary of automatic lineage extraciton support in our data source. Please refer to the **Important Capabilities** table in the source documentation. Note that even if the source does not support automatic extraction, you can still add lineage manually using our API & SDKs.

| Source | Table-Level Lineage | Column-Level Lineage | Related Configs |
| ---------- | ------ | ----- |----- |
| [ABS Data Lake](../../generated/ingestion/sources/abs.md) | ❌ | ❌ | |
| [Athena](../../generated/ingestion/sources/athena.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage|
| [BigQuery](../../generated/ingestion/sources/bigquery.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- include_table_location_lineage<br />- gcs_lineage_config<br />- lineage_use_sql_parser<br />- lineage_parse_view_ddl<br />- lineage_sql_parser_use_raw_names<br />- extract_column_lineage<br />- extract_lineage_from_catalog<br />- include_table_lineage<br />- include_column_lineage_with_gcs<br />- upstream_lineage_in_report|
| [Business Glossary](../../generated/ingestion/sources/business-glossary.md) | ❌ | ❌ | |
| [Cassandra](../../generated/ingestion/sources/cassandra.md) | ❌ | ❌ | |
| [ClickHouse `clickhouse`](../../generated/ingestion/sources/clickhouse.md) | ❌ | ❌ | |
| [ClickHouse `clickhouse-usage`](../../generated/ingestion/sources/clickhouse.md) | ❌ | ❌ | |
| [CockroachDB](../../generated/ingestion/sources/cockroachdb.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage|
| [CSV Enricher](../../generated/ingestion/sources/csv-enricher.md) | ❌ | ❌ | |
| [Databricks](../../generated/ingestion/sources/databricks.md) | ✅ | ✅ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage<br />- include_external_lineage<br />- include_column_lineage<br />- column_lineage_column_limit|
| [DataHub](../../generated/ingestion/sources/datahub.md) | ❌ | ❌ | |
| [DataHubGc](../../generated/ingestion/sources/datahubgc.md) | ❌ | ❌ | |
| [dbt `dbt`](../../generated/ingestion/sources/dbt.md) | ✅ | ✅ | - incremental_lineage<br />- prefer_sql_parser_lineage<br />- skip_sources_in_lineage<br />- include_column_lineage|
| [dbt `dbt-cloud`](../../generated/ingestion/sources/dbt.md) | ✅ | ✅ | - incremental_lineage<br />- prefer_sql_parser_lineage<br />- skip_sources_in_lineage<br />- include_column_lineage|
| [Delta Lake](../../generated/ingestion/sources/delta-lake.md) | ❌ | ❌ | |
| [Dremio](../../generated/ingestion/sources/dremio.md) | ✅ | ❌ | - include_query_lineage|
| [Druid](../../generated/ingestion/sources/druid.md) | ❌ | ❌ | |
| [Elasticsearch](../../generated/ingestion/sources/elasticsearch.md) | ❌ | ❌ | |
| [Feast](../../generated/ingestion/sources/feast.md) | ✅ | ❌ | |
| [File Based Lineage](../../generated/ingestion/sources/file-based-lineage.md) | ✅ | ✅ | |
| [Fivetran](../../generated/ingestion/sources/fivetran.md) | ❌ | ✅ | - include_column_lineage|
| [Glue](../../generated/ingestion/sources/glue.md) | ✅ | ❌ | - emit_s3_lineage<br />- glue_s3_lineage_direction<br />- include_column_lineage|
| [Google Cloud Storage](../../generated/ingestion/sources/gcs.md) | ❌ | ❌ | |
| [Grafana](../../generated/ingestion/sources/grafana.md) | ❌ | ❌ | |
| [Hive](../../generated/ingestion/sources/hive.md) | ❌ | ❌ | |
| [Hive Metastore `hive-metastore`](../../generated/ingestion/sources/hive-metastore.md) | ❌ | ❌ | |
| [Hive Metastore `presto-on-hive`](../../generated/ingestion/sources/hive-metastore.md) | ❌ | ❌ | |
| [Kafka](../../generated/ingestion/sources/kafka.md) | ❌ | ❌ | |
| [Kafka Connect](../../generated/ingestion/sources/kafka-connect.md) | ✅ | ❌ | - convert_lineage_urns_to_lowercase|
| [Looker `looker`](../../generated/ingestion/sources/looker.md) | ✅ | ✅ | - extract_column_level_lineage|
| [Looker `lookml`](../../generated/ingestion/sources/looker.md) | ✅ | ✅ | - extract_column_level_lineage|
| [MariaDB](../../generated/ingestion/sources/mariadb.md) | ❌ | ❌ | |
| [Metabase](../../generated/ingestion/sources/metabase.md) | ✅ | ❌ | |
| [Metadata File `file`](../../generated/ingestion/sources/metadata-file.md) | ❌ | ❌ | |
| [Metadata File `metadata-file`](../../generated/ingestion/sources/metadata-file.md) | ❌ | ❌ | |
| [Microsoft SQL Server](../../generated/ingestion/sources/mssql.md) | ❌ | ❌ | |
| [MLflow](../../generated/ingestion/sources/mlflow.md) | ❌ | ❌ | |
| [Mode](../../generated/ingestion/sources/mode.md) | ✅ | ✅ | |
| [MongoDB](../../generated/ingestion/sources/mongodb.md) | ❌ | ❌ | |
| [MySQL](../../generated/ingestion/sources/mysql.md) | ❌ | ❌ | |
| [Neo4j](../../generated/ingestion/sources/neo4j.md) | ❌ | ❌ | |
| [NiFi](../../generated/ingestion/sources/nifi.md) | ✅ | ❌ | - incremental_lineage|
| [Okta](../../generated/ingestion/sources/okta.md) | ❌ | ❌ | |
| [Oracle](../../generated/ingestion/sources/oracle.md) | ❌ | ❌ | |
| [Postgres](../../generated/ingestion/sources/postgres.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage|
| [PowerBI `powerbi`](../../generated/ingestion/sources/powerbi.md) | ✅ | ✅ | - extract_lineage<br />- convert_lineage_urns_to_lowercase<br />- enable_advance_lineage_sql_construct<br />- extract_column_level_lineage|
| [PowerBI `powerbi-report-server`](../../generated/ingestion/sources/powerbi.md) | ❌ | ❌ | |
| [Preset](../../generated/ingestion/sources/preset.md) | ✅ | ❌ | |
| [Presto](../../generated/ingestion/sources/presto.md) | ❌ | ❌ | |
| [Qlik Sense](../../generated/ingestion/sources/qlik-sense.md) | ✅ | ✅ | |
| [Redash](../../generated/ingestion/sources/redash.md) | ✅ | ❌ | |
| [Redshift](../../generated/ingestion/sources/redshift.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- s3_lineage_config<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- use_lineage_v2<br />- lineage_v2_generate_queries<br />- include_table_lineage<br />- include_copy_lineage<br />- include_unload_lineage<br />- include_table_rename_lineage<br />- table_lineage_mode<br />- extract_column_level_lineage<br />- resolve_temp_table_in_lineage|
| [S3 / Local Files](../../generated/ingestion/sources/s3.md) | ❌ | ❌ | |
| [SageMaker](../../generated/ingestion/sources/sagemaker.md) | ✅ | ❌ | |
| [Salesforce](../../generated/ingestion/sources/salesforce.md) | ❌ | ❌ | |
| [SAP Analytics Cloud](../../generated/ingestion/sources/sac.md) | ✅ | ❌ | - incremental_lineage|
| [SAP HANA](../../generated/ingestion/sources/hana.md) | ❌ | ❌ | |
| [Sigma](../../generated/ingestion/sources/sigma.md) | ✅ | ❌ | - extract_lineage<br />- workbook_lineage_pattern|
| [Slack](../../generated/ingestion/sources/slack.md) | ❌ | ❌ | |
| [Snowflake](../../generated/ingestion/sources/snowflake.md) | ✅ | ✅ | - enable_stateful_lineage_ingestion<br />- incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage<br />- ignore_start_time_lineage<br />- upstream_lineage_in_report<br />- include_column_lineage|
| [SQL Queries](../../generated/ingestion/sources/sql-queries.md) | ✅ | ✅ | |
| [Superset](../../generated/ingestion/sources/superset.md) | ✅ | ❌ | |
| [Tableau](../../generated/ingestion/sources/tableau.md) | ✅ | ✅ | - extract_column_level_lineage<br />- lineage_overrides<br />- extract_lineage_from_unsupported_custom_sql_queries<br />- force_extraction_of_lineage_from_custom_sql_queries|
| [Teradata](../../generated/ingestion/sources/teradata.md) | ✅ | ✅ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_table_lineage|
| [Trino `trino`](../../generated/ingestion/sources/trino.md) | ❌ | ❌ | |
| [Trino `starburst-trino-usage`](../../generated/ingestion/sources/trino.md) | ❌ | ❌ | |
| [Vertica](../../generated/ingestion/sources/vertica.md) | ✅ | ❌ | - incremental_lineage<br />- include_table_location_lineage<br />- include_view_lineage<br />- include_view_column_lineage<br />- include_projection_lineage|

        
### SQL Parser Lineage Extraction

If you’re using a different database system for which we don’t support column-level lineage out of the box, but you do have a database query log available, 
we have a SQL queries connector that generates column-level lineage and detailed table usage statistics from the query log.

If these does not suit your needs, you can use the new `DataHubGraph.parse_sql_lineage()` method in our SDK. (See the source code [here](/docs/python-sdk/clients/))

For more information, refer to the [Extracting Column-Level Lineage from SQL](https://blog.datahubproject.io/extracting-column-level-lineage-from-sql-779b8ce17567) 


:::tip Our Roadmap
We're actively working on expanding lineage support for new data sources.
Visit our [Official Roadmap](https://feature-requests.datahubproject.io/roadmap) for upcoming updates!
:::

## References

- [DataHub Basics: Lineage 101](https://www.youtube.com/watch?v=rONGpsndzRw&t=1s)
- [DataHub November 2022 Town Hall](https://www.youtube.com/watch?v=BlCLhG8lGoY&t=1s) - Including Manual Lineage Demo
- [Data in Context: Lineage Explorer in DataHub](https://blog.datahubproject.io/data-in-context-lineage-explorer-in-datahub-a53a9a476dc4)
- [Harnessing the Power of Data Lineage with DataHub](https://blog.datahubproject.io/harnessing-the-power-of-data-lineage-with-datahub-ad086358dec4)
- [Data Lineage: What It Is And Why It Matters](https://blog.datahubproject.io/data-lineage-what-it-is-and-why-it-matters-1a8d9846f0bd)
                        
