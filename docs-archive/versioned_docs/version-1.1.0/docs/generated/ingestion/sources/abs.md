---
sidebar_position: 1
title: ABS Data Lake
slug: /generated/ingestion/sources/abs
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/abs.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ABS Data Lake
This connector ingests Azure Blob Storage (abbreviated to abs) datasets into DataHub. It allows mapping an individual
file or a folder of files to a dataset in DataHub.
To specify the group of files that form a dataset, use `path_specs` configuration in ingestion recipe. Refer
section [Path Specs](/docs/generated/ingestion/sources/s3/#path-specs) for more details.

### Concept Mapping

This ingestion source maps the following Source System Concepts to DataHub Concepts:

| Source Concept                         | DataHub Concept                                                                           | Notes            |
| -------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------- |
| `"abs"`                                | [Data Platform](/docs/generated/metamodel/entities/dataplatform/) |                  |
| abs blob / Folder containing abs blobs | [Dataset](/docs/generated/metamodel/entities/dataset/)            |                  |
| abs container                          | [Container](/docs/generated/metamodel/entities/container/)        | Subtype `Folder` |

This connector supports both local files and those stored on Azure Blob Storage (which must be identified using the
prefix `http(s)://<account>.blob.core.windows.net/` or `azure://`).

### Supported file types

Supported file types are as follows:

- CSV (\*.csv)
- TSV (\*.tsv)
- JSONL (\*.jsonl)
- JSON (\*.json)
- Parquet (\*.parquet)
- Apache Avro (\*.avro)

Schemas for Parquet and Avro files are extracted as provided.

Schemas for schemaless formats (CSV, TSV, JSONL, JSON) are inferred. For CSV, TSV and JSONL files, we consider the first
100 rows by default, which can be controlled via the `max_rows` recipe parameter (see [below](#config-details))
JSON file schemas are inferred on the basis of the entire file (given the difficulty in extracting only the first few
objects of the file), which may impact performance.
We are working on using iterator-based JSON parsers to avoid reading in the entire JSON object.

### Profiling

Profiling is not available in the current release.
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Optionally enabled via configuration |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Tags | ✅ | Can extract ABS object/container tags if enabled |



### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: abs
  config:
    path_specs:
      - include: "https://storageaccountname.blob.core.windows.net/covid19-lake/covid_knowledge_graph/csv/nodes/*.*"

    azure_config:
      account_name: "*****"
      sas_token: "*****"
      container_name: "covid_knowledge_graph"
    env: "PROD"

# sink configs

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">path_specs</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of PathSpec. See [below](#path-spec) the details about PathSpec  |
| <div className="path-line"><span className="path-prefix">path_specs.</span><span className="path-main">PathSpec</span></div> <div className="type-name-line"><span className="type-name">PathSpec</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">include</span>&nbsp;<abbr title="Required if PathSpec is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to table. Name variable `{table}` is used to mark the folder with dataset. In absence of `{table}`, file level dataset will be created. Check below examples for more details.  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">allow_double_stars</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Allow double stars in the include path. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">autodetect_partitions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Autodetect partition(s) from the path. If set to true, it will autodetect partition key/value if the folder format is {partition_key}={partition_value} for example `year=2024` <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">default_extension</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | For files without extension it will assume the specified file type. If it is not set the files without extensions will be skipped.  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">enable_compression</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable or disable processing compressed files. Currently .gz and .bz files are supported. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">include_hidden_folders</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include hidden folders in the traversal (folders starting with . or _ <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">sample_files</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Not listing all the files but only taking a handful amount of sample file to infer the schema. File count and file size calculation will be disabled. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">table_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Display name of the dataset.Combination of named variables from include path and strings  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">traversal_method</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Method to traverse the folder. ALL: Traverse all the folders, MIN_MAX: Traverse the folders by finding min and max value, MAX: Traverse the folder with max value <div className="default-line default-line-with-docs">Default: <span className="default-value">MAX</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">exclude</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | list of paths in glob pattern which will be excluded while scanning for the datasets <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.exclude.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">file_types</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Files with extenstions specified here (subset of default value) only will be scanned to create dataset. Other files will be omitted. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;csv&#x27;, &#x27;tsv&#x27;, &#x27;json&#x27;, &#x27;parquet&#x27;, &#x27;avro&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.file_types.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">tables_filter_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | The tables_filter_pattern configuration field uses regular expressions to filter the tables part of the Pathspec for ingestion, allowing fine-grained control over which tables are included or excluded based on specified patterns. The default setting allows all tables. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.tables_filter_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.tables_filter_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.tables_filter_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.tables_filter_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.tables_filter_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">add_partition_columns_to_schema</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to add partition fields to the schema. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">max_rows</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of rows to use when inferring schemas for TSV and CSV files. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-main">number_of_files_to_sample</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of files to list to sample for schema inference. This will be ignored if sample_files is set to False in the pathspec. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-main">platform</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The platform that this source connects to (either 'abs' or 'file'). If not specified, the platform will be inferred from the path_specs. <div className="default-line default-line-with-docs">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">spark_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Spark configuration properties to set on the SparkSession. Put config property names into quotes. For example: '"spark.executor.memory": "2g"' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-main">spark_driver_memory</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Max amount of memory to grant Spark. <div className="default-line default-line-with-docs">Default: <span className="default-value">4g</span></div> |
| <div className="path-line"><span className="path-main">use_abs_blob_properties</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to create tags in datahub from the abs blob properties  |
| <div className="path-line"><span className="path-main">use_abs_blob_tags</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to create tags in datahub from the abs blob tags  |
| <div className="path-line"><span className="path-main">use_abs_container_properties</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to create tags in datahub from the abs container properties  |
| <div className="path-line"><span className="path-main">verify_ssl</span></div> <div className="type-name-line"><span className="type-name">One of boolean, string</span></div> | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">azure_config</span></div> <div className="type-name-line"><span className="type-name">AzureConnectionConfig</span></div> | Azure configuration  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">account_name</span>&nbsp;<abbr title="Required if azure_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of the Azure storage account.  See [Microsoft official documentation on how to create a storage account.](https://docs.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account)  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">container_name</span>&nbsp;<abbr title="Required if azure_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure storage account container name.  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">account_key</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure storage account access key that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">base_path</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Base folder in hierarchical namespaces to start from. <div className="default-line default-line-with-docs">Default: <span className="default-value">/</span></div> |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">client_id</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure client (Application) ID required when a `client_secret` is used as a credential.  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">client_secret</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure client secret that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">sas_token</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure storage account Shared Access Signature (SAS) token that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**  |
| <div className="path-line"><span className="path-prefix">azure_config.</span><span className="path-main">tenant_id</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure tenant (Directory) ID required when a `client_secret` is used as a credential.  |
| <div className="path-line"><span className="path-main">profile_patterns</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | regex patterns for tables to profile  <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_patterns.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_patterns.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_patterns.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_patterns.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_patterns.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">DataLakeProfilerConfig</span></div> | Data profiling configuration <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;operation&#95;config&#x27;: &#123;&#x27;lower&#95;fre...</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether profiling should be done. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_distinct_value_frequencies</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for distinct value frequencies. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_histogram</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the histogram for numeric fields. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_max_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the max value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_mean_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the mean value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_median_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the median value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_min_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the min value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_null_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of nulls for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_quantiles</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the quantiles of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_sample_values</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the sample values for all columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_stddev_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the standard deviation of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_number_of_fields_to_profile</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | A positive integer that specifies the maximum number of columns to profile for any table. `None` implies all columns. The cost of profiling goes up significantly as the number of columns to profile goes up.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_level_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to perform profiling at table-level only or include column-level profiling as well. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">operation_config</span></div> <div className="type-name-line"><span className="type-name">OperationConfig</span></div> | Experimental feature. To specify operation configs.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">lower_freq_profile_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_date_of_month</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_day_of_week</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">fail_safe_threshold</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'. <div className="default-line default-line-with-docs">Default: <span className="default-value">75.0</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataLakeSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "path_specs": {
      "title": "Path Specs",
      "description": "List of PathSpec. See [below](#path-spec) the details about PathSpec",
      "type": "array",
      "items": {
        "$ref": "#/definitions/PathSpec"
      }
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "platform": {
      "title": "Platform",
      "description": "The platform that this source connects to (either 'abs' or 'file'). If not specified, the platform will be inferred from the path_specs.",
      "default": "",
      "type": "string"
    },
    "azure_config": {
      "title": "Azure Config",
      "description": "Azure configuration",
      "allOf": [
        {
          "$ref": "#/definitions/AzureConnectionConfig"
        }
      ]
    },
    "use_abs_container_properties": {
      "title": "Use Abs Container Properties",
      "description": "Whether to create tags in datahub from the abs container properties",
      "type": "boolean"
    },
    "use_abs_blob_tags": {
      "title": "Use Abs Blob Tags",
      "description": "Whether to create tags in datahub from the abs blob tags",
      "type": "boolean"
    },
    "use_abs_blob_properties": {
      "title": "Use Abs Blob Properties",
      "description": "Whether to create tags in datahub from the abs blob properties",
      "type": "boolean"
    },
    "profile_patterns": {
      "title": "Profile Patterns",
      "description": "regex patterns for tables to profile ",
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
        "profile_table_level_only": false,
        "max_number_of_fields_to_profile": null,
        "include_field_null_count": true,
        "include_field_min_value": true,
        "include_field_max_value": true,
        "include_field_mean_value": true,
        "include_field_median_value": true,
        "include_field_stddev_value": true,
        "include_field_quantiles": true,
        "include_field_distinct_value_frequencies": true,
        "include_field_histogram": true,
        "include_field_sample_values": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/DataLakeProfilerConfig"
        }
      ]
    },
    "spark_driver_memory": {
      "title": "Spark Driver Memory",
      "description": "Max amount of memory to grant Spark.",
      "default": "4g",
      "type": "string"
    },
    "spark_config": {
      "title": "Spark Config",
      "description": "Spark configuration properties to set on the SparkSession. Put config property names into quotes. For example: '\"spark.executor.memory\": \"2g\"'",
      "default": {},
      "type": "object"
    },
    "max_rows": {
      "title": "Max Rows",
      "description": "Maximum number of rows to use when inferring schemas for TSV and CSV files.",
      "default": 100,
      "type": "integer"
    },
    "add_partition_columns_to_schema": {
      "title": "Add Partition Columns To Schema",
      "description": "Whether to add partition fields to the schema.",
      "default": false,
      "type": "boolean"
    },
    "verify_ssl": {
      "title": "Verify Ssl",
      "description": "Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use.",
      "default": true,
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "string"
        }
      ]
    },
    "number_of_files_to_sample": {
      "title": "Number Of Files To Sample",
      "description": "Number of files to list to sample for schema inference. This will be ignored if sample_files is set to False in the pathspec.",
      "default": 100,
      "type": "integer"
    }
  },
  "required": [
    "path_specs"
  ],
  "additionalProperties": false,
  "definitions": {
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
        },
        "tables_filter_pattern": {
          "title": "Tables Filter Pattern",
          "description": "The tables_filter_pattern configuration field uses regular expressions to filter the tables part of the Pathspec for ingestion, allowing fine-grained control over which tables are included or excluded based on specified patterns. The default setting allows all tables.",
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
        }
      },
      "required": [
        "include"
      ],
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
        },
        "fail_safe_threshold": {
          "title": "Fail Safe Threshold",
          "description": "Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'.",
          "default": 75.0,
          "minimum": 0.0,
          "maximum": 100.0,
          "type": "number"
        }
      },
      "additionalProperties": false
    },
    "AzureConnectionConfig": {
      "title": "AzureConnectionConfig",
      "description": "Common Azure credentials config.\n\nhttps://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-directory-file-acl-python",
      "type": "object",
      "properties": {
        "base_path": {
          "title": "Base Path",
          "description": "Base folder in hierarchical namespaces to start from.",
          "default": "/",
          "type": "string"
        },
        "container_name": {
          "title": "Container Name",
          "description": "Azure storage account container name.",
          "type": "string"
        },
        "account_name": {
          "title": "Account Name",
          "description": "Name of the Azure storage account.  See [Microsoft official documentation on how to create a storage account.](https://docs.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account)",
          "type": "string"
        },
        "account_key": {
          "title": "Account Key",
          "description": "Azure storage account access key that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**",
          "type": "string"
        },
        "sas_token": {
          "title": "Sas Token",
          "description": "Azure storage account Shared Access Signature (SAS) token that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**",
          "type": "string"
        },
        "client_secret": {
          "title": "Client Secret",
          "description": "Azure client secret that can be used as a credential. **An account key, a SAS token or a client secret is required for authentication.**",
          "type": "string"
        },
        "client_id": {
          "title": "Client Id",
          "description": "Azure client (Application) ID required when a `client_secret` is used as a credential.",
          "type": "string"
        },
        "tenant_id": {
          "title": "Tenant Id",
          "description": "Azure tenant (Directory) ID required when a `client_secret` is used as a credential.",
          "type": "string"
        }
      },
      "required": [
        "container_name",
        "account_name"
      ],
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
    "DataLakeProfilerConfig": {
      "title": "DataLakeProfilerConfig",
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
        "profile_table_level_only": {
          "title": "Profile Table Level Only",
          "description": "Whether to perform profiling at table-level only or include column-level profiling as well.",
          "default": false,
          "type": "boolean"
        },
        "max_number_of_fields_to_profile": {
          "title": "Max Number Of Fields To Profile",
          "description": "A positive integer that specifies the maximum number of columns to profile for any table. `None` implies all columns. The cost of profiling goes up significantly as the number of columns to profile goes up.",
          "exclusiveMinimum": 0,
          "type": "integer"
        },
        "include_field_null_count": {
          "title": "Include Field Null Count",
          "description": "Whether to profile for the number of nulls for each column.",
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
          "default": true,
          "type": "boolean"
        },
        "include_field_distinct_value_frequencies": {
          "title": "Include Field Distinct Value Frequencies",
          "description": "Whether to profile for distinct value frequencies.",
          "default": true,
          "type": "boolean"
        },
        "include_field_histogram": {
          "title": "Include Field Histogram",
          "description": "Whether to profile for the histogram for numeric fields.",
          "default": true,
          "type": "boolean"
        },
        "include_field_sample_values": {
          "title": "Include Field Sample Values",
          "description": "Whether to profile for the sample values for all columns.",
          "default": true,
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

### Path Specs

Path Specs (`path_specs`) is a list of Path Spec (`path_spec`) objects, where each individual `path_spec` represents one or more datasets. The include path (`path_spec.include`) represents a formatted path to the dataset. This path must end with `*.*` or `*.[ext]` to represent the leaf level. If `*.[ext]` is provided, then only files with the specified extension type will be scanned. "`.[ext]`" can be any of the [supported file types](#supported-file-types). Refer to [example 1](#example-1---individual-file-as-dataset) below for more details.

All folder levels need to be specified in the include path. You can use `/*/` to represent a folder level and avoid specifying the exact folder name. To map a folder as a dataset, use the `{table}` placeholder to represent the folder level for which the dataset is to be created. For a partitioned dataset, you can use the placeholder `{partition_key[i]}` to represent the name of the `i`th partition and `{partition[i]}` to represent the value of the `i`th partition. During ingestion, `i` will be used to match the partition_key to the partition. Refer to [examples 2 and 3](#example-2---folder-of-files-as-dataset-without-partitions) below for more details.

Exclude paths (`path_spec.exclude`) can be used to ignore paths that are not relevant to the current `path_spec`. This path cannot have named variables (`{}`). The exclude path can have `**` to represent multiple folder levels. Refer to [example 4](#example-4---folder-of-files-as-dataset-with-partitions-and-exclude-filter) below for more details.

Refer to [example 5](#example-5---advanced---either-individual-file-or-folder-of-files-as-dataset) if your container has a more complex dataset representation.

**Additional points to note**

- Folder names should not contain {, }, \*, / in their names.
- Named variable {folder} is reserved for internal working. please do not use in named variables.

### Path Specs - Examples

#### Example 1 - Individual file as Dataset

Container structure:

```
test-container
├── employees.csv
├── departments.json
└── food_items.csv
```

Path specs config to ingest `employees.csv` and `food_items.csv` as datasets:

```
path_specs:
    - include: https://storageaccountname.blob.core.windows.net/test-container/*.csv

```

This will automatically ignore `departments.json` file. To include it, use `*.*` instead of `*.csv`.

#### Example 2 - Folder of files as Dataset (without Partitions)

Container structure:

```
test-container
└──  offers
     ├── 1.avro
     └── 2.avro

```

Path specs config to ingest folder `offers` as dataset:

```
path_specs:
    - include: https://storageaccountname.blob.core.windows.net/test-container/{table}/*.avro
```

`{table}` represents folder for which dataset will be created.

#### Example 3 - Folder of files as Dataset (with Partitions)

Container structure:

```
test-container
├── orders
│   └── year=2022
│       └── month=2
│           ├── 1.parquet
│           └── 2.parquet
└── returns
    └── year=2021
        └── month=2
            └── 1.parquet

```

Path specs config to ingest folders `orders` and `returns` as datasets:

```
path_specs:
    - include: https://storageaccountname.blob.core.windows.net/test-container/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
```

One can also use `include: https://storageaccountname.blob.core.windows.net/test-container/{table}/*/*/*.parquet` here however above format is preferred as it allows declaring partitions explicitly.

#### Example 4 - Folder of files as Dataset (with Partitions), and Exclude Filter

Container structure:

```
test-container
├── orders
│   └── year=2022
│       └── month=2
│           ├── 1.parquet
│           └── 2.parquet
└── tmp_orders
    └── year=2021
        └── month=2
            └── 1.parquet


```

Path specs config to ingest folder `orders` as dataset but not folder `tmp_orders`:

```
path_specs:
    - include: https://storageaccountname.blob.core.windows.net/test-container/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
      exclude:
        - **/tmp_orders/**
```

#### Example 5 - Advanced - Either Individual file OR Folder of files as Dataset

Container structure:

```
test-container
├── customers
│   ├── part1.json
│   ├── part2.json
│   ├── part3.json
│   └── part4.json
├── employees.csv
├── food_items.csv
├── tmp_10101000.csv
└──  orders
     └── year=2022
         └── month=2
             ├── 1.parquet
             ├── 2.parquet
             └── 3.parquet

```

Path specs config:

```
path_specs:
    - include: https://storageaccountname.blob.core.windows.net/test-container/*.csv
      exclude:
        - **/tmp_10101000.csv
    - include: https://storageaccountname.blob.core.windows.net/test-container/{table}/*.json
    - include: https://storageaccountname.blob.core.windows.net/test-container/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
```

Above config has 3 path_specs and will ingest following datasets

- `employees.csv` - Single File as Dataset
- `food_items.csv` - Single File as Dataset
- `customers` - Folder as Dataset
- `orders` - Folder as Dataset
  and will ignore file `tmp_10101000.csv`

**Valid path_specs.include**

```python
https://storageaccountname.blob.core.windows.net/my-container/foo/tests/bar.avro # single file table
https://storageaccountname.blob.core.windows.net/my-container/foo/tests/*.* # mulitple file level tables
https://storageaccountname.blob.core.windows.net/my-container/foo/tests/{table}/*.avro #table without partition
https://storageaccountname.blob.core.windows.net/my-container/foo/tests/{table}/*/*.avro #table where partitions are not specified
https://storageaccountname.blob.core.windows.net/my-container/foo/tests/{table}/*.* # table where no partitions as well as data type specified
https://storageaccountname.blob.core.windows.net/my-container/{dept}/tests/{table}/*.avro # specifying keywords to be used in display name
https://storageaccountname.blob.core.windows.net/my-container/{dept}/tests/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.avro # specify partition key and value format
https://storageaccountname.blob.core.windows.net/my-container/{dept}/tests/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.avro # specify partition value only format
https://storageaccountname.blob.core.windows.net/my-container/{dept}/tests/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # for all extensions
https://storageaccountname.blob.core.windows.net/my-container/*/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # table is present at 2 levels down in container
https://storageaccountname.blob.core.windows.net/my-container/*/*/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # table is present at 3 levels down in container
```

**Valid path_specs.exclude**

- \*\*/tests/\*\*
- https://storageaccountname.blob.core.windows.net/my-container/hr/**
- \*_/tests/_.csv
- https://storageaccountname.blob.core.windows.net/my-container/foo/*/my_table/**

If you would like to write a more complicated function for resolving file names, then a {transformer} would be a good fit.

:::caution

Specify as long fixed prefix ( with out /\*/ ) as possible in `path_specs.include`. This will reduce the scanning time and cost, specifically on AWS S3

:::

:::caution

Running profiling against many tables or over many rows can run up significant costs.
While we've done our best to limit the expensiveness of the queries the profiler runs, you
should be prudent about the set of tables profiling is enabled on or the frequency
of the profiling runs.

:::

:::caution

If you are ingesting datasets from AWS S3, we recommend running the ingestion on a server in the same region to avoid high egress costs.

:::

### Compatibility

Profiles are computed with PyDeequ, which relies on PySpark. Therefore, for computing profiles, we currently require Spark 3.0.3 with Hadoop 3.2 to be installed and the `SPARK_HOME` and `SPARK_VERSION` environment variables to be set. The Spark+Hadoop binary can be downloaded [here](https://www.apache.org/dyn/closer.lua/spark/spark-3.0.3/spark-3.0.3-bin-hadoop3.2.tgz).

For an example guide on setting up PyDeequ on AWS, see [this guide](https://aws.amazon.com/blogs/big-data/testing-data-quality-at-scale-with-pydeequ/).

:::caution

From Spark 3.2.0+, Avro reader fails on column names that don't start with a letter and contains other character than letters, number, and underscore. [https://github.com/apache/spark/blob/72c62b6596d21e975c5597f8fff84b1a9d070a02/connector/avro/src/main/scala/org/apache/spark/sql/avro/AvroFileFormat.scala#L158]
Avro files that contain such columns won't be profiled.
:::

### Code Coordinates
- Class Name: `datahub.ingestion.source.abs.source.ABSSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/abs/source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for ABS Data Lake, feel free to ping us on [our Slack](https://datahub.com/slack).
