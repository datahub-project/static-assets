---
sidebar_position: 48
title: Oracle
slug: /generated/ingestion/sources/oracle
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/oracle.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Oracle
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md) | ✅ | Optionally enabled via `classification.enabled` |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Domains](../../../domains.md) | ✅ | Enabled by default |
| Schema Metadata | ✅ | Enabled by default |


This plugin extracts the following:

- Metadata for databases, schemas, and tables
- Column types associated with each table
- Table, row, and column statistics via optional SQL profiling

Using the Oracle source requires that you've also installed the correct drivers; see the [cx_Oracle docs](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html). The easiest one is the [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html).

### Prerequisites

#### Data Dictionary Mode/Views

The Oracle ingestion source supports two modes for extracting metadata information (see `data_dictionary_mode` option): `ALL` and `DBA`. In the `ALL` mode, the SQLAlchemy backend queries `ALL_` data dictionary views to extract metadata information. In the `DBA` mode, the Oracle ingestion source directly queries `DBA_` data dictionary views to extract metadata information. `ALL_` views only provide information accessible to the user used for ingestion while `DBA_` views provide information for the entire database (that is, all schema objects in the database).

The following table contains a brief description of what each data dictionary view is used for:

| Data Dictionary View                               | What's it used for?                                   |
| -------------------------------------------------- | ----------------------------------------------------- |
| `ALL_TABLES` or `DBA_TABLES`                       | Get list of all relational tables in the database     |
| `ALL_VIEWS` or `DBA_VIEWS`                         | Get list of all views in the database                 |
| `ALL_TAB_COMMENTS` or `DBA_TAB_COMMENTS`           | Get comments on tables and views                      |
| `ALL_TAB_COLS` or `DBA_TAB_COLS`                   | Get description of the columns of tables and views    |
| `ALL_COL_COMMENTS` or `DBA_COL_COMMENTS`           | Get comments on the columns of tables and views       |
| `ALL_TAB_IDENTITY_COLS` or `DBA_TAB_IDENTITY_COLS` | Get table identity columns                            |
| `ALL_CONSTRAINTS` or `DBA_CONSTRAINTS`             | Get constraint definitions on tables                  |
| `ALL_CONS_COLUMNS` or `DBA_CONS_COLUMNS`           | Get list of columns that are specified in constraints |
| `ALL_USERS` or `DBA_USERS`                         | Get all schema names                                  |

#### Data Dictionary Views accessible information and required privileges

- `ALL_` views display all the information accessible to the user used for ingestion, including information from the user's schema as well as information from objects in other schemas, if the user has access to those objects by way of grants of privileges or roles.
- `DBA_` views display all relevant information in the entire database. They can be queried only by users with the `SYSDBA` system privilege or `SELECT ANY DICTIONARY` privilege, or `SELECT_CATALOG_ROLE` role, or by users with direct privileges granted to them.

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: oracle
  config:
    # Coordinates
    host_port: localhost:5432
    database: dbname

    # Credentials
    username: user
    password: pass

    # Options
    service_name: svc # omit database if using this option

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
| <div className="path-line"><span className="path-main">host_port</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | host URL  |
| <div className="path-line"><span className="path-main">add_database_name_to_urn</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Add oracle database name to urn, default urn is schema.table <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">convert_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert dataset urns to lowercase. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">data_dictionary_mode</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The data dictionary views mode, to extract information about schema objects ('ALL' and 'DBA' views are supported). (https://docs.oracle.com/cd/E11882_01/nav/catalog_views.htm) <div className="default-line default-line-with-docs">Default: <span className="default-value">ALL</span></div> |
| <div className="path-line"><span className="path-main">database</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | If using, omit `service_name`.  |
| <div className="path-line"><span className="path-main">enable_thick_mode</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Connection defaults to thin mode. Set to True to enable thick mode. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_table_location_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If the source supports it, include table lineage to the underlying storage location. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_tables</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether tables should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates column-level lineage for  view->view and table->view lineage using DataHub's sql parser. Requires `include_view_lineage` to be enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_view_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates view->view and table->view lineage using DataHub's sql parser. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_views</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether views should be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">incremental_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, emits lineage as incremental to existing lineage already in DataHub. When disabled, re-states lineage on each run. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs. To set connection arguments in the URL, specify them under `connect_args`.  |
| <div className="path-line"><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | password  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Will be set automatically to default value. <div className="default-line default-line-with-docs">Default: <span className="default-value">oracle</span></div> |
| <div className="path-line"><span className="path-main">service_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Oracle service name. If using, omit `database`.  |
| <div className="path-line"><span className="path-main">sqlalchemy_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | URI of database to connect to. See https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls. Takes precedence over other connection parameters.  |
| <div className="path-line"><span className="path-main">thick_mode_lib_dir</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | If using thick mode on Windows or Mac, set thick_mode_lib_dir to the oracle client libraries path. On Linux, this value is ignored, as ldconfig or LD_LIBRARY_PATH will define the location.  |
| <div className="path-line"><span className="path-main">use_file_backed_cache</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to use a file backed cache for the view definitions. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | username  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">map(str,AllowDenyPattern)</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profile_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter tables (or specific columns) for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">schema_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for schemas to filter in ingestion. Specify regex to only match the schema name. e.g. to match all tables in schema analytics, use the regex 'analytics' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">schema_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">schema_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. Specify regex to match the entire table name in database.schema.table format. e.g. to match all tables starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">view_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for views to filter in ingestion. Note: Defaults to table_pattern if not specified. Specify regex to match the entire view name in database.schema.view format. e.g. to match all views starting with customer in Customer database and public schema, use the regex 'Customer.public.customer.*' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">view_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">view_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">classification</span></div> <div className="type-name-line"><span className="type-name">ClassificationConfig</span></div> | For details, refer to [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md). <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;sample&#95;size&#x27;: 100, &#x27;max&#95;worker...</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether classification should be used to auto-detect glossary terms <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">info_type_to_term</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">classification.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker processes to use for classification. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">14</span></div> |
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
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of worker threads to use for profiling. Set to 1 to disable. <div className="default-line default-line-with-docs">Default: <span className="default-value">70</span></div> |
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
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">fail_safe_threshold</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'. <div className="default-line default-line-with-docs">Default: <span className="default-value">75.0</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "OracleConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "schema_pattern": {
      "title": "Schema Pattern",
      "description": "Regex patterns for schemas to filter in ingestion. Specify regex to only match the schema name. e.g. to match all tables in schema analytics, use the regex 'analytics'",
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
    "classification": {
      "title": "Classification",
      "description": "For details, refer to [Classification](../../../../metadata-ingestion/docs/dev_guides/classification.md).",
      "default": {
        "enabled": false,
        "sample_size": 100,
        "max_workers": 14,
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
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "options": {
      "title": "Options",
      "description": "Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs. To set connection arguments in the URL, specify them under `connect_args`.",
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
        "max_workers": 70,
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
    "username": {
      "title": "Username",
      "description": "username",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "password",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "host_port": {
      "title": "Host Port",
      "description": "host URL",
      "type": "string"
    },
    "database": {
      "title": "Database",
      "description": "If using, omit `service_name`.",
      "type": "string"
    },
    "scheme": {
      "title": "Scheme",
      "description": "Will be set automatically to default value.",
      "default": "oracle",
      "type": "string"
    },
    "sqlalchemy_uri": {
      "title": "Sqlalchemy Uri",
      "description": "URI of database to connect to. See https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls. Takes precedence over other connection parameters.",
      "type": "string"
    },
    "service_name": {
      "title": "Service Name",
      "description": "Oracle service name. If using, omit `database`.",
      "type": "string"
    },
    "add_database_name_to_urn": {
      "title": "Add Database Name To Urn",
      "description": "Add oracle database name to urn, default urn is schema.table",
      "default": false,
      "type": "boolean"
    },
    "data_dictionary_mode": {
      "title": "Data Dictionary Mode",
      "description": "The data dictionary views mode, to extract information about schema objects ('ALL' and 'DBA' views are supported). (https://docs.oracle.com/cd/E11882_01/nav/catalog_views.htm)",
      "default": "ALL",
      "type": "string"
    },
    "enable_thick_mode": {
      "title": "Enable Thick Mode",
      "description": "Connection defaults to thin mode. Set to True to enable thick mode.",
      "default": false,
      "type": "boolean"
    },
    "thick_mode_lib_dir": {
      "title": "Thick Mode Lib Dir",
      "description": "If using thick mode on Windows or Mac, set thick_mode_lib_dir to the oracle client libraries path. On Linux, this value is ignored, as ldconfig or LD_LIBRARY_PATH will define the location.",
      "type": "string"
    }
  },
  "required": [
    "host_port"
  ],
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
          "default": 14,
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
          "default": 70,
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
    }
  }
}
```


</TabItem>
</Tabs>

As a SQL-based service, the Oracle integration is also supported by our SQL profiler. See here for more details on configuration.

### Code Coordinates
- Class Name: `datahub.ingestion.source.sql.oracle.OracleSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/sql/oracle.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Oracle, feel free to ping us on [our Slack](https://datahub.com/slack).
