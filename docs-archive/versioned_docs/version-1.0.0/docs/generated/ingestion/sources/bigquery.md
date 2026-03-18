---
sidebar_position: 4
title: BigQuery
slug: /generated/ingestion/sources/bigquery
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/bigquery.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BigQuery
Ingesting metadata from BigQuery requires using the **bigquery** module.
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md) | ✅ | Optionally enabled via `classification.enabled` |
| Column-level Lineage | ✅ | Optionally enabled via configuration |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Optionally enabled via configuration |
| Dataset Usage | ✅ | Enabled by default, can be disabled via configuration `include_usage_statistics` |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Domains](../../../domains.md) | ✅ | Supported via the `domain` config field |
| Partition Support | ✅ | Enabled by default, partition keys and clustering keys are supported. |
| [Platform Instance](../../../platform-instances.md) | ❌ | Platform instance is pre-set to the BigQuery project id |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Optionally enabled via configuration |


### Prerequisites
To understand how BigQuery ingestion needs to be set up, first familiarize yourself with the concepts in the diagram below:
<p align="center">
  <img width="70%"  src="https://github.com/datahub-project/static-assets/raw/main/imgs/integrations/bigquery/source-bigquery-setup.png"/>
</p>

There are two important concepts to understand and identify:
- *Extractor Project*: This is the project associated with a service-account, whose credentials you will be configuring in the connector. The connector uses this service-account to run jobs (including queries) within the project.
- *Bigquery Projects* are the projects from which table metadata, lineage, usage, and profiling data need to be collected. By default, the extractor project is included in the list of projects that DataHub collects metadata from, but you can control that by passing in a specific list of project ids that you want to collect metadata from. Read the configuration section below to understand how to limit the list of projects that DataHub extracts metadata from. 

#### Create a datahub profile in GCP
1. Create a custom role for datahub as per [BigQuery docs](https://cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).
2. Follow the sections below to grant permissions to this role on this project and other projects.

##### Basic Requirements (needed for metadata ingestion)
1. Identify your Extractor Project where the service account will run queries to extract metadata.

| permission                       | Description                                                                                                                                                                                                                          | Capability                                                                                                    |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `bigquery.jobs.create`           | Run jobs (e.g. queries) within the project. *This only needs for the extractor project where the service account belongs*                                                                                                            |                                                                                                               |
| `bigquery.jobs.list`             | Manage the queries that the service account has sent. *This only needs for the extractor project where the service account belongs*                                                                                                  |                                                                                                               |
| `bigquery.readsessions.create`   | Create a session for streaming large results. *This only needs for the extractor project where the service account belongs*                                                                                                          |                                                                                                               |
| `bigquery.readsessions.getData`  | Get data from the read session. *This only needs for the extractor project where the service account belongs*                                                                                                                        |
2. Grant the following permissions to the Service Account on every project where you would like to extract metadata from

:::info

If you have multiple projects in your BigQuery setup, the role should be granted these permissions in each of the projects.

:::
| Permission                        | Description                                                                                                     | Capability                           | Default GCP Role Which Contains This Permission                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------|
| `bigquery.datasets.get`           | Retrieve metadata about a dataset.                                                                               | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.datasets.getIamPolicy`  | Read a dataset's IAM permissions.                                                                                | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.tables.list`            | List BigQuery tables.                                                                                           | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.tables.get`             | Retrieve metadata for a table.                                                                                  | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.routines.get`           | Get Routines. Needs to retrieve metadata for a table from system table.                                          | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.routines.list`          | List Routines. Needs to retrieve metadata for a table from system table.                                         | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `resourcemanager.projects.get`    | Retrieve project names and metadata.                                                                            | Table Metadata Extraction           | [roles/bigquery.metadataViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)  |
| `bigquery.jobs.listAll`           | List all jobs (queries) submitted by any user. Needs for Lineage extraction.                                    | Lineage Extraction/Usage Extraction | [roles/bigquery.resourceViewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.resourceViewer)  |
| `logging.logEntries.list`         | Fetch log entries for lineage/usage data. Not required if `use_exported_bigquery_audit_metadata` is enabled.    | Lineage Extraction/Usage Extraction | [roles/logging.privateLogViewer](https://cloud.google.com/logging/docs/access-control#logging.privateLogViewer) |
| `logging.privateLogEntries.list`  | Fetch log entries for lineage/usage data. Not required if `use_exported_bigquery_audit_metadata` is enabled.    | Lineage Extraction/Usage Extraction | [roles/logging.privateLogViewer](https://cloud.google.com/logging/docs/access-control#logging.privateLogViewer) |
| `bigquery.tables.getData`         | Access table data to extract storage size, last updated at, data profiles etc.                                   | Profiling                           |                                                                           |
| `datacatalog.policyTags.get`      | *Optional* Get policy tags for columns with associated policy tags. This permission is required only if `extract_policy_tags_from_catalog` is enabled.       | Policy Tag Extraction               | [roles/datacatalog.viewer](https://cloud.google.com/data-catalog/docs/access-control#permissions-and-roles)    |


#### Create a service account in the Extractor Project

1. Setup a ServiceAccount as per [BigQuery docs](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console)
   and assign the previously created role to this service account.
2. Download a service account JSON keyfile.
   Example credential file:

```json
{
   "type": "service_account",
   "project_id": "project-id-1234567",
   "private_key_id": "d0121d0000882411234e11166c6aaa23ed5d74e0",
   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIyourkey\n-----END PRIVATE KEY-----",
   "client_email": "test@suppproject-id-1234567.iam.gserviceaccount.com",
   "client_id": "113545814931671546333",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test%suppproject-id-1234567.iam.gserviceaccount.com"
}
```

3. To provide credentials to the source, you can either:

   Set an environment variable:

   ```sh
   $ export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
   ```

   _or_

   Set credential config in your source based on the credential json file. For example:

   ```yml
   credential:
     project_id: project-id-1234567
     private_key_id: "d0121d0000882411234e11166c6aaa23ed5d74e0"
     private_key: "-----BEGIN PRIVATE KEY-----\nMIIyourkey\n-----END PRIVATE KEY-----\n"
     client_email: "test@suppproject-id-1234567.iam.gserviceaccount.com"
     client_id: "123456678890"
   ```

##### Profiling Requirements

To profile BigQuery external tables backed by Google Drive document, you need to grant document's "Viewer" access to service account's email address (`client_email` in credentials json file). To find the Google Drive document linked to BigQuery table, open the BigQuery console, locate the needed table,  select "Details" from the drop-down menu in the top-right corner and refer "Source" field . To share access of Google Drive document, open the document, click "Share" in the top-right corner, add the service account's email address that needs "Viewer" access. ![Google Drive Sharing Dialog](https://github.com/datahub-project/static-assets/raw/main/imgs/integrations/bigquery/google_drive_share.png)
 
### Lineage Computation Details

When `use_exported_bigquery_audit_metadata` is set to `true`, lineage information will be computed using exported bigquery logs. On how to setup exported bigquery audit logs, refer to the following [docs](https://cloud.google.com/bigquery/docs/reference/auditlogs#defining_a_bigquery_log_sink_using_gcloud) on BigQuery audit logs. Note that only protoPayloads with "type.googleapis.com/google.cloud.audit.BigQueryAuditMetadata" are supported by the current ingestion version. The `bigquery_audit_metadata_datasets` parameter will be used only if `use_exported_bigquery_audit_metadat` is set to `true`.

Note: the `bigquery_audit_metadata_datasets` parameter receives a list of datasets, in the format $PROJECT.$DATASET. This way queries from a multiple number of projects can be used to compute lineage information.

Note: Since bigquery source also supports dataset level lineage, the auth client will require additional permissions to be able to access the google audit logs. Refer the permissions section in bigquery-usage section below which also accesses the audit logs.

### Profiling Details

For performance reasons, we only profile the latest partition for partitioned tables and the latest shard for sharded tables.
You can set partition explicitly with `partition.partition_datetime` property if you want, though note that partition config will be applied to all partitioned tables.

### Caveats

- For materialized views, lineage is dependent on logs being retained. If your GCP logging is retained for 30 days (default) and 30 days have passed since the creation of the materialized view we won't be able to get lineage for them.

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: bigquery
  config:
    dataset_pattern:
      allow:
        - finance_bq_dataset
    table_pattern:
      deny:
        # The exact name of the table is revenue_table_name
        # The reason we have this `.*` at the beginning is because the current implmenetation of table_pattern is testing
        # project_id.dataset_name.table_name
        # We will improve this in the future
        - .*revenue_table_name
    include_table_lineage: true
    include_usage_statistics: true
    profiling:
      enabled: true
      profile_table_level_only: true

sink:
  # sink configs

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">bucket_duration</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Size of the time window to aggregate usage stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">DAY</span></div> |
| <div className="path-line"><span className="path-main">column_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of columns to process in a table. This is a low level config property which should be touched with care. This restriction is needed because excessively wide tables can result in failure to ingest the schema. <div className="default-line default-line-with-docs">Default: <span className="default-value">300</span></div> |
| <div className="path-line"><span className="path-main">convert_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert dataset urns to lowercase. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">debug_include_full_payloads</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include full payload into events. It is only for debugging and internal use. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">enable_legacy_sharded_table_support</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use the legacy sharded table urn suffix added. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">enable_stateful_lineage_ingestion</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable stateful lineage ingestion. This will store lineage window timestamps after successful lineage ingestion. and will not run lineage ingestion for same timestamps in subsequent run.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">enable_stateful_profiling</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable stateful profiling. This will store profiling timestamps per dataset after successful profiling. and will not run profiling again in subsequent run if table has not been updated.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">enable_stateful_usage_ingestion</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable stateful lineage ingestion. This will store usage window timestamps after successful usage ingestion. and will not run usage ingestion for same timestamps in subsequent run.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">end_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Latest date of lineage/usage to consider. Default: Current time in UTC  |
| <div className="path-line"><span className="path-main">exclude_empty_projects</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to exclude empty projects from being ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extra_client_options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Additional options to pass to google.cloud.logging_v2.client.Client. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-main">extract_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, generate column level lineage. Requires lineage_use_sql_parser to be enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_lineage_from_catalog</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | This flag enables the data lineage extraction from Data Lineage API exposed by Google Data Catalog. NOTE: This extractor can't build views lineage. It's recommended to enable the view's DDL parsing. Read the docs to have more information about: https://cloud.google.com/data-catalog/docs/concepts/about-data-lineage <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_policy_tags_from_catalog</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | This flag enables the extraction of policy tags from the Google Data Catalog API. When enabled, the extractor will fetch policy tags associated with BigQuery table columns. For more information about policy tags and column-level security, refer to the documentation: https://cloud.google.com/bigquery/docs/column-level-security-intro <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_column_lineage_with_gcs</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, column-level lineage will be extracted from the gcs. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_data_platform_instance</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to create a DataPlatformInstance aspect, equal to the BigQuery project id. If enabled, will cause redundancy in the browse path for BigQuery entities in the UI, because the project id is represented as the top-level container. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_external_url</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to populate BigQuery Console url to Datasets/Tables <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, generate query entities associated with lineage edges. Only applicable if `use_queries_v2` is enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_query_usage_statistics</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, generate query popularity statistics. Only applicable if `use_queries_v2` is enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_schema_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the BigQuery schema, i.e. projects, schemas, tables, and views. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_table_constraints</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest table constraints. If you know you don't use table constraints, you can disable it to save one extra query per dataset. In general it should be enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_table_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable lineage generation. Is enabled by default. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_table_location_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If the source supports it, include table lineage to the underlying storage location. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_table_snapshots</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether table snapshots should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether tables should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_usage_statistics</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Generate usage statistic <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates column-level lineage for  view->view and table->view lineage using DataHub's sql parser. Requires `include_view_lineage` to be enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates view->view and table->view lineage using DataHub's sql parser. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_views</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether views should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">incremental_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, emits lineage as incremental to existing lineage already in DataHub. When disabled, re-states lineage on each run. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">lineage_sql_parser_use_raw_names</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | This parameter ignores the lowercase pattern stipulated in the SQLParser. NOTE: Ignored if lineage_use_sql_parser is False. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">lineage_use_sql_parser</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use sql parser to resolve view/table lineage. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">log_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of log item will be queried per page for lineage collection <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-main">match_fully_qualified_names</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | [deprecated] Whether `dataset_pattern` is matched against fully qualified dataset name `<project_id>.<dataset_name>`. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">max_query_duration</span></div> <div className="type-name-line"><span className="type-name">number(time-delta)</span></div> | Correction to pad start_time and end_time with. For handling the case where the read happens within our time range but the query completion event is delayed and happens after the configured end time. <div className="default-line default-line-with-docs">Default: <span className="default-value">900.0</span></div> |
| <div className="path-line"><span className="path-main">max_threads_dataset_parallelism</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use to parallelize BigQuery Dataset Metadata Extraction. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">20</span></div> |
| <div className="path-line"><span className="path-main">number_of_datasets_process_in_batch_if_profiling_enabled</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of partitioned table queried in batch when getting metadata. This is a low level config property which should be touched with care. This restriction is needed because we query partitions system view which throws error if we try to touch too many tables. <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">project_on_behalf</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | [Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account.  |
| <div className="path-line"><span className="path-main">rate_limit</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Should we rate limit requests made to API. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">requests_per_min</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Used to control number of API calls made per min. Only used when `rate_limit` is set to `True`. <div className="default-line default-line-with-docs">Default: <span className="default-value">60</span></div> |
| <div className="path-line"><span className="path-main">schema_resolution_batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of tables to process in a batch when resolving schema from DataHub. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">bigquery</span></div> |
| <div className="path-line"><span className="path-main">sharded_table_pattern</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The regex pattern to match sharded tables and group as one table. This is a very low level config parameter, only change if you know what you are doing,  <div className="default-line default-line-with-docs">Default: <span className="default-value">((.+\D)&#91;&#95;$&#93;?)?(\d\d\d\d(?:0&#91;1-9&#93;&#124;1&#91;0-2&#93;)(?:0&#91;1-9&#93;&#124;...</span></div> |
| <div className="path-line"><span className="path-main">start_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.  |
| <div className="path-line"><span className="path-main">temp_table_dataset_prefix</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | If you are creating temp tables in a dataset with a particular prefix you can use this config to set the prefix for the dataset. This is to support workflows from before bigquery's introduction of temp tables. By default we use `_` because of datasets that begin with an underscore are hidden by default https://cloud.google.com/bigquery/docs/datasets#dataset-naming. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#95;</span></div> |
| <div className="path-line"><span className="path-main">upstream_lineage_in_report</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Useful for debugging lineage information. Set to True to see the raw lineage created internally. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">use_date_sharded_audit_log_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to read date sharded tables or time partitioned tables when extracting usage from exported audit logs. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">use_exported_bigquery_audit_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When configured, use BigQueryAuditMetadata in bigquery_audit_metadata_datasets to compute lineage information. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">use_file_backed_cache</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to use a file backed cache for the view definitions. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">use_queries_v2</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, uses the new queries extractor to extract queries from bigquery. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">use_tables_list_query_v2</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | List tables using an improved query that extracts partitions and last modified timestamps more accurately. Requires the ability to read table data. Automatically enabled when profiling is enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">bigquery_audit_metadata_datasets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | A list of datasets that contain a table named cloudaudit_googleapis_com_data_access which contain BigQuery audit logs, specifically, those containing BigQueryAuditMetadata. It is recommended that the project of the dataset is also specified, for example, projectA.datasetB.  |
| <div className="path-line"><span className="path-prefix">bigquery_audit_metadata_datasets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">capture_dataset_label_as_tag</span></div> <div className="type-name-line"><span className="type-name">One of boolean, AllowDenyPattern</span></div> | Capture BigQuery dataset labels as DataHub tag <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">capture_dataset_label_as_tag.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">capture_dataset_label_as_tag.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_dataset_label_as_tag.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">capture_dataset_label_as_tag.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_dataset_label_as_tag.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">capture_table_label_as_tag</span></div> <div className="type-name-line"><span className="type-name">One of boolean, AllowDenyPattern</span></div> | Capture BigQuery table labels as DataHub tag <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">capture_table_label_as_tag.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">capture_table_label_as_tag.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_table_label_as_tag.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">capture_table_label_as_tag.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_table_label_as_tag.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">capture_view_label_as_tag</span></div> <div className="type-name-line"><span className="type-name">One of boolean, AllowDenyPattern</span></div> | Capture BigQuery view labels as DataHub tag <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">capture_view_label_as_tag.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">capture_view_label_as_tag.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_view_label_as_tag.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">capture_view_label_as_tag.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">capture_view_label_as_tag.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">credential</span></div> <div className="type-name-line"><span className="type-name">BigQueryCredential</span></div> | BigQuery credential informations  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_email</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client email  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client Id  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">private_key</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n'  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">private_key_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key id  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">project_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Project id to set the credentials  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">auth_provider_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Auth provider x509 certificate url <div className="default-line default-line-with-docs">Default: <span className="default-value">https://www.googleapis.com/oauth2/v1/certs</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">auth_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://accounts.google.com/o/oauth2/auth</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">token_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Token uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://oauth2.googleapis.com/token</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication type <div className="default-line default-line-with-docs">Default: <span className="default-value">service&#95;account</span></div> |
| <div className="path-line"><span className="path-main">dataset_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for dataset to filter in ingestion. Specify regex to only match the schema name. e.g. to match all tables in schema analytics, use the regex 'analytics' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">map(str,AllowDenyPattern)</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">gcs_lineage_config</span></div> <div className="type-name-line"><span className="type-name">GcsLineageProviderConfig</span></div> | Common config for gcs lineage generation <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;path&#95;specs&#x27;: &#91;&#93;, &#x27;strip&#95;urls&#x27;: True, &#x27;ignore&#95;non...</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.</span><span className="path-main">ignore_non_path_spec_path</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ignore paths that are not match in path_specs. It only applies if path_specs are specified. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.</span><span className="path-main">strip_urls</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Strip filename from gcs url. It only applies if path_specs are not specified. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.</span><span className="path-main">path_specs</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of PathSpec. See below the details about PathSpec <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.</span><span className="path-main">PathSpec</span></div> <div className="type-name-line"><span className="type-name">PathSpec</span></div> |   |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">include</span>&nbsp;<abbr title="Required if PathSpec is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to table. Name variable `{table}` is used to mark the folder with dataset. In absence of `{table}`, file level dataset will be created. Check below examples for more details.  |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">allow_double_stars</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Allow double stars in the include path. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">autodetect_partitions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Autodetect partition(s) from the path. If set to true, it will autodetect partition key/value if the folder format is {partition_key}={partition_value} for example `year=2024` <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">default_extension</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | For files without extension it will assume the specified file type. If it is not set the files without extensions will be skipped.  |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">enable_compression</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable or disable processing compressed files. Currently .gz and .bz files are supported. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">include_hidden_folders</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include hidden folders in the traversal (folders starting with . or _ <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">sample_files</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Not listing all the files but only taking a handful amount of sample file to infer the schema. File count and file size calculation will be disabled. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">table_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Display name of the dataset.Combination of named variables from include path and strings  |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">traversal_method</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Method to traverse the folder. ALL: Traverse all the folders, MIN_MAX: Traverse the folders by finding min and max value, MAX: Traverse the folder with max value <div className="default-line default-line-with-docs">Default: <span className="default-value">MAX</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">exclude</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | list of paths in glob pattern which will be excluded while scanning for the datasets <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.exclude.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.</span><span className="path-main">file_types</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Files with extenstions specified here (subset of default value) only will be scanned to create dataset. Other files will be omitted. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;csv&#x27;, &#x27;tsv&#x27;, &#x27;json&#x27;, &#x27;parquet&#x27;, &#x27;avro&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">gcs_lineage_config.path_specs.PathSpec.file_types.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profile_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter tables (or specific columns) for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">project_id_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for project_id to filter in ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">project_id_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">project_id_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_id_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">project_id_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_id_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">project_ids</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Ingests specified project_ids. Use this property if you want to specify what projects to ingest or don't want to give project resourcemanager.projects.list to your service account. Overrides `project_id_pattern`.  |
| <div className="path-line"><span className="path-prefix">project_ids.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">project_labels</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Ingests projects with the specified labels. Set value in the format of `key:value`. Use this property to define which projects to ingest basedon project-level labels. If project_ids or project_id is set, this configuration has no effect. The ingestion process filters projects by label first, and then applies the project_id_pattern.  |
| <div className="path-line"><span className="path-prefix">project_labels.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">region_qualifiers</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | BigQuery regions to be scanned for bigquery jobs when using `use_queries_v2`. See [this](https://cloud.google.com/bigquery/docs/information-schema-jobs#scope_and_syntax) for details. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;region-us&#x27;, &#x27;region-eu&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">region_qualifiers.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. Specify regex to match the entire table name in database.schema.table format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">table_snapshot_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for table snapshots to filter in ingestion. Specify regex to match the entire snapshot name in database.schema.snapshot format. e.g. to match all snapshots starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_snapshot_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">table_snapshot_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_snapshot_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_snapshot_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_snapshot_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">usage</span></div> <div className="type-name-line"><span className="type-name">BigQueryUsageConfig</span></div> | Usage related configs <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;bucket&#95;duration&#x27;: &#x27;DAY&#x27;, &#x27;end&#95;time&#x27;: &#x27;2025-05-08...</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">apply_view_usage_to_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to apply view's usage to its base tables. If set to False, uses sql parser and applies usage to views / tables mentioned in the query. If set to True, usage is applied to base tables only. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">bucket_duration</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Size of the time window to aggregate usage stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">DAY</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">end_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Latest date of lineage/usage to consider. Default: Current time in UTC  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">format_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to format sql queries <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to display operational stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_read_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report read operational stats. Experimental. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_top_n_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the top_n_queries. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">max_query_duration</span></div> <div className="type-name-line"><span className="type-name">number(time-delta)</span></div> | Correction to pad start_time and end_time with. For handling the case where the read happens within our time range but the query completion event is delayed and happens after the configured end time. <div className="default-line default-line-with-docs">Default: <span className="default-value">900.0</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">start_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">top_n_queries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of top queries to save to each table. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">user_email_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | regex patterns for user emails to filter in usage. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">view_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for views to filter in ingestion. Note: Defaults to table_pattern if not specified. Specify regex to match the entire view name in database.schema.view format. e.g. to match all views starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">classification</span></div> <div className="type-name-line"><span className="type-name">ClassificationConfig</span></div> | For details, refer to [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md). <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;sample&#95;size&#x27;: 100, &#x27;max&#95;worker...</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether classification should be used to auto-detect glossary terms <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">info_type_to_term</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker processes to use for classification. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">sample_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of sample values used for classification. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">classifiers</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Classifiers to use to auto-detect glossary terms. If more than one classifier, infotype predictions from the classifier defined later in sequence take precedance. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#123;&#x27;type&#x27;: &#x27;datahub&#x27;, &#x27;config&#x27;: None&#125;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.classifiers.</span><span className="path-main">DynamicTypedClassifierConfig</span></div> <div className="type-name-line"><span className="type-name">DynamicTypedClassifierConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.classifiers.DynamicTypedClassifierConfig.</span><span className="path-main">type</span>&nbsp;<abbr title="Required if DynamicTypedClassifierConfig is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The type of the classifier to use. For DataHub,  use `datahub`  |
| <div className="path-line"><span className="path-prefix">classification.classifiers.DynamicTypedClassifierConfig.</span><span className="path-main">config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | The configuration required for initializing the classifier. If not specified, uses defaults for classifer type.  |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">column_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter columns for classification. This is used in combination with other patterns in parent config. Specify regex to match the column name in `database.schema.table.column` format. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.column_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">classification.column_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.column_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.column_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.column_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter tables for classification. This is used in combination with other patterns in parent config. Specify regex to match the entire table name in `database.schema.table` format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">classification.table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.table_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">classification.table_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">GEProfilingConfig</span></div> |  <div className="default-line ">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;operation&#95;config&#x27;: &#123;&#x27;lower&#95;fre...</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">catch_exceptions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> |  <div className="default-line ">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether profiling should be done. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">field_sample_values_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Upper limit for number of sample values to collect for all columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">20</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_distinct_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of distinct values for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_distinct_value_frequencies</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for distinct value frequencies. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_histogram</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the histogram for numeric fields. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_max_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the max value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_mean_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the mean value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_median_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the median value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_min_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the min value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_null_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of nulls for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_quantiles</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the quantiles of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_sample_values</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the sample values for all columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_stddev_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the standard deviation of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Max number of documents to profile. By default, profiles all documents.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_number_of_fields_to_profile</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | A positive integer that specifies the maximum number of columns to profile for any table. `None` implies all columns. The cost of profiling goes up significantly as the number of columns to profile goes up.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use for profiling. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">50</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">offset</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Offset in documents to profile. By default, uses no offset.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">partition_datetime</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | If specified, profile only the partition which matches this datetime. If not specified, profile the latest partition. Only Bigquery supports this.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">partition_profiling_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile partitioned tables. Only BigQuery and Aws Athena supports this. If enabled, latest partition data is used for profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_external_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile external tables. Only Snowflake and Redshift supports this. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_if_updated_since_days</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Profile table only if it has been updated since these many number of days. If set to `null`, no constraint of last modified time for tables to profile. Supported only in `snowflake` and `BigQuery`.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_nested_fields</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile complex types like structs, arrays and maps.  <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_level_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to perform profiling at table-level only, or include column-level profiling as well. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_row_count_estimate_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use an approximate query for row count. This will be much faster but slightly less accurate. Only supported for Postgres and MySQL.  <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_row_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Profile tables only if their row count is less than specified count. If set to `null`, no limit on the row count of tables to profile. Supported only in `Snowflake`, `BigQuery`. Supported for `Oracle` based on gathered stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">5000000</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_size_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Profile tables only if their size is less than specified GBs. If set to `null`, no limit on the size of tables to profile. Supported only in `Snowflake`, `BigQuery` and `Databricks`. Supported for `Oracle` based on calculated size from gathered stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">5</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">query_combiner_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | *This feature is still experimental and can be disabled if it causes issues.* Reduces the total number of queries issued and speeds up profiling by dynamically combining SQL queries where possible. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">report_dropped_profiles</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report datasets or dataset columns which were not profiled. Set to `True` for debugging purposes. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">sample_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of rows to be sampled from table for column level profiling.Applicable only if `use_sampling` is set to True. <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">turn_off_expensive_profiling_metrics</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to turn off expensive profiling or not. This turns off profiling for quantiles, distinct_value_frequencies, histogram & sample_values. This also limits maximum number of fields being profiled to 10. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">use_sampling</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile column level stats on sample of table. Only BigQuery and Snowflake support this. If enabled, profiling is done on rows sampled from table. Sampling is not done for smaller tables.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">operation_config</span></div> <div className="type-name-line"><span className="type-name">OperationConfig</span></div> | Experimental feature. To specify operation configs.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">lower_freq_profile_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_date_of_month</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_day_of_week</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">tags_to_ignore_sampling</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Fixed list of tags to ignore sampling. If not specified, tables will be sampled based on `use_sampling`.  |
| <div className="path-line"><span className="path-prefix">profiling.tags_to_ignore_sampling.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "BigQueryV2Config",
  "description": "Any source that produces gcs lineage from/to Datasets should inherit this class.\nThis is needeed to group all lineage related configs under `gcs_lineage_config` config property.",
  "type": "object",
  "properties": {
    "classification": {
      "title": "Classification",
      "description": "For details, refer to [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md).",
      "default": {
        "enabled": false,
        "sample_size": 100,
        "max_workers": 10,
        "table_pattern": {
          "allow": [
            ".*"
          ],
          "deny": [],
          "ignoreCase": true
        },
        "column_pattern": {
          "allow": [
            ".*"
          ],
          "deny": [],
          "ignoreCase": true
        },
        "info_type_to_term": {},
        "classifiers": [
          {
            "type": "datahub",
            "config": null
          }
        ]
      },
      "allOf": [
        {
          "$ref": "#/definitions/ClassificationConfig"
        }
      ]
    },
    "enable_stateful_profiling": {
      "title": "Enable Stateful Profiling",
      "description": "Enable stateful profiling. This will store profiling timestamps per dataset after successful profiling. and will not run profiling again in subsequent run if table has not been updated. ",
      "default": true,
      "type": "boolean"
    },
    "enable_stateful_lineage_ingestion": {
      "title": "Enable Stateful Lineage Ingestion",
      "description": "Enable stateful lineage ingestion. This will store lineage window timestamps after successful lineage ingestion. and will not run lineage ingestion for same timestamps in subsequent run. ",
      "default": true,
      "type": "boolean"
    },
    "bucket_duration": {
      "description": "Size of the time window to aggregate usage stats.",
      "default": "DAY",
      "allOf": [
        {
          "$ref": "#/definitions/BucketDuration"
        }
      ]
    },
    "end_time": {
      "title": "End Time",
      "description": "Latest date of lineage/usage to consider. Default: Current time in UTC",
      "type": "string",
      "format": "date-time"
    },
    "start_time": {
      "title": "Start Time",
      "description": "Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.",
      "type": "string",
      "format": "date-time"
    },
    "enable_stateful_usage_ingestion": {
      "title": "Enable Stateful Usage Ingestion",
      "description": "Enable stateful lineage ingestion. This will store usage window timestamps after successful usage ingestion. and will not run usage ingestion for same timestamps in subsequent run. ",
      "default": true,
      "type": "boolean"
    },
    "table_pattern": {
      "title": "Table Pattern",
      "description": "Regex patterns for tables to filter in ingestion. Specify regex to match the entire table name in database.schema.table format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*'",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "view_pattern": {
      "title": "View Pattern",
      "description": "Regex patterns for views to filter in ingestion. Note: Defaults to table_pattern if not specified. Specify regex to match the entire view name in database.schema.view format. e.g. to match all views starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*'",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "incremental_lineage": {
      "title": "Incremental Lineage",
      "description": "When enabled, emits lineage as incremental to existing lineage already in DataHub. When disabled, re-states lineage on each run.",
      "default": false,
      "type": "boolean"
    },
    "convert_urns_to_lowercase": {
      "title": "Convert Urns To Lowercase",
      "description": "Whether to convert dataset urns to lowercase.",
      "default": false,
      "type": "boolean"
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "options": {
      "title": "Options",
      "description": "Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.",
      "type": "object"
    },
    "profile_pattern": {
      "title": "Profile Pattern",
      "description": "Regex patterns to filter tables (or specific columns) for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered.",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "domain": {
      "title": "Domain",
      "description": "Attach domains to databases, schemas or tables during ingestion using regex patterns. Domain key can be a guid like *urn:li:domain:ec428203-ce86-4db3-985d-5a8ee6df32ba* or a string like \"Marketing\".) If you provide strings, then datahub will attempt to resolve this name to a guid, and will error out if this fails. There can be multiple domain keys specified.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/AllowDenyPattern"
      }
    },
    "include_views": {
      "title": "Include Views",
      "description": "Whether views should be ingested.",
      "default": true,
      "type": "boolean"
    },
    "include_tables": {
      "title": "Include Tables",
      "description": "Whether tables should be ingested.",
      "default": true,
      "type": "boolean"
    },
    "include_table_location_lineage": {
      "title": "Include Table Location Lineage",
      "description": "If the source supports it, include table lineage to the underlying storage location.",
      "default": true,
      "type": "boolean"
    },
    "include_view_lineage": {
      "title": "Include View Lineage",
      "description": "Populates view->view and table->view lineage using DataHub's sql parser.",
      "default": true,
      "type": "boolean"
    },
    "include_view_column_lineage": {
      "title": "Include View Column Lineage",
      "description": "Populates column-level lineage for  view->view and table->view lineage using DataHub's sql parser. Requires `include_view_lineage` to be enabled.",
      "default": true,
      "type": "boolean"
    },
    "use_file_backed_cache": {
      "title": "Use File Backed Cache",
      "description": "Whether to use a file backed cache for the view definitions.",
      "default": true,
      "type": "boolean"
    },
    "profiling": {
      "title": "Profiling",
      "default": {
        "enabled": false,
        "operation_config": {
          "lower_freq_profile_enabled": false,
          "profile_day_of_week": null,
          "profile_date_of_month": null
        },
        "limit": null,
        "offset": null,
        "profile_table_level_only": false,
        "include_field_null_count": true,
        "include_field_distinct_count": true,
        "include_field_min_value": true,
        "include_field_max_value": true,
        "include_field_mean_value": true,
        "include_field_median_value": true,
        "include_field_stddev_value": true,
        "include_field_quantiles": false,
        "include_field_distinct_value_frequencies": false,
        "include_field_histogram": false,
        "include_field_sample_values": true,
        "max_workers": 50,
        "report_dropped_profiles": false,
        "turn_off_expensive_profiling_metrics": false,
        "field_sample_values_limit": 20,
        "max_number_of_fields_to_profile": null,
        "profile_if_updated_since_days": null,
        "profile_table_size_limit": 5,
        "profile_table_row_limit": 5000000,
        "profile_table_row_count_estimate_only": false,
        "query_combiner_enabled": true,
        "catch_exceptions": true,
        "partition_profiling_enabled": true,
        "partition_datetime": null,
        "use_sampling": true,
        "sample_size": 10000,
        "profile_external_tables": false,
        "tags_to_ignore_sampling": null,
        "profile_nested_fields": false
      },
      "allOf": [
        {
          "$ref": "#/definitions/GEProfilingConfig"
        }
      ]
    },
    "include_data_platform_instance": {
      "title": "Include Data Platform Instance",
      "description": "Whether to create a DataPlatformInstance aspect, equal to the BigQuery project id. If enabled, will cause redundancy in the browse path for BigQuery entities in the UI, because the project id is represented as the top-level container.",
      "default": false,
      "type": "boolean"
    },
    "enable_legacy_sharded_table_support": {
      "title": "Enable Legacy Sharded Table Support",
      "description": "Use the legacy sharded table urn suffix added.",
      "default": true,
      "type": "boolean"
    },
    "project_ids": {
      "title": "Project Ids",
      "description": "Ingests specified project_ids. Use this property if you want to specify what projects to ingest or don't want to give project resourcemanager.projects.list to your service account. Overrides `project_id_pattern`.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "project_labels": {
      "title": "Project Labels",
      "description": "Ingests projects with the specified labels. Set value in the format of `key:value`. Use this property to define which projects to ingest basedon project-level labels. If project_ids or project_id is set, this configuration has no effect. The ingestion process filters projects by label first, and then applies the project_id_pattern.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "project_id_pattern": {
      "title": "Project Id Pattern",
      "description": "Regex patterns for project_id to filter in ingestion.",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "dataset_pattern": {
      "title": "Dataset Pattern",
      "description": "Regex patterns for dataset to filter in ingestion. Specify regex to only match the schema name. e.g. to match all tables in schema analytics, use the regex 'analytics'",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "match_fully_qualified_names": {
      "title": "Match Fully Qualified Names",
      "description": "[deprecated] Whether `dataset_pattern` is matched against fully qualified dataset name `<project_id>.<dataset_name>`.",
      "default": true,
      "type": "boolean"
    },
    "table_snapshot_pattern": {
      "title": "Table Snapshot Pattern",
      "description": "Regex patterns for table snapshots to filter in ingestion. Specify regex to match the entire snapshot name in database.schema.snapshot format. e.g. to match all snapshots starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*'",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "rate_limit": {
      "title": "Rate Limit",
      "description": "Should we rate limit requests made to API.",
      "default": false,
      "type": "boolean"
    },
    "requests_per_min": {
      "title": "Requests Per Min",
      "description": "Used to control number of API calls made per min. Only used when `rate_limit` is set to `True`.",
      "default": 60,
      "type": "integer"
    },
    "temp_table_dataset_prefix": {
      "title": "Temp Table Dataset Prefix",
      "description": "If you are creating temp tables in a dataset with a particular prefix you can use this config to set the prefix for the dataset. This is to support workflows from before bigquery's introduction of temp tables. By default we use `_` because of datasets that begin with an underscore are hidden by default https://cloud.google.com/bigquery/docs/datasets#dataset-naming.",
      "default": "_",
      "type": "string"
    },
    "sharded_table_pattern": {
      "title": "Sharded Table Pattern",
      "description": "The regex pattern to match sharded tables and group as one table. This is a very low level config parameter, only change if you know what you are doing, ",
      "default": "((.+\\D)[_$]?)?(\\d\\d\\d\\d(?:0[1-9]|1[0-2])(?:0[1-9]|[12][0-9]|3[01]))$",
      "deprecated": true,
      "type": "string"
    },
    "credential": {
      "title": "Credential",
      "description": "BigQuery credential informations",
      "allOf": [
        {
          "$ref": "#/definitions/BigQueryCredential"
        }
      ]
    },
    "extra_client_options": {
      "title": "Extra Client Options",
      "description": "Additional options to pass to google.cloud.logging_v2.client.Client.",
      "default": {},
      "type": "object"
    },
    "project_on_behalf": {
      "title": "Project On Behalf",
      "description": "[Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account.",
      "type": "string"
    },
    "gcs_lineage_config": {
      "title": "Gcs Lineage Config",
      "description": "Common config for gcs lineage generation",
      "default": {
        "path_specs": [],
        "strip_urls": true,
        "ignore_non_path_spec_path": false
      },
      "allOf": [
        {
          "$ref": "#/definitions/GcsLineageProviderConfig"
        }
      ]
    },
    "include_schema_metadata": {
      "title": "Include Schema Metadata",
      "description": "Whether to ingest the BigQuery schema, i.e. projects, schemas, tables, and views.",
      "default": true,
      "type": "boolean"
    },
    "usage": {
      "title": "Usage",
      "description": "Usage related configs",
      "default": {
        "bucket_duration": "DAY",
        "end_time": "2025-05-08T12:15:33.308228+00:00",
        "start_time": "2025-05-07T00:00:00+00:00",
        "queries_character_limit": 24000,
        "top_n_queries": 10,
        "user_email_pattern": {
          "allow": [
            ".*"
          ],
          "deny": [],
          "ignoreCase": true
        },
        "include_operational_stats": true,
        "include_read_operational_stats": false,
        "format_sql_queries": false,
        "include_top_n_queries": true,
        "max_query_duration": 900.0,
        "apply_view_usage_to_tables": false
      },
      "allOf": [
        {
          "$ref": "#/definitions/BigQueryUsageConfig"
        }
      ]
    },
    "include_usage_statistics": {
      "title": "Include Usage Statistics",
      "description": "Generate usage statistic",
      "default": true,
      "type": "boolean"
    },
    "capture_table_label_as_tag": {
      "title": "Capture Table Label As Tag",
      "description": "Capture BigQuery table labels as DataHub tag",
      "default": false,
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "capture_view_label_as_tag": {
      "title": "Capture View Label As Tag",
      "description": "Capture BigQuery view labels as DataHub tag",
      "default": false,
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "capture_dataset_label_as_tag": {
      "title": "Capture Dataset Label As Tag",
      "description": "Capture BigQuery dataset labels as DataHub tag",
      "default": false,
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "include_table_constraints": {
      "title": "Include Table Constraints",
      "description": "Whether to ingest table constraints. If you know you don't use table constraints, you can disable it to save one extra query per dataset. In general it should be enabled",
      "default": true,
      "type": "boolean"
    },
    "include_external_url": {
      "title": "Include External Url",
      "description": "Whether to populate BigQuery Console url to Datasets/Tables",
      "default": true,
      "type": "boolean"
    },
    "include_table_snapshots": {
      "title": "Include Table Snapshots",
      "description": "Whether table snapshots should be ingested.",
      "default": true,
      "type": "boolean"
    },
    "debug_include_full_payloads": {
      "title": "Debug Include Full Payloads",
      "description": "Include full payload into events. It is only for debugging and internal use.",
      "default": false,
      "type": "boolean"
    },
    "number_of_datasets_process_in_batch_if_profiling_enabled": {
      "title": "Number Of Datasets Process In Batch If Profiling Enabled",
      "description": "Number of partitioned table queried in batch when getting metadata. This is a low level config property which should be touched with care. This restriction is needed because we query partitions system view which throws error if we try to touch too many tables.",
      "default": 1000,
      "type": "integer"
    },
    "use_tables_list_query_v2": {
      "title": "Use Tables List Query V2",
      "description": "List tables using an improved query that extracts partitions and last modified timestamps more accurately. Requires the ability to read table data. Automatically enabled when profiling is enabled.",
      "default": false,
      "type": "boolean"
    },
    "use_queries_v2": {
      "title": "Use Queries V2",
      "description": "If enabled, uses the new queries extractor to extract queries from bigquery.",
      "default": false,
      "type": "boolean"
    },
    "include_queries": {
      "title": "Include Queries",
      "description": "If enabled, generate query entities associated with lineage edges. Only applicable if `use_queries_v2` is enabled.",
      "default": true,
      "type": "boolean"
    },
    "include_query_usage_statistics": {
      "title": "Include Query Usage Statistics",
      "description": "If enabled, generate query popularity statistics. Only applicable if `use_queries_v2` is enabled.",
      "default": true,
      "type": "boolean"
    },
    "column_limit": {
      "title": "Column Limit",
      "description": "Maximum number of columns to process in a table. This is a low level config property which should be touched with care. This restriction is needed because excessively wide tables can result in failure to ingest the schema.",
      "default": 300,
      "type": "integer"
    },
    "lineage_use_sql_parser": {
      "title": "Lineage Use Sql Parser",
      "description": "Use sql parser to resolve view/table lineage.",
      "default": true,
      "type": "boolean"
    },
    "lineage_sql_parser_use_raw_names": {
      "title": "Lineage Sql Parser Use Raw Names",
      "description": "This parameter ignores the lowercase pattern stipulated in the SQLParser. NOTE: Ignored if lineage_use_sql_parser is False.",
      "default": false,
      "type": "boolean"
    },
    "extract_column_lineage": {
      "title": "Extract Column Lineage",
      "description": "If enabled, generate column level lineage. Requires lineage_use_sql_parser to be enabled.",
      "default": false,
      "type": "boolean"
    },
    "extract_lineage_from_catalog": {
      "title": "Extract Lineage From Catalog",
      "description": "This flag enables the data lineage extraction from Data Lineage API exposed by Google Data Catalog. NOTE: This extractor can't build views lineage. It's recommended to enable the view's DDL parsing. Read the docs to have more information about: https://cloud.google.com/data-catalog/docs/concepts/about-data-lineage",
      "default": false,
      "type": "boolean"
    },
    "extract_policy_tags_from_catalog": {
      "title": "Extract Policy Tags From Catalog",
      "description": "This flag enables the extraction of policy tags from the Google Data Catalog API. When enabled, the extractor will fetch policy tags associated with BigQuery table columns. For more information about policy tags and column-level security, refer to the documentation: https://cloud.google.com/bigquery/docs/column-level-security-intro",
      "default": false,
      "type": "boolean"
    },
    "scheme": {
      "title": "Scheme",
      "default": "bigquery",
      "type": "string"
    },
    "log_page_size": {
      "title": "Log Page Size",
      "description": "The number of log item will be queried per page for lineage collection",
      "default": 1000,
      "exclusiveMinimum": 0,
      "type": "integer"
    },
    "include_table_lineage": {
      "title": "Include Table Lineage",
      "description": "Option to enable/disable lineage generation. Is enabled by default.",
      "default": true,
      "type": "boolean"
    },
    "include_column_lineage_with_gcs": {
      "title": "Include Column Lineage With Gcs",
      "description": "When enabled, column-level lineage will be extracted from the gcs.",
      "default": true,
      "type": "boolean"
    },
    "max_query_duration": {
      "title": "Max Query Duration",
      "description": "Correction to pad start_time and end_time with. For handling the case where the read happens within our time range but the query completion event is delayed and happens after the configured end time.",
      "default": 900.0,
      "type": "number",
      "format": "time-delta"
    },
    "bigquery_audit_metadata_datasets": {
      "title": "Bigquery Audit Metadata Datasets",
      "description": "A list of datasets that contain a table named cloudaudit_googleapis_com_data_access which contain BigQuery audit logs, specifically, those containing BigQueryAuditMetadata. It is recommended that the project of the dataset is also specified, for example, projectA.datasetB.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "use_exported_bigquery_audit_metadata": {
      "title": "Use Exported Bigquery Audit Metadata",
      "description": "When configured, use BigQueryAuditMetadata in bigquery_audit_metadata_datasets to compute lineage information.",
      "default": false,
      "type": "boolean"
    },
    "use_date_sharded_audit_log_tables": {
      "title": "Use Date Sharded Audit Log Tables",
      "description": "Whether to read date sharded tables or time partitioned tables when extracting usage from exported audit logs.",
      "default": false,
      "type": "boolean"
    },
    "upstream_lineage_in_report": {
      "title": "Upstream Lineage In Report",
      "description": "Useful for debugging lineage information. Set to True to see the raw lineage created internally.",
      "default": false,
      "type": "boolean"
    },
    "exclude_empty_projects": {
      "title": "Exclude Empty Projects",
      "description": "Option to exclude empty projects from being ingested.",
      "default": false,
      "type": "boolean"
    },
    "schema_resolution_batch_size": {
      "title": "Schema Resolution Batch Size",
      "description": "The number of tables to process in a batch when resolving schema from DataHub.",
      "default": 100,
      "hidden_from_schema": true,
      "type": "integer"
    },
    "max_threads_dataset_parallelism": {
      "title": "Max Threads Dataset Parallelism",
      "description": "Number of worker threads to use to parallelize BigQuery Dataset Metadata Extraction. Set to 1 to disable.",
      "default": 20,
      "type": "integer"
    },
    "region_qualifiers": {
      "title": "Region Qualifiers",
      "description": "BigQuery regions to be scanned for bigquery jobs when using `use_queries_v2`. See [this](https://cloud.google.com/bigquery/docs/information-schema-jobs#scope_and_syntax) for details.",
      "default": [
        "region-us",
        "region-eu"
      ],
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false,
  "definitions": {
    "AllowDenyPattern": {
      "title": "AllowDenyPattern",
      "description": "A class to store allow deny regexes",
      "type": "object",
      "properties": {
        "allow": {
          "title": "Allow",
          "description": "List of regex patterns to include in ingestion",
          "default": [
            ".*"
          ],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "deny": {
          "title": "Deny",
          "description": "List of regex patterns to exclude from ingestion.",
          "default": [],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "ignoreCase": {
          "title": "Ignorecase",
          "description": "Whether to ignore case sensitivity during pattern matching.",
          "default": true,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "DynamicTypedClassifierConfig": {
      "title": "DynamicTypedClassifierConfig",
      "type": "object",
      "properties": {
        "type": {
          "title": "Type",
          "description": "The type of the classifier to use. For DataHub,  use `datahub`",
          "type": "string"
        },
        "config": {
          "title": "Config",
          "description": "The configuration required for initializing the classifier. If not specified, uses defaults for classifer type."
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "ClassificationConfig": {
      "title": "ClassificationConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether classification should be used to auto-detect glossary terms",
          "default": false,
          "type": "boolean"
        },
        "sample_size": {
          "title": "Sample Size",
          "description": "Number of sample values used for classification.",
          "default": 100,
          "type": "integer"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "Number of worker processes to use for classification. Set to 1 to disable.",
          "default": 10,
          "type": "integer"
        },
        "table_pattern": {
          "title": "Table Pattern",
          "description": "Regex patterns to filter tables for classification. This is used in combination with other patterns in parent config. Specify regex to match the entire table name in `database.schema.table` format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*'",
          "default": {
            "allow": [
              ".*"
            ],
            "deny": [],
            "ignoreCase": true
          },
          "allOf": [
            {
              "$ref": "#/definitions/AllowDenyPattern"
            }
          ]
        },
        "column_pattern": {
          "title": "Column Pattern",
          "description": "Regex patterns to filter columns for classification. This is used in combination with other patterns in parent config. Specify regex to match the column name in `database.schema.table.column` format.",
          "default": {
            "allow": [
              ".*"
            ],
            "deny": [],
            "ignoreCase": true
          },
          "allOf": [
            {
              "$ref": "#/definitions/AllowDenyPattern"
            }
          ]
        },
        "info_type_to_term": {
          "title": "Info Type To Term",
          "description": "Optional mapping to provide glossary term identifier for info type",
          "default": {},
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "classifiers": {
          "title": "Classifiers",
          "description": "Classifiers to use to auto-detect glossary terms. If more than one classifier, infotype predictions from the classifier defined later in sequence take precedance.",
          "default": [
            {
              "type": "datahub",
              "config": null
            }
          ],
          "type": "array",
          "items": {
            "$ref": "#/definitions/DynamicTypedClassifierConfig"
          }
        }
      },
      "additionalProperties": false
    },
    "BucketDuration": {
      "title": "BucketDuration",
      "description": "An enumeration.",
      "enum": [
        "DAY",
        "HOUR"
      ],
      "type": "string"
    },
    "DynamicTypedStateProviderConfig": {
      "title": "DynamicTypedStateProviderConfig",
      "type": "object",
      "properties": {
        "type": {
          "title": "Type",
          "description": "The type of the state provider to use. For DataHub use `datahub`",
          "type": "string"
        },
        "config": {
          "title": "Config",
          "description": "The configuration required for initializing the state provider. Default: The datahub_api config if set at pipeline level. Otherwise, the default DatahubClientConfig. See the defaults (https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/graph/client.py#L19).",
          "default": {},
          "type": "object"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "StatefulStaleMetadataRemovalConfig": {
      "title": "StatefulStaleMetadataRemovalConfig",
      "description": "Base specialized config for Stateful Ingestion with stale metadata removal capability.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "default": false,
          "type": "boolean"
        },
        "remove_stale_metadata": {
          "title": "Remove Stale Metadata",
          "description": "Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled.",
          "default": true,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "OperationConfig": {
      "title": "OperationConfig",
      "type": "object",
      "properties": {
        "lower_freq_profile_enabled": {
          "title": "Lower Freq Profile Enabled",
          "description": "Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling.",
          "default": false,
          "type": "boolean"
        },
        "profile_day_of_week": {
          "title": "Profile Day Of Week",
          "description": "Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.",
          "type": "integer"
        },
        "profile_date_of_month": {
          "title": "Profile Date Of Month",
          "description": "Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.",
          "type": "integer"
        }
      },
      "additionalProperties": false
    },
    "GEProfilingConfig": {
      "title": "GEProfilingConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether profiling should be done.",
          "default": false,
          "type": "boolean"
        },
        "operation_config": {
          "title": "Operation Config",
          "description": "Experimental feature. To specify operation configs.",
          "allOf": [
            {
              "$ref": "#/definitions/OperationConfig"
            }
          ]
        },
        "limit": {
          "title": "Limit",
          "description": "Max number of documents to profile. By default, profiles all documents.",
          "type": "integer"
        },
        "offset": {
          "title": "Offset",
          "description": "Offset in documents to profile. By default, uses no offset.",
          "type": "integer"
        },
        "profile_table_level_only": {
          "title": "Profile Table Level Only",
          "description": "Whether to perform profiling at table-level only, or include column-level profiling as well.",
          "default": false,
          "type": "boolean"
        },
        "include_field_null_count": {
          "title": "Include Field Null Count",
          "description": "Whether to profile for the number of nulls for each column.",
          "default": true,
          "type": "boolean"
        },
        "include_field_distinct_count": {
          "title": "Include Field Distinct Count",
          "description": "Whether to profile for the number of distinct values for each column.",
          "default": true,
          "type": "boolean"
        },
        "include_field_min_value": {
          "title": "Include Field Min Value",
          "description": "Whether to profile for the min value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_max_value": {
          "title": "Include Field Max Value",
          "description": "Whether to profile for the max value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_mean_value": {
          "title": "Include Field Mean Value",
          "description": "Whether to profile for the mean value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_median_value": {
          "title": "Include Field Median Value",
          "description": "Whether to profile for the median value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_stddev_value": {
          "title": "Include Field Stddev Value",
          "description": "Whether to profile for the standard deviation of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_quantiles": {
          "title": "Include Field Quantiles",
          "description": "Whether to profile for the quantiles of numeric columns.",
          "default": false,
          "type": "boolean"
        },
        "include_field_distinct_value_frequencies": {
          "title": "Include Field Distinct Value Frequencies",
          "description": "Whether to profile for distinct value frequencies.",
          "default": false,
          "type": "boolean"
        },
        "include_field_histogram": {
          "title": "Include Field Histogram",
          "description": "Whether to profile for the histogram for numeric fields.",
          "default": false,
          "type": "boolean"
        },
        "include_field_sample_values": {
          "title": "Include Field Sample Values",
          "description": "Whether to profile for the sample values for all columns.",
          "default": true,
          "type": "boolean"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "Number of worker threads to use for profiling. Set to 1 to disable.",
          "default": 50,
          "type": "integer"
        },
        "report_dropped_profiles": {
          "title": "Report Dropped Profiles",
          "description": "Whether to report datasets or dataset columns which were not profiled. Set to `True` for debugging purposes.",
          "default": false,
          "type": "boolean"
        },
        "turn_off_expensive_profiling_metrics": {
          "title": "Turn Off Expensive Profiling Metrics",
          "description": "Whether to turn off expensive profiling or not. This turns off profiling for quantiles, distinct_value_frequencies, histogram & sample_values. This also limits maximum number of fields being profiled to 10.",
          "default": false,
          "type": "boolean"
        },
        "field_sample_values_limit": {
          "title": "Field Sample Values Limit",
          "description": "Upper limit for number of sample values to collect for all columns.",
          "default": 20,
          "type": "integer"
        },
        "max_number_of_fields_to_profile": {
          "title": "Max Number Of Fields To Profile",
          "description": "A positive integer that specifies the maximum number of columns to profile for any table. `None` implies all columns. The cost of profiling goes up significantly as the number of columns to profile goes up.",
          "exclusiveMinimum": 0,
          "type": "integer"
        },
        "profile_if_updated_since_days": {
          "title": "Profile If Updated Since Days",
          "description": "Profile table only if it has been updated since these many number of days. If set to `null`, no constraint of last modified time for tables to profile. Supported only in `snowflake` and `BigQuery`.",
          "exclusiveMinimum": 0,
          "type": "number"
        },
        "profile_table_size_limit": {
          "title": "Profile Table Size Limit",
          "description": "Profile tables only if their size is less than specified GBs. If set to `null`, no limit on the size of tables to profile. Supported only in `Snowflake`, `BigQuery` and `Databricks`. Supported for `Oracle` based on calculated size from gathered stats.",
          "default": 5,
          "type": "integer"
        },
        "profile_table_row_limit": {
          "title": "Profile Table Row Limit",
          "description": "Profile tables only if their row count is less than specified count. If set to `null`, no limit on the row count of tables to profile. Supported only in `Snowflake`, `BigQuery`. Supported for `Oracle` based on gathered stats.",
          "default": 5000000,
          "type": "integer"
        },
        "profile_table_row_count_estimate_only": {
          "title": "Profile Table Row Count Estimate Only",
          "description": "Use an approximate query for row count. This will be much faster but slightly less accurate. Only supported for Postgres and MySQL. ",
          "default": false,
          "type": "boolean"
        },
        "query_combiner_enabled": {
          "title": "Query Combiner Enabled",
          "description": "*This feature is still experimental and can be disabled if it causes issues.* Reduces the total number of queries issued and speeds up profiling by dynamically combining SQL queries where possible.",
          "default": true,
          "type": "boolean"
        },
        "catch_exceptions": {
          "title": "Catch Exceptions",
          "default": true,
          "type": "boolean"
        },
        "partition_profiling_enabled": {
          "title": "Partition Profiling Enabled",
          "description": "Whether to profile partitioned tables. Only BigQuery and Aws Athena supports this. If enabled, latest partition data is used for profiling.",
          "default": true,
          "type": "boolean"
        },
        "partition_datetime": {
          "title": "Partition Datetime",
          "description": "If specified, profile only the partition which matches this datetime. If not specified, profile the latest partition. Only Bigquery supports this.",
          "type": "string",
          "format": "date-time"
        },
        "use_sampling": {
          "title": "Use Sampling",
          "description": "Whether to profile column level stats on sample of table. Only BigQuery and Snowflake support this. If enabled, profiling is done on rows sampled from table. Sampling is not done for smaller tables. ",
          "default": true,
          "type": "boolean"
        },
        "sample_size": {
          "title": "Sample Size",
          "description": "Number of rows to be sampled from table for column level profiling.Applicable only if `use_sampling` is set to True.",
          "default": 10000,
          "type": "integer"
        },
        "profile_external_tables": {
          "title": "Profile External Tables",
          "description": "Whether to profile external tables. Only Snowflake and Redshift supports this.",
          "default": false,
          "type": "boolean"
        },
        "tags_to_ignore_sampling": {
          "title": "Tags To Ignore Sampling",
          "description": "Fixed list of tags to ignore sampling. If not specified, tables will be sampled based on `use_sampling`.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "profile_nested_fields": {
          "title": "Profile Nested Fields",
          "description": "Whether to profile complex types like structs, arrays and maps. ",
          "default": false,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "BigQueryCredential": {
      "title": "BigQueryCredential",
      "type": "object",
      "properties": {
        "project_id": {
          "title": "Project Id",
          "description": "Project id to set the credentials",
          "type": "string"
        },
        "private_key_id": {
          "title": "Private Key Id",
          "description": "Private key id",
          "type": "string"
        },
        "private_key": {
          "title": "Private Key",
          "description": "Private key in a form of '-----BEGIN PRIVATE KEY-----\\nprivate-key\\n-----END PRIVATE KEY-----\\n'",
          "type": "string"
        },
        "client_email": {
          "title": "Client Email",
          "description": "Client email",
          "type": "string"
        },
        "client_id": {
          "title": "Client Id",
          "description": "Client Id",
          "type": "string"
        },
        "auth_uri": {
          "title": "Auth Uri",
          "description": "Authentication uri",
          "default": "https://accounts.google.com/o/oauth2/auth",
          "type": "string"
        },
        "token_uri": {
          "title": "Token Uri",
          "description": "Token uri",
          "default": "https://oauth2.googleapis.com/token",
          "type": "string"
        },
        "auth_provider_x509_cert_url": {
          "title": "Auth Provider X509 Cert Url",
          "description": "Auth provider x509 certificate url",
          "default": "https://www.googleapis.com/oauth2/v1/certs",
          "type": "string"
        },
        "type": {
          "title": "Type",
          "description": "Authentication type",
          "default": "service_account",
          "type": "string"
        },
        "client_x509_cert_url": {
          "title": "Client X509 Cert Url",
          "description": "If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email",
          "type": "string"
        }
      },
      "required": [
        "project_id",
        "private_key_id",
        "private_key",
        "client_email",
        "client_id"
      ],
      "additionalProperties": false
    },
    "SortKeyType": {
      "title": "SortKeyType",
      "description": "An enumeration.",
      "enum": [
        "STRING",
        "INTEGER",
        "FLOAT",
        "DATETIME",
        "DATE"
      ]
    },
    "SortKey": {
      "title": "SortKey",
      "type": "object",
      "properties": {
        "key": {
          "title": "Key",
          "description": "The key to sort on. This can be a compound key based on the path_spec variables.",
          "type": "string"
        },
        "type": {
          "description": "The date format to use when sorting. This is used to parse the date from the key. The format should follow the java [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) format.",
          "default": "STRING",
          "allOf": [
            {
              "$ref": "#/definitions/SortKeyType"
            }
          ]
        },
        "date_format": {
          "title": "Date Format",
          "description": "The date format to use when sorting. This is used to parse the date from the key. The format should follow the java [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) format.",
          "type": "string"
        }
      },
      "required": [
        "key"
      ],
      "additionalProperties": false
    },
    "FolderTraversalMethod": {
      "title": "FolderTraversalMethod",
      "description": "An enumeration.",
      "enum": [
        "ALL",
        "MIN_MAX",
        "MAX"
      ]
    },
    "PathSpec": {
      "title": "PathSpec",
      "type": "object",
      "properties": {
        "include": {
          "title": "Include",
          "description": "Path to table. Name variable `{table}` is used to mark the folder with dataset. In absence of `{table}`, file level dataset will be created. Check below examples for more details.",
          "type": "string"
        },
        "exclude": {
          "title": "Exclude",
          "description": "list of paths in glob pattern which will be excluded while scanning for the datasets",
          "default": [],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "file_types": {
          "title": "File Types",
          "description": "Files with extenstions specified here (subset of default value) only will be scanned to create dataset. Other files will be omitted.",
          "default": [
            "csv",
            "tsv",
            "json",
            "parquet",
            "avro"
          ],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "default_extension": {
          "title": "Default Extension",
          "description": "For files without extension it will assume the specified file type. If it is not set the files without extensions will be skipped.",
          "type": "string"
        },
        "table_name": {
          "title": "Table Name",
          "description": "Display name of the dataset.Combination of named variables from include path and strings",
          "type": "string"
        },
        "enable_compression": {
          "title": "Enable Compression",
          "description": "Enable or disable processing compressed files. Currently .gz and .bz files are supported.",
          "default": true,
          "type": "boolean"
        },
        "sample_files": {
          "title": "Sample Files",
          "description": "Not listing all the files but only taking a handful amount of sample file to infer the schema. File count and file size calculation will be disabled. This can affect performance significantly if enabled",
          "default": true,
          "type": "boolean"
        },
        "allow_double_stars": {
          "title": "Allow Double Stars",
          "description": "Allow double stars in the include path. This can affect performance significantly if enabled",
          "default": false,
          "type": "boolean"
        },
        "autodetect_partitions": {
          "title": "Autodetect Partitions",
          "description": "Autodetect partition(s) from the path. If set to true, it will autodetect partition key/value if the folder format is {partition_key}={partition_value} for example `year=2024`",
          "default": true,
          "type": "boolean"
        },
        "traversal_method": {
          "description": "Method to traverse the folder. ALL: Traverse all the folders, MIN_MAX: Traverse the folders by finding min and max value, MAX: Traverse the folder with max value",
          "default": "MAX",
          "allOf": [
            {
              "$ref": "#/definitions/FolderTraversalMethod"
            }
          ]
        },
        "include_hidden_folders": {
          "title": "Include Hidden Folders",
          "description": "Include hidden folders in the traversal (folders starting with . or _",
          "default": false,
          "type": "boolean"
        }
      },
      "required": [
        "include"
      ],
      "additionalProperties": false
    },
    "GcsLineageProviderConfig": {
      "title": "GcsLineageProviderConfig",
      "description": "Any source that produces gcs lineage from/to Datasets should inherit this class.",
      "type": "object",
      "properties": {
        "path_specs": {
          "title": "Path Specs",
          "description": "List of PathSpec. See below the details about PathSpec",
          "default": [],
          "type": "array",
          "items": {
            "$ref": "#/definitions/PathSpec"
          }
        },
        "strip_urls": {
          "title": "Strip Urls",
          "description": "Strip filename from gcs url. It only applies if path_specs are not specified.",
          "default": true,
          "type": "boolean"
        },
        "ignore_non_path_spec_path": {
          "title": "Ignore Non Path Spec Path",
          "description": "Ignore paths that are not match in path_specs. It only applies if path_specs are specified.",
          "default": false,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "BigQueryUsageConfig": {
      "title": "BigQueryUsageConfig",
      "type": "object",
      "properties": {
        "bucket_duration": {
          "description": "Size of the time window to aggregate usage stats.",
          "default": "DAY",
          "allOf": [
            {
              "$ref": "#/definitions/BucketDuration"
            }
          ]
        },
        "end_time": {
          "title": "End Time",
          "description": "Latest date of lineage/usage to consider. Default: Current time in UTC",
          "type": "string",
          "format": "date-time"
        },
        "start_time": {
          "title": "Start Time",
          "description": "Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.",
          "type": "string",
          "format": "date-time"
        },
        "top_n_queries": {
          "title": "Top N Queries",
          "description": "Number of top queries to save to each table.",
          "default": 10,
          "exclusiveMinimum": 0,
          "type": "integer"
        },
        "user_email_pattern": {
          "title": "User Email Pattern",
          "description": "regex patterns for user emails to filter in usage.",
          "default": {
            "allow": [
              ".*"
            ],
            "deny": [],
            "ignoreCase": true
          },
          "allOf": [
            {
              "$ref": "#/definitions/AllowDenyPattern"
            }
          ]
        },
        "include_operational_stats": {
          "title": "Include Operational Stats",
          "description": "Whether to display operational stats.",
          "default": true,
          "type": "boolean"
        },
        "include_read_operational_stats": {
          "title": "Include Read Operational Stats",
          "description": "Whether to report read operational stats. Experimental.",
          "default": false,
          "type": "boolean"
        },
        "format_sql_queries": {
          "title": "Format Sql Queries",
          "description": "Whether to format sql queries",
          "default": false,
          "type": "boolean"
        },
        "include_top_n_queries": {
          "title": "Include Top N Queries",
          "description": "Whether to ingest the top_n_queries.",
          "default": true,
          "type": "boolean"
        },
        "max_query_duration": {
          "title": "Max Query Duration",
          "description": "Correction to pad start_time and end_time with. For handling the case where the read happens within our time range but the query completion event is delayed and happens after the configured end time.",
          "default": 900.0,
          "type": "number",
          "format": "time-delta"
        },
        "apply_view_usage_to_tables": {
          "title": "Apply View Usage To Tables",
          "description": "Whether to apply view's usage to its base tables. If set to False, uses sql parser and applies usage to views / tables mentioned in the query. If set to True, usage is applied to base tables only.",
          "default": false,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.bigquery_v2.bigquery.BigqueryV2Source`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/bigquery_v2/bigquery.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for BigQuery, feel free to ping us on [our Slack](https://slack.datahubproject.io).
