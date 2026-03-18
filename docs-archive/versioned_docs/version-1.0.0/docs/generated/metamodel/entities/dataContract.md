---
sidebar_position: 36
title: DataContract
slug: /generated/metamodel/entities/datacontract
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/metamodel/entities/dataContract.md
---
# DataContract
## Aspects

### dataContractProperties
Information about a data contract
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "dataContractProperties"
  },
  "name": "DataContractProperties",
  "namespace": "com.linkedin.datacontract",
  "fields": [
    {
      "Relationship": {
        "entityTypes": [
          "dataset"
        ],
        "name": "ContractFor"
      },
      "java": {
        "class": "com.linkedin.common.urn.Urn"
      },
      "type": "string",
      "name": "entity",
      "doc": "The entity that this contract is associated with. Currently, we only support Dataset contracts, but\nin the future we may also support Data Product level contracts."
    },
    {
      "Relationship": {
        "/*/assertion": {
          "entityTypes": [
            "assertion"
          ],
          "name": "IncludesSchemaAssertion"
        }
      },
      "type": [
        "null",
        {
          "type": "array",
          "items": {
            "type": "record",
            "name": "SchemaContract",
            "namespace": "com.linkedin.datacontract",
            "fields": [
              {
                "Relationship": {
                  "entityTypes": [
                    "assertion"
                  ],
                  "name": "IncludesSchemaAssertion"
                },
                "java": {
                  "class": "com.linkedin.common.urn.Urn"
                },
                "type": "string",
                "name": "assertion",
                "doc": "The assertion representing the schema contract."
              }
            ],
            "doc": "Expectations for a logical schema"
          }
        }
      ],
      "name": "schema",
      "default": null,
      "doc": "An optional set of schema contracts. If this is a dataset contract, there will only be one."
    },
    {
      "Relationship": {
        "/*/assertion": {
          "entityTypes": [
            "assertion"
          ],
          "name": "IncludesFreshnessAssertion"
        }
      },
      "type": [
        "null",
        {
          "type": "array",
          "items": {
            "type": "record",
            "name": "FreshnessContract",
            "namespace": "com.linkedin.datacontract",
            "fields": [
              {
                "java": {
                  "class": "com.linkedin.common.urn.Urn"
                },
                "type": "string",
                "name": "assertion",
                "doc": "The assertion representing the SLA contract."
              }
            ],
            "doc": "A contract pertaining to the operational SLAs of a physical data asset"
          }
        }
      ],
      "name": "freshness",
      "default": null,
      "doc": "An optional set of FRESHNESS contracts. If this is a dataset contract, there will only be one."
    },
    {
      "Relationship": {
        "/*/assertion": {
          "entityTypes": [
            "assertion"
          ],
          "name": "IncludesDataQualityAssertion"
        }
      },
      "type": [
        "null",
        {
          "type": "array",
          "items": {
            "type": "record",
            "name": "DataQualityContract",
            "namespace": "com.linkedin.datacontract",
            "fields": [
              {
                "Relationship": {
                  "entityTypes": [
                    "assertion"
                  ],
                  "name": "IncludesDataQualityAssertion"
                },
                "java": {
                  "class": "com.linkedin.common.urn.Urn"
                },
                "type": "string",
                "name": "assertion",
                "doc": "The assertion representing the Data Quality contract.\nE.g. a table or column-level assertion."
              }
            ],
            "doc": "A data quality contract pertaining to a physical data asset\nData Quality contracts are used to make assertions about data quality metrics for a physical data asset"
          }
        }
      ],
      "name": "dataQuality",
      "default": null,
      "doc": "An optional set of Data Quality contracts, e.g. table and column level contract constraints."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "rawContract",
      "default": null,
      "doc": "YAML-formatted contract definition"
    }
  ],
  "doc": "Information about a data contract"
}
```
</details>

### dataContractStatus
Information about the status of a data contract
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "dataContractStatus"
  },
  "name": "DataContractStatus",
  "namespace": "com.linkedin.datacontract",
  "fields": [
    {
      "Searchable": {
        "/*": {
          "fieldType": "TEXT",
          "queryByDefault": true
        }
      },
      "type": {
        "type": "map",
        "values": "string"
      },
      "name": "customProperties",
      "default": {},
      "doc": "Custom property bag."
    },
    {
      "Searchable": {},
      "type": {
        "type": "enum",
        "symbolDocs": {
          "ACTIVE": "The data contract is active.",
          "PENDING": "The data contract is pending implementation."
        },
        "name": "DataContractState",
        "namespace": "com.linkedin.datacontract",
        "symbols": [
          "ACTIVE",
          "PENDING"
        ]
      },
      "name": "state",
      "doc": "The latest state of the data contract"
    }
  ],
  "doc": "Information about the status of a data contract"
}
```
</details>

### status
The lifecycle status metadata of an entity, e.g. dataset, metric, feature, etc.
This aspect is used to represent soft deletes conventionally.
<details>
<summary>Schema</summary>

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "status"
  },
  "name": "Status",
  "namespace": "com.linkedin.common",
  "fields": [
    {
      "Searchable": {
        "fieldType": "BOOLEAN"
      },
      "type": "boolean",
      "name": "removed",
      "default": false,
      "doc": "Whether the entity has been removed (soft-deleted)."
    }
  ],
  "doc": "The lifecycle status metadata of an entity, e.g. dataset, metric, feature, etc.\nThis aspect is used to represent soft deletes conventionally."
}
```
</details>

## Relationships

### Outgoing
These are the relationships stored in this entity's aspects
- ContractFor

   - Dataset via `dataContractProperties.entity`
- IncludesSchemaAssertion

   - Assertion via `dataContractProperties.schema`
   - Assertion via `dataContractProperties.schema.assertion`
- IncludesFreshnessAssertion

   - Assertion via `dataContractProperties.freshness`
- IncludesDataQualityAssertion

   - Assertion via `dataContractProperties.dataQuality`
   - Assertion via `dataContractProperties.dataQuality.assertion`
## [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
