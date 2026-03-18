---
sidebar_position: 49
title: PowerBI
slug: /generated/ingestion/sources/powerbi
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/powerbi.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PowerBI
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| Column-level Lineage | ✅ | Disabled by default, configured using `extract_column_level_lineage`.  |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Optionally enabled via configuration profiling.enabled |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Ownership | ✅ | Enabled by default |
| Extract Tags | ✅ | Enabled by default |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default, configured using `extract_lineage`. |


This plugin extracts the following:
- Power BI dashboards, tiles and datasets
- Names, descriptions and URLs of dashboard and tile
- Owners of dashboards

## Configuration Notes
1. Refer [Microsoft AD App Creation doc](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal) to create a Microsoft AD Application. Once Microsoft AD Application is created you can configure client-credential i.e. client_id and client_secret in recipe for ingestion.
2. Enable admin access only if you want to ingest dataset, lineage and endorsement tags. Refer section [Admin Ingestion vs. Basic Ingestion](#admin-ingestion-vs-basic-ingestion) for more detail. 

    Login to PowerBI as Admin and from `Admin API settings` allow below permissions

    - Allow service principals to use read-only admin APIs
    - Enhance admin APIs responses with detailed metadata
    - Enhance admin APIs responses with DAX and mashup expressions

## Concept mapping 

| PowerBI           | Datahub             |                                                                                               
|-------------------|---------------------|
| `Dashboard`       | `Dashboard`         |
| `Dataset's Table` | `Dataset`           |
| `Tile`            | `Chart`             |
| `Report.webUrl`   | `Chart.externalUrl` |
| `Workspace`       | `Container`         |
| `Report`          | `Dashboard`         |
| `PaginatedReport` | `Dashboard`         |
| `Page`            | `Chart`             |
| `App`             | `Dashboard`         |

- If `Tile` is created from report then `Chart.externalUrl` is set to Report.webUrl.
- The `Page` is unavailable for PowerBI PaginatedReport.

## Lineage

This source extract table lineage for tables present in PowerBI Datasets. Lets consider a PowerBI Dataset `SALES_REPORT` and a PostgreSQL database is configured as data-source in `SALES_REPORT` dataset. 

Consider `SALES_REPORT` PowerBI Dataset has a table `SALES_ANALYSIS` which is backed by `SALES_ANALYSIS_VIEW` of PostgreSQL Database then in this case `SALES_ANALYSIS_VIEW` will appear as upstream dataset for `SALES_ANALYSIS` table.

You can control table lineage ingestion using `extract_lineage` configuration parameter, by default it is set to `true`. 

PowerBI Source extracts the lineage information by parsing PowerBI M-Query expression.

PowerBI Source supports M-Query expression for below listed PowerBI Data Sources 

1.  Snowflake 
2.  Oracle 
3.  PostgreSQL
4.  Microsoft SQL Server
5.  Google BigQuery
6.  Databricks

Native SQL query parsing is supported for `Snowflake` and `Amazon Redshift` data-sources.

For example refer below native SQL query. The table `OPERATIONS_ANALYTICS.TRANSFORMED_PROD.V_UNIT_TARGET` will be ingested as upstream table.

```shell
let
  Source = Value.NativeQuery(
    Snowflake.Databases(
      "sdfsd788.ws-east-2.fakecomputing.com", 
      "operations_analytics_prod", 
      [Role = "OPERATIONS_ANALYTICS_MEMBER"]
    ){[Name = "OPERATIONS_ANALYTICS"]}[Data], 
    "select #(lf)UPPER(REPLACE(AGENT_NAME,\'-\',\'\')) AS Agent,#(lf)TIER,#(lf)UPPER(MANAGER),#(lf)TEAM_TYPE,#(lf)DATE_TARGET,#(lf)MONTHID,#(lf)TARGET_TEAM,#(lf)SELLER_EMAIL,#(lf)concat((UPPER(REPLACE(AGENT_NAME,\'-\',\'\'))), MONTHID) as AGENT_KEY,#(lf)UNIT_TARGET AS SME_Quota,#(lf)AMV_TARGET AS Revenue_Quota,#(lf)SERVICE_QUOTA,#(lf)BL_TARGET,#(lf)SOFTWARE_QUOTA as Software_Quota#(lf)#(lf)from OPERATIONS_ANALYTICS.TRANSFORMED_PROD.V_UNIT_TARGETS#(lf)#(lf)where YEAR_TARGET >= 2020#(lf)and TEAM_TYPE = \'foo\'#(lf)and TARGET_TEAM = \'bar\'", 
    null, 
    [EnableFolding = true]
  ), 
  #"Added Conditional Column" = Table.AddColumn(
    Source, 
    "Has PS Software Quota?", 
    each 
      if [TIER] = "Expansion (Medium)" then
        "Yes"
      else if [TIER] = "Acquisition" then
        "Yes"
      else
        "No"
  )
in
  #"Added Conditional Column"
```
Use full-table-name in `from` clause. For example dev.public.category 

## M-Query Pattern Supported For Lineage Extraction
Lets consider a M-Query which combine two PostgreSQL tables. Such M-Query can be written as per below patterns.

**Pattern-1**

```shell
let
Source = PostgreSQL.Database("localhost", "book_store"),
book_date = Source{[Schema="public",Item="book"]}[Data],
issue_history = Source{[Schema="public",Item="issue_history"]}[Data],
combine_result  = Table.Combine({book_date, issue_history})
in
combine_result
```

**Pattern-2**

```shell
let
Source = PostgreSQL.Database("localhost", "book_store"),
combine_result  = Table.Combine({Source{[Schema="public",Item="book"]}[Data], Source{[Schema="public",Item="issue_history"]}[Data]})
in
combine_result
```

`Pattern-2` is *not* supported for upstream table lineage extraction as it uses nested item-selector i.e. {Source{[Schema="public",Item="book"]}[Data], Source{[Schema="public",Item="issue_history"]}[Data]} as argument to M-QUery table function i.e. Table.Combine

`Pattern-1` is supported as it first assigns the table from schema to variable and then variable is used in M-Query Table function i.e. Table.Combine

## Extract endorsements to tags

By default, extracting endorsement information to tags is disabled. The feature may be useful if organization uses [endorsements](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-endorse-content) to identify content quality.

Please note that the default implementation overwrites tags for the ingested entities, if you need to preserve existing tags, consider using a [transformer](../../../../metadata-ingestion/docs/transformer/dataset_transformer.md#simple-add-dataset-globaltags) with `semantics: PATCH` tags instead of `OVERWRITE`.

## Profiling

The profiling implementation is done through querying [DAX query endpoint](https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries). Therefore, the principal needs to have permission to query the datasets to be profiled. Usually this means that the service principal should have `Contributor` role for the workspace to be ingested. Profiling is done with column-based queries to be able to handle wide datasets without timeouts.

Take into account that the profiling implementation executes a fairly big number of DAX queries, and for big datasets this is a significant load to the PowerBI system.

The `profiling_pattern` setting may be used to limit profiling actions to only a certain set of resources in PowerBI. Both allowed and deny rules are matched against the following pattern for every table in a PowerBI Dataset: `workspace_name.dataset_name.table_name`. Users may limit profiling with these settings at table level, dataset level or workspace level.

## Admin Ingestion vs. Basic Ingestion
PowerBI provides two sets of API i.e. [Basic API and Admin API](https://learn.microsoft.com/en-us/rest/api/power-bi/). 

The Basic API returns metadata of PowerBI resources where service principal has granted access explicitly on resources,
whereas Admin API returns metadata of all PowerBI resources irrespective of whether service principal has granted
or doesn't grant access explicitly on resources.

The Admin Ingestion (explained below) is the recommended way to execute PowerBI ingestion as this ingestion can extract most of the metadata.


### Admin Ingestion: Service Principal As Admin in Tenant Setting and Added as Member In Workspace
To grant admin access to the service principal, visit your PowerBI tenant Settings.

If you have added service principal as `member` in workspace and also allowed below permissions from PowerBI tenant Settings

  - Allow service principal to use read-only PowerBI Admin APIs
  - Enhance admin APIs responses with detailed metadata
  - Enhance admin APIs responses with DAX and mashup expressions

PowerBI Source would be able to ingest below listed metadata of that particular workspace 

  - Lineage 
  - PowerBI Dataset 
  - Endorsement as tag
  - Dashboards 
  - Reports 
  - Dashboard Tiles
  - Report Pages
  - App

If you don't want to add a service principal as a member in your workspace, then you can enable the `admin_apis_only: true` in recipe to use PowerBI Admin API only. 

Caveats of setting `admin_apis_only` to `true`:
  - Report's pages would not get ingested as page API is not available in PowerBI Admin API
  - [PowerBI Parameters](https://learn.microsoft.com/en-us/power-query/power-query-query-parameters) would not get resolved to actual values while processing M-Query for table lineage
  - Dataset profiling is unavailable, as it requires access to the workspace API


### Basic Ingestion: Service Principal As Member In Workspace 
If you have added service principal as `member` in workspace then PowerBI Source would be able to ingest below metadata of that particular workspace 

  - Dashboards 
  - Reports 
  - Dashboard's Tiles
  - Report's Pages

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: "powerbi"
  config:
    # Your Power BI tenant identifier
    tenant_id: a949d688-67c0-4bf1-a344-e939411c6c0a

    # Azure AD Application identifier
    client_id: foo
    # Azure AD App client secret
    client_secret: bar
    
    # Ingest elements of below PowerBi Workspace into Datahub
    workspace_id_pattern:
      allow:
        - 4bd10256-e999-45dd-8e56-571c77153a5f
      deny:

    # Enable / Disable ingestion of ownership information for dashboards
    extract_ownership: true
    
    # Enable/Disable extracting workspace information to DataHub containers
    extract_workspaces_to_containers: true
    
    # Enable / Disable ingestion of endorsements.
    # Please notice that this may overwrite any existing tags defined to ingested entities!
    extract_endorsements_to_tags: false
    
    # Optional -- This mapping is optional and only required to configure platform-instance for upstream tables
    # A mapping of PowerBI datasource's server i.e host[:port] to data platform instance.
    # :port is optional and only needed if your datasource server is running on non-standard port.
    # For Google BigQuery the datasource's server is google bigquery project name
    server_to_platform_instance:
        ap-south-1.snowflakecomputing.com:
          platform_instance: operational_instance
          env: DEV
        oracle-server:1920:
          platform_instance: high_performance_production_unit
          env: PROD
        big-query-sales-project:
          platform_instance: sn-2
          env: QA

    # Need admin_api, only ingest workspace that are modified since...
    modified_since: "2023-02-10T00:00:00.0000000Z"

    ownership:
        # create powerbi user as datahub corpuser, false will still extract ownership of workspace/ dashboards
        create_corp_user: false
        # use email to build user urn instead of powerbi user identifier
        use_powerbi_email: true
        # remove email suffix like @acryl.io
        remove_email_suffix: true
        # only ingest user with certain authority
        owner_criteria: ["ReadWriteReshareExplore","Owner","Admin"]
    # wrap powerbi tables (datahub dataset) under 1 powerbi dataset (datahub container)
    extract_datasets_to_containers: true
    # only ingest dataset that are endorsed, like "Certified"
    filter_dataset_endorsements: 
      allow:
        - Certified
      
    # extract powerbi dashboards and tiles
    extract_dashboards: false
    # extract powerbi dataset table schema
    extract_dataset_schema: true

    # Enable PowerBI dataset profiling
    profiling:
      enabled: false
    # Pattern to limit which resources to profile
    # Matched resource format is following:
    # workspace_name.dataset_name.table_name
    profile_pattern:
      deny:
        - .*


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
| <div className="path-line"><span className="path-main">client_id</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure app client identifier  |
| <div className="path-line"><span className="path-main">client_secret</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure app client secret  |
| <div className="path-line"><span className="path-main">tenant_id</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | PowerBI tenant identifier  |
| <div className="path-line"><span className="path-main">admin_apis_only</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Retrieve metadata using PowerBI Admin API only. If this is enabled, then Report Pages will not be extracted. Admin API access is required if this setting is enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">convert_lineage_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert the urns of ingested lineage dataset to lowercase <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">convert_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert the PowerBI assets urns to lowercase <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">enable_advance_lineage_sql_construct</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to enable advance native sql construct for parsing like join, sub-queries. along this flag , the native_query_parsing should be enabled. By default convert_lineage_urns_to_lowercase is enabled, in-case if you have disabled it in previous ingestion execution then it may break lineageas this option generates the upstream datasets URN in lowercase. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_app</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest workspace app. Requires DataHub server 0.14.2+. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_column_level_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract column level lineage. Works only if configs `native_query_parsing`, `enable_advance_lineage_sql_construct` & `extract_lineage` are enabled.Works for M-Query where native SQL is used for transformation. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_dashboards</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest PBI Dashboard and Tiles as Datahub Dashboard and Chart <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_dataset_schema</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest PBI Dataset Table columns and measures <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_datasets_to_containers</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | PBI tables will be grouped under a Datahub Container, the container reflect a PBI Dataset <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_endorsements_to_tags</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract endorsements to tags, note that this may overwrite existing tags. Admin API access is required if this setting is enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_independent_datasets</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract datasets not used in any PowerBI visualization <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether lineage should be ingested between X and Y. Admin API access is required if this setting is enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_ownership</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether ownership should be ingested. Admin API access is required if this setting is enabled. Note that enabling this may overwrite owners that you've added inside DataHub's web application. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">extract_reports</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether reports should be ingested <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">extract_workspaces_to_containers</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Extract workspaces to DataHub containers <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_workspace_name_in_dataset_urn</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | It is recommended to set this to true, as it helps prevent the overwriting of datasets.Read section #11560 at https://datahubproject.io/docs/how/updating-datahub/ before enabling this option.To maintain backward compatibility, this is set to False. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">m_query_parse_timeout</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Timeout for PowerBI M-query parsing in seconds. Table-level lineage is determined by analyzing the M-query expression. Increase this value if you encounter the 'M-Query Parsing Timeout' message in the connector report. <div className="default-line default-line-with-docs">Default: <span className="default-value">70</span></div> |
| <div className="path-line"><span className="path-main">modified_since</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Get only recently modified workspaces based on modified_since datetime '2023-02-10T00:00:00.0000000Z', excludeInActiveWorkspaces limit to last 30 days  |
| <div className="path-line"><span className="path-main">native_query_parsing</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether PowerBI native query should be parsed to extract lineage <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">patch_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Patch dashboard metadata <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">scan_batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | batch size for sending workspace_ids to PBI, 100 is the limit <div className="default-line default-line-with-docs">Default: <span className="default-value">1</span></div> |
| <div className="path-line"><span className="path-main">scan_timeout</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | timeout for PowerBI metadata scanning <div className="default-line default-line-with-docs">Default: <span className="default-value">60</span></div> |
| <div className="path-line"><span className="path-main">workspace_id_as_urn_part</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | It is recommended to set this to True only if you have legacy workspaces based on Office 365 groups, as those workspaces can have identical names. To maintain backward compatibility, this is set to False which uses workspace name <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">filter_dataset_endorsements</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Filter and ingest datasets which are 'Certified' or 'Promoted' endorsement. If both are added, dataset which are 'Certified' or 'Promoted' will be ingested . Default setting allows all dataset to be ingested <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">filter_dataset_endorsements.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">filter_dataset_endorsements.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">filter_dataset_endorsements.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">filter_dataset_endorsements.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">filter_dataset_endorsements.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">ownership</span></div> <div className="type-name-line"><span className="type-name">OwnershipMapping</span></div> | Configure how is ownership ingested <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;create&#95;corp&#95;user&#x27;: True, &#x27;use&#95;powerbi&#95;email&#x27;: Tr...</span></div> |
| <div className="path-line"><span className="path-prefix">ownership.</span><span className="path-main">create_corp_user</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether ingest PowerBI user as Datahub Corpuser <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">ownership.</span><span className="path-main">dataset_configured_by_as_owner</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Take PBI dataset configuredBy as dataset owner if exist <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">ownership.</span><span className="path-main">remove_email_suffix</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Remove PowerBI User email suffix for example, @acryl.io <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">ownership.</span><span className="path-main">use_powerbi_email</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use PowerBI User email to ingest as corpuser, default is powerbi user identifier <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">ownership.</span><span className="path-main">owner_criteria</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Need to have certain authority to qualify as owner for example ['ReadWriteReshareExplore','Owner','Admin']  |
| <div className="path-line"><span className="path-prefix">ownership.owner_criteria.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">profile_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter tables for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered. Matched format is 'workspacename.datasetname.tablename' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">profile_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">profile_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">server_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">One of map(str,union), map(str,union)</span></div> |   |
| <div className="path-line"><span className="path-prefix">server_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | DataHub platform instance name. To generate correct urn for upstream dataset, this should match with platform instance name used in ingestion recipe of other datahub sources.  |
| <div className="path-line"><span className="path-prefix">server_to_platform_instance.`key`.</span><span className="path-main">metastore</span>&nbsp;<abbr title="Required if server_to_platform_instance is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Databricks Unity Catalog metastore name.  |
| <div className="path-line"><span className="path-prefix">server_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by DataHub platform ingestion source belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">workspace_id_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter PowerBI workspaces in ingestion. Note: This field works in conjunction with 'workspace_type_filter' and both must be considered when filtering workspaces. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_id_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_id_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_id_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">workspace_id_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_id_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">workspace_type_filter</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Ingest the metadata of the workspace where the workspace type corresponds to the specified workspace_type_filter. Note: This field works in conjunction with 'workspace_id_pattern'. Both must be matched for a workspace to be processed. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;Workspace&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_type_filter.</span><span className="path-main">enum</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "Workspace", "PersonalGroup", "Personal", "AdminWorkspace", "AdminInsights"  |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">PowerBiProfilingConfig</span></div> |  <div className="default-line ">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether profiling of PowerBI datasets should be done <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | PowerBI Stateful Ingestion Config.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "PowerBiDashboardSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
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
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "PowerBI Stateful Ingestion Config.",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
        }
      ]
    },
    "tenant_id": {
      "title": "Tenant Id",
      "description": "PowerBI tenant identifier",
      "type": "string"
    },
    "workspace_id_pattern": {
      "title": "Workspace Id Pattern",
      "description": "Regex patterns to filter PowerBI workspaces in ingestion. Note: This field works in conjunction with 'workspace_type_filter' and both must be considered when filtering workspaces.",
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
    "server_to_platform_instance": {
      "title": "Server To Platform Instance",
      "description": "A mapping of PowerBI datasource's server i.e host[:port] to Data platform instance. :port is optional and only needed if your datasource server is running on non-standard port. For Google BigQuery the datasource's server is google bigquery project name. For Databricks Unity Catalog the datasource's server is workspace FQDN.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "anyOf": [
          {
            "$ref": "#/definitions/PlatformDetail"
          },
          {
            "$ref": "#/definitions/DataBricksPlatformDetail"
          }
        ]
      }
    },
    "client_id": {
      "title": "Client Id",
      "description": "Azure app client identifier",
      "type": "string"
    },
    "client_secret": {
      "title": "Client Secret",
      "description": "Azure app client secret",
      "type": "string"
    },
    "scan_timeout": {
      "title": "Scan Timeout",
      "description": "timeout for PowerBI metadata scanning",
      "default": 60,
      "type": "integer"
    },
    "scan_batch_size": {
      "title": "Scan Batch Size",
      "description": "batch size for sending workspace_ids to PBI, 100 is the limit",
      "default": 1,
      "exclusiveMinimum": 0,
      "maximum": 100,
      "type": "integer"
    },
    "workspace_id_as_urn_part": {
      "title": "Workspace Id As Urn Part",
      "description": "It is recommended to set this to True only if you have legacy workspaces based on Office 365 groups, as those workspaces can have identical names. To maintain backward compatibility, this is set to False which uses workspace name",
      "default": false,
      "type": "boolean"
    },
    "extract_ownership": {
      "title": "Extract Ownership",
      "description": "Whether ownership should be ingested. Admin API access is required if this setting is enabled. Note that enabling this may overwrite owners that you've added inside DataHub's web application.",
      "default": false,
      "type": "boolean"
    },
    "extract_reports": {
      "title": "Extract Reports",
      "description": "Whether reports should be ingested",
      "default": true,
      "type": "boolean"
    },
    "ownership": {
      "title": "Ownership",
      "description": "Configure how is ownership ingested",
      "default": {
        "create_corp_user": true,
        "use_powerbi_email": true,
        "remove_email_suffix": false,
        "dataset_configured_by_as_owner": false,
        "owner_criteria": null
      },
      "allOf": [
        {
          "$ref": "#/definitions/OwnershipMapping"
        }
      ]
    },
    "modified_since": {
      "title": "Modified Since",
      "description": "Get only recently modified workspaces based on modified_since datetime '2023-02-10T00:00:00.0000000Z', excludeInActiveWorkspaces limit to last 30 days",
      "type": "string"
    },
    "extract_dashboards": {
      "title": "Extract Dashboards",
      "description": "Whether to ingest PBI Dashboard and Tiles as Datahub Dashboard and Chart",
      "default": true,
      "type": "boolean"
    },
    "extract_dataset_schema": {
      "title": "Extract Dataset Schema",
      "description": "Whether to ingest PBI Dataset Table columns and measures",
      "default": false,
      "type": "boolean"
    },
    "extract_lineage": {
      "title": "Extract Lineage",
      "description": "Whether lineage should be ingested between X and Y. Admin API access is required if this setting is enabled",
      "default": true,
      "type": "boolean"
    },
    "extract_endorsements_to_tags": {
      "title": "Extract Endorsements To Tags",
      "description": "Whether to extract endorsements to tags, note that this may overwrite existing tags. Admin API access is required if this setting is enabled.",
      "default": false,
      "type": "boolean"
    },
    "filter_dataset_endorsements": {
      "title": "Filter Dataset Endorsements",
      "description": "Filter and ingest datasets which are 'Certified' or 'Promoted' endorsement. If both are added, dataset which are 'Certified' or 'Promoted' will be ingested . Default setting allows all dataset to be ingested",
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
    "extract_workspaces_to_containers": {
      "title": "Extract Workspaces To Containers",
      "description": "Extract workspaces to DataHub containers",
      "default": true,
      "type": "boolean"
    },
    "extract_datasets_to_containers": {
      "title": "Extract Datasets To Containers",
      "description": "PBI tables will be grouped under a Datahub Container, the container reflect a PBI Dataset",
      "default": false,
      "type": "boolean"
    },
    "native_query_parsing": {
      "title": "Native Query Parsing",
      "description": "Whether PowerBI native query should be parsed to extract lineage",
      "default": true,
      "type": "boolean"
    },
    "convert_urns_to_lowercase": {
      "title": "Convert Urns To Lowercase",
      "description": "Whether to convert the PowerBI assets urns to lowercase",
      "default": false,
      "type": "boolean"
    },
    "convert_lineage_urns_to_lowercase": {
      "title": "Convert Lineage Urns To Lowercase",
      "description": "Whether to convert the urns of ingested lineage dataset to lowercase",
      "default": true,
      "type": "boolean"
    },
    "admin_apis_only": {
      "title": "Admin Apis Only",
      "description": "Retrieve metadata using PowerBI Admin API only. If this is enabled, then Report Pages will not be extracted. Admin API access is required if this setting is enabled",
      "default": false,
      "type": "boolean"
    },
    "extract_independent_datasets": {
      "title": "Extract Independent Datasets",
      "description": "Whether to extract datasets not used in any PowerBI visualization",
      "default": false,
      "type": "boolean"
    },
    "enable_advance_lineage_sql_construct": {
      "title": "Enable Advance Lineage Sql Construct",
      "description": "Whether to enable advance native sql construct for parsing like join, sub-queries. along this flag , the native_query_parsing should be enabled. By default convert_lineage_urns_to_lowercase is enabled, in-case if you have disabled it in previous ingestion execution then it may break lineageas this option generates the upstream datasets URN in lowercase.",
      "default": true,
      "type": "boolean"
    },
    "extract_column_level_lineage": {
      "title": "Extract Column Level Lineage",
      "description": "Whether to extract column level lineage. Works only if configs `native_query_parsing`, `enable_advance_lineage_sql_construct` & `extract_lineage` are enabled.Works for M-Query where native SQL is used for transformation.",
      "default": false,
      "type": "boolean"
    },
    "profile_pattern": {
      "title": "Profile Pattern",
      "description": "Regex patterns to filter tables for profiling during ingestion. Note that only tables allowed by the `table_pattern` will be considered. Matched format is 'workspacename.datasetname.tablename'",
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
      "default": {
        "enabled": false
      },
      "allOf": [
        {
          "$ref": "#/definitions/PowerBiProfilingConfig"
        }
      ]
    },
    "patch_metadata": {
      "title": "Patch Metadata",
      "description": "Patch dashboard metadata",
      "default": true,
      "type": "boolean"
    },
    "workspace_type_filter": {
      "title": "Workspace Type Filter",
      "description": "Ingest the metadata of the workspace where the workspace type corresponds to the specified workspace_type_filter. Note: This field works in conjunction with 'workspace_id_pattern'. Both must be matched for a workspace to be processed.",
      "default": [
        "Workspace"
      ],
      "type": "array",
      "items": {
        "enum": [
          "Workspace",
          "PersonalGroup",
          "Personal",
          "AdminWorkspace",
          "AdminInsights"
        ],
        "type": "string"
      }
    },
    "include_workspace_name_in_dataset_urn": {
      "title": "Include Workspace Name In Dataset Urn",
      "description": "It is recommended to set this to true, as it helps prevent the overwriting of datasets.Read section #11560 at https://datahubproject.io/docs/how/updating-datahub/ before enabling this option.To maintain backward compatibility, this is set to False.",
      "default": false,
      "type": "boolean"
    },
    "extract_app": {
      "title": "Extract App",
      "description": "Whether to ingest workspace app. Requires DataHub server 0.14.2+.",
      "default": false,
      "type": "boolean"
    },
    "m_query_parse_timeout": {
      "title": "M Query Parse Timeout",
      "description": "Timeout for PowerBI M-query parsing in seconds. Table-level lineage is determined by analyzing the M-query expression. Increase this value if you encounter the 'M-Query Parsing Timeout' message in the connector report.",
      "default": 70,
      "type": "integer"
    }
  },
  "required": [
    "tenant_id",
    "client_id",
    "client_secret"
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
    "PlatformDetail": {
      "title": "PlatformDetail",
      "type": "object",
      "properties": {
        "platform_instance": {
          "title": "Platform Instance",
          "description": "DataHub platform instance name. To generate correct urn for upstream dataset, this should match with platform instance name used in ingestion recipe of other datahub sources.",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "The environment that all assets produced by DataHub platform ingestion source belong to",
          "default": "PROD",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "DataBricksPlatformDetail": {
      "title": "DataBricksPlatformDetail",
      "description": "metastore is an additional field used in Databricks connector to generate the dataset urn",
      "type": "object",
      "properties": {
        "platform_instance": {
          "title": "Platform Instance",
          "description": "DataHub platform instance name. To generate correct urn for upstream dataset, this should match with platform instance name used in ingestion recipe of other datahub sources.",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "The environment that all assets produced by DataHub platform ingestion source belong to",
          "default": "PROD",
          "type": "string"
        },
        "metastore": {
          "title": "Metastore",
          "description": "Databricks Unity Catalog metastore name.",
          "type": "string"
        }
      },
      "required": [
        "metastore"
      ],
      "additionalProperties": false
    },
    "OwnershipMapping": {
      "title": "OwnershipMapping",
      "type": "object",
      "properties": {
        "create_corp_user": {
          "title": "Create Corp User",
          "description": "Whether ingest PowerBI user as Datahub Corpuser",
          "default": true,
          "type": "boolean"
        },
        "use_powerbi_email": {
          "title": "Use Powerbi Email",
          "description": "Use PowerBI User email to ingest as corpuser, default is powerbi user identifier",
          "default": true,
          "type": "boolean"
        },
        "remove_email_suffix": {
          "title": "Remove Email Suffix",
          "description": "Remove PowerBI User email suffix for example, @acryl.io",
          "default": false,
          "type": "boolean"
        },
        "dataset_configured_by_as_owner": {
          "title": "Dataset Configured By As Owner",
          "description": "Take PBI dataset configuredBy as dataset owner if exist",
          "default": false,
          "type": "boolean"
        },
        "owner_criteria": {
          "title": "Owner Criteria",
          "description": "Need to have certain authority to qualify as owner for example ['ReadWriteReshareExplore','Owner','Admin']",
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": false
    },
    "PowerBiProfilingConfig": {
      "title": "PowerBiProfilingConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether profiling of PowerBI datasets should be done",
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
- Class Name: `datahub.ingestion.source.powerbi.powerbi.PowerBiDashboardSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/powerbi/powerbi.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for PowerBI, feel free to ping us on [our Slack](https://slack.datahubproject.io).
