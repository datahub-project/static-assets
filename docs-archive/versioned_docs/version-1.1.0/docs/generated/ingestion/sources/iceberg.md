---
sidebar_position: 30
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
| Extract Ownership | ✅ | Automatically ingests ownership information from table properties based on `user_ownership_property` and `group_ownership_property` |
| Partition Support | ❌ | Currently not supported. |
| [Platform Instance](../../../platform-instances.md) | ✅ | Optionally enabled via configuration, an Iceberg instance represents the catalog name where the table is stored. |


## Integration Details

The DataHub Iceberg source plugin extracts metadata from [Iceberg tables](https://iceberg.apache.org/spec/) stored in a distributed or local file system.
Typically, Iceberg tables are stored in a distributed file system like S3 or Azure Data Lake Storage (ADLS) and registered in a catalog.  There are various catalog
implementations like Filesystem-based, RDBMS-based or even REST-based catalogs.  This Iceberg source plugin relies on the
[pyiceberg library](https://py.iceberg.apache.org/).


### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">catalog</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">map(str,object)</span></div> |   |
| <div className="path-line"><span className="path-main">group_ownership_property</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Iceberg table property to look for a `CorpGroup` owner.  Can only hold a single group value.  If property has no value, no owner information will be emitted.  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">processing_threads</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | How many threads will be processing tables <div className="default-line default-line-with-docs">Default: <span className="default-value">1</span></div> |
| <div className="path-line"><span className="path-main">user_ownership_property</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Iceberg table property to look for a `CorpUser` owner.  Can only hold a single user value.  If property has no value, no owner information will be emitted. <div className="default-line default-line-with-docs">Default: <span className="default-value">owner</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">namespace_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for namespaces to filter in ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">namespace_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">namespace_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">namespace_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">namespace_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">namespace_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
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
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">fail_safe_threshold</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'. <div className="default-line default-line-with-docs">Default: <span className="default-value">75.0</span></div> |
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
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.",
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
      "description": "Catalog configuration where to find Iceberg tables.  Only one catalog specification is supported.  The format is the same as [pyiceberg's catalog configuration](https://py.iceberg.apache.org/configuration/), where the catalog name is specified as the object name and attributes are set as key-value pairs.",
      "type": "object",
      "additionalProperties": {
        "type": "object"
      }
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
    "namespace_pattern": {
      "title": "Namespace Pattern",
      "description": "Regex patterns for namespaces to filter in ingestion.",
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
    },
    "processing_threads": {
      "title": "Processing Threads",
      "description": "How many threads will be processing tables",
      "default": 1,
      "type": "integer"
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
    "StatefulStaleMetadataRemovalConfig": {
      "title": "StatefulStaleMetadataRemovalConfig",
      "description": "Base specialized config for Stateful Ingestion with stale metadata removal capability.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "default": false,
          "type": "boolean"
        },
        "remove_stale_metadata": {
          "title": "Remove Stale Metadata",
          "description": "Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled.",
          "default": true,
          "type": "boolean"
        },
        "fail_safe_threshold": {
          "title": "Fail Safe Threshold",
          "description": "Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'.",
          "default": 75.0,
          "minimum": 0.0,
          "maximum": 100.0,
          "type": "number"
        }
      },
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

## Setting up connection to an Iceberg catalog

There are multiple servers compatible with the Iceberg Catalog specification. DataHub's `iceberg` connector uses `pyiceberg`
library to extract metadata from them. The recipe for the source consists of 2 parts:

1. `catalog` part which is passed as-is to the `pyiceberg` library and configures the connection and its details (i.e. authentication).
   The name of catalog specified in the recipe has no consequence, it is just a formal requirement from the library.
   Only one catalog will be considered for the ingestion.
2. The remaining configuration consists of parameters, such as `env` or `stateful_ingestion` which are standard
   DataHub's ingestor configuration parameters and are described in the [Config Details](#config-details) chapter.

This chapter showcases several examples of setting up connections to an Iceberg catalog, varying based on the underlying
implementation. Iceberg is designed to have catalog and warehouse separated, which is reflected in how we configure it.
It is especially visible when using Iceberg REST Catalog - which can use many blob storages
(AWS S3, Azure Blob Storage, MinIO) as a warehouse.

Note that, for advanced users, it is possible to specify a custom catalog client implementation via `py-catalog-impl`
configuration option - refer to `pyiceberg` documentation on details.

### Glue catalog + S3 warehouse

The minimal configuration for connecting to Glue catalog with S3 warehouse:

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      my_catalog:
        type: "glue"
        s3.region: "us-west-2"
        region_name: "us-west-2"
```

Where `us-west-2` is the region from which you want to ingest. The above configuration will work assuming your pod or environment in which
you run your datahub CLI is already authenticated to AWS and has proper permissions granted (see below). If you need
to specify secrets directly, use the following configuration as the template:

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      demo:
        type: "glue"
        s3.region: "us-west-2"
        s3.access-key-id: "${AWS_ACCESS_KEY_ID}"
        s3.secret-access-key: "${AWS_SECRET_ACCESS_KEY}"
        s3.session-token: "${AWS_SESSION_TOKEN}"

        aws_access_key_id: "${AWS_ACCESS_KEY_ID}"
        aws_secret_access_key: "${AWS_SECRET_ACCESS_KEY}"
        aws_session_token: "${AWS_SESSION_TOKEN}"
        region_name: "us-west-2"
```

This example uses references to fill credentials (either from Secrets defined in Managed Ingestion or environmental variables).
It is possible (but not recommended due to security concerns) to provide those values in plaintext, directly in the recipe.

#### Glue and S3 permissions required

The role used by the ingestor for ingesting metadata from Glue Iceberg Catalog and S3 warehouse is:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["glue:GetDatabases", "glue:GetTables", "glue:GetTable"],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket", "s3:GetObjectVersion"],
      "Resource": [
        "arn:aws:s3:::<bucket used by the warehouse>",
        "arn:aws:s3:::<bucket used by the warehouse>/*"
      ]
    }
  ]
}
```

### Iceberg REST Catalog + MinIO

The following configuration assumes MinIO defines authentication using the `s3.*` prefix. Note the specification of `s3.endpoint`, assuming
MinIO listens on port `9000` at `minio-host`. The `uri` parameter points at Iceberg REST Catalog (IRC) endpoint (in this case `iceberg-catalog:8181`).

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      demo:
        type: "rest"
        uri: "http://iceberg-catalog:8181"
        s3.access-key-id: "${AWS_ACCESS_KEY_ID}"
        s3.secret-access-key: "${AWS_SECRET_ACCESS_KEY}"
        s3.region: "eu-east-1"
        s3.endpoint: "http://minio-host:9000"
```

### Iceberg REST Catalog (with authentication) + S3

This example assumes IRC requires token authentication (via `Authorization` header). There are more options available,
see https://py.iceberg.apache.org/configuration/#rest-catalog for details. Moreover, the assumption here is that the
environment (i.e. pod) is already authenticated to perform actions against AWS S3.

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      demo:
        type: "rest"
        uri: "http://iceberg-catalog-uri"
        token: "token-value"
        s3.region: "us-west-2"
```

#### Special REST connection parameters for resiliency

Unlike other parameters provided in the dictionary under the `catalog` key, `connection` parameter is a custom feature in
DataHub, allowing to inject connection resiliency parameters to the REST connection made by the ingestor. `connection`
allows for 2 parameters:

- `timeout` is provided as amount of seconds, it needs to be whole number (or `null` to turn it off)
- `retry` is a complex object representing parameters used to create [urllib3 Retry object](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#module-urllib3.util.retry).
  There are many possible parameters, most important would be `total` (total retries) and `backoff_factor`. See the linked docs
  for the details.

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      demo:
        type: "rest"
        uri: "http://iceberg-catalog-uri"
        connection:
          retry:
            backoff_factor: 0.5
            total: 3
          timeout: 120
```

### SQL catalog + Azure DLS as the warehouse

This example targets `Postgres` as the sql-type `Iceberg` catalog and uses Azure DLS as the warehouse.

```yaml
source:
  type: "iceberg"
  config:
    env: dev
    catalog:
      demo:
        type: sql
        uri: postgresql+psycopg2://user:password@sqldatabase.postgres.database.azure.com:5432/icebergcatalog
        adlfs.tenant-id: <Azure tenant ID>
        adlfs.account-name: <Azure storage account name>
        adlfs.client-id: <Azure Client/Application ID>
        adlfs.client-secret: <Azure Client Secret>
```

## Concept Mapping

<!-- This should be a manual mapping of concepts from the source to the DataHub Metadata Model -->
<!-- Authors should provide as much context as possible about how this mapping was generated, including assumptions made, known shortcuts, & any other caveats -->

This ingestion source maps the following Source System Concepts to DataHub Concepts:

<!-- Remove all unnecessary/irrelevant DataHub Concepts -->

| Source Concept                                                                                                                          | DataHub Concept                                                        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iceberg`                                                                                                                               | [Data Platform](docs/generated/metamodel/entities/dataPlatform.md)     |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Table                                                                                                                                   | [Dataset](docs/generated/metamodel/entities/dataset.md)                | An Iceberg table is registered inside a catalog using a name, where the catalog is responsible for creating, dropping and renaming tables. Catalogs manage a collection of tables that are usually grouped into namespaces. The name of a table is mapped to a Dataset name. If a [Platform Instance](/docs/platform-instances/) is configured, it will be used as a prefix: `<platform_instance>.my.namespace.table`. |
| [Table property](https://iceberg.apache.org/docs/latest/configuration/#table-properties)                                                | [User (a.k.a CorpUser)](docs/generated/metamodel/entities/corpuser.md) | The value of a table property can be used as the name of a CorpUser owner. This table property name can be configured with the source option `user_ownership_property`.                                                                                                                                                                                                                                                                        |
| [Table property](https://iceberg.apache.org/docs/latest/configuration/#table-properties)                                                | CorpGroup                                                              | The value of a table property can be used as the name of a CorpGroup owner. This table property name can be configured with the source option `group_ownership_property`.                                                                                                                                                                                                                                                                      |
| Table parent folders (excluding [warehouse catalog location](https://iceberg.apache.org/docs/latest/configuration/#catalog-properties)) | Container                                                              | Available in a future release                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Table schema](https://iceberg.apache.org/spec/#schemas-and-data-types)                                                                 | SchemaField                                                            | Maps to the fields defined within the Iceberg table schema definition.                                                                                                                                                                                                                                                                                                                                                                         |

## Troubleshooting

### Exceptions while increasing `processing_threads`

Each processing thread will open several files/sockets to download manifest files from blob storage. If you experience
exceptions appearing when increasing `processing_threads` configuration parameter, try to increase limit of open
files (e.g. using `ulimit` in Linux).

## DataHub Iceberg REST Catalog

DataHub also implements the Iceberg REST Catalog. See the [Iceberg Catalog documentation](docs/iceberg-catalog.md) for more details.

### Code Coordinates
- Class Name: `datahub.ingestion.source.iceberg.iceberg.IcebergSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/iceberg/iceberg.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Iceberg, feel free to ping us on [our Slack](https://datahub.com/slack).
