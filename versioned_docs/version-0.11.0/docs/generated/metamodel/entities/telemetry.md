---
sidebar_position: 40
title: Telemetry
slug: /generated/metamodel/entities/telemetry
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/metamodel/entities/telemetry.md
---
# Telemetry
## Aspects

### telemetryClientId
A simple wrapper around a String to persist the client ID for telemetry in DataHub's backend DB
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "telemetryClientId"
  },
  "name": "TelemetryClientId",
  "namespace": "com.linkedin.telemetry",
  "fields": [
    {
      "type": "string",
      "name": "clientId",
      "doc": "A string representing the telemetry client ID"
    }
  ],
  "doc": "A simple wrapper around a String to persist the client ID for telemetry in DataHub's backend DB"
}
```
</details>

## Relationships

## [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
