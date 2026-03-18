---
sidebar_position: 9
title: Databricks
slug: /generated/ingestion/sources/databricks
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/databricks.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Databricks
DataHub supports integration with Databricks ecosystem using a multitude of connectors, depending on your exact setup. 

## Databricks Unity Catalog (new)

The recently introduced [Unity Catalog](https://www.databricks.com/product/unity-catalog) provides a new way to govern your assets within the Databricks lakehouse. If you have Unity Catalog Enabled Workspace, you can use the `unity-catalog` source (aka `databricks` source, see below for details) to integrate your metadata into DataHub as an alternate to the Hive pathway. This also ingests hive metastore catalog in Databricks and is recommended approach to ingest Databricks ecosystem in DataHub.

## Databricks Hive (old)

The alternative way to integrate is via the Hive connector. The [Hive starter recipe](http://datahubproject.io/docs/generated/ingestion/sources/hive#starter-recipe) has a section describing how to connect to your Databricks workspace.


## Databricks Spark

To complete the picture, we recommend adding push-based ingestion from your Spark jobs to see real-time activity and lineage between your Databricks tables and your Spark jobs. Use the Spark agent to push metadata to DataHub using the instructions [here](../../../../metadata-integration/java/acryl-spark-lineage/README.md#configuration-instructions-databricks).

## Watch the DataHub Talk at the Data and AI Summit 2022

For a deeper look at how to think about DataHub within and across your Databricks ecosystem, watch the recording of our talk at the Data and AI Summit 2022. 
<p align="center">
<a href="https://www.youtube.com/watch?v=SCP0PR3t7dc">
<img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/metadata-ingestion/databricks/data_and_ai_summit_2022.png"/>
</a>
</p>



![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| Column-level Lineage | ✅ | Enabled by default |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Supported via the `profiling.enabled` config |
| Dataset Usage | ✅ | Enabled by default |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Domains](../../../domains.md) | ✅ | Supported via the `domain` config field |
| Extract Ownership | ✅ | Supported via the `include_ownership` config |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default |


This plugin extracts the following metadata from Databricks Unity Catalog:
- metastores
- schemas
- tables and column lineage

### Prerequisities
- Get your Databricks instance's [workspace url](https://docs.databricks.com/workspace/workspace-details.html#workspace-instance-names-urls-and-ids)
- Create a [Databricks Service Principal](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#what-is-a-service-principal)
  + You can skip this step and use your own account to get things running quickly,
  but we strongly recommend creating a dedicated service principal for production use.
- Generate a Databricks Personal Access token following the following guides:
  + [Service Principals](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#personal-access-tokens)
  + [Personal Access Tokens](https://docs.databricks.com/dev-tools/auth.html#databricks-personal-access-tokens)
- Provision your service account:
  + To ingest your workspace's metadata and lineage, your service principal must have all of the following:
    * One of: metastore admin role, ownership of, or `USE CATALOG` privilege on any catalogs you want to ingest
    * One of: metastore admin role, ownership of, or `USE SCHEMA` privilege on any schemas you want to ingest
    * Ownership of or `SELECT` privilege on any tables and views you want to ingest
    * [Ownership documentation](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/ownership.html)
    * [Privileges documentation](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/privileges.html)
  + To ingest legacy hive_metastore catalog (`include_hive_metastore` - enabled by default), your service principal must have all of the following:
    * `READ_METADATA` and `USAGE` privilege on `hive_metastore` catalog
    * `READ_METADATA` and `USAGE` privilege on schemas you want to ingest
    * `READ_METADATA` and `USAGE` privilege on tables and views you want to ingest
    * [Hive Metastore Privileges documentation](https://docs.databricks.com/en/sql/language-manual/sql-ref-privileges-hms.html)
  + To ingest your workspace's notebooks and respective lineage, your service principal must have `CAN_READ` privileges on the folders containing the notebooks you want to ingest: [guide](https://docs.databricks.com/en/security/auth-authz/access-control/workspace-acl.html#folder-permissions).
  + To `include_usage_statistics` (enabled by default), your service principal must have `CAN_MANAGE` permissions on any SQL Warehouses you want to ingest: [guide](https://docs.databricks.com/security/auth-authz/access-control/sql-endpoint-acl.html).
  + To ingest `profiling` information with `method: ge`, you need `SELECT` privileges on all profiled tables.
  + To ingest `profiling` information with `method: analyze` and `call_analyze: true` (enabled by default), your service principal must have ownership or `MODIFY` privilege on any tables you want to profile.
    * Alternatively, you can run [ANALYZE TABLE](https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-analyze-table.html) yourself on any tables you want to profile, then set `call_analyze` to `false`.
    You will still need `SELECT` privilege on those tables to fetch the results.
- Check the starter recipe below and replace `workspace_url` and `token` with your information from the previous steps.

### CLI based Ingestion

#### Install the Plugin
The `unity-catalog` source works out of the box with `acryl-datahub`.

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: unity-catalog
  config:
    workspace_url: https://my-workspace.cloud.databricks.com
    token: "<token>"
    include_metastore: false
    include_ownership: true
    profiling:
      method: "ge"
      enabled: true
      warehouse_id: "<warehouse_id>"
      profile_table_level_only: false
      max_wait_secs: 60
      pattern:
        deny:
          - ".*\\.unwanted_schema"

#    emit_siblings: true
#    delta_lake_options:
#      platform_instance_name: null
#      env: 'PROD'

#    profiling:
#      method: "analyze"
#      enabled: true
#      warehouse_id: "<warehouse_id>"
#      profile_table_level_only: true
#      call_analyze: true

#    catalogs: ["my_catalog"]
#    schema_pattern:
#      deny:
#        - information_schema
#    table_pattern:
#      allow:
#        - my_catalog.my_schema.my_table
#     First you have to create domains on Datahub by following this guide -> https://datahubproject.io/docs/domains/#domains-setup-prerequisites-and-permissions
#    domain:
#      urn:li:domain:1111-222-333-444-555:
#        allow:
#          - main.*

    stateful_ingestion:
      enabled: true

pipeline_name: acme-corp-unity


# sink configs if needed

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">token</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Databricks personal access token  |
| <div className="path-line"><span className="path-main">workspace_url</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Databricks workspace url. e.g. https://my-workspace.cloud.databricks.com  |
| <div className="path-line"><span className="path-main">bucket_duration</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Size of the time window to aggregate usage stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">DAY</span></div> |
| <div className="path-line"><span className="path-main">column_lineage_column_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Limit the number of columns to get column level lineage.  <div className="default-line default-line-with-docs">Default: <span className="default-value">300</span></div> |
| <div className="path-line"><span className="path-main">convert_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert dataset urns to lowercase. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">emit_siblings</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to emit siblings relation with corresponding delta-lake platform's table. If enabled, this will also ingest the corresponding delta-lake table. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">enable_stateful_profiling</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable stateful profiling. This will store profiling timestamps per dataset after successful profiling. and will not run profiling again in subsequent run if table has not been updated.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">end_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Latest date of lineage/usage to consider. Default: Current time in UTC  |
| <div className="path-line"><span className="path-main">format_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to format sql queries <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable lineage generation. Currently we have to call a rest call per column to get column level lineage due to the Databrick api which can slow down ingestion.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_external_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable lineage generation for external tables. Only external S3 tables are supported at the moment. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_hive_metastore</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest legacy `hive_metastore` catalog. This requires executing queries on SQL warehouse. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_metastore</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the workspace's metastore as a container and include it in all urns. Changing this will affect the urns of all entities in the workspace. This config is deprecated and will be removed in the future, so it is recommended to not set this to `True` for new ingestions. If you have an existing unity catalog ingestion, you'll want to avoid duplicates by soft deleting existing data. If stateful ingestion is enabled, running with `include_metastore: false` should be sufficient. Otherwise, we recommend deleting via the cli: `datahub delete --platform databricks` and re-ingesting with `include_metastore: false`. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_notebooks</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest notebooks, represented as DataHub datasets. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to display operational stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_ownership</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable ownership generation for metastores, catalogs, schemas, and tables. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_read_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report read operational stats. Experimental. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_table_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable lineage generation. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_table_location_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If the source supports it, include table lineage to the underlying storage location. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether tables should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_top_n_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the top_n_queries. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_usage_statistics</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Generate usage statistics. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates column-level lineage for  view->view and table->view lineage using DataHub's sql parser. Requires `include_view_lineage` to be enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates view->view and table->view lineage using DataHub's sql parser. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_views</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether views should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">incremental_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, emits lineage as incremental to existing lineage already in DataHub. When disabled, re-states lineage on each run. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_data_platform_instance_aspect</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Option to enable/disable ingestion of the data platform instance aspect. The default data platform instance id for a dataset is workspace_name <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">databricks</span></div> |
| <div className="path-line"><span className="path-main">start_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.  |
| <div className="path-line"><span className="path-main">top_n_queries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of top queries to save to each table. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-main">use_file_backed_cache</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to use a file backed cache for the view definitions. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">warehouse_id</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | SQL Warehouse id, for running queries. If not set, will use the default warehouse.  |
| <div className="path-line"><span className="path-main">workspace_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of the workspace. Default to deployment name present in workspace_url  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">catalog_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for catalogs to filter in ingestion. Specify regex to match the full `metastore.catalog` name. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">catalog_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">catalog_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">catalog_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">catalog_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">catalog_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">catalogs</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Fixed list of catalogs to ingest. If not specified, catalogs will be ingested based on `catalog_pattern`.  |
| <div className="path-line"><span className="path-prefix">catalogs.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">classification</span></div> <div className="type-name-line"><span className="type-name">ClassificationConfig</span></div> | For details, refer [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md). <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;sample&#95;size&#x27;: 100, &#x27;max&#95;worker...</span></div> |
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
| <div className="path-line"><span className="path-main">delta_lake_options</span></div> <div className="type-name-line"><span className="type-name">DeltaLakeDetails</span></div> | Details about the delta lake, incase to emit siblings <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;platform&#95;instance&#95;name&#x27;: None, &#x27;env&#x27;: &#x27;PROD&#x27;&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">delta_lake_options.</span><span className="path-main">platform_instance_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Delta-lake paltform instance name  |
| <div className="path-line"><span className="path-prefix">delta_lake_options.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Delta-lake environment <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">map(str,AllowDenyPattern)</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">notebook_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for notebooks to filter in ingestion, based on notebook *path*. Specify regex to match the entire notebook path in `/<dir>/.../<name>` format. e.g. to match all notebooks in the root Shared directory, use the regex `/Shared/.*`. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">notebook_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">notebook_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">notebook_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">notebook_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">notebook_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profile_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter tables (or specific columns) for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">schema_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for schemas to filter in ingestion. Specify regex to the full `metastore.catalog.schema` name. e.g. to match all tables in schema analytics, use the regex `^mymetastore\.mycatalog\.analytics$`. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. Specify regex to match the entire table name in `catalog.schema.table` format. e.g. to match all tables starting with customer in Customer catalog and public schema, use the regex `Customer\.public\.customer.*`. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">user_email_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | regex patterns for user emails to filter in usage. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">user_email_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">user_email_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">user_email_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">user_email_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">user_email_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">view_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for views to filter in ingestion. Note: Defaults to table_pattern if not specified. Specify regex to match the entire view name in database.schema.view format. e.g. to match all views starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">One of UnityCatalogGEProfilerConfig, UnityCatalogAnalyzeProfilerConfig</span></div> | Data profiling configuration <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;operation&#95;config&#x27;: &#123;&#x27;lower&#95;fre...</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">call_analyze</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to call ANALYZE TABLE as part of profile ingestion.If false, will ingest the results of the most recent ANALYZE TABLE call, if any. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
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
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_wait_secs</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum time to wait for a table to be profiled.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use for profiling. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">50</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">method</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "ge" <div className="default-line default-line-with-docs">Default: <span className="default-value">ge</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">offset</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Offset in documents to profile. By default, uses no offset.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">partition_datetime</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | If specified, profile only the partition which matches this datetime. If not specified, profile the latest partition. Only Bigquery supports this.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">partition_profiling_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile partitioned tables. Only BigQuery and Aws Athena supports this. If enabled, latest partition data is used for profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_external_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile external tables. Only Snowflake and Redshift supports this. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_if_updated_since_days</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Profile table only if it has been updated since these many number of days. If set to `null`, no constraint of last modified time for tables to profile. Supported only in `snowflake` and `BigQuery`.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_level_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to perform profiling at table-level only, or include column-level profiling as well. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_row_count_estimate_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use an approximate query for row count. This will be much faster but slightly less accurate. Only supported for Postgres and MySQL.  <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_row_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Profile tables only if their row count is less then specified count. If set to `null`, no limit on the row count of tables to profile. Supported only in `snowflake` and `BigQuery` <div className="default-line default-line-with-docs">Default: <span className="default-value">5000000</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_size_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Profile tables only if their size is less then specified GBs. If set to `null`, no limit on the size of tables to profile. Supported only in `snowflake` and `BigQuery` <div className="default-line default-line-with-docs">Default: <span className="default-value">5</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">query_combiner_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | *This feature is still experimental and can be disabled if it causes issues.* Reduces the total number of queries issued and speeds up profiling by dynamically combining SQL queries where possible. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">report_dropped_profiles</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report datasets or dataset columns which were not profiled. Set to `True` for debugging purposes. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">sample_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of rows to be sampled from table for column level profiling.Applicable only if `use_sampling` is set to True. <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">turn_off_expensive_profiling_metrics</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to turn off expensive profiling or not. This turns off profiling for quantiles, distinct_value_frequencies, histogram & sample_values. This also limits maximum number of fields being profiled to 10. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">use_sampling</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile column level stats on sample of table. Only BigQuery and Snowflake support this. If enabled, profiling is done on rows sampled from table. Sampling is not done for smaller tables.  <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">warehouse_id</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | SQL Warehouse id, for running profiling queries.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">operation_config</span></div> <div className="type-name-line"><span className="type-name">One of OperationConfig, union(allOf), OperationConfig</span></div> | Experimental feature. To specify operation configs.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">lower_freq_profile_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_date_of_month</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_day_of_week</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">pattern</span></div> <div className="type-name-line"><span className="type-name">One of AllowDenyPattern, union(allOf), AllowDenyPattern</span></div> | Regex patterns to filter tables for profiling during ingestion. Specify regex to match the `catalog.schema.table` format. Note that only tables allowed by the `table_pattern` will be considered. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profiling.pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">tags_to_ignore_sampling</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Fixed list of tags to ignore sampling. If not specified, tables will be sampled based on `use_sampling`.  |
| <div className="path-line"><span className="path-prefix">profiling.tags_to_ignore_sampling.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Unity Catalog Stateful Ingestion Config.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "UnityCatalogSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "convert_urns_to_lowercase": {
      "title": "Convert Urns To Lowercase",
      "description": "Whether to convert dataset urns to lowercase.",
      "default": false,
      "type": "boolean"
    },
    "enable_stateful_profiling": {
      "title": "Enable Stateful Profiling",
      "description": "Enable stateful profiling. This will store profiling timestamps per dataset after successful profiling. and will not run profiling again in subsequent run if table has not been updated. ",
      "default": true,
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
      "description": "The instance of the platform that all assets produced by this recipe belong to",
      "type": "string"
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
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Unity Catalog Stateful Ingestion Config.",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
        }
      ]
    },
    "schema_pattern": {
      "title": "Schema Pattern",
      "description": "Regex patterns for schemas to filter in ingestion. Specify regex to the full `metastore.catalog.schema` name. e.g. to match all tables in schema analytics, use the regex `^mymetastore\\.mycatalog\\.analytics$`.",
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
    "table_pattern": {
      "title": "Table Pattern",
      "description": "Regex patterns for tables to filter in ingestion. Specify regex to match the entire table name in `catalog.schema.table` format. e.g. to match all tables starting with customer in Customer catalog and public schema, use the regex `Customer\\.public\\.customer.*`.",
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
    "classification": {
      "title": "Classification",
      "description": "For details, refer [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md).",
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
    "incremental_lineage": {
      "title": "Incremental Lineage",
      "description": "When enabled, emits lineage as incremental to existing lineage already in DataHub. When disabled, re-states lineage on each run.",
      "default": false,
      "type": "boolean"
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
      "description": "Attach domains to catalogs, schemas or tables during ingestion using regex patterns. Domain key can be a guid like *urn:li:domain:ec428203-ce86-4db3-985d-5a8ee6df32ba* or a string like \"Marketing\".) If you provide strings, then datahub will attempt to resolve this name to a guid, and will error out if this fails. There can be multiple domain keys specified.",
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
      "description": "Data profiling configuration",
      "default": {
        "enabled": false,
        "operation_config": {
          "lower_freq_profile_enabled": false,
          "profile_day_of_week": null,
          "profile_date_of_month": null
        },
        "limit": null,
        "offset": null,
        "report_dropped_profiles": false,
        "turn_off_expensive_profiling_metrics": false,
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
        "field_sample_values_limit": 20,
        "max_number_of_fields_to_profile": null,
        "profile_if_updated_since_days": null,
        "profile_table_size_limit": 5,
        "profile_table_row_limit": 5000000,
        "profile_table_row_count_estimate_only": false,
        "max_workers": 50,
        "query_combiner_enabled": true,
        "catch_exceptions": true,
        "partition_profiling_enabled": true,
        "partition_datetime": null,
        "use_sampling": true,
        "sample_size": 10000,
        "profile_external_tables": false,
        "tags_to_ignore_sampling": null,
        "method": "ge",
        "warehouse_id": null,
        "pattern": {
          "allow": [
            ".*"
          ],
          "deny": [],
          "ignoreCase": true
        },
        "max_wait_secs": null
      },
      "discriminator": {
        "propertyName": "method",
        "mapping": {
          "ge": "#/definitions/UnityCatalogGEProfilerConfig",
          "analyze": "#/definitions/UnityCatalogAnalyzeProfilerConfig"
        }
      },
      "oneOf": [
        {
          "$ref": "#/definitions/UnityCatalogGEProfilerConfig"
        },
        {
          "$ref": "#/definitions/UnityCatalogAnalyzeProfilerConfig"
        }
      ]
    },
    "token": {
      "title": "Token",
      "description": "Databricks personal access token",
      "type": "string"
    },
    "workspace_url": {
      "title": "Workspace Url",
      "description": "Databricks workspace url. e.g. https://my-workspace.cloud.databricks.com",
      "type": "string"
    },
    "warehouse_id": {
      "title": "Warehouse Id",
      "description": "SQL Warehouse id, for running queries. If not set, will use the default warehouse.",
      "type": "string"
    },
    "include_hive_metastore": {
      "title": "Include Hive Metastore",
      "description": "Whether to ingest legacy `hive_metastore` catalog. This requires executing queries on SQL warehouse.",
      "default": true,
      "type": "boolean"
    },
    "workspace_name": {
      "title": "Workspace Name",
      "description": "Name of the workspace. Default to deployment name present in workspace_url",
      "type": "string"
    },
    "include_metastore": {
      "title": "Include Metastore",
      "description": "Whether to ingest the workspace's metastore as a container and include it in all urns. Changing this will affect the urns of all entities in the workspace. This config is deprecated and will be removed in the future, so it is recommended to not set this to `True` for new ingestions. If you have an existing unity catalog ingestion, you'll want to avoid duplicates by soft deleting existing data. If stateful ingestion is enabled, running with `include_metastore: false` should be sufficient. Otherwise, we recommend deleting via the cli: `datahub delete --platform databricks` and re-ingesting with `include_metastore: false`.",
      "default": false,
      "type": "boolean"
    },
    "ingest_data_platform_instance_aspect": {
      "title": "Ingest Data Platform Instance Aspect",
      "description": "Option to enable/disable ingestion of the data platform instance aspect. The default data platform instance id for a dataset is workspace_name",
      "default": false,
      "type": "boolean"
    },
    "catalogs": {
      "title": "Catalogs",
      "description": "Fixed list of catalogs to ingest. If not specified, catalogs will be ingested based on `catalog_pattern`.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "catalog_pattern": {
      "title": "Catalog Pattern",
      "description": "Regex patterns for catalogs to filter in ingestion. Specify regex to match the full `metastore.catalog` name.",
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
    "notebook_pattern": {
      "title": "Notebook Pattern",
      "description": "Regex patterns for notebooks to filter in ingestion, based on notebook *path*. Specify regex to match the entire notebook path in `/<dir>/.../<name>` format. e.g. to match all notebooks in the root Shared directory, use the regex `/Shared/.*`.",
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
    "include_table_lineage": {
      "title": "Include Table Lineage",
      "description": "Option to enable/disable lineage generation.",
      "default": true,
      "type": "boolean"
    },
    "include_external_lineage": {
      "title": "Include External Lineage",
      "description": "Option to enable/disable lineage generation for external tables. Only external S3 tables are supported at the moment.",
      "default": true,
      "type": "boolean"
    },
    "include_notebooks": {
      "title": "Include Notebooks",
      "description": "Ingest notebooks, represented as DataHub datasets.",
      "default": false,
      "type": "boolean"
    },
    "include_ownership": {
      "title": "Include Ownership",
      "description": "Option to enable/disable ownership generation for metastores, catalogs, schemas, and tables.",
      "default": false,
      "type": "boolean"
    },
    "include_column_lineage": {
      "title": "Include Column Lineage",
      "description": "Option to enable/disable lineage generation. Currently we have to call a rest call per column to get column level lineage due to the Databrick api which can slow down ingestion. ",
      "default": true,
      "type": "boolean"
    },
    "column_lineage_column_limit": {
      "title": "Column Lineage Column Limit",
      "description": "Limit the number of columns to get column level lineage. ",
      "default": 300,
      "type": "integer"
    },
    "include_usage_statistics": {
      "title": "Include Usage Statistics",
      "description": "Generate usage statistics.",
      "default": true,
      "type": "boolean"
    },
    "emit_siblings": {
      "title": "Emit Siblings",
      "description": "Whether to emit siblings relation with corresponding delta-lake platform's table. If enabled, this will also ingest the corresponding delta-lake table.",
      "default": true,
      "type": "boolean"
    },
    "delta_lake_options": {
      "title": "Delta Lake Options",
      "description": "Details about the delta lake, incase to emit siblings",
      "default": {
        "platform_instance_name": null,
        "env": "PROD"
      },
      "allOf": [
        {
          "$ref": "#/definitions/DeltaLakeDetails"
        }
      ]
    },
    "scheme": {
      "title": "Scheme",
      "default": "databricks",
      "type": "string"
    }
  },
  "required": [
    "token",
    "workspace_url"
  ],
  "additionalProperties": false,
  "definitions": {
    "BucketDuration": {
      "title": "BucketDuration",
      "description": "An enumeration.",
      "enum": [
        "DAY",
        "HOUR"
      ],
      "type": "string"
    },
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
    "UnityCatalogGEProfilerConfig": {
      "title": "UnityCatalogGEProfilerConfig",
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
          "description": "Profile tables only if their size is less then specified GBs. If set to `null`, no limit on the size of tables to profile. Supported only in `snowflake` and `BigQuery`",
          "default": 5,
          "type": "integer"
        },
        "profile_table_row_limit": {
          "title": "Profile Table Row Limit",
          "description": "Profile tables only if their row count is less then specified count. If set to `null`, no limit on the row count of tables to profile. Supported only in `snowflake` and `BigQuery`",
          "default": 5000000,
          "type": "integer"
        },
        "profile_table_row_count_estimate_only": {
          "title": "Profile Table Row Count Estimate Only",
          "description": "Use an approximate query for row count. This will be much faster but slightly less accurate. Only supported for Postgres and MySQL. ",
          "default": false,
          "type": "boolean"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "Number of worker threads to use for profiling. Set to 1 to disable.",
          "default": 50,
          "type": "integer"
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
        "method": {
          "title": "Method",
          "default": "ge",
          "enum": [
            "ge"
          ],
          "type": "string"
        },
        "warehouse_id": {
          "title": "Warehouse Id",
          "description": "SQL Warehouse id, for running profiling queries.",
          "type": "string"
        },
        "pattern": {
          "title": "Pattern",
          "description": "Regex patterns to filter tables for profiling during ingestion. Specify regex to match the `catalog.schema.table` format. Note that only tables allowed by the `table_pattern` will be considered.",
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
        "max_wait_secs": {
          "title": "Max Wait Secs",
          "description": "Maximum time to wait for a table to be profiled.",
          "type": "integer"
        }
      },
      "additionalProperties": false
    },
    "UnityCatalogAnalyzeProfilerConfig": {
      "title": "UnityCatalogAnalyzeProfilerConfig",
      "type": "object",
      "properties": {
        "method": {
          "title": "Method",
          "default": "analyze",
          "enum": [
            "analyze"
          ],
          "type": "string"
        },
        "warehouse_id": {
          "title": "Warehouse Id",
          "description": "SQL Warehouse id, for running profiling queries.",
          "type": "string"
        },
        "pattern": {
          "title": "Pattern",
          "description": "Regex patterns to filter tables for profiling during ingestion. Specify regex to match the `catalog.schema.table` format. Note that only tables allowed by the `table_pattern` will be considered.",
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
        "profile_table_level_only": {
          "title": "Profile Table Level Only",
          "description": "Whether to perform profiling at table-level only or include column-level profiling as well.",
          "default": false,
          "type": "boolean"
        },
        "call_analyze": {
          "title": "Call Analyze",
          "description": "Whether to call ANALYZE TABLE as part of profile ingestion.If false, will ingest the results of the most recent ANALYZE TABLE call, if any.",
          "default": true,
          "type": "boolean"
        },
        "max_wait_secs": {
          "title": "Max Wait Secs",
          "description": "Maximum time to wait for an ANALYZE TABLE query to complete.",
          "default": 3600,
          "type": "integer"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "Number of worker threads to use for profiling. Set to 1 to disable.",
          "default": 50,
          "type": "integer"
        }
      },
      "additionalProperties": false
    },
    "DeltaLakeDetails": {
      "title": "DeltaLakeDetails",
      "type": "object",
      "properties": {
        "platform_instance_name": {
          "title": "Platform Instance Name",
          "description": "Delta-lake paltform instance name",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "Delta-lake environment",
          "default": "PROD",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>



### Advanced

#### Multiple Databricks Workspaces

If you have multiple databricks workspaces **that point to the same Unity Catalog metastore**, our suggestion is to use separate recipes for ingesting the workspace-specific Hive Metastore catalog and Unity Catalog metastore's information schema.

To ingest Hive metastore information schema
- Setup one ingestion recipe per workspace
- Use platform instance equivalent to workspace name
- Ingest only hive_metastore catalog in the recipe using config `catalogs: ["hive_metastore"]`

To ingest Unity Catalog information schema
- Disable hive metastore catalog ingestion in the recipe using config `include_hive_metastore: False`
- Ideally, just ingest from one workspace
- To ingest from both workspaces (e.g. if each workspace has different permissions and therefore restricted view of the UC metastore):
    - Use same platform instance for all workspaces using same UC metastore
    - Ingest usage from only one workspace (you lose usage from other workspace)
    - Use filters to only ingest each catalog once, but shouldn’t be necessary


### Troubleshooting

#### No data lineage captured or missing lineage

Check that you meet the [Unity Catalog lineage requirements](https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html#requirements).

Also check the [Unity Catalog limitations](https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html#limitations) to make sure that lineage would be expected to exist in this case.

#### Lineage extraction is too slow

Currently, there is no way to get table or column lineage in bulk from the Databricks Unity Catalog REST api. Table lineage calls require one API call per table, and column lineage calls require one API call per column. If you find metadata extraction taking too long, you can turn off column level lineage extraction via the `include_column_lineage` config flag.

### Code Coordinates
- Class Name: `datahub.ingestion.source.unity.source.UnityCatalogSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/unity/source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Databricks, feel free to ping us on [our Slack](https://slack.datahubproject.io).
