---
sidebar_position: 13
title: DataHubGc
slug: /generated/ingestion/sources/datahubgc
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahubgc.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubGc
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


DataHubGcSource is responsible for performing garbage collection tasks on DataHub.

This source performs the following tasks:
1. Cleans up expired tokens.
2. Truncates Elasticsearch indices based on configuration.
3. Cleans up data processes and soft-deleted entities if configured.



### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">cleanup_expired_tokens</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to clean up expired tokens or not <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">dry_run</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to perform a dry run or not. This is only supported for dataprocess cleanup and soft deleted entities cleanup. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">truncate_index_older_than_days</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Indices older than this number of days will be truncated <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-main">truncate_indices</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to truncate elasticsearch indices or not which can be safely truncated <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">truncation_sleep_between_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Sleep between truncation monitoring. <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-main">truncation_watch_until</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Wait for truncation of indices until this number of documents are left <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-main">dataprocess_cleanup</span></div> <div className="type-name-line"><span className="type-name">DataProcessCleanupConfig</span></div> | Configuration for data process cleanup  |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of entities to get in a batch from API <div className="default-line default-line-with-docs">Default: <span className="default-value">500</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">delay</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Delay between each batch <div className="default-line default-line-with-docs">Default: <span className="default-value">0.25</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">delete_empty_data_flows</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to delete Data Flows without runs <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">delete_empty_data_jobs</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to delete Data Jobs without runs <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do data process cleanup. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">hard_delete_entities</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to hard delete entities <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">keep_last_n</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of latest aspects to keep <div className="default-line default-line-with-docs">Default: <span className="default-value">5</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of workers to use for deletion <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">retention_days</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of days to retain metadata in DataHub <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.</span><span className="path-main">aspects_to_clean</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of aspect names to clean up <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;DataprocessInstance&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">dataprocess_cleanup.aspects_to_clean.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">execution_request_cleanup</span></div> <div className="type-name-line"><span className="type-name">DatahubExecutionRequestCleanupConfig</span></div> | Configuration for execution request cleanup  |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">batch_read_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of records per read operation <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Global switch for this cleanup task <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">keep_history_max_count</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of execution requests to keep, per ingestion source <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">keep_history_max_days</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of days to keep execution requests for, per ingestion source <div className="default-line default-line-with-docs">Default: <span className="default-value">90</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">keep_history_min_count</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Minimum number of execution requests to keep, per ingestion source <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">limit_entities_delete</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Max number of execution requests to hard delete. <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">max_read_errors</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of read errors before aborting <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">execution_request_cleanup.</span><span className="path-main">runtime_limit_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum runtime in seconds for the cleanup task <div className="default-line default-line-with-docs">Default: <span className="default-value">3600</span></div> |
| <div className="path-line"><span className="path-main">soft_deleted_entities_cleanup</span></div> <div className="type-name-line"><span className="type-name">SoftDeletedEntitiesCleanupConfig</span></div> | Configuration for soft deleted entities cleanup  |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of entities to get in a batch from GraphQL <div className="default-line default-line-with-docs">Default: <span className="default-value">500</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">delay</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Delay between each batch <div className="default-line default-line-with-docs">Default: <span className="default-value">0.25</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to do soft deletion cleanup. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">futures_max_at_time</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Max number of futures to have at a time. <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">limit_entities_delete</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Max number of entities to delete. <div className="default-line default-line-with-docs">Default: <span className="default-value">25000</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">max_workers</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of workers to use for deletion <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">platform</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Platform to cleanup  |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">query</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Query to filter entities  |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">retention_days</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of days to retain metadata in DataHub <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">runtime_limit_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Runtime limit in seconds <div className="default-line default-line-with-docs">Default: <span className="default-value">7200</span></div> |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Environment to cleanup  |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.</span><span className="path-main">entity_types</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of entity types to cleanup  |
| <div className="path-line"><span className="path-prefix">soft_deleted_entities_cleanup.entity_types.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataHubGcSourceConfig",
  "type": "object",
  "properties": {
    "dry_run": {
      "title": "Dry Run",
      "description": "Whether to perform a dry run or not. This is only supported for dataprocess cleanup and soft deleted entities cleanup.",
      "default": false,
      "type": "boolean"
    },
    "cleanup_expired_tokens": {
      "title": "Cleanup Expired Tokens",
      "description": "Whether to clean up expired tokens or not",
      "default": true,
      "type": "boolean"
    },
    "truncate_indices": {
      "title": "Truncate Indices",
      "description": "Whether to truncate elasticsearch indices or not which can be safely truncated",
      "default": true,
      "type": "boolean"
    },
    "truncate_index_older_than_days": {
      "title": "Truncate Index Older Than Days",
      "description": "Indices older than this number of days will be truncated",
      "default": 30,
      "type": "integer"
    },
    "truncation_watch_until": {
      "title": "Truncation Watch Until",
      "description": "Wait for truncation of indices until this number of documents are left",
      "default": 10000,
      "type": "integer"
    },
    "truncation_sleep_between_seconds": {
      "title": "Truncation Sleep Between Seconds",
      "description": "Sleep between truncation monitoring.",
      "default": 30,
      "type": "integer"
    },
    "dataprocess_cleanup": {
      "title": "Dataprocess Cleanup",
      "description": "Configuration for data process cleanup",
      "allOf": [
        {
          "$ref": "#/definitions/DataProcessCleanupConfig"
        }
      ]
    },
    "soft_deleted_entities_cleanup": {
      "title": "Soft Deleted Entities Cleanup",
      "description": "Configuration for soft deleted entities cleanup",
      "allOf": [
        {
          "$ref": "#/definitions/SoftDeletedEntitiesCleanupConfig"
        }
      ]
    },
    "execution_request_cleanup": {
      "title": "Execution Request Cleanup",
      "description": "Configuration for execution request cleanup",
      "allOf": [
        {
          "$ref": "#/definitions/DatahubExecutionRequestCleanupConfig"
        }
      ]
    }
  },
  "additionalProperties": false,
  "definitions": {
    "DataProcessCleanupConfig": {
      "title": "DataProcessCleanupConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether to do data process cleanup.",
          "default": true,
          "type": "boolean"
        },
        "retention_days": {
          "title": "Retention Days",
          "description": "Number of days to retain metadata in DataHub",
          "default": 10,
          "type": "integer"
        },
        "aspects_to_clean": {
          "title": "Aspects To Clean",
          "description": "List of aspect names to clean up",
          "default": [
            "DataprocessInstance"
          ],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "keep_last_n": {
          "title": "Keep Last N",
          "description": "Number of latest aspects to keep",
          "default": 5,
          "type": "integer"
        },
        "delete_empty_data_jobs": {
          "title": "Delete Empty Data Jobs",
          "description": "Whether to delete Data Jobs without runs",
          "default": false,
          "type": "boolean"
        },
        "delete_empty_data_flows": {
          "title": "Delete Empty Data Flows",
          "description": "Whether to delete Data Flows without runs",
          "default": false,
          "type": "boolean"
        },
        "hard_delete_entities": {
          "title": "Hard Delete Entities",
          "description": "Whether to hard delete entities",
          "default": false,
          "type": "boolean"
        },
        "batch_size": {
          "title": "Batch Size",
          "description": "The number of entities to get in a batch from API",
          "default": 500,
          "type": "integer"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "The number of workers to use for deletion",
          "default": 10,
          "type": "integer"
        },
        "delay": {
          "title": "Delay",
          "description": "Delay between each batch",
          "default": 0.25,
          "type": "number"
        }
      },
      "additionalProperties": false
    },
    "SoftDeletedEntitiesCleanupConfig": {
      "title": "SoftDeletedEntitiesCleanupConfig",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether to do soft deletion cleanup.",
          "default": true,
          "type": "boolean"
        },
        "retention_days": {
          "title": "Retention Days",
          "description": "Number of days to retain metadata in DataHub",
          "default": 10,
          "type": "integer"
        },
        "batch_size": {
          "title": "Batch Size",
          "description": "The number of entities to get in a batch from GraphQL",
          "default": 500,
          "type": "integer"
        },
        "delay": {
          "title": "Delay",
          "description": "Delay between each batch",
          "default": 0.25,
          "type": "number"
        },
        "max_workers": {
          "title": "Max Workers",
          "description": "The number of workers to use for deletion",
          "default": 10,
          "type": "integer"
        },
        "entity_types": {
          "title": "Entity Types",
          "description": "List of entity types to cleanup",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "platform": {
          "title": "Platform",
          "description": "Platform to cleanup",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "Environment to cleanup",
          "type": "string"
        },
        "query": {
          "title": "Query",
          "description": "Query to filter entities",
          "type": "string"
        },
        "limit_entities_delete": {
          "title": "Limit Entities Delete",
          "description": "Max number of entities to delete.",
          "default": 25000,
          "type": "integer"
        },
        "futures_max_at_time": {
          "title": "Futures Max At Time",
          "description": "Max number of futures to have at a time.",
          "default": 1000,
          "type": "integer"
        },
        "runtime_limit_seconds": {
          "title": "Runtime Limit Seconds",
          "description": "Runtime limit in seconds",
          "default": 7200,
          "type": "integer"
        }
      },
      "additionalProperties": false
    },
    "DatahubExecutionRequestCleanupConfig": {
      "title": "DatahubExecutionRequestCleanupConfig",
      "type": "object",
      "properties": {
        "keep_history_min_count": {
          "title": "Keep History Min Count",
          "description": "Minimum number of execution requests to keep, per ingestion source",
          "default": 10,
          "type": "integer"
        },
        "keep_history_max_count": {
          "title": "Keep History Max Count",
          "description": "Maximum number of execution requests to keep, per ingestion source",
          "default": 1000,
          "type": "integer"
        },
        "keep_history_max_days": {
          "title": "Keep History Max Days",
          "description": "Maximum number of days to keep execution requests for, per ingestion source",
          "default": 90,
          "type": "integer"
        },
        "batch_read_size": {
          "title": "Batch Read Size",
          "description": "Number of records per read operation",
          "default": 100,
          "type": "integer"
        },
        "enabled": {
          "title": "Enabled",
          "description": "Global switch for this cleanup task",
          "default": true,
          "type": "boolean"
        },
        "runtime_limit_seconds": {
          "title": "Runtime Limit Seconds",
          "description": "Maximum runtime in seconds for the cleanup task",
          "default": 3600,
          "type": "integer"
        },
        "limit_entities_delete": {
          "title": "Limit Entities Delete",
          "description": "Max number of execution requests to hard delete.",
          "default": 10000,
          "type": "integer"
        },
        "max_read_errors": {
          "title": "Max Read Errors",
          "description": "Maximum number of read errors before aborting",
          "default": 10,
          "type": "integer"
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.gc.datahub_gc.DataHubGcSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/gc/datahub_gc.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHubGc, feel free to ping us on [our Slack](https://slack.datahubproject.io).
