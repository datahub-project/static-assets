---
sidebar_position: 39
title: MLflow
slug: /generated/ingestion/sources/mlflow
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/mlflow.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MLflow
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Descriptions | ✅ | Extract descriptions for MLflow Registered Models and Model Versions |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Extract Tags | ✅ | Extract tags for MLflow Registered Model Stages |


### Concept Mapping

This ingestion source maps the following MLflow Concepts to DataHub Concepts:

|                                  Source Concept                                   |                                       DataHub Concept                                       | Notes                                                                                                                                                                                            |
|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`Registered Model`](https://mlflow.org/docs/latest/model-registry.html#concepts) | [`MlModelGroup`](/docs/generated/metamodel/entities/mlmodelgroup/) | The name of a Model Group is the same as a Registered Model's name (e.g. my_mlflow_model)                                                                                                        |
|  [`Model Version`](https://mlflow.org/docs/latest/model-registry.html#concepts)   |      [`MlModel`](/docs/generated/metamodel/entities/mlmodel/)      | The name of a Model is `{registered_model_name}{model_name_separator}{model_version}` (e.g. my_mlflow_model_1 for Registered Model named my_mlflow_model and Version 1, my_mlflow_model_2, etc.) |
|   [`Model Stage`](https://mlflow.org/docs/latest/model-registry.html#concepts)    |          [`Tag`](/docs/generated/metamodel/entities/tag/)          | The mapping between Model Stages and generated Tags is the following:<br/>- Production: mlflow_production<br/>- Staging: mlflow_staging<br/>- Archived: mlflow_archived<br/>- None: mlflow_none  |

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: mlflow
  config:
    # Coordinates
    tracking_uri: tracking_uri

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
| <div className="path-line"><span className="path-main">base_external_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Base URL to use when constructing external URLs to MLflow. If not set, tracking_uri is used if it's an HTTP URL. If neither is set, external URLs are not generated.  |
| <div className="path-line"><span className="path-main">model_name_separator</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | A string which separates model name from its version (e.g. model_1 or model-1) <div className="default-line default-line-with-docs">Default: <span className="default-value">&#95;</span></div> |
| <div className="path-line"><span className="path-main">registry_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Registry server URI. If not set, an MLflow default registry_uri is used (value of tracking_uri or `MLFLOW_REGISTRY_URI` environment variable)  |
| <div className="path-line"><span className="path-main">tracking_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tracking server URI. If not set, an MLflow default tracking_uri is used (local `mlruns/` directory or `MLFLOW_TRACKING_URI` environment variable)  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulIngestionConfig</span></div> | Stateful Ingestion Config  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "MLflowConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
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
    "tracking_uri": {
      "title": "Tracking Uri",
      "description": "Tracking server URI. If not set, an MLflow default tracking_uri is used (local `mlruns/` directory or `MLFLOW_TRACKING_URI` environment variable)",
      "type": "string"
    },
    "registry_uri": {
      "title": "Registry Uri",
      "description": "Registry server URI. If not set, an MLflow default registry_uri is used (value of tracking_uri or `MLFLOW_REGISTRY_URI` environment variable)",
      "type": "string"
    },
    "model_name_separator": {
      "title": "Model Name Separator",
      "description": "A string which separates model name from its version (e.g. model_1 or model-1)",
      "default": "_",
      "type": "string"
    },
    "base_external_url": {
      "title": "Base External Url",
      "description": "Base URL to use when constructing external URLs to MLflow. If not set, tracking_uri is used if it's an HTTP URL. If neither is set, external URLs are not generated.",
      "type": "string"
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
- Class Name: `datahub.ingestion.source.mlflow.MLflowSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/mlflow.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for MLflow, feel free to ping us on [our Slack](https://slack.datahubproject.io).
