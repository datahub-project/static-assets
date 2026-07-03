---
sidebar_position: 39
title: DataType
slug: /generated/metamodel/entities/datatype
custom_edit_url: null
---
# DataType
A type of data element stored within DataHub.
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Technical Reference Guide

The sections above provide an overview of how to use this entity. The following sections provide detailed technical information about how metadata is stored and represented in DataHub.

**Aspects** are the individual pieces of metadata that can be attached to an entity. Each aspect contains specific information (like ownership, tags, or properties) and is stored as a separate record, allowing for flexible and incremental metadata updates.

**Relationships** show how this entity connects to other entities in the metadata graph. These connections are derived from the fields within each aspect and form the foundation of DataHub's knowledge graph.

### Reading the Field Tables

Each aspect's field table includes an **Annotations** column that provides additional metadata about how fields are used:

- **⚠️ Deprecated**: This field is deprecated and may be removed in a future version. Check the description for the recommended alternative
- **Searchable**: This field is indexed and can be searched in DataHub's search interface
- **Searchable (fieldname)**: When the field name in parentheses is shown, it indicates the field is indexed under a different name in the search index. For example, `dashboardTool` is indexed as `tool`
- **→ RelationshipName**: This field creates a relationship to another entity. The arrow indicates this field contains a reference (URN) to another entity, and the name indicates the type of relationship (e.g., `→ Contains`, `→ OwnedBy`)

Fields with complex types (like `Edge`, `AuditStamp`) link to their definitions in the [Common Types](#common-types) section below.

### Aspects

#### dataTypeInfo
None

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| qualifiedName | string | ✓ | The qualified name for the data type. Usually a unique namespace + name, e.g. datahub.string | Searchable |
| displayName | string |  | An optional display name for the data type. |  |
| description | string |  | An optional description for the data type. |  |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "dataTypeInfo"
  },
  "name": "DataTypeInfo",
  "namespace": "com.linkedin.datatype",
  "fields": [
    {
      "Searchable": {
        "fieldType": "KEYWORD",
        "searchLabel": "qualifiedName",
        "searchTier": 1
      },
      "type": "string",
      "name": "qualifiedName",
      "doc": "The qualified name for the data type. Usually a unique namespace + name, e.g. datahub.string"
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "displayName",
      "default": null,
      "doc": "An optional display name for the data type."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "description",
      "default": null,
      "doc": "An optional description for the data type."
    }
  ]
}
```

</TabItem>
</Tabs>


#### institutionalMemory
Institutional memory of an entity. This is a way to link to relevant documentation and provide description of the documentation. Institutional or tribal knowledge is very important for users to leverage the entity.

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| elements | InstitutionalMemoryMetadata[] | ✓ | List of records that represent institutional memory of an entity. Each record consists of a link,... |  |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "institutionalMemory"
  },
  "name": "InstitutionalMemory",
  "namespace": "com.linkedin.common",
  "fields": [
    {
      "type": {
        "type": "array",
        "items": {
          "type": "record",
          "name": "InstitutionalMemoryMetadata",
          "namespace": "com.linkedin.common",
          "fields": [
            {
              "java": {
                "class": "com.linkedin.common.url.Url",
                "coercerClass": "com.linkedin.common.url.UrlCoercer"
              },
              "type": "string",
              "name": "url",
              "doc": "Link to an engineering design document or a wiki page."
            },
            {
              "type": "string",
              "name": "description",
              "doc": "Description of the link."
            },
            {
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
              "name": "createStamp",
              "doc": "Audit stamp associated with creation of this record"
            },
            {
              "type": [
                "null",
                "com.linkedin.common.AuditStamp"
              ],
              "name": "updateStamp",
              "default": null,
              "doc": "Audit stamp associated with updation of this record"
            },
            {
              "type": [
                "null",
                {
                  "type": "record",
                  "name": "InstitutionalMemoryMetadataSettings",
                  "namespace": "com.linkedin.common",
                  "fields": [
                    {
                      "type": "boolean",
                      "name": "showInAssetPreview",
                      "default": false,
                      "doc": "Show record in asset preview like on entity header and search previews"
                    }
                  ],
                  "doc": "Settings related to a record of InstitutionalMemoryMetadata"
                }
              ],
              "name": "settings",
              "default": null,
              "doc": "Settings for this record"
            }
          ],
          "doc": "Metadata corresponding to a record of institutional memory."
        }
      },
      "name": "elements",
      "doc": "List of records that represent institutional memory of an entity. Each record consists of a link, description, creator and timestamps associated with that record."
    }
  ],
  "doc": "Institutional memory of an entity. This is a way to link to relevant documentation and provide description of the documentation. Institutional or tribal knowledge is very important for users to leverage the entity."
}
```

</TabItem>
</Tabs>


#### status
The lifecycle status metadata of an entity, e.g. dataset, metric, feature, etc.
This aspect is used to represent soft deletes conventionally.

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| removed | boolean | ✓ | Whether the entity has been removed (soft-deleted). | Searchable |

</TabItem>
<TabItem value="raw" label="Raw Schema">

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

</TabItem>
</Tabs>


### Relationships

### [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)


:::note 💡 **Contributing to this documentation**
This page is auto-generated from the underlying source code. To make changes, please edit the relevant source files in the [metadata-models](https://github.com/datahub-project/datahub/tree/master/metadata-models) directory. 

**Tip:** For quick typo fixes or documentation updates, you can click the ✏️ **Edit** icon directly in the GitHub UI to open a Pull Request. For larger changes and PR naming conventions, please refer to our [Contributing Guide](/docs/contributing).
:::
