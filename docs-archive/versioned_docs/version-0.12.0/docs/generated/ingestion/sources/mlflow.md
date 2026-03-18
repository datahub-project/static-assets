---
sidebar_position: 30
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
| Extract Tags | ✅ | Extract tags for MLflow Registered Model Stages |


### Concept Mapping

This ingestion source maps the following MLflow Concepts to DataHub Concepts:

|                                  Source Concept                                   |                                       DataHub Concept                                       | Notes                                                                                                                                                                                            |
|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`Registered Model`](https://mlflow.org/docs/latest/model-registry.html#concepts) | [`MlModelGroup`](/docs/generated/metamodel/entities/mlmodelgroup/) | The name of a Model Group is the same as a Registered Model's name (e.g. my_mlflow_model)                                                                                                        |
|  [`Model Version`](https://mlflow.org/docs/latest/model-registry.html#concepts)   |      [`MlModel`](/docs/generated/metamodel/entities/mlmodel/)      | The name of a Model is `{registered_model_name}{model_name_separator}{model_version}` (e.g. my_mlflow_model_1 for Registered Model named my_mlflow_model and Version 1, my_mlflow_model_2, etc.) |
|   [`Model Stage`](https://mlflow.org/docs/latest/model-registry.html#concepts)    |          [`Tag`](/docs/generated/metamodel/entities/tag/)          | The mapping between Model Stages and generated Tags is the following:<br/>- Production: mlflow_production<br/>- Staging: mlflow_staging<br/>- Archived: mlflow_archived<br/>- None: mlflow_none  |

### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[mlflow]'
```

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
| <div className="path-line"><span className="path-main">model_name_separator</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | A string which separates model name from its version (e.g. model_1 or model-1) <div className="default-line default-line-with-docs">Default: <span className="default-value">&#95;</span></div> |
| <div className="path-line"><span className="path-main">registry_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Registry server URI. If not set, an MLflow default registry_uri is used (value of tracking_uri or `MLFLOW_REGISTRY_URI` environment variable)  |
| <div className="path-line"><span className="path-main">tracking_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Tracking server URI. If not set, an MLflow default tracking_uri is used (local `mlruns/` directory or `MLFLOW_TRACKING_URI` environment variable)  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "MLflowConfig",
  "description": "Any source that produces dataset urns in a single environment should inherit this class",
  "type": "object",
  "properties": {
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
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
    }
  },
  "additionalProperties": false
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.mlflow.MLflowSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/mlflow.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for MLflow, feel free to ping us on [our Slack](https://slack.datahubproject.io).
