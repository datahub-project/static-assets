---
sidebar_position: 56
title: DataHubOpenAPISchema
slug: /generated/metamodel/entities/datahubopenapischema
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/metamodel/entities/dataHubOpenAPISchema.md
---
# DataHubOpenAPISchema
Contains aspects which are used in OpenAPI requests/responses which are not otherwise present in the data model.
## Aspects

### systemMetadata
Metadata associated with each metadata change that is processed by the system
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "systemMetadata"
  },
  "name": "SystemMetadata",
  "namespace": "com.linkedin.mxe",
  "fields": [
    {
      "type": [
        "long",
        "null"
      ],
      "name": "lastObserved",
      "default": 0,
      "doc": "The timestamp the metadata was observed at"
    },
    {
      "type": [
        "string",
        "null"
      ],
      "name": "runId",
      "default": "no-run-id-provided",
      "doc": "The original run id that produced the metadata. Populated in case of batch-ingestion."
    },
    {
      "type": [
        "string",
        "null"
      ],
      "name": "lastRunId",
      "default": "no-run-id-provided",
      "doc": "The last run id that produced the metadata. Populated in case of batch-ingestion."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "pipelineName",
      "default": null,
      "doc": "The ingestion pipeline id that produced the metadata. Populated in case of batch ingestion."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "registryName",
      "default": null,
      "doc": "The model registry name that was used to process this event"
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "registryVersion",
      "default": null,
      "doc": "The model registry version that was used to process this event"
    },
    {
      "type": [
        "null",
        {
          "type": "map",
          "values": "string"
        }
      ],
      "name": "properties",
      "default": null,
      "doc": "Additional properties"
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "version",
      "default": null,
      "doc": "Aspect version\n   Initial implementation will use the aspect version's number, however stored as\n   a string in the case where a different aspect versioning scheme is later adopted."
    }
  ],
  "doc": "Metadata associated with each metadata change that is processed by the system"
}
```
</details>

## Relationships

## [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
