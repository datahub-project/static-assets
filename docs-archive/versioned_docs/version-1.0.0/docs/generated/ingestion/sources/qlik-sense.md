---
sidebar_position: 54
title: Qlik Sense
slug: /generated/ingestion/sources/qlik-sense
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/qlik-sense.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Qlik Sense
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| Column-level Lineage | ✅ | Disabled by default.  |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Ownership | ✅ | Enabled by default, configured using `ingest_owner` |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default. |


This plugin extracts the following:
- Qlik Sense Spaces and Apps as Container.
- Qlik Datasets
- Sheets as dashboard and its charts

## Integration Details

This source extracts the following:

- Accessible spaces and apps within that spaces as Container.
- Qlik Datasets as Datahub Datasets with schema metadata.
- Sheets as Datahub dashboard and charts present inside sheets.

## Configuration Notes

1. Refer [doc](https://qlik.dev/authenticate/api-key/generate-your-first-api-key/) to generate an API key from the hub.
2. Get tenant hostname from About tab after login to qlik sense account.

## Concept mapping 

| Qlik Sense             | Datahub												         | Notes                            |
|------------------------|---------------------------------------------------------------|----------------------------------|
| `Space`                | [Container](../../metamodel/entities/container.md)     	     | SubType `"Qlik Space"`           |
| `App`                  | [Container](../../metamodel/entities/container.md)            | SubType `"Qlik App"`             |
| `Sheet`                | [Dashboard](../../metamodel/entities/dashboard.md)            |                                  |
| `Chart`                | [Chart](../../metamodel/entities/chart.md)                    |                                  |
| `Dataset`              | [Dataset](../../metamodel/entities/dataset.md)                | SubType `"Qlik Dataset"`         |
| `User`                 | [User (a.k.a CorpUser)](../../metamodel/entities/corpuser.md) | Optionally Extracted             |
### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: qlik-sense
  config:
    # Coordinates
    tenant_hostname: "xyz12xz.us.qlikcloud.com"
    # Credentials
    api_key: "QLIK_API_KEY"
    
    # Optional - filter for certain space names instead of ingesting everything.
    # Mention 'personal_space' if entities of personal space need to ingest
    # space_pattern:
    #   allow:
    #     - space_name

    ingest_owner: true
    
    # Optional -- This mapping is optional and only required to configure platform-instance for Qlik app dataset upstream source tables
    # A mapping of the Qlik app dataset upstream tables from data connection to platform instance. Use 'data_connection_name' as key.
    # data_connection_to_platform_instance:
    #   data_connection_name:
    #     platform_instance: cloud_instance
    #     env: DEV

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
| <div className="path-line"><span className="path-main">api_key</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Qlik API Key  |
| <div className="path-line"><span className="path-main">tenant_hostname</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Qlik Tenant hostname  |
| <div className="path-line"><span className="path-main">ingest_owner</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest Owner from source. This will override Owner info entered from UI <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">data_connection_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> | Any source that connects to a platform should inherit this class  |
| <div className="path-line"><span className="path-prefix">data_connection_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-prefix">data_connection_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">space_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter Qlik spaces in ingestion.Mention 'personal_space' if entities of personal space need to ingest <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">space_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">space_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulIngestionConfig</span></div> | Stateful Ingestion Config  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "QlikSourceConfig",
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
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Stateful Ingestion Config",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulIngestionConfig"
        }
      ]
    },
    "tenant_hostname": {
      "title": "Tenant Hostname",
      "description": "Qlik Tenant hostname",
      "type": "string"
    },
    "api_key": {
      "title": "Api Key",
      "description": "Qlik API Key",
      "type": "string"
    },
    "space_pattern": {
      "title": "Space Pattern",
      "description": "Regex patterns to filter Qlik spaces in ingestion.Mention 'personal_space' if entities of personal space need to ingest",
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
    "ingest_owner": {
      "title": "Ingest Owner",
      "description": "Ingest Owner from source. This will override Owner info entered from UI",
      "default": true,
      "type": "boolean"
    },
    "data_connection_to_platform_instance": {
      "title": "Data Connection To Platform Instance",
      "description": "A mapping of the Qlik app dataset upstream tables from data connection to platform instance.Use 'data_connection_name' as key.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/PlatformDetail"
      }
    }
  },
  "required": [
    "tenant_hostname",
    "api_key"
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
    "StatefulIngestionConfig": {
      "title": "StatefulIngestionConfig",
      "description": "Basic Stateful Ingestion Specific Configuration for any source.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "default": false,
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
      "description": "Any source that connects to a platform should inherit this class",
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
          "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
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


### Code Coordinates
- Class Name: `datahub.ingestion.source.qlik_sense.qlik_sense.QlikSenseSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/qlik_sense/qlik_sense.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Qlik Sense, feel free to ping us on [our Slack](https://slack.datahubproject.io).
