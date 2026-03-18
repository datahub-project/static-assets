---
sidebar_position: 13
title: DynamoDB
slug: /generated/ingestion/sources/dynamodb
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/dynamodb.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DynamoDB
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Platform Instance](../../../platform-instances.md) | ✅ | By default, platform_instance will use the AWS account id |


This plugin extracts the following:

AWS DynamoDB table names with their region, and infer schema of attribute names and types by scanning
the table


### Prerequisities

In order to execute this source, you need to attach the `AmazonDynamoDBReadOnlyAccess` policy to a user in your AWS account. Then create an API access key and secret for the user.

For a user to be able to create API access key, it needs the following access key permissions. Your AWS account admin can create a policy with these permissions and attach to the user, you can find more details in [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "iam:ListAccessKeys",
        "iam:CreateAccessKey",
        "iam:UpdateAccessKey",
        "iam:DeleteAccessKey"
      ],
      "Resource": "arn:aws:iam::${aws_account_id}:user/${aws:username}"
    }
  ]
}
```

### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[dynamodb]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: dynamodb
  config:
    platform_instance: "AWS_ACCOUNT_ID"
    aws_access_key_id: "${AWS_ACCESS_KEY_ID}"
    aws_secret_access_key: "${AWS_SECRET_ACCESS_KEY}"
    #
    # If there are items that have most representative fields of the table, users could use the
    # `include_table_item` option to provide a list of primary keys of the table in dynamodb format.
    # For each `region.table`, the list of primary keys can be at most 100.
    # We include these items in addition to the first 100 items in the table when we scan it.
    #
    # include_table_item:
    #   region.table_name:
    #     [
    #       {
    #         "partition_key_name": { "attribute_type": "attribute_value" },
    #         "sort_key_name": { "attribute_type": "attribute_value" },
    #       },
    #     ]

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
| <div className="path-line"><span className="path-main">aws_access_key_id</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | AWS Access Key ID.  |
| <div className="path-line"><span className="path-main">aws_secret_access_key</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | AWS Secret Key.  |
| <div className="path-line"><span className="path-main">include_table_item</span></div> <div className="type-name-line"><span className="type-name">map(str,array)</span></div> |   |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">map(str,AllowDenyPattern)</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">table_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for tables to filter in ingestion. The table name format is 'region.table' <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">table_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | The type of the ingestion state provider registered with datahub. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DynamoDBConfig",
  "description": "Any source that is a primary producer of Dataset metadata should inherit this class",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
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
    "aws_access_key_id": {
      "title": "Aws Access Key Id",
      "description": "AWS Access Key ID.",
      "type": "string"
    },
    "aws_secret_access_key": {
      "title": "Aws Secret Access Key",
      "description": "AWS Secret Key.",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "domain": {
      "title": "Domain",
      "description": "regex patterns for tables to filter to assign domain_key. ",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/AllowDenyPattern"
      }
    },
    "include_table_item": {
      "title": "Include Table Item",
      "description": "[Advanced] The primary keys of items of a table in dynamodb format the user would like to include in schema. Refer \"Advanced Configurations\" section for more details",
      "type": "object",
      "additionalProperties": {
        "type": "array",
        "items": {
          "type": "object"
        }
      }
    },
    "table_pattern": {
      "title": "Table Pattern",
      "description": "Regex patterns for tables to filter in ingestion. The table name format is 'region.table'",
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
    }
  },
  "required": [
    "aws_access_key_id",
    "aws_secret_access_key"
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
    }
  }
}
```


</TabItem>
</Tabs>

## Advanced Configurations

### Using `include_table_item` config

If there are items that have most representative fields of the table, users could use the `include_table_item` option to provide a list of primary keys of the table in dynamodb format. We include these items in addition to the first 100 items in the table when we scan it.

Take [AWS DynamoDB Developer Guide Example tables and data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleTables.html) as an example, if a account has a table `Reply` in the `us-west-2` region with composite primary key `Id` and `ReplyDateTime`, users can use `include_table_item` to include 2 items as following:

Example:

```yml
# The table name should be in the format of region.table_name
# The primary keys should be in the DynamoDB format
include_table_item:
  us-west-2.Reply:
    [
      {
        "ReplyDateTime": { "S": "2015-09-22T19:58:22.947Z" },
        "Id": { "S": "Amazon DynamoDB#DynamoDB Thread 1" },
      },
      {
        "ReplyDateTime": { "S": "2015-10-05T19:58:22.947Z" },
        "Id": { "S": "Amazon DynamoDB#DynamoDB Thread 2" },
      },
    ]
```

### Code Coordinates
- Class Name: `datahub.ingestion.source.dynamodb.dynamodb.DynamoDBSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/dynamodb/dynamodb.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DynamoDB, feel free to ping us on [our Slack](https://slack.datahubproject.io).
