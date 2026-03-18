---
sidebar_position: 60
title: Sigma
slug: /generated/ingestion/sources/sigma
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/sigma.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Sigma
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Ownership | ✅ | Enabled by default, configured using `ingest_owner` |
| Extract Tags | ✅ | Enabled by default |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default. |


This plugin extracts the following:
- Sigma Workspaces and Workbooks as Container.
- Sigma Datasets
- Pages as Dashboard and its Elements as Charts

## Integration Details

This source extracts the following:

- Workspaces and workbooks within that workspaces as Container.
- Sigma Datasets as Datahub Datasets.
- Pages as Datahub dashboards and elements present inside pages as charts.

## Configuration Notes

1. Refer [doc](https://help.sigmacomputing.com/docs/generate-api-client-credentials) to generate an API client credentials.
2. Provide the generated Client ID and Secret in Recipe.

## Concept mapping 

| Sigma                  | Datahub												         | Notes                            |
|------------------------|---------------------------------------------------------------|----------------------------------|
| `Workspace`            | [Container](../../metamodel/entities/container.md)     	     | SubType `"Sigma Workspace"`      |
| `Workbook`             | [Dashboard](../../metamodel/entities/dashboard.md)            | SubType `"Sigma Workbook"`       |
| `Page`                 | [Dashboard](../../metamodel/entities/dashboard.md)            |                                  |
| `Element`              | [Chart](../../metamodel/entities/chart.md)                    |                                  |
| `Dataset`              | [Dataset](../../metamodel/entities/dataset.md)                | SubType `"Sigma Dataset"`        |
| `User`                 | [User (a.k.a CorpUser)](../../metamodel/entities/corpuser.md) | Optionally Extracted             |

## Advanced Configurations

### Chart source platform mapping
If you want to provide platform details(platform name, platform instance and env) for chart's all external upstream data sources, then you can use `chart_sources_platform_mapping` as below:

#### Example - For just one specific chart's external upstream data sources
```yml
    chart_sources_platform_mapping:
      'workspace_name/workbook_name/chart_name_1': 
        data_source_platform: snowflake
        platform_instance: new_instance
        env: PROD

      'workspace_name/folder_name/workbook_name/chart_name_2': 
        data_source_platform: postgres
        platform_instance: cloud_instance
        env: DEV
```

#### Example - For all charts within one specific workbook
```yml
    chart_sources_platform_mapping:
      'workspace_name/workbook_name_1': 
        data_source_platform: snowflake
        platform_instance: new_instance
        env: PROD
      
      'workspace_name/folder_name/workbook_name_2': 
        data_source_platform: snowflake
        platform_instance: new_instance
        env: PROD
```

#### Example - For all workbooks charts within one specific workspace
```yml
    chart_sources_platform_mapping:
      'workspace_name': 
        data_source_platform: snowflake
        platform_instance: new_instance
        env: PROD
```

#### Example - All workbooks use the same connection
```yml
    chart_sources_platform_mapping:
      '*': 
        data_source_platform: snowflake
        platform_instance: new_instance
        env: PROD
```

### CLI based Ingestion

#### Install the Plugin
The `sigma` source works out of the box with `acryl-datahub`.

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: sigma
  config:
    # Coordinates
    api_url: "https://aws-api.sigmacomputing.com/v2"
    # Credentials
    client_id: "CLIENTID"
    client_secret: "CLIENT_SECRET"
    
    # Optional - filter for certain workspace names instead of ingesting everything.
    # workspace_pattern:
    #   allow:
    #     - workspace_name

    ingest_owner: true
    
    # Optional - mapping of sigma workspace/workbook/chart folder path to all chart's data sources platform details present inside that folder path.
    # chart_sources_platform_mapping:
    #   folder_path:
    #     data_source_platform: postgres
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
| <div className="path-line"><span className="path-main">client_id</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Sigma Client ID  |
| <div className="path-line"><span className="path-main">client_secret</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Sigma Client Secret  |
| <div className="path-line"><span className="path-main">api_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Sigma API hosted URL. <div className="default-line default-line-with-docs">Default: <span className="default-value">https://aws-api.sigmacomputing.com/v2</span></div> |
| <div className="path-line"><span className="path-main">extract_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract lineage of workbook's elements and datasets or not. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">ingest_owner</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Ingest Owner from source. This will override Owner info entered from UI. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">ingest_shared_entities</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the shared entities or not. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">chart_sources_platform_mapping</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> | Any source that connects to a platform should inherit this class  |
| <div className="path-line"><span className="path-prefix">chart_sources_platform_mapping.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-prefix">chart_sources_platform_mapping.`key`.</span><span className="path-main">data_source_platform</span>&nbsp;<abbr title="Required if chart_sources_platform_mapping is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | A chart's data sources platform name.  |
| <div className="path-line"><span className="path-prefix">chart_sources_platform_mapping.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">workbook_lineage_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter workbook's elements and datasets lineage in ingestion.Requires extract_lineage to be enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">workbook_lineage_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">workbook_lineage_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workbook_lineage_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">workbook_lineage_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workbook_lineage_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">workspace_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns to filter Sigma workspaces in ingestion.Mention 'My documents' if personal entities also need to ingest. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">workspace_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">workspace_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Sigma Stateful Ingestion Config.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "SigmaSourceConfig",
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
      "description": "Sigma Stateful Ingestion Config.",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
        }
      ]
    },
    "api_url": {
      "title": "Api Url",
      "description": "Sigma API hosted URL.",
      "default": "https://aws-api.sigmacomputing.com/v2",
      "type": "string"
    },
    "client_id": {
      "title": "Client Id",
      "description": "Sigma Client ID",
      "type": "string"
    },
    "client_secret": {
      "title": "Client Secret",
      "description": "Sigma Client Secret",
      "type": "string"
    },
    "workspace_pattern": {
      "title": "Workspace Pattern",
      "description": "Regex patterns to filter Sigma workspaces in ingestion.Mention 'My documents' if personal entities also need to ingest.",
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
      "description": "Ingest Owner from source. This will override Owner info entered from UI.",
      "default": true,
      "type": "boolean"
    },
    "ingest_shared_entities": {
      "title": "Ingest Shared Entities",
      "description": "Whether to ingest the shared entities or not.",
      "default": false,
      "type": "boolean"
    },
    "extract_lineage": {
      "title": "Extract Lineage",
      "description": "Whether to extract lineage of workbook's elements and datasets or not.",
      "default": true,
      "type": "boolean"
    },
    "workbook_lineage_pattern": {
      "title": "Workbook Lineage Pattern",
      "description": "Regex patterns to filter workbook's elements and datasets lineage in ingestion.Requires extract_lineage to be enabled.",
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
    "chart_sources_platform_mapping": {
      "title": "Chart Sources Platform Mapping",
      "description": "A mapping of the sigma workspace/workbook/chart folder path to all chart's data sources platform details present inside that folder path.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/PlatformDetail"
      }
    }
  },
  "required": [
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
        },
        "data_source_platform": {
          "title": "Data Source Platform",
          "description": "A chart's data sources platform name.",
          "type": "string"
        }
      },
      "required": [
        "data_source_platform"
      ],
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.sigma.sigma.SigmaSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/sigma/sigma.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Sigma, feel free to ping us on [our Slack](https://slack.datahubproject.io).
