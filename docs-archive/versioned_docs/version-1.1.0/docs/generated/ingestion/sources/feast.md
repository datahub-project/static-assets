---
sidebar_position: 21
title: Feast
slug: /generated/ingestion/sources/feast
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/feast.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Feast
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Descriptions | ✅ | Enabled by default |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Schema Metadata | ✅ | Enabled by default |
| Table-Level Lineage | ✅ | Enabled by default |


This plugin extracts:

- Entities as [`MLPrimaryKey`](/docs/graphql/objects#mlprimarykey)
- Fields as [`MLFeature`](/docs/graphql/objects#mlfeature)
- Feature views and on-demand feature views as [`MLFeatureTable`](/docs/graphql/objects#mlfeaturetable)
- Batch and stream source details as [`Dataset`](/docs/graphql/objects#dataset)
- Column types associated with each entity and feature


### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: feast
  config:
    # Coordinates
    path: "/path/to/repository/"
    # Options
    environment: "PROD"

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
| <div className="path-line"><span className="path-main">path</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to Feast repository  |
| <div className="path-line"><span className="path-main">enable_owner_extraction</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If this is disabled, then we NEVER try to map owners. If this is enabled, then owner_mappings is REQUIRED to extract ownership. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">enable_tag_extraction</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If this is disabled, then we NEVER try to extract tags. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">environment</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Environment to use when constructing URNs <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">fs_yaml_file</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to the `feature_store.yaml` file used to configure the feature store  |
| <div className="path-line"><span className="path-main">owner_mappings</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Mapping of owner names to owner types  |
| <div className="path-line"><span className="path-prefix">owner_mappings.</span><span className="path-main">map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulIngestionConfig</span></div> | Stateful Ingestion Config  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "FeastRepositorySourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Stateful Ingestion Config",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulIngestionConfig"
        }
      ]
    },
    "path": {
      "title": "Path",
      "description": "Path to Feast repository",
      "type": "string"
    },
    "fs_yaml_file": {
      "title": "Fs Yaml File",
      "description": "Path to the `feature_store.yaml` file used to configure the feature store",
      "type": "string"
    },
    "environment": {
      "title": "Environment",
      "description": "Environment to use when constructing URNs",
      "default": "PROD",
      "type": "string"
    },
    "owner_mappings": {
      "title": "Owner Mappings",
      "description": "Mapping of owner names to owner types",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {
          "type": "string"
        }
      }
    },
    "enable_owner_extraction": {
      "title": "Enable Owner Extraction",
      "description": "If this is disabled, then we NEVER try to map owners. If this is enabled, then owner_mappings is REQUIRED to extract ownership.",
      "default": false,
      "type": "boolean"
    },
    "enable_tag_extraction": {
      "title": "Enable Tag Extraction",
      "description": "If this is disabled, then we NEVER try to extract tags.",
      "default": false,
      "type": "boolean"
    }
  },
  "required": [
    "path"
  ],
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
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.feast.FeastRepositorySource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/feast.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Feast, feel free to ping us on [our Slack](https://datahub.com/slack).
