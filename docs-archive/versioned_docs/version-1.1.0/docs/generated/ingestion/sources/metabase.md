---
sidebar_position: 37
title: Metabase
slug: /generated/ingestion/sources/metabase
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/metabase.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Metabase
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Supported by default |


This plugin extracts Charts, dashboards, and associated metadata. This plugin is in beta and has only been tested
on PostgreSQL and H2 database.

### Collection

[/api/collection](https://www.metabase.com/docs/latest/api/collection) endpoint is used to
retrieve the available collections.

[/api/collection/<COLLECTION_ID>/items?models=dashboard](https://www.metabase.com/docs/latest/api/collection#get-apicollectioniditems) endpoint is used to retrieve a given collection and list their dashboards.

 ### Dashboard

[/api/dashboard/<DASHBOARD_ID>](https://www.metabase.com/docs/latest/api/dashboard) endpoint is used to retrieve a given Dashboard and grab its information.

- Title and description
- Last edited by
- Owner
- Link to the dashboard in Metabase
- Associated charts

### Chart

[/api/card](https://www.metabase.com/docs/latest/api-documentation.html#card) endpoint is used to
retrieve the following information.

- Title and description
- Last edited by
- Owner
- Link to the chart in Metabase
- Datasource and lineage

The following properties for a chart are ingested in DataHub.

| Name          | Description                                     |
| ------------- | ----------------------------------------------- |
| `Dimensions`  | Column names                                    |
| `Filters`     | Any filters applied to the chart                |
| `Metrics`     | All columns that are being used for aggregation |




### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">api_key</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Metabase API key. If provided, the username and password will be ignored. Recommended method.  |
| <div className="path-line"><span className="path-main">connect_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Metabase host URL. <div className="default-line default-line-with-docs">Default: <span className="default-value">localhost:3000</span></div> |
| <div className="path-line"><span className="path-main">database_alias_map</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Database name map to use when constructing dataset URN.  |
| <div className="path-line"><span className="path-main">database_id_to_instance_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">default_schema</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Default schema name to use when schema is not provided in an SQL query <div className="default-line default-line-with-docs">Default: <span className="default-value">public</span></div> |
| <div className="path-line"><span className="path-main">display_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | optional URL to use in links (if `connect_uri` is only for ingestion)  |
| <div className="path-line"><span className="path-main">engine_platform_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">exclude_other_user_collections</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Flag that if true, exclude other user collections <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Metabase password, used when an API key is not provided.  |
| <div className="path-line"><span className="path-main">platform_instance_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Metabase username, used when an API key is not provided.  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
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
  "title": "MetabaseConfig",
  "description": "Any non-Dataset source that produces lineage to Datasets should inherit this class.\ne.g. Orchestrators, Pipelines, BI Tools etc.",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance_map": {
      "title": "Platform Instance Map",
      "description": "A holder for platform -> platform_instance mappings to generate correct dataset urns",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "connect_uri": {
      "title": "Connect Uri",
      "description": "Metabase host URL.",
      "default": "localhost:3000",
      "type": "string"
    },
    "display_uri": {
      "title": "Display Uri",
      "description": "optional URL to use in links (if `connect_uri` is only for ingestion)",
      "type": "string"
    },
    "username": {
      "title": "Username",
      "description": "Metabase username, used when an API key is not provided.",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "Metabase password, used when an API key is not provided.",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "api_key": {
      "title": "Api Key",
      "description": "Metabase API key. If provided, the username and password will be ignored. Recommended method.",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "database_alias_map": {
      "title": "Database Alias Map",
      "description": "Database name map to use when constructing dataset URN.",
      "type": "object"
    },
    "engine_platform_map": {
      "title": "Engine Platform Map",
      "description": "Custom mappings between metabase database engines and DataHub platforms",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "database_id_to_instance_map": {
      "title": "Database Id To Instance Map",
      "description": "Custom mappings between metabase database id and DataHub platform instance",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "default_schema": {
      "title": "Default Schema",
      "description": "Default schema name to use when schema is not provided in an SQL query",
      "default": "public",
      "type": "string"
    },
    "exclude_other_user_collections": {
      "title": "Exclude Other User Collections",
      "description": "Flag that if true, exclude other user collections",
      "default": false,
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
    }
  }
}
```


</TabItem>
</Tabs>

Metabase databases will be mapped to a DataHub platform based on the engine listed in the
[api/database](https://www.metabase.com/docs/latest/api-documentation.html#database) response. This mapping can be
customized by using the `engine_platform_map` config option. For example, to map databases using the `athena` engine to
the underlying datasets in the `glue` platform, the following snippet can be used:

```yml
engine_platform_map:
  athena: glue
```

DataHub will try to determine database name from Metabase [api/database](https://www.metabase.com/docs/latest/api-documentation.html#database)
payload. However, the name can be overridden from `database_alias_map` for a given database connected to Metabase.

If several platform instances with the same platform (e.g. from several distinct clickhouse clusters) are present in DataHub,
the mapping between database id in Metabase and platform instance in DataHub may be configured with the following map:

```yml
database_id_to_instance_map:
  "42": platform_instance_in_datahub
```

The key in this map must be string, not integer although Metabase API provides `id` as number.
If `database_id_to_instance_map` is not specified, `platform_instance_map` is used for platform instance mapping. If none of the above are specified, platform instance is not used when constructing `urn` when searching for dataset relations.

If needed it is possible to exclude collections from other users by setting the following configuration:

```yaml
exclude_other_user_collections: true
```

## Compatibility

Metabase version [v0.48.3](https://www.metabase.com/start/oss/)

### Code Coordinates
- Class Name: `datahub.ingestion.source.metabase.MetabaseSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/metabase.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Metabase, feel free to ping us on [our Slack](https://datahub.com/slack).
