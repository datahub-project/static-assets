---
sidebar_position: 26
title: Incident
slug: /generated/metamodel/entities/incident
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/metamodel/entities/incident.md
---
# Incident
An incident for an asset.
## Aspects

### incidentInfo
Information about an incident raised on an asset.
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "incidentInfo"
  },
  "name": "IncidentInfo",
  "namespace": "com.linkedin.incident",
  "fields": [
    {
      "Searchable": {
        "addToFilters": true,
        "filterNameOverride": "Type"
      },
      "type": {
        "type": "enum",
        "symbolDocs": {
          "CUSTOM": "A custom type of incident",
          "OPERATIONAL": "A misc. operational incident, e.g. failure to materialize a dataset."
        },
        "name": "IncidentType",
        "namespace": "com.linkedin.incident",
        "symbols": [
          "OPERATIONAL",
          "CUSTOM"
        ],
        "doc": "A type of asset incident"
      },
      "name": "type",
      "doc": "The type of incident"
    },
    {
      "Searchable": {
        "addToFilters": true,
        "filterNameOverride": "Other Type"
      },
      "type": [
        "null",
        "string"
      ],
      "name": "customType",
      "default": null,
      "doc": "An optional custom incident type. Present only if type is 'CUSTOM'."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "title",
      "default": null,
      "doc": "Optional title associated with the incident"
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "description",
      "default": null,
      "doc": "Optional description associated with the incident"
    },
    {
      "Relationship": {
        "/*": {
          "entityTypes": [
            "dataset",
            "chart",
            "dashboard",
            "dataFlow",
            "dataJob",
            "schemaField"
          ],
          "name": "IncidentOn"
        }
      },
      "Searchable": {
        "/*": {
          "fieldType": "URN"
        }
      },
      "type": {
        "type": "array",
        "items": "string"
      },
      "name": "entities",
      "doc": "A reference to the entity associated with the incident."
    },
    {
      "Searchable": {
        "addToFilters": true,
        "filterNameOverride": "Priority"
      },
      "type": [
        "int",
        "null"
      ],
      "name": "priority",
      "default": 0,
      "doc": "A numeric severity or priority for the incident. On the UI we will translate this into something easy to understand."
    },
    {
      "type": {
        "type": "record",
        "name": "IncidentStatus",
        "namespace": "com.linkedin.incident",
        "fields": [
          {
            "Searchable": {
              "addToFilters": true,
              "filterNameOverride": "Status"
            },
            "type": {
              "type": "enum",
              "symbolDocs": {
                "ACTIVE": "The incident is ongoing, or active.",
                "RESOLVED": "The incident is resolved."
              },
              "name": "IncidentState",
              "namespace": "com.linkedin.incident",
              "symbols": [
                "ACTIVE",
                "RESOLVED"
              ]
            },
            "name": "state",
            "doc": "The state of the incident"
          },
          {
            "type": [
              "null",
              "string"
            ],
            "name": "message",
            "default": null,
            "doc": "Optional message associated with the incident"
          },
          {
            "Searchable": {
              "/time": {
                "fieldName": "lastUpdated",
                "fieldType": "COUNT"
              }
            },
            "type": {
              "type": "record",
              "name": "AuditStamp",
              "namespace": "com.linkedin.common",
              "fields": [
                {
                  "type": "long",
                  "name": "time",
                  "doc": "When did the resource/association/sub-resource move into the specific lifecycle stage represented by this AuditEvent."
                },
                {
                  "java": {
                    "class": "com.linkedin.common.urn.Urn"
                  },
                  "type": "string",
                  "name": "actor",
                  "doc": "The entity (e.g. a member URN) which will be credited for moving the resource/association/sub-resource into the specific lifecycle stage. It is also the one used to authorize the change."
                },
                {
                  "java": {
                    "class": "com.linkedin.common.urn.Urn"
                  },
                  "type": [
                    "null",
                    "string"
                  ],
                  "name": "impersonator",
                  "default": null,
                  "doc": "The entity (e.g. a service URN) which performs the change on behalf of the Actor and must be authorized to act as the Actor."
                },
                {
                  "type": [
                    "null",
                    "string"
                  ],
                  "name": "message",
                  "default": null,
                  "doc": "Additional context around how DataHub was informed of the particular change. For example: was the change created by an automated process, or manually."
                }
              ],
              "doc": "Data captured on a resource/association/sub-resource level giving insight into when that resource/association/sub-resource moved into a particular lifecycle stage, and who acted to move it into that specific lifecycle stage."
            },
            "name": "lastUpdated",
            "doc": "The time at which the request was initially created"
          }
        ],
        "doc": "Information about an incident raised on an asset"
      },
      "name": "status",
      "doc": "The current status of an incident, i.e. active or inactive."
    },
    {
      "type": [
        "null",
        {
          "type": "record",
          "Aspect": {
            "name": "incidentSource"
          },
          "name": "IncidentSource",
          "namespace": "com.linkedin.incident",
          "fields": [
            {
              "Searchable": {
                "addToFilters": true,
                "filterNameOverride": "Source"
              },
              "type": {
                "type": "enum",
                "symbolDocs": {
                  "MANUAL": "Manually created incident, via UI or API."
                },
                "name": "IncidentSourceType",
                "namespace": "com.linkedin.incident",
                "symbols": [
                  "MANUAL"
                ]
              },
              "name": "type",
              "doc": "Message associated with the incident"
            },
            {
              "Searchable": {
                "fieldType": "URN"
              },
              "java": {
                "class": "com.linkedin.common.urn.Urn"
              },
              "type": [
                "null",
                "string"
              ],
              "name": "sourceUrn",
              "default": null,
              "doc": "Reference to an URN related to the source of an incident."
            }
          ],
          "doc": "Information about the source of an incident raised on an asset."
        }
      ],
      "name": "source",
      "default": null,
      "doc": "The source of an incident, i.e. how it was generated."
    },
    {
      "Searchable": {
        "/time": {
          "fieldName": "created",
          "fieldType": "COUNT"
        }
      },
      "type": "com.linkedin.common.AuditStamp",
      "name": "created",
      "doc": "The time at which the request was initially created"
    }
  ],
  "doc": "Information about an incident raised on an asset."
}
```
</details>

## Relationships

### Outgoing
These are the relationships stored in this entity's aspects
- IncidentOn

   - Dataset via `incidentInfo.entities`
   - Chart via `incidentInfo.entities`
   - Dashboard via `incidentInfo.entities`
   - DataFlow via `incidentInfo.entities`
   - DataJob via `incidentInfo.entities`
   - SchemaField via `incidentInfo.entities`
### Incoming
These are the relationships stored in other entity's aspects
- ResolvedIncidents

   - Dataset via `incidentsSummary.resolvedIncidentDetails`
   - DataJob via `incidentsSummary.resolvedIncidentDetails`
   - DataFlow via `incidentsSummary.resolvedIncidentDetails`
   - Chart via `incidentsSummary.resolvedIncidentDetails`
   - Dashboard via `incidentsSummary.resolvedIncidentDetails`
- ActiveIncidents

   - Dataset via `incidentsSummary.activeIncidentDetails`
   - DataJob via `incidentsSummary.activeIncidentDetails`
   - DataFlow via `incidentsSummary.activeIncidentDetails`
   - Chart via `incidentsSummary.activeIncidentDetails`
   - Dashboard via `incidentsSummary.activeIncidentDetails`
## [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
