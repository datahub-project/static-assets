---
sidebar_position: 39
title: Mode
slug: /generated/ingestion/sources/mode
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/mode.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Mode
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| Column-level Lineage | ✅ | Supported by default |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Ownership | ✅ | Enabled by default |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Supported by default |



This plugin extracts Charts, Reports, and associated metadata from a given Mode workspace. This plugin is in beta and has only been tested
on PostgreSQL database.

### Report

[/api/{account}/reports/{report}](https://mode.com/developer/api-reference/analytics/reports/) endpoint is used to
retrieve the following report information.

- Title and description
- Last edited by
- Owner
- Link to the Report in Mode for exploration
- Associated charts within the report

### Chart

[/api/{workspace}/reports/{report}/queries/{query}/charts'](https://mode.com/developer/api-reference/analytics/charts/#getChart) endpoint is used to
retrieve the following information.

- Title and description
- Last edited by
- Owner
- Link to the chart in Metabase
- Datasource and lineage information from Report queries.

The following properties for a chart are ingested in DataHub.

#### Chart Information
| Name      | Description                            |
|-----------|----------------------------------------|
| `Filters` | Filters applied to the chart           |
| `Metrics` | Fields or columns used for aggregation |
| `X`       | Fields used in X-axis                  |
| `X2`      | Fields used in second X-axis           |
| `Y`       | Fields used in Y-axis                  |
| `Y2`      | Fields used in second Y-axis           |


#### Table Information
| Name      | Description                  |
|-----------|------------------------------|
| `Columns` | Column names in a table      |
| `Filters` | Filters applied to the table |



#### Pivot Table Information
| Name      | Description                            |
|-----------|----------------------------------------|
| `Columns` | Column names in a table                |
| `Filters` | Filters applied to the table           |
| `Metrics` | Fields or columns used for aggregation |
| `Rows`    | Row names in a table                   |



### CLI based Ingestion

#### Install the Plugin
The `mode` source works out of the box with `acryl-datahub`.

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: mode
  config:
    # Coordinates
    connect_uri: http://app.mode.com

    # Credentials
    token: token
    password: pass

    # Options
    workspace: "datahub"
    default_schema: "public"
    owner_username_instead_of_email: False
    api_options:
      retry_backoff_multiplier: 2
      max_retry_interval: 10
      max_attempts: 5

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
| <div className="path-line"><span className="path-main">password</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | When creating workspace API key this is the 'Secret'.  |
| <div className="path-line"><span className="path-main">token</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | When creating workspace API key this is the 'Key ID'.  |
| <div className="path-line"><span className="path-main">workspace</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The Mode workspace name. Find it in Settings > Workspace > Details.  |
| <div className="path-line"><span className="path-main">connect_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Mode host URL. <div className="default-line default-line-with-docs">Default: <span className="default-value">https://app.mode.com</span></div> |
| <div className="path-line"><span className="path-main">default_schema</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Default schema to use when schema is not provided in an SQL query <div className="default-line default-line-with-docs">Default: <span className="default-value">public</span></div> |
| <div className="path-line"><span className="path-main">exclude_restricted</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Exclude restricted collections <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_embed_url</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to Ingest embed URL for Reports <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">owner_username_instead_of_email</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Use username for owner URN instead of Email <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">platform_instance_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">tag_measures_and_dimensions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Tag measures and dimensions in the schema <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">api_options</span></div> <div className="type-name-line"><span className="type-name">ModeAPIConfig</span></div> | Retry/Wait settings for Mode API to avoid "Too many Requests" error. See Mode API Options below <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;retry&#95;backoff&#95;multiplier&#x27;: 2, &#x27;max&#95;retry&#95;interva...</span></div> |
| <div className="path-line"><span className="path-prefix">api_options.</span><span className="path-main">max_attempts</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of attempts to retry before failing <div className="default-line default-line-with-docs">Default: <span className="default-value">5</span></div> |
| <div className="path-line"><span className="path-prefix">api_options.</span><span className="path-main">max_retry_interval</span></div> <div className="type-name-line"><span className="type-name">One of integer, number</span></div> | Maximum interval to wait when retrying <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">api_options.</span><span className="path-main">retry_backoff_multiplier</span></div> <div className="type-name-line"><span className="type-name">One of integer, number</span></div> | Multiplier for exponential backoff when waiting to retry <div className="default-line default-line-with-docs">Default: <span className="default-value">2</span></div> |
| <div className="path-line"><span className="path-prefix">api_options.</span><span className="path-main">timeout</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Timout setting, how long to wait for the Mode rest api to send data before giving up <div className="default-line default-line-with-docs">Default: <span className="default-value">40</span></div> |
| <div className="path-line"><span className="path-main">space_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for mode spaces to filter in ingestion (Spaces named as 'Personal' are filtered by default.) Specify regex to only match the space name. e.g. to only ingest space named analytics, use the regex 'analytics' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#x27;^Personal$&#x27;&#93;, &#x27;ignoreC...</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "ModeConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
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
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "connect_uri": {
      "title": "Connect Uri",
      "description": "Mode host URL.",
      "default": "https://app.mode.com",
      "type": "string"
    },
    "token": {
      "title": "Token",
      "description": "When creating workspace API key this is the 'Key ID'.",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "When creating workspace API key this is the 'Secret'.",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "exclude_restricted": {
      "title": "Exclude Restricted",
      "description": "Exclude restricted collections",
      "default": false,
      "type": "boolean"
    },
    "workspace": {
      "title": "Workspace",
      "description": "The Mode workspace name. Find it in Settings > Workspace > Details.",
      "type": "string"
    },
    "default_schema": {
      "title": "Default Schema",
      "description": "Default schema to use when schema is not provided in an SQL query",
      "default": "public",
      "type": "string"
    },
    "space_pattern": {
      "title": "Space Pattern",
      "description": "Regex patterns for mode spaces to filter in ingestion (Spaces named as 'Personal' are filtered by default.) Specify regex to only match the space name. e.g. to only ingest space named analytics, use the regex 'analytics'",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [
          "^Personal$"
        ],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "owner_username_instead_of_email": {
      "title": "Owner Username Instead Of Email",
      "description": "Use username for owner URN instead of Email",
      "default": true,
      "type": "boolean"
    },
    "api_options": {
      "title": "Api Options",
      "description": "Retry/Wait settings for Mode API to avoid \"Too many Requests\" error. See Mode API Options below",
      "default": {
        "retry_backoff_multiplier": 2,
        "max_retry_interval": 10,
        "max_attempts": 5,
        "timeout": 40
      },
      "allOf": [
        {
          "$ref": "#/definitions/ModeAPIConfig"
        }
      ]
    },
    "ingest_embed_url": {
      "title": "Ingest Embed Url",
      "description": "Whether to Ingest embed URL for Reports",
      "default": true,
      "type": "boolean"
    },
    "tag_measures_and_dimensions": {
      "title": "Tag Measures And Dimensions",
      "description": "Tag measures and dimensions in the schema",
      "default": true,
      "type": "boolean"
    }
  },
  "required": [
    "token",
    "password",
    "workspace"
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
    "ModeAPIConfig": {
      "title": "ModeAPIConfig",
      "type": "object",
      "properties": {
        "retry_backoff_multiplier": {
          "title": "Retry Backoff Multiplier",
          "description": "Multiplier for exponential backoff when waiting to retry",
          "default": 2,
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "number"
            }
          ]
        },
        "max_retry_interval": {
          "title": "Max Retry Interval",
          "description": "Maximum interval to wait when retrying",
          "default": 10,
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "number"
            }
          ]
        },
        "max_attempts": {
          "title": "Max Attempts",
          "description": "Maximum number of attempts to retry before failing",
          "default": 5,
          "type": "integer"
        },
        "timeout": {
          "title": "Timeout",
          "description": "Timout setting, how long to wait for the Mode rest api to send data before giving up",
          "default": 40,
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

See Mode's [Authentication documentation](https://mode.com/developer/api-reference/authentication/) on how to generate `token` and `password`.

### Code Coordinates
- Class Name: `datahub.ingestion.source.mode.ModeSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/mode.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Mode, feel free to ping us on [our Slack](https://slack.datahubproject.io).
