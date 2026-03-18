---
sidebar_position: 17
title: Dremio
slug: /generated/ingestion/sources/dremio
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/dremio.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dremio
### Concept Mapping

Here's a table for **Concept Mapping** between Dremio and DataHub to provide a clear overview of how entities and concepts in Dremio are mapped to corresponding entities in DataHub:

| Source Concept             | DataHub Concept | Notes                                                      |
| -------------------------- | --------------- | ---------------------------------------------------------- |
| **Physical Dataset/Table** | `Dataset`       | Subtype: `Table`                                           |
| **Virtual Dataset/Views**  | `Dataset`       | Subtype: `View`                                            |
| **Spaces**                 | `Container`     | Mapped to DataHub’s `Container` aspect. Subtype: `Space`   |
| **Folders**                | `Container`     | Mapped as a `Container` in DataHub. Subtype: `Folder`      |
| **Sources**                | `Container`     | Represented as a `Container` in DataHub. Subtype: `Source` |
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Optionally enabled via configuration |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Domains](../../../domains.md) | ✅ | Supported via the `domain` config field |
| Extract Ownership | ✅ | Enabled by default |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default |


This plugin integrates with Dremio to extract and ingest metadata into DataHub.
The following types of metadata are extracted:

- Metadata for Spaces, Folders, Sources, and Datasets:
    - Includes physical and virtual datasets, with detailed information about each dataset.
    - Extracts metadata about Dremio's organizational hierarchy: Spaces (top-level), Folders (sub-level), and Sources (external data connections).

- Schema and Column Information:
    - Column types and schema metadata associated with each physical and virtual dataset.
    - Extracts column-level metadata, such as names, data types, and descriptions, if available.

- Lineage Information:
    - Dataset-level and column-level lineage tracking:
        - Dataset-level lineage shows dependencies and relationships between physical and virtual datasets.
        - Column-level lineage tracks transformations applied to individual columns across datasets.
    - Lineage information helps trace the flow of data and transformations within Dremio.

- Ownership and Glossary Terms:
    - Metadata related to ownership of datasets, extracted from Dremio’s ownership model.
    - Glossary terms and business metadata associated with datasets, providing additional context to the data.
    - Note: Ownership information will only be available for the Cloud and Enterprise editions, it will not be available for the Community edition.

- Optional SQL Profiling (if enabled):
    - Table, row, and column statistics can be profiled and ingested via optional SQL queries.
    - Extracts statistics about tables and columns, such as row counts and data distribution, for better insight into the dataset structure.

### Setup

This integration pulls metadata directly from the Dremio APIs.

You'll need to have a Dremio instance up and running with access to the necessary datasets, and API access should be enabled with a valid token.

The API token should have the necessary permissions to **read metadata** and **retrieve lineage**.

#### Steps to Get the Required Information

1. **Generate an API Token**:

   - Log in to your Dremio instance.
   - Navigate to your user profile in the top-right corner.
   - Select **Generate API Token** to create an API token for programmatic access.

2. **Permissions**:

   - The token should have **read-only** or **admin** permissions that allow it to:
     - View all datasets (physical and virtual).
     - Access all spaces, folders, and sources.
     - Retrieve dataset and column-level lineage information.

3. **Verify External Data Source Permissions**:
   - If Dremio is connected to external data sources (e.g., AWS S3, relational databases), ensure that Dremio has access to the credentials required for querying those sources.

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: dremio
  config:
    # Coordinates
    hostname: localhost
    port: 9047
    tls: true

    # Credentials with personal access token(recommended)
    authentication_method: PAT
    password: pass
    # OR Credentials with basic auth
    # authentication_method: password
    # username: user
    # password: pass

    #For cloud instance
    #is_dremio_cloud: True
    #dremio_cloud_project_id: <project_id>

    include_query_lineage: True

    ingest_owner: true

    #Optional
    source_mappings:
      - platform: s3
        source_name: samples

    #Optional
    schema_pattern:
      allow:
        - "<source_name>.<table_name>"

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
| <div className="path-line"><span className="path-main">authentication_method</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication method: 'password' or 'PAT' (Personal Access Token) <div className="default-line default-line-with-docs">Default: <span className="default-value">PAT</span></div> |
| <div className="path-line"><span className="path-main">disable_certificate_verification</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Disable TLS certificate verification <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Domain for all source objects.  |
| <div className="path-line"><span className="path-main">dremio_cloud_project_id</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | ID of Dremio Cloud Project. Found in Project Settings in the Dremio Cloud UI  |
| <div className="path-line"><span className="path-main">dremio_cloud_region</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "US", "EU" <div className="default-line default-line-with-docs">Default: <span className="default-value">US</span></div> |
| <div className="path-line"><span className="path-main">hostname</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Hostname or IP Address of the Dremio server  |
| <div className="path-line"><span className="path-main">include_query_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to include query-based lineage information. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_owner</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest Owner from source. This will override Owner info entered from UI <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">is_dremio_cloud</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether this is a Dremio Cloud instance <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use for parallel processing <div className="default-line default-line-with-docs">Default: <span className="default-value">50</span></div> |
| <div className="path-line"><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Dremio password or Personal Access Token  |
| <div className="path-line"><span className="path-main">path_to_certificates</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to SSL certificates <div className="default-line default-line-with-docs">Default: <span className="default-value">/Users/pedro/dev/oss/datahub/metadata-ingestion/ve...</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">port</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Port of the Dremio REST API <div className="default-line default-line-with-docs">Default: <span className="default-value">9047</span></div> |
| <div className="path-line"><span className="path-main">tls</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether the Dremio REST API port is encrypted <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Dremio username  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">dataset_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables and views to filter in ingestion. Specify regex to match the entire table name in dremio.schema.table format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'dremio.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">dataset_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">dataset_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profile_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to profile <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">schema_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for schemas to filter <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">source_mappings</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Mappings from Dremio sources to DataHub platforms and datasets.  |
| <div className="path-line"><span className="path-prefix">source_mappings.</span><span className="path-main">DremioSourceMapping</span></div> <div className="type-name-line"><span className="type-name">DremioSourceMapping</span></div> | Any source that produces dataset urns in a single environment should inherit this class  |
| <div className="path-line"><span className="path-prefix">source_mappings.DremioSourceMapping.</span><span className="path-main">platform</span>&nbsp;<abbr title="Required if DremioSourceMapping is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Source connection made by Dremio (e.g. S3, Snowflake)  |
| <div className="path-line"><span className="path-prefix">source_mappings.DremioSourceMapping.</span><span className="path-main">source_name</span>&nbsp;<abbr title="Required if DremioSourceMapping is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Alias of platform in Dremio connection  |
| <div className="path-line"><span className="path-prefix">source_mappings.DremioSourceMapping.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-prefix">source_mappings.DremioSourceMapping.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">usage</span></div> <div className="type-name-line"><span className="type-name">BaseUsageConfig</span></div> | The usage config to use when generating usage statistics <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;bucket&#95;duration&#x27;: &#x27;DAY&#x27;, &#x27;end&#95;time&#x27;: &#x27;2025-05-08...</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">bucket_duration</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Size of the time window to aggregate usage stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">DAY</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">end_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Latest date of lineage/usage to consider. Default: Current time in UTC  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">format_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to format sql queries <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to display operational stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_read_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report read operational stats. Experimental. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_top_n_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the top_n_queries. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">start_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">top_n_queries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of top queries to save to each table. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">user_email_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | regex patterns for user emails to filter in usage. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">ProfileConfig</span></div> | Configuration for profiling <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;operation&#95;config&#x27;: &#123;&#x27;lower&#95;fre...</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether profiling should be done. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_distinct_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of distinct values for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_distinct_value_frequencies</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for distinct value frequencies. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_histogram</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the histogram for numeric fields. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_max_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the max value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_mean_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the mean value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_min_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the min value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_null_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of nulls for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_quantiles</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the quantiles of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_sample_values</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the sample values for all columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_stddev_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the standard deviation of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Max number of documents to profile. By default, profiles all documents.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use for profiling. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">50</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">offset</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Offset in documents to profile. By default, uses no offset.  |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">profile_table_level_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to perform profiling at table-level only, or include column-level profiling as well. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">query_timeout</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Time before cancelling Dremio profiling query <div className="default-line default-line-with-docs">Default: <span className="default-value">300</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">operation_config</span></div> <div className="type-name-line"><span className="type-name">OperationConfig</span></div> | Experimental feature. To specify operation configs.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">lower_freq_profile_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_date_of_month</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_day_of_week</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DremioSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "hostname": {
      "title": "Hostname",
      "description": "Hostname or IP Address of the Dremio server",
      "type": "string"
    },
    "port": {
      "title": "Port",
      "description": "Port of the Dremio REST API",
      "default": 9047,
      "type": "integer"
    },
    "username": {
      "title": "Username",
      "description": "Dremio username",
      "type": "string"
    },
    "authentication_method": {
      "title": "Authentication Method",
      "description": "Authentication method: 'password' or 'PAT' (Personal Access Token)",
      "default": "PAT",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "Dremio password or Personal Access Token",
      "type": "string"
    },
    "tls": {
      "title": "Tls",
      "description": "Whether the Dremio REST API port is encrypted",
      "default": true,
      "type": "boolean"
    },
    "disable_certificate_verification": {
      "title": "Disable Certificate Verification",
      "description": "Disable TLS certificate verification",
      "default": false,
      "type": "boolean"
    },
    "path_to_certificates": {
      "title": "Path To Certificates",
      "description": "Path to SSL certificates",
      "default": "/Users/pedro/dev/oss/datahub/metadata-ingestion/venv/lib/python3.10/site-packages/certifi/cacert.pem",
      "type": "string"
    },
    "is_dremio_cloud": {
      "title": "Is Dremio Cloud",
      "description": "Whether this is a Dremio Cloud instance",
      "default": false,
      "type": "boolean"
    },
    "dremio_cloud_region": {
      "title": "Dremio Cloud Region",
      "description": "Dremio Cloud region ('US' or 'EU')",
      "default": "US",
      "enum": [
        "US",
        "EU"
      ],
      "type": "string"
    },
    "dremio_cloud_project_id": {
      "title": "Dremio Cloud Project Id",
      "description": "ID of Dremio Cloud Project. Found in Project Settings in the Dremio Cloud UI",
      "type": "string"
    },
    "domain": {
      "title": "Domain",
      "description": "Domain for all source objects.",
      "type": "string"
    },
    "source_mappings": {
      "title": "Source Mappings",
      "description": "Mappings from Dremio sources to DataHub platforms and datasets.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/DremioSourceMapping"
      }
    },
    "schema_pattern": {
      "title": "Schema Pattern",
      "description": "Regex patterns for schemas to filter",
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
      "description": "Regex patterns for tables and views to filter in ingestion. Specify regex to match the entire table name in dremio.schema.table format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'dremio.public.customer.*'",
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
    "usage": {
      "title": "Usage",
      "description": "The usage config to use when generating usage statistics",
      "default": {
        "bucket_duration": "DAY",
        "end_time": "2025-05-08T12:15:35.858134+00:00",
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
        "include_top_n_queries": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/BaseUsageConfig"
        }
      ]
    },
    "profile_pattern": {
      "title": "Profile Pattern",
      "description": "Regex patterns for tables to profile",
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
      "description": "Configuration for profiling",
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
        "include_field_median_value": false,
        "include_field_stddev_value": true,
        "include_field_quantiles": false,
        "include_field_distinct_value_frequencies": false,
        "include_field_histogram": false,
        "include_field_sample_values": true,
        "max_workers": 50,
        "query_timeout": 300
      },
      "allOf": [
        {
          "$ref": "#/definitions/ProfileConfig"
        }
      ]
    },
    "max_workers": {
      "title": "Max Workers",
      "description": "Number of worker threads to use for parallel processing",
      "default": 50,
      "type": "integer"
    },
    "include_query_lineage": {
      "title": "Include Query Lineage",
      "description": "Whether to include query-based lineage information.",
      "default": false,
      "type": "boolean"
    },
    "ingest_owner": {
      "title": "Ingest Owner",
      "description": "Ingest Owner from source. This will override Owner info entered from UI",
      "default": true,
      "type": "boolean"
    }
  },
  "additionalProperties": false,
  "definitions": {
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
    "DremioSourceMapping": {
      "title": "DremioSourceMapping",
      "description": "Any source that produces dataset urns in a single environment should inherit this class",
      "type": "object",
      "properties": {
        "platform_instance": {
          "title": "Platform Instance",
          "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "The environment that all assets produced by this connector belong to",
          "default": "PROD",
          "type": "string"
        },
        "platform": {
          "title": "Platform",
          "description": "Source connection made by Dremio (e.g. S3, Snowflake)",
          "type": "string"
        },
        "source_name": {
          "title": "Source Name",
          "description": "Alias of platform in Dremio connection",
          "type": "string"
        }
      },
      "required": [
        "platform",
        "source_name"
      ],
      "additionalProperties": false
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
    "BucketDuration": {
      "title": "BucketDuration",
      "description": "An enumeration.",
      "enum": [
        "DAY",
        "HOUR"
      ],
      "type": "string"
    },
    "BaseUsageConfig": {
      "title": "BaseUsageConfig",
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
    "ProfileConfig": {
      "title": "ProfileConfig",
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
        "query_timeout": {
          "title": "Query Timeout",
          "description": "Time before cancelling Dremio profiling query",
          "default": 300,
          "type": "integer"
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>

### Starter Receipe for Dremio Cloud Instance 

```
source:
  type: dremio
  config:
    # Authentication details
    authentication_method: PAT        # Use Personal Access Token for authentication
    password: <your_api_token>        # Replace <your_api_token> with your Dremio Cloud API token
    is_dremio_cloud: True             # Set to True for Dremio Cloud instances
    dremio_cloud_project_id: <project_id>  # Provide the Project ID for Dremio Cloud

    # Enable query lineage tracking
    include_query_lineage: True       

    #Optional
    source_mappings:
      - platform: s3                 
        source_name: samples       
    
    # Optional
    schema_pattern:
      allow:
        - "<source_name>.<table_name>" 

sink:
    # Define your sink configuration here

```
### Code Coordinates
- Class Name: `datahub.ingestion.source.dremio.dremio_source.DremioSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/dremio/dremio_source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Dremio, feel free to ping us on [our Slack](https://slack.datahubproject.io).
