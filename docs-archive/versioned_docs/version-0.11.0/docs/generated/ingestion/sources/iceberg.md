---
sidebar_position: 20
title: Iceberg
slug: /generated/ingestion/sources/iceberg
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/iceberg.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Iceberg
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ✅ | Optionally enabled via configuration. |
| Descriptions | ✅ | Enabled by default. |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled via stateful ingestion |
| [Domains](../../../domains.md) | ❌ | Currently not supported. |
| Extract Ownership | ✅ | Optionally enabled via configuration by specifying which Iceberg table property holds user or group ownership. |
| Partition Support | ❌ | Currently not supported. |
| [Platform Instance](../../../platform-instances.md) | ✅ | Optionally enabled via configuration, an Iceberg instance represents the catalog name where the table is stored. |


## Integration Details

The DataHub Iceberg source plugin extracts metadata from [Iceberg tables](https://iceberg.apache.org/spec/) stored in a distributed or local file system.
Typically, Iceberg tables are stored in a distributed file system like S3 or Azure Data Lake Storage (ADLS) and registered in a catalog.  There are various catalog
implementations like Filesystem-based, RDBMS-based or even REST-based catalogs.  This Iceberg source plugin relies on the
[pyiceberg library](https://py.iceberg.apache.org/).


### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[iceberg]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: "iceberg"
  config:
    env: PROD
    catalog:
      name: my_iceberg_catalog
      type: rest
      # Catalog configuration follows pyiceberg's documentation (https://py.iceberg.apache.org/configuration)
      config:
        uri: http://localhost:8181
        s3.access-key-id: admin
        s3.secret-access-key: password
        s3.region: us-east-1
        warehouse: s3a://warehouse/wh/
        s3.endpoint: http://localhost:9000
    platform_instance: my_iceberg_catalog
    table_pattern:
      allow:
        - marketing.*
    profiling:
      enabled: true

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
| <div className="path-line"><span className="path-main">catalog</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">IcebergCatalogConfig</span></div> | Catalog configuration where to find Iceberg tables.  See [pyiceberg's catalog configuration details](https://py.iceberg.apache.org/configuration/).  |
| <div className="path-line"><span className="path-prefix">catalog.</span><span className="path-main">config</span>&nbsp;<abbr title="Required if catalog is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">catalog.</span><span className="path-main">type</span>&nbsp;<abbr title="Required if catalog is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Type of catalog.  See [PyIceberg](https://py.iceberg.apache.org/configuration/) for list of possible values.  |
| <div className="path-line"><span className="path-prefix">catalog.</span><span className="path-main">name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of catalog <div className="default-line default-line-with-docs">Default: <span className="default-value">default</span></div> |
| <div className="path-line"><span className="path-main">group_ownership_property</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Iceberg table property to look for a `CorpGroup` owner.  Can only hold a single group value.  If property has no value, no owner information will be emitted.  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">user_ownership_property</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Iceberg table property to look for a `CorpUser` owner.  Can only hold a single user value.  If property has no value, no owner information will be emitted. <div className="default-line default-line-with-docs">Default: <span className="default-value">owner</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">profiling</span></div> <div className="type-name-line"><span className="type-name">IcebergProfilingConfig</span></div> |  <div className="default-line ">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: False, &#x27;include&#95;field&#95;null&#95;count&#x27;: Tru...</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether profiling should be done. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_max_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the max value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_min_value</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the min value of numeric columns. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">include_field_null_count</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to profile for the number of nulls for each column. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.</span><span className="path-main">operation_config</span></div> <div className="type-name-line"><span className="type-name">OperationConfig</span></div> | Experimental feature. To specify operation configs.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">lower_freq_profile_enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_date_of_month</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-prefix">profiling.operation_config.</span><span className="path-main">profile_day_of_week</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.  |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Iceberg Stateful Ingestion Config.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | The type of the ingestion state provider registered with datahub. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "IcebergSourceConfig",
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
      "description": "The instance of the platform that all assets produced by this recipe belong to",
      "type": "string"
    },
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Iceberg Stateful Ingestion Config.",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
        }
      ]
    },
    "catalog": {
      "title": "Catalog",
      "description": "Catalog configuration where to find Iceberg tables.  See [pyiceberg's catalog configuration details](https://py.iceberg.apache.org/configuration/).",
      "allOf": [
        {
          "$ref": "#/definitions/IcebergCatalogConfig"
        }
      ]
    },
    "table_pattern": {
      "title": "Table Pattern",
      "description": "Regex patterns for tables to filter in ingestion.",
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
    "user_ownership_property": {
      "title": "User Ownership Property",
      "description": "Iceberg table property to look for a `CorpUser` owner.  Can only hold a single user value.  If property has no value, no owner information will be emitted.",
      "default": "owner",
      "type": "string"
    },
    "group_ownership_property": {
      "title": "Group Ownership Property",
      "description": "Iceberg table property to look for a `CorpGroup` owner.  Can only hold a single group value.  If property has no value, no owner information will be emitted.",
      "type": "string"
    },
    "profiling": {
      "title": "Profiling",
      "default": {
        "enabled": false,
        "include_field_null_count": true,
        "include_field_min_value": true,
        "include_field_max_value": true,
        "operation_config": {
          "lower_freq_profile_enabled": false,
          "profile_day_of_week": null,
          "profile_date_of_month": null
        }
      },
      "allOf": [
        {
          "$ref": "#/definitions/IcebergProfilingConfig"
        }
      ]
    }
  },
  "required": [
    "catalog"
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
          "description": "The configuration required for initializing the state provider. Default: The datahub_api config if set at pipeline level. Otherwise, the default DatahubClientConfig. See the defaults (https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/graph/client.py#L19)."
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
          "description": "The type of the ingestion state provider registered with datahub.",
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
    "IcebergCatalogConfig": {
      "title": "IcebergCatalogConfig",
      "description": "Iceberg catalog config.\n\nhttps://py.iceberg.apache.org/configuration/",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "description": "Name of catalog",
          "default": "default",
          "type": "string"
        },
        "type": {
          "title": "Type",
          "description": "Type of catalog.  See [PyIceberg](https://py.iceberg.apache.org/configuration/) for list of possible values.",
          "type": "string"
        },
        "config": {
          "title": "Config",
          "description": "Catalog specific configuration.  See [PyIceberg documentation](https://py.iceberg.apache.org/configuration/) for details.",
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        }
      },
      "required": [
        "type",
        "config"
      ],
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
    "OperationConfig": {
      "title": "OperationConfig",
      "type": "object",
      "properties": {
        "lower_freq_profile_enabled": {
          "title": "Lower Freq Profile Enabled",
          "description": "Whether to do profiling at lower freq or not. This does not do any scheduling just adds additional checks to when not to run profiling.",
          "default": false,
          "type": "boolean"
        },
        "profile_day_of_week": {
          "title": "Profile Day Of Week",
          "description": "Number between 0 to 6 for day of week (both inclusive). 0 is Monday and 6 is Sunday. If not specified, defaults to Nothing and this field does not take affect.",
          "type": "integer"
        },
        "profile_date_of_month": {
          "title": "Profile Date Of Month",
          "description": "Number between 1 to 31 for date of month (both inclusive). If not specified, defaults to Nothing and this field does not take affect.",
          "type": "integer"
        }
      },
      "additionalProperties": false
    },
    "IcebergProfilingConfig": {
      "title": "IcebergProfilingConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether profiling should be done.",
          "default": false,
          "type": "boolean"
        },
        "include_field_null_count": {
          "title": "Include Field Null Count",
          "description": "Whether to profile for the number of nulls for each column.",
          "default": true,
          "type": "boolean"
        },
        "include_field_min_value": {
          "title": "Include Field Min Value",
          "description": "Whether to profile for the min value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "include_field_max_value": {
          "title": "Include Field Max Value",
          "description": "Whether to profile for the max value of numeric columns.",
          "default": true,
          "type": "boolean"
        },
        "operation_config": {
          "title": "Operation Config",
          "description": "Experimental feature. To specify operation configs.",
          "allOf": [
            {
              "$ref": "#/definitions/OperationConfig"
            }
          ]
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>

### Concept Mapping

<!-- This should be a manual mapping of concepts from the source to the DataHub Metadata Model -->
<!-- Authors should provide as much context as possible about how this mapping was generated, including assumptions made, known shortcuts, & any other caveats -->

This ingestion source maps the following Source System Concepts to DataHub Concepts:

<!-- Remove all unnecessary/irrelevant DataHub Concepts -->

| Source Concept | DataHub Concept | Notes |
| -- | -- | -- |
| `iceberg` | [Data Platform](docs/generated/metamodel/entities/dataPlatform.md) | |
| Table | [Dataset](docs/generated/metamodel/entities/dataset.md) | Each Iceberg table maps to a Dataset named using the parent folders.  If a table is stored under `my/namespace/table`, the dataset name will be `my.namespace.table`.  If a [Platform Instance](/docs/platform-instances/) is configured, it will be used as a prefix: `<platform_instance>.my.namespace.table`. |
| [Table property](https://iceberg.apache.org/docs/latest/configuration/#table-properties) | [User (a.k.a CorpUser)](docs/generated/metamodel/entities/corpuser.md) | The value of a table property can be used as the name of a CorpUser owner.  This table property name can be configured with the source option `user_ownership_property`. |
| [Table property](https://iceberg.apache.org/docs/latest/configuration/#table-properties) | CorpGroup | The value of a table property can be used as the name of a CorpGroup owner.  This table property name can be configured with the source option `group_ownership_property`. |
| Table parent folders (excluding [warehouse catalog location](https://iceberg.apache.org/docs/latest/configuration/#catalog-properties)) | Container | Available in a future release | 
| [Table schema](https://iceberg.apache.org/spec/#schemas-and-data-types) | SchemaField | Maps to the fields defined within the Iceberg table schema definition. | 

## Troubleshooting

### [Common Issue]

[Provide description of common issues with this integration and steps to resolve]

### Code Coordinates
- Class Name: `datahub.ingestion.source.iceberg.iceberg.IcebergSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/iceberg/iceberg.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Iceberg, feel free to ping us on [our Slack](https://slack.datahubproject.io).
