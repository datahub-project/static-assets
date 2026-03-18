---
title: ML System
slug: /api/tutorials/ml
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/api/tutorials/ml.md
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ML System

## Why Would You Integrate ML System with DataHub?

Machine learning systems have become a crucial feature in modern data stacks.
However, the relationships between the different components of a machine learning system, such as features, models, and feature tables, can be complex.
DataHub makes these relationships discoverable and facilitate utilization by other members of the organization.

For technical details on ML entities, please refer to the following docs:

- [MlFeature](/docs/generated/metamodel/entities/mlFeature.md)
- [MlPrimaryKey](/docs/generated/metamodel/entities/mlPrimaryKey.md)
- [MlFeatureTable](/docs/generated/metamodel/entities/mlFeatureTable.md)
- [MlModel](/docs/generated/metamodel/entities/mlModel.md)
- [MlModelGroup](/docs/generated/metamodel/entities/mlModelGroup.md)

### Goal Of This Guide

This guide will show you how to

- Create ML entities: MlFeature, MlFeatureTable, MlModel, MlModelGroup, MlPrimaryKey
- Read ML entities: MlFeature, MlFeatureTable, MlModel, MlModelGroup, MlPrimaryKey
- Attach MlModel to MlFeature
- Attach MlFeatures to MlFeatureTable
- Attached MlFeatures to upstream Datasets that power them

## Prerequisites

For this tutorial, you need to deploy DataHub Quickstart and ingest sample data.
For detailed steps, please refer to [Datahub Quickstart Guide](/docs/quickstart.md).

## Create ML Entities

### Create MlFeature

An ML Feature represents an instance of a feature that can be used across different machine learning models. Features are organized into Feature Tables to be consumed by machine learning models. For example, if we were modeling features for a Users Feature Table, the Features would be `age`, `sign_up_date`, `active_in_past_30_days` and so forth.Using Features in DataHub allows users to see the sources a feature was generated from and how a feature is used to train models.

<Tabs>
<TabItem value="python" label="Python" default>

```python
# Inlined from /metadata-ingestion/examples/library/create_mlfeature.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server="http://localhost:8080", extra_headers={})

dataset_urn = builder.make_dataset_urn(
    name="fct_users_created", platform="hive", env="PROD"
)
feature_urn = builder.make_ml_feature_urn(
    feature_table_name="users_feature_table",
    feature_name="user_signup_date",
)

#  Create feature
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlFeature",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=feature_urn,
    aspectName="mlFeatureProperties",
    aspect=models.MLFeaturePropertiesClass(
        description="Represents the date the user created their account",
        # attaching a source to a feature creates lineage between the feature
        # and the upstream dataset. This is how lineage between your data warehouse
        # and machine learning ecosystem is established.
        sources=[dataset_urn],
        dataType="TIME",
    ),
)

# Emit metadata!
emitter.emit(metadata_change_proposal)

```

Note that when creating a feature, you create upstream lineage to the data warehouse using `sources`.

</TabItem>
</Tabs>

### Create MlPrimaryKey

An ML Primary Key represents a specific element of a Feature Table that indicates what group the other features belong to. For example, if a Feature Table contained features for Users, the ML Primary Key would likely be `user_id` or some similar unique identifier for a user. Using ML Primary Keys in DataHub allow users to indicate how ML Feature Tables are structured.

<Tabs>
<TabItem value="python" label="Python" default>

```python
# Inlined from /metadata-ingestion/examples/library/create_mlprimarykey.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server="http://localhost:8080", extra_headers={})

dataset_urn = builder.make_dataset_urn(
    name="fct_users_created", platform="hive", env="PROD"
)
primary_key_urn = builder.make_ml_primary_key_urn(
    feature_table_name="users_feature_table",
    primary_key_name="user_id",
)

#  Create feature
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlPrimaryKey",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=primary_key_urn,
    aspectName="mlPrimaryKeyProperties",
    aspect=models.MLPrimaryKeyPropertiesClass(
        description="Represents the id of the user the other features relate to.",
        # attaching a source to a ml primary key creates lineage between the feature
        # and the upstream dataset. This is how lineage between your data warehouse
        # and machine learning ecosystem is established.
        sources=[dataset_urn],
        dataType="TEXT",
    ),
)

# Emit metadata!
emitter.emit(metadata_change_proposal)

```

Note that when creating a primary key, you create upstream lineage to the data warehouse using `sources`.

</TabItem>
</Tabs>

### Create MlFeatureTable

A feature table represents a group of similar Features that can all be used together to train a model. For example, if there was a Users Feature Table, it would contain documentation around how to use the Users collection of Features and references to each Feature and ML Primary Key contained within it.

<Tabs>
<TabItem value="python" label="Python" default>

```python
# Inlined from /metadata-ingestion/examples/library/create_mlfeature_table.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server="http://localhost:8080", extra_headers={})

feature_table_urn = builder.make_ml_feature_table_urn(
    feature_table_name="users_feature_table", platform="feast"
)

feature_urns = [
    builder.make_ml_feature_urn(
        feature_name="user_signup_date", feature_table_name="users_feature_table"
    ),
    builder.make_ml_feature_urn(
        feature_name="user_last_active_date", feature_table_name="users_feature_table"
    ),
]

primary_key_urns = [
    builder.make_ml_primary_key_urn(
        feature_table_name="users_feature_table",
        primary_key_name="user_id",
    )
]

feature_table_properties = models.MLFeatureTablePropertiesClass(
    description="Test description",
    # link your features to a feature table
    mlFeatures=feature_urns,
    # link your primary keys to the feature table
    mlPrimaryKeys=primary_key_urns,
)

# MCP creation
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlFeatureTable",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=feature_table_urn,
    aspect=feature_table_properties,
)

# Emit metadata!
emitter.emit(metadata_change_proposal)

```

Note that when creating a feature table, you connect the table to its features and primary key using `mlFeatures` and `mlPrimaryKeys`.

</TabItem>
</Tabs>

### Create MlModel

An ML Model in Acryl represents an individual version of a trained Machine Learning Model. Another way to think about the ML Model entity is as an istance of a training run. An ML Model entity tracks the exact ML Features used in that instance of training, along with the training results. This entity does not represents all versions of a ML Model. For example, if we train a model for homepage customization on a certain day, that would be a ML Model in DataHub. If you re-train the model the next day off of new data or with different parameters, that would produce a second ML Model entity.

<Tabs>
<TabItem value="python" label="Python" default>

```python
# Inlined from /metadata-ingestion/examples/library/create_mlmodel.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server="http://localhost:8080", extra_headers={})
model_urn = builder.make_ml_model_urn(
    model_name="my-recommendations-model-run-1", platform="science", env="PROD"
)
model_group_urns = [
    builder.make_ml_model_group_urn(
        group_name="my-recommendations-model-group", platform="science", env="PROD"
    )
]
feature_urns = [
    builder.make_ml_feature_urn(
        feature_name="user_signup_date", feature_table_name="users_feature_table"
    ),
    builder.make_ml_feature_urn(
        feature_name="user_last_active_date", feature_table_name="users_feature_table"
    ),
]

metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlModel",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=model_urn,
    aspectName="mlModelProperties",
    aspect=models.MLModelPropertiesClass(
        description="my feature",
        groups=model_group_urns,
        mlFeatures=feature_urns,
        trainingMetrics=[
            models.MLMetricClass(
                name="accuracy", description="accuracy of the model", value="1.0"
            )
        ],
        hyperParams=[
            models.MLHyperParamClass(
                name="hyper_1", description="hyper_1", value="0.102"
            )
        ],
    ),
)

# Emit metadata!
emitter.emit(metadata_change_proposal)

```

Note that when creating a model, you link it to a list of features using `mlFeatures`. This indicates how the individual instance of the model was trained.
Additionally, you can access the relationship to model groups with `groups`. An ML Model is connected to the warehouse tables it depends on via its dependency on the ML Features it reads from.

</TabItem>
</Tabs>

### Create MlModelGroup

An ML Model Group represents the grouping of all training runs of a single Machine Learning model category. It will store documentation about the group of ML Models, along with references to each individual ML Model instance.

<Tabs>
<TabItem value="python" label="Python" default>

```python
# Inlined from /metadata-ingestion/examples/library/create_mlmodel_group.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server="http://localhost:8080", extra_headers={})
model_group_urn = builder.make_ml_model_group_urn(
    group_name="my-recommendations-model-group", platform="science", env="PROD"
)


metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlModelGroup",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=model_group_urn,
    aspectName="mlModelGroupProperties",
    aspect=models.MLModelGroupPropertiesClass(
        description="Grouping of ml model training runs related to home page recommendations.",
    ),
)


# Emit metadata!
emitter.emit(metadata_change_proposal)

```

</TabItem>
</Tabs>

### Expected Outcome of creating entities

You can search the entities in DataHub UI.

<p align="center">
  <img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/apis/tutorials/feature-table-created.png"/>
</p>

<p align="center">
  <img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/apis/tutorials/model-group-created.png"/>
</p>

## Read ML Entities

### Read MLFeature

<Tabs>
<TabItem value="graphql" label="GraphQL" default>

```json
query {
  mlFeature(urn: "urn:li:mlFeature:(test_feature_table_all_feature_dtypes,test_BOOL_LIST_feature)"){
    name
    featureNamespace
    description
    properties {
      description
      dataType
      version {
        versionTag
      }
    }
  }
}
```

Expected response:

```json
{
  "data": {
    "mlFeature": {
      "name": "test_BOOL_LIST_feature",
      "featureNamespace": "test_feature_table_all_feature_dtypes",
      "description": null,
      "properties": {
        "description": null,
        "dataType": "SEQUENCE",
        "version": null
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="curl" label="Curl" default>

```json
curl --location --request POST 'http://localhost:8080/api/graphql' \
--header 'Authorization: Bearer <my-access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "{ mlFeature(urn: \"urn:li:mlFeature:(test_feature_table_all_feature_dtypes,test_BOOL_LIST_feature)\") { name featureNamespace description properties { description dataType version { versionTag } } } }"
}'
```

Expected response:

```json
{
  "data": {
    "mlFeature": {
      "name": "test_BOOL_LIST_feature",
      "featureNamespace": "test_feature_table_all_feature_dtypes",
      "description": null,
      "properties": {
        "description": null,
        "dataType": "SEQUENCE",
        "version": null
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/read_mlfeature.py
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

# Imports for metadata model classes
from datahub.metadata.schema_classes import MLFeaturePropertiesClass

# First we get the current owners
gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

urn = "urn:li:mlFeature:(test_feature_table_all_feature_dtypes,test_BOOL_feature)"
result = graph.get_aspect(entity_urn=urn, aspect_type=MLFeaturePropertiesClass)

print(result)

```

</TabItem>
</Tabs>

### Read MlPrimaryKey

<Tabs>
<TabItem value="graphql" label="GraphQL" default>

```json
query {
  mlPrimaryKey(urn: "urn:li:mlPrimaryKey:(user_features,user_id)"){
    name
    featureNamespace
    description
    dataType
    properties {
      description
      dataType
      version {
        versionTag
      }
    }
  }
}
```

Expected response:

```json
{
  "data": {
    "mlPrimaryKey": {
      "name": "user_id",
      "featureNamespace": "user_features",
      "description": "User's internal ID",
      "dataType": "ORDINAL",
      "properties": {
        "description": "User's internal ID",
        "dataType": "ORDINAL",
        "version": null
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="curl" label="Curl" default>

```json
curl --location --request POST 'http://localhost:8080/api/graphql' \
--header 'Authorization: Bearer <my-access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "query {  mlPrimaryKey(urn: \"urn:li:mlPrimaryKey:(user_features,user_id)\"){    name    featureNamespace    description    dataType    properties {      description      dataType      version {        versionTag      }    }  }}"
}'
```

Expected response:

```json
{
  "data": {
    "mlPrimaryKey": {
      "name": "user_id",
      "featureNamespace": "user_features",
      "description": "User's internal ID",
      "dataType": "ORDINAL",
      "properties": {
        "description": "User's internal ID",
        "dataType": "ORDINAL",
        "version": null
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/read_mlprimarykey.py
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

# Imports for metadata model classes
from datahub.metadata.schema_classes import MLPrimaryKeyPropertiesClass

# First we get the current owners
gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

urn = "urn:li:mlPrimaryKey:(user_features,user_id)"
result = graph.get_aspect(entity_urn=urn, aspect_type=MLPrimaryKeyPropertiesClass)
print(result)

```

</TabItem>
</Tabs>

### Read MLFeatureTable

<Tabs>
<TabItem value="graphql" label="GraphQL" default>

```json
query {
  mlFeatureTable(urn: "urn:li:mlFeatureTable:(urn:li:dataPlatform:feast,test_feature_table_all_feature_dtypes)"){
    name
    description
    platform {
      name
    }
    properties {
      description
      mlFeatures {
        name
      }
    }
  }
}
```

Expected Response:

```json
{
  "data": {
    "mlFeatureTable": {
      "name": "test_feature_table_all_feature_dtypes",
      "description": null,
      "platform": {
        "name": "feast"
      },
      "properties": {
        "description": null,
        "mlFeatures": [
          {
            "name": "test_BOOL_LIST_feature"
          },
          ...{
            "name": "test_STRING_feature"
          }
        ]
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="curl" label="Curl">

```json
curl --location --request POST 'http://localhost:8080/api/graphql' \
--header 'Authorization: Bearer <my-access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "{ mlFeatureTable(urn: \"urn:li:mlFeatureTable:(urn:li:dataPlatform:feast,test_feature_table_all_feature_dtypes)\") { name description platform { name } properties { description mlFeatures { name } } } }"
}'
```

Expected Response:

```json
{
  "data": {
    "mlFeatureTable": {
      "name": "test_feature_table_all_feature_dtypes",
      "description": null,
      "platform": {
        "name": "feast"
      },
      "properties": {
        "description": null,
        "mlFeatures": [
          {
            "name": "test_BOOL_LIST_feature"
          },
          ...{
            "name": "test_STRING_feature"
          }
        ]
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/read_mlfeature_table.py
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

# Imports for metadata model classes
from datahub.metadata.schema_classes import MLFeatureTablePropertiesClass

# First we get the current owners
gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

urn = "urn:li:mlFeatureTable:(urn:li:dataPlatform:feast,test_feature_table_all_feature_dtypes)"
result = graph.get_aspect(entity_urn=urn, aspect_type=MLFeatureTablePropertiesClass)

print(result)

```

</TabItem>
</Tabs>

### Read MLModel

<Tabs>
<TabItem value="graphql" label="GraphQL" default>

```json
query {
  mlModel(urn: "urn:li:mlModel:(urn:li:dataPlatform:science,scienceModel,PROD)"){
    name
    description
    properties {
      description
      version
      type
      mlFeatures
      groups {
        urn
        name
      }
    }
  }
}
```

Expected Response:

```json
{
  "data": {
    "mlModel": {
      "name": "scienceModel",
      "description": "A sample model for predicting some outcome.",
      "properties": {
        "description": "A sample model for predicting some outcome.",
        "version": null,
        "type": "Naive Bayes classifier",
        "mlFeatures": null,
        "groups": []
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="curl" label="Curl" default>

```json
curl --location --request POST 'http://localhost:8080/api/graphql' \
--header 'Authorization: Bearer <my-access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "{ mlModel(urn: \"urn:li:mlModel:(urn:li:dataPlatform:science,scienceModel,PROD)\") { name description properties { description version type mlFeatures groups { urn name } } } }"
}'
```

Expected Response:

```json
{
  "data": {
    "mlModel": {
      "name": "scienceModel",
      "description": "A sample model for predicting some outcome.",
      "properties": {
        "description": "A sample model for predicting some outcome.",
        "version": null,
        "type": "Naive Bayes classifier",
        "mlFeatures": null,
        "groups": []
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/read_mlmodel.py
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

# Imports for metadata model classes
from datahub.metadata.schema_classes import MLModelPropertiesClass

# First we get the current owners
gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

urn = "urn:li:mlModel:(urn:li:dataPlatform:science,scienceModel,PROD)"
result = graph.get_aspect(entity_urn=urn, aspect_type=MLModelPropertiesClass)

print(result)

```

</TabItem>
</Tabs>

### Read MLModelGroup

<Tabs>
<TabItem value="graphql" label="GraphQL" default>

```json
query {
  mlModelGroup(urn: "urn:li:mlModelGroup:(urn:li:dataPlatform:science,my-model-group,PROD)"){
    name
    description
    platform {
      name
    }
    properties {
      description
    }
  }
}
```

Expected Response: (Note that this entity does not exist in the sample ingestion and you might want to create this entity first.)

```json
{
  "data": {
    "mlModelGroup": {
      "name": "my-model-group",
      "description": "my model group",
      "platform": {
        "name": "science"
      },
      "properties": {
        "description": "my model group"
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="curl" label="Curl">

```json
curl --location --request POST 'http://localhost:8080/api/graphql' \
--header 'Authorization: Bearer <my-access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "{ mlModelGroup(urn: \"urn:li:mlModelGroup:(urn:li:dataPlatform:science,my-model-group,PROD)\") { name description platform { name } properties { description } } }"
}'
```

Expected Response: (Note that this entity does not exist in the sample ingestion and you might want to create this entity first.)

```json
{
  "data": {
    "mlModelGroup": {
      "name": "my-model-group",
      "description": "my model group",
      "platform": {
        "name": "science"
      },
      "properties": {
        "description": "my model group"
      }
    }
  },
  "extensions": {}
}
```

</TabItem>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/read_mlmodel_group.py
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

# Imports for metadata model classes
from datahub.metadata.schema_classes import MLModelGroupPropertiesClass

# First we get the current owners
gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

urn = "urn:li:mlModelGroup:(urn:li:dataPlatform:science,my-model-group,PROD)"
result = graph.get_aspect(entity_urn=urn, aspect_type=MLModelGroupPropertiesClass)

print(result)

```

</TabItem>
</Tabs>

## Add ML Entities

### Add MlFeature to MlFeatureTable

<Tabs>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/add_mlfeature_to_mlfeature_table.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph
from datahub.metadata.schema_classes import MLFeatureTablePropertiesClass

gms_endpoint = "http://localhost:8080"
# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server=gms_endpoint, extra_headers={})

feature_table_urn = builder.make_ml_feature_table_urn(
    feature_table_name="my-feature-table", platform="feast"
)
feature_urns = [
    builder.make_ml_feature_urn(
        feature_name="my-feature2", feature_table_name="my-feature-table"
    ),
]

# This code concatenates the new features with the existing features in the feature table.
# If you want to replace all existing features with only the new ones, you can comment out this line.
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))
feature_table_properties = graph.get_aspect(
    entity_urn=feature_table_urn, aspect_type=MLFeatureTablePropertiesClass
)
if feature_table_properties:
    current_features = feature_table_properties.mlFeatures
    print("current_features:", current_features)
    if current_features:
        feature_urns += current_features

feature_table_properties = models.MLFeatureTablePropertiesClass(mlFeatures=feature_urns)
# MCP createion
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlFeatureTable",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=feature_table_urn,
    aspect=feature_table_properties,
)

# Emit metadata! This is a blocking call
emitter.emit(metadata_change_proposal)

```

</TabItem>
</Tabs>

### Add MlFeature to MLModel

<Tabs>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/add_mlfeature_to_mlmodel.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph
from datahub.metadata.schema_classes import MLModelPropertiesClass

gms_endpoint = "http://localhost:8080"
# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server=gms_endpoint, extra_headers={})

model_urn = builder.make_ml_model_urn(
    model_name="my-test-model", platform="science", env="PROD"
)
feature_urns = [
    builder.make_ml_feature_urn(
        feature_name="my-feature3", feature_table_name="my-feature-table"
    ),
]

# This code concatenates the new features with the existing features in the model
# If you want to replace all existing features with only the new ones, you can comment out this line.
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))
model_properties = graph.get_aspect(
    entity_urn=model_urn, aspect_type=MLModelPropertiesClass
)
if model_properties:
    current_features = model_properties.mlFeatures
    print("current_features:", current_features)
    if current_features:
        feature_urns += current_features

model_properties = models.MLModelPropertiesClass(mlFeatures=feature_urns)

# MCP creation
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlModel",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=model_urn,
    aspect=model_properties,
)

# Emit metadata!
emitter.emit(metadata_change_proposal)

```

</TabItem>
</Tabs>

### Add MLGroup To MLModel

<Tabs>
<TabItem value="python" label="Python">

```python
# Inlined from /metadata-ingestion/examples/library/add_mlgroup_to_mlmodel.py
import datahub.emitter.mce_builder as builder
import datahub.metadata.schema_classes as models
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

gms_endpoint = "http://localhost:8080"
# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(gms_server=gms_endpoint, extra_headers={})

model_group_urns = [
    builder.make_ml_model_group_urn(
        group_name="my-model-group", platform="science", env="PROD"
    )
]
model_urn = builder.make_ml_model_urn(
    model_name="science-model", platform="science", env="PROD"
)

# This code concatenates the new features with the existing features in the feature table.
# If you want to replace all existing features with only the new ones, you can comment out this line.
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

target_model_properties = graph.get_aspect(
    entity_urn=model_urn, aspect_type=models.MLModelPropertiesClass
)
if target_model_properties:
    current_model_groups = target_model_properties.groups
    print("current_model_groups:", current_model_groups)
    if current_model_groups:
        model_group_urns += current_model_groups

model_properties = models.MLModelPropertiesClass(groups=model_group_urns)
# MCP createion
metadata_change_proposal = MetadataChangeProposalWrapper(
    entityType="mlModel",
    changeType=models.ChangeTypeClass.UPSERT,
    entityUrn=model_urn,
    aspect=model_properties,
)

# Emit metadata! This is a blocking call
emitter.emit(metadata_change_proposal)

```

</TabItem>
</Tabs>

### Expected Outcome of Adding ML Entities

You can access to `Features` or `Group` Tab of each entity to view the added entities.

<p align="center">
  <img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/apis/tutorials/feature-added-to-model.png"/>
</p>

<p align="center">
  <img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/apis/tutorials/model-group-added-to-model.png"/>
</p>
