---
sidebar_position: 69
title: Tableau
slug: /generated/ingestion/sources/tableau
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/tableau.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Tableau
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Column-level Lineage | ✅ | Enabled by default, configure using `extract_column_level_lineage` |
| Dataset Usage | ✅ | Dashboard/Chart view counts, enabled using extract_usage_stats config |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default when stateful ingestion is turned on. |
| [Domains](../../../domains.md) | ❌ | Requires transformer |
| Extract Ownership | ✅ | Requires recipe configuration |
| Extract Tags | ✅ | Requires recipe configuration |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default |


### Prerequisites

In order to ingest metadata from Tableau, you will need:

- Tableau Server Version 2021.1.10 and above. It may also work for older versions.
- [Enable the Tableau Metadata API](https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_start.html#enable-the-tableau-metadata-api-for-tableau-server) for Tableau Server, if its not already enabled. This is always enabled for Tableau Cloud.

### Authentication

DataHub supports two authentication methods:

1. Username/Password
2. [Personal Access Token](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens)

Either way, the user/token must have at least the **Site Administrator Explorer** site role.

:::info

We need at least the **Site Administrator Explorer** site role in order to get complete metadata from Tableau. Roles with higher privileges, like **Site Administrator Creator** or **Server Admin** also work.

With any lower role, the Tableau Metadata API returns missing/partial metadata.
This particularly affects data source fields and definitions, which impacts our ability to extract most columns and generate column lineage. Some table-level lineage is also impacted.
Other site roles, like Viewer or Explorer, are insufficient due to these limitations in the current Tableau Metadata API.

:::

### Ingestion through UI

The following video shows you how to get started with ingesting Tableau metadata through the UI.

<div
  style={{
    position: "relative",
    paddingBottom: "57.692307692307686%",
    height: 0
  }}
>
  <iframe
    src="https://www.loom.com/embed/ef521c4e66564614a6ddde35dc3840f8"
    frameBorder={0}
    webkitallowfullscreen=""
    mozallowfullscreen=""
    allowFullScreen=""
    style={{
      position: "absolute",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%"
    }}
  />
</div>

### Integration Details

This plugin extracts Sheets, Dashboards, Embedded and Published Data sources metadata within Workbooks in a given project
on a Tableau site. Tableau's GraphQL interface is used to extract metadata information. Queries used to extract metadata are located
in `metadata-ingestion/src/datahub/ingestion/source/tableau_common.py`

#### Concept Mapping

This ingestion source maps the following Source System Concepts to DataHub Concepts:

| Source Concept              | DataHub Concept                                               | Notes                             |
| --------------------------- | ------------------------------------------------------------- | --------------------------------- |
| `"Tableau"`                 | [Data Platform](../../metamodel/entities/dataPlatform.md)     |
| Project                     | [Container](../../metamodel/entities/container.md)            | SubType `"Project"`               |
| Embedded DataSource         | [Dataset](../../metamodel/entities/dataset.md)                | SubType `"Embedded Data Source"`  |
| Published DataSource        | [Dataset](../../metamodel/entities/dataset.md)                | SubType `"Published Data Source"` |
| Custom SQL Table            | [Dataset](../../metamodel/entities/dataset.md)                | SubTypes `"View"`, `"Custom SQL"` |
| Embedded or External Tables | [Dataset](../../metamodel/entities/dataset.md)                |                                   |
| Sheet                       | [Chart](../../metamodel/entities/chart.md)                    |                                   |
| Dashboard                   | [Dashboard](../../metamodel/entities/dashboard.md)            |                                   |
| User                        | [User (a.k.a CorpUser)](../../metamodel/entities/corpuser.md) | Optionally Extracted              |
| Workbook                    | [Container](../../metamodel/entities/container.md)            | SubType `"Workbook"`              |
| Tag                         | [Tag](../../metamodel/entities/tag.md)                        | Optionally Extracted              |

#### Lineage

Lineage is emitted as received from Tableau's metadata API for

- Sheets contained within a Dashboard
- Embedded or Published Data Sources depended on by a Sheet
- Published Data Sources upstream to Embedded datasource
- Tables upstream to Embedded or Published Data Source
- Custom SQL datasources upstream to Embedded or Published Data Source
- Tables upstream to Custom SQL Data Source

#### Caveats

- Tableau metadata API might return incorrect schema name for tables for some databases, leading to incorrect metadata in DataHub. This source attempts to extract correct schema from databaseTable's fully qualified name, wherever possible. Read [Using the databaseTable object in query](https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_model.html#schema_attribute) for caveats in using schema attribute.

### Troubleshooting

#### Why are only some workbooks/custom SQLs/published datasources ingested from the specified project?

This may happen when the Tableau API returns NODE_LIMIT_EXCEEDED error in response to metadata query and returns partial results with message "Showing partial results. , The request exceeded the ‘n’ node limit. Use pagination, additional filtering, or both in the query to adjust results." To resolve this, consider

- reducing the page size using the `page_size` config param in datahub recipe (Defaults to 10).
- increasing tableau configuration [metadata query node limit](https://help.tableau.com/current/server/en-us/cli_configuration-set_tsm.htm#metadata_nodelimit) to higher value.

#### `PERMISSIONS_MODE_SWITCHED` error in ingestion report

This error occurs if the Tableau site is using external assets. For more detail, refer to the Tableau documentation [Manage Permissions for External Assets](https://help.tableau.com/current/online/en-us/dm_perms_assets.htm).

Follow the below steps to enable the derived permissions:

1.  Sign in to Tableau Cloud or Tableau Server as an admin.
2.  From the left navigation pane, click Settings.
3.  On the General tab, under Automatic Access to Metadata about Databases and Tables, select the `Automatically grant authorized users access to metadata about databases and tables` check box.

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: tableau
  config:
    # Coordinates
    connect_uri: https://prod-ca-a.online.tableau.com
    site: acryl
    platform_instance: acryl_instance
    project_pattern: ["^default$", "^Project 2$", "^/Project A/Nested Project B$"]

    # Credentials
    username: "${TABLEAU_USER}"
    password: "${TABLEAU_PASSWORD}"

    # Options
    ingest_tags: True
    ingest_owner: True
    default_schema_map:
      mydatabase: public
      anotherdatabase: anotherschema

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
| <div className="path-line"><span className="path-main">connect_uri</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau host URL.  |
| <div className="path-line"><span className="path-main">add_site_container</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, sites are added as containers and therefore visible in the folder structure within Datahub. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">custom_sql_table_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of custom sql datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">dashboard_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of dashboards to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">database_hostname_to_platform_instance_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">database_server_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of database servers to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">database_table_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of database tables to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">default_schema_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">embedded_datasource_field_upstream_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of upstream fields to query at a time for embedded datasources using the Tableau API; fallbacks to `page_size` * 10 if not set.  |
| <div className="path-line"><span className="path-main">embedded_datasource_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of embedded datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">extract_column_level_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, extracts column-level lineage from Tableau Datasources <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_lineage_from_unsupported_custom_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | [Experimental] Whether to extract lineage from unsupported custom sql queries using SQL parsing <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_project_hierarchy</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract entire project hierarchy for nested projects. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_usage_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | [experimental] Extract usage statistics for dashboards and charts. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">force_extraction_of_lineage_from_custom_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | [Experimental] Force extraction of lineage from custom sql queries using SQL parsing, ignoring Tableau metadata <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_embed_url</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest a URL to render an embedded Preview of assets within Tableau. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_external_links_for_charts</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest a URL to link out to from charts. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">ingest_external_links_for_dashboards</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest a URL to link out to from dashboards. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">ingest_multiple_sites</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, ingests multiple sites the user has access to. If the user doesn't have access to the default site, specify an initial site to query in the site property. By default all sites the user has access to will be ingested. You can filter sites with the site_name_pattern property. This flag is currently only supported for Tableau Server. Tableau Cloud is not supported. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_owner</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest Owner from source. This will override Owner info entered from UI <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_tables_external</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest details for tables external to (not embedded in) tableau as entities. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_tags</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest Tags from source. This will override Tags entered from UI <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">max_retries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of retries for failed requests. <div className="default-line default-line-with-docs">Default: <span className="default-value">3</span></div> |
| <div className="path-line"><span className="path-main">page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of metadata objects (e.g. CustomSQLTable, PublishedDatasource, etc) to query at a time using the Tableau API. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau password, must be set if authenticating using username/password.  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">platform_instance_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">project_path_separator</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The separator used for the project_path_pattern field between project names. By default, we use a slash. You can change this if your Tableau projects contain slashes in their names, and you'd like to filter by project. <div className="default-line default-line-with-docs">Default: <span className="default-value">/</span></div> |
| <div className="path-line"><span className="path-main">published_datasource_field_upstream_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of upstream fields to query at a time for published datasources using the Tableau API; fallbacks to `page_size` * 10 if not set.  |
| <div className="path-line"><span className="path-main">published_datasource_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of published datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">session_trust_env</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Configures the trust_env property in the requests session. If set to false (default value) it will bypass proxy settings. See https://requests.readthedocs.io/en/latest/api/#requests.Session.trust_env for more information. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">sheet_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of sheets to query at a time using the Tableau API; fallbacks to `page_size` if not set.  |
| <div className="path-line"><span className="path-main">site</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau Site. Always required for Tableau Online. Use emptystring to connect with Default site on Tableau Server. <div className="default-line default-line-with-docs">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-main">sql_parsing_disable_schema_awareness</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | [Experimental] Ignore pre ingested tables schemas during parsing of SQL queries (allows to workaround ingestion errors when pre ingested schema and queries are out of sync) <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ssl_verify</span></div> <div className="type-name-line"><span className="type-name">One of boolean, string</span></div> | Whether to verify SSL certificates. If using self-signed certificates, set to false or provide the path to the .pem certificate bundle. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">token_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau token name, must be set if authenticating using a personal access token.  |
| <div className="path-line"><span className="path-main">token_value</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau token value, must be set if authenticating using a personal access token.  |
| <div className="path-line"><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tableau username, must be set if authenticating using username/password.  |
| <div className="path-line"><span className="path-main">workbook_page_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | [advanced] Number of workbooks to query at a time using the Tableau API; defaults to `1` and fallbacks to `page_size` if not set. <div className="default-line default-line-with-docs">Default: <span className="default-value">1</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Environment to use in namespace when constructing URNs. <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">ingest_hidden_assets</span></div> <div className="type-name-line"><span className="type-name">One of array, boolean</span></div> | When enabled, hidden worksheets and dashboards are ingested into Datahub. If a dashboard or worksheet is hidden in Tableau the luid is blank. A list of asset types can also be specified, to only ingest those hidden assets. Current options supported are 'worksheet' and 'dashboard'. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;worksheet&#x27;, &#x27;dashboard&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">ingest_hidden_assets.</span><span className="path-main">enum</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "worksheet", "dashboard"  |
| <div className="path-line"><span className="path-main">lineage_overrides</span></div> <div className="type-name-line"><span className="type-name">TableauLineageOverrides</span></div> | Mappings to change generated dataset urns. Use only if you really know what you are doing.  |
| <div className="path-line"><span className="path-prefix">lineage_overrides.</span><span className="path-main">database_override_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">lineage_overrides.</span><span className="path-main">platform_override_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">permission_ingestion</span></div> <div className="type-name-line"><span className="type-name">PermissionIngestionConfig</span></div> | Configuration settings for ingesting Tableau groups and their capabilities as custom properties.  |
| <div className="path-line"><span className="path-prefix">permission_ingestion.</span><span className="path-main">enable_workbooks</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable group permission ingestion for workbooks. Default: True <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">permission_ingestion.</span><span className="path-main">group_name_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Filter for Tableau group names when ingesting group permissions. For example, you could filter for groups that include the term 'Consumer' in their name by adding '^.*Consumer$' to the allow list.By default, all groups will be ingested. You can both allow and deny groups based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns.  <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">permission_ingestion.group_name_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">permission_ingestion.group_name_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">permission_ingestion.group_name_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">permission_ingestion.group_name_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">permission_ingestion.group_name_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">project_path_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Filters Tableau projects by their full path. For instance, 'My Project/Nested Project' targets a specific nested project named 'Nested Project'. This is also useful when you need to exclude all nested projects under a particular project. You can allow or deny projects by specifying their path or a regular expression pattern. Deny patterns always override allow patterns. By default, all projects are ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">project_path_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">project_path_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_path_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">project_path_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_path_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">project_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | [deprecated] Use project_path_pattern instead. Filter for specific Tableau projects. For example, use 'My Project' to ingest a root-level Project with name 'My Project', or 'My Project/Nested Project' to ingest a nested Project with name 'Nested Project'. By default, all Projects nested inside a matching Project will be included in ingestion. You can both allow and deny projects based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns. By default, all projects will be ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">project_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">project_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">project_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">project_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">projects</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | [deprecated] Use project_pattern instead. List of tableau projects  <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;default&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">projects.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">site_name_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Filter for specific Tableau sites. By default, all sites will be included in the ingestion. You can both allow and deny sites based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns. This property is currently only supported for Tableau Server. Tableau Cloud is not supported.  <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">site_name_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">site_name_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">site_name_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">site_name_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">site_name_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">tags_for_hidden_assets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Tags to be added to hidden dashboards and views. If a dashboard or view is hidden in Tableau the luid is blank. This can only be used with ingest_tags enabled as it will overwrite tags entered from the UI. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">tags_for_hidden_assets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
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
  "title": "TableauConfig",
  "description": "Any non-Dataset source that produces lineage to Datasets should inherit this class.\ne.g. Orchestrators, Pipelines, BI Tools etc.",
  "type": "object",
  "properties": {
    "page_size": {
      "title": "Page Size",
      "description": "[advanced] Number of metadata objects (e.g. CustomSQLTable, PublishedDatasource, etc) to query at a time using the Tableau API.",
      "default": 10,
      "type": "integer"
    },
    "database_server_page_size": {
      "title": "Database Server Page Size",
      "description": "[advanced] Number of database servers to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "workbook_page_size": {
      "title": "Workbook Page Size",
      "description": "[advanced] Number of workbooks to query at a time using the Tableau API; defaults to `1` and fallbacks to `page_size` if not set.",
      "default": 1,
      "type": "integer"
    },
    "sheet_page_size": {
      "title": "Sheet Page Size",
      "description": "[advanced] Number of sheets to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "dashboard_page_size": {
      "title": "Dashboard Page Size",
      "description": "[advanced] Number of dashboards to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "embedded_datasource_page_size": {
      "title": "Embedded Datasource Page Size",
      "description": "[advanced] Number of embedded datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "embedded_datasource_field_upstream_page_size": {
      "title": "Embedded Datasource Field Upstream Page Size",
      "description": "[advanced] Number of upstream fields to query at a time for embedded datasources using the Tableau API; fallbacks to `page_size` * 10 if not set.",
      "type": "integer"
    },
    "published_datasource_page_size": {
      "title": "Published Datasource Page Size",
      "description": "[advanced] Number of published datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "published_datasource_field_upstream_page_size": {
      "title": "Published Datasource Field Upstream Page Size",
      "description": "[advanced] Number of upstream fields to query at a time for published datasources using the Tableau API; fallbacks to `page_size` * 10 if not set.",
      "type": "integer"
    },
    "custom_sql_table_page_size": {
      "title": "Custom Sql Table Page Size",
      "description": "[advanced] Number of custom sql datasources to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "database_table_page_size": {
      "title": "Database Table Page Size",
      "description": "[advanced] Number of database tables to query at a time using the Tableau API; fallbacks to `page_size` if not set.",
      "type": "integer"
    },
    "connect_uri": {
      "title": "Connect Uri",
      "description": "Tableau host URL.",
      "type": "string"
    },
    "username": {
      "title": "Username",
      "description": "Tableau username, must be set if authenticating using username/password.",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "Tableau password, must be set if authenticating using username/password.",
      "type": "string"
    },
    "token_name": {
      "title": "Token Name",
      "description": "Tableau token name, must be set if authenticating using a personal access token.",
      "type": "string"
    },
    "token_value": {
      "title": "Token Value",
      "description": "Tableau token value, must be set if authenticating using a personal access token.",
      "type": "string"
    },
    "site": {
      "title": "Site",
      "description": "Tableau Site. Always required for Tableau Online. Use emptystring to connect with Default site on Tableau Server.",
      "default": "",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "max_retries": {
      "title": "Max Retries",
      "description": "Number of retries for failed requests.",
      "default": 3,
      "type": "integer"
    },
    "ssl_verify": {
      "title": "Ssl Verify",
      "description": "Whether to verify SSL certificates. If using self-signed certificates, set to false or provide the path to the .pem certificate bundle.",
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
    "session_trust_env": {
      "title": "Session Trust Env",
      "description": "Configures the trust_env property in the requests session. If set to false (default value) it will bypass proxy settings. See https://requests.readthedocs.io/en/latest/api/#requests.Session.trust_env for more information.",
      "default": false,
      "type": "boolean"
    },
    "extract_column_level_lineage": {
      "title": "Extract Column Level Lineage",
      "description": "When enabled, extracts column-level lineage from Tableau Datasources",
      "default": true,
      "type": "boolean"
    },
    "env": {
      "title": "Env",
      "description": "Environment to use in namespace when constructing URNs.",
      "default": "PROD",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "platform_instance_map": {
      "title": "Platform Instance Map",
      "description": "A holder for platform -> platform_instance mappings to generate correct dataset urns",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "projects": {
      "title": "Projects",
      "description": "[deprecated] Use project_pattern instead. List of tableau projects ",
      "default": [
        "default"
      ],
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "project_pattern": {
      "title": "Project Pattern",
      "description": "[deprecated] Use project_path_pattern instead. Filter for specific Tableau projects. For example, use 'My Project' to ingest a root-level Project with name 'My Project', or 'My Project/Nested Project' to ingest a nested Project with name 'Nested Project'. By default, all Projects nested inside a matching Project will be included in ingestion. You can both allow and deny projects based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns. By default, all projects will be ingested.",
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
    "project_path_pattern": {
      "title": "Project Path Pattern",
      "description": "Filters Tableau projects by their full path. For instance, 'My Project/Nested Project' targets a specific nested project named 'Nested Project'. This is also useful when you need to exclude all nested projects under a particular project. You can allow or deny projects by specifying their path or a regular expression pattern. Deny patterns always override allow patterns. By default, all projects are ingested.",
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
    "project_path_separator": {
      "title": "Project Path Separator",
      "description": "The separator used for the project_path_pattern field between project names. By default, we use a slash. You can change this if your Tableau projects contain slashes in their names, and you'd like to filter by project.",
      "default": "/",
      "type": "string"
    },
    "default_schema_map": {
      "title": "Default Schema Map",
      "description": "Default schema to use when schema is not found.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "ingest_tags": {
      "title": "Ingest Tags",
      "description": "Ingest Tags from source. This will override Tags entered from UI",
      "default": false,
      "type": "boolean"
    },
    "ingest_owner": {
      "title": "Ingest Owner",
      "description": "Ingest Owner from source. This will override Owner info entered from UI",
      "default": false,
      "type": "boolean"
    },
    "ingest_tables_external": {
      "title": "Ingest Tables External",
      "description": "Ingest details for tables external to (not embedded in) tableau as entities.",
      "default": false,
      "type": "boolean"
    },
    "lineage_overrides": {
      "title": "Lineage Overrides",
      "description": "Mappings to change generated dataset urns. Use only if you really know what you are doing.",
      "allOf": [
        {
          "$ref": "#/definitions/TableauLineageOverrides"
        }
      ]
    },
    "database_hostname_to_platform_instance_map": {
      "title": "Database Hostname To Platform Instance Map",
      "description": "Mappings to change platform instance in generated dataset urns based on database. Use only if you really know what you are doing.",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "extract_usage_stats": {
      "title": "Extract Usage Stats",
      "description": "[experimental] Extract usage statistics for dashboards and charts.",
      "default": false,
      "type": "boolean"
    },
    "ingest_embed_url": {
      "title": "Ingest Embed Url",
      "description": "Ingest a URL to render an embedded Preview of assets within Tableau.",
      "default": false,
      "type": "boolean"
    },
    "ingest_external_links_for_dashboards": {
      "title": "Ingest External Links For Dashboards",
      "description": "Ingest a URL to link out to from dashboards.",
      "default": true,
      "type": "boolean"
    },
    "ingest_external_links_for_charts": {
      "title": "Ingest External Links For Charts",
      "description": "Ingest a URL to link out to from charts.",
      "default": true,
      "type": "boolean"
    },
    "extract_project_hierarchy": {
      "title": "Extract Project Hierarchy",
      "description": "Whether to extract entire project hierarchy for nested projects.",
      "default": true,
      "type": "boolean"
    },
    "extract_lineage_from_unsupported_custom_sql_queries": {
      "title": "Extract Lineage From Unsupported Custom Sql Queries",
      "description": "[Experimental] Whether to extract lineage from unsupported custom sql queries using SQL parsing",
      "default": false,
      "type": "boolean"
    },
    "force_extraction_of_lineage_from_custom_sql_queries": {
      "title": "Force Extraction Of Lineage From Custom Sql Queries",
      "description": "[Experimental] Force extraction of lineage from custom sql queries using SQL parsing, ignoring Tableau metadata",
      "default": false,
      "type": "boolean"
    },
    "sql_parsing_disable_schema_awareness": {
      "title": "Sql Parsing Disable Schema Awareness",
      "description": "[Experimental] Ignore pre ingested tables schemas during parsing of SQL queries (allows to workaround ingestion errors when pre ingested schema and queries are out of sync)",
      "default": false,
      "type": "boolean"
    },
    "ingest_multiple_sites": {
      "title": "Ingest Multiple Sites",
      "description": "When enabled, ingests multiple sites the user has access to. If the user doesn't have access to the default site, specify an initial site to query in the site property. By default all sites the user has access to will be ingested. You can filter sites with the site_name_pattern property. This flag is currently only supported for Tableau Server. Tableau Cloud is not supported.",
      "default": false,
      "type": "boolean"
    },
    "site_name_pattern": {
      "title": "Site Name Pattern",
      "description": "Filter for specific Tableau sites. By default, all sites will be included in the ingestion. You can both allow and deny sites based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns. This property is currently only supported for Tableau Server. Tableau Cloud is not supported. ",
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
    "add_site_container": {
      "title": "Add Site Container",
      "description": "When enabled, sites are added as containers and therefore visible in the folder structure within Datahub.",
      "default": false,
      "type": "boolean"
    },
    "permission_ingestion": {
      "title": "Permission Ingestion",
      "description": "Configuration settings for ingesting Tableau groups and their capabilities as custom properties.",
      "allOf": [
        {
          "$ref": "#/definitions/PermissionIngestionConfig"
        }
      ]
    },
    "ingest_hidden_assets": {
      "title": "Ingest Hidden Assets",
      "description": "When enabled, hidden worksheets and dashboards are ingested into Datahub. If a dashboard or worksheet is hidden in Tableau the luid is blank. A list of asset types can also be specified, to only ingest those hidden assets. Current options supported are 'worksheet' and 'dashboard'.",
      "default": [
        "worksheet",
        "dashboard"
      ],
      "anyOf": [
        {
          "type": "array",
          "items": {
            "enum": [
              "worksheet",
              "dashboard"
            ],
            "type": "string"
          }
        },
        {
          "type": "boolean"
        }
      ]
    },
    "tags_for_hidden_assets": {
      "title": "Tags For Hidden Assets",
      "description": "Tags to be added to hidden dashboards and views. If a dashboard or view is hidden in Tableau the luid is blank. This can only be used with ingest_tags enabled as it will overwrite tags entered from the UI.",
      "default": [],
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "connect_uri"
  ],
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
    "TableauLineageOverrides": {
      "title": "TableauLineageOverrides",
      "type": "object",
      "properties": {
        "platform_override_map": {
          "title": "Platform Override Map",
          "description": "A holder for platform -> platform mappings to generate correct dataset urns",
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "database_override_map": {
          "title": "Database Override Map",
          "description": "A holder for database -> database mappings to generate correct dataset urns",
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        }
      },
      "additionalProperties": false
    },
    "PermissionIngestionConfig": {
      "title": "PermissionIngestionConfig",
      "type": "object",
      "properties": {
        "enable_workbooks": {
          "title": "Enable Workbooks",
          "description": "Whether or not to enable group permission ingestion for workbooks. Default: True",
          "default": true,
          "type": "boolean"
        },
        "group_name_pattern": {
          "title": "Group Name Pattern",
          "description": "Filter for Tableau group names when ingesting group permissions. For example, you could filter for groups that include the term 'Consumer' in their name by adding '^.*Consumer$' to the allow list.By default, all groups will be ingested. You can both allow and deny groups based on their name using their name, or a Regex pattern. Deny patterns always take precedence over allow patterns. ",
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
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.tableau.tableau.TableauSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/tableau/tableau.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Tableau, feel free to ping us on [our Slack](https://datahub.com/slack).
