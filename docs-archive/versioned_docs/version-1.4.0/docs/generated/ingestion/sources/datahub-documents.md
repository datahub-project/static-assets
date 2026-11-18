---
sidebar_position: 16
title: DataHubDocuments
slug: /generated/ingestion/sources/datahub-documents
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahub-documents.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubDocuments
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default via stateful ingestion. |


This source extracts Document entities from DataHub and generates semantic embeddings.

It supports:
- **Batch mode**: Fetches documents via GraphQL
- **Event-driven mode**: Processes documents in real-time from Kafka MCL events (recommended)
- **Incremental processing**: Only reprocesses documents when content changes
- **Smart defaults**: Auto-configures connection, chunking, and embeddings from server

The minimal configuration requires just `config: {}` when using environment variables
(DATAHUB_GMS_URL and DATAHUB_GMS_TOKEN) and will automatically align with your server's
semantic search configuration.

**Prerequisites:** Before using this source, configure semantic search on your DataHub server.
See the [Semantic Search Configuration Guide](https://github.com/datahub-project/datahub/blob/master/docs/generated/how-to/semantic-search-configuration) for setup instructions.


### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">min_text_length</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Minimum text length in characters to process (shorter documents are skipped) <div className="default-line default-line-with-docs">Default: <span className="default-value">50</span></div> |
| <div className="path-line"><span className="path-main">partition_strategy</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Text partitioning strategy. Currently only 'markdown' is supported. This field is included in the document hash to trigger reprocessing if the strategy changes. <div className="default-line default-line-with-docs">Default: <span className="default-value">markdown</span></div> |
| <div className="path-line"><span className="path-main">skip_empty_text</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Skip documents with no text content <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">chunking</span></div> <div className="type-name-line"><span className="type-name">ChunkingConfig</span></div> | Chunking strategy configuration.  |
| <div className="path-line"><span className="path-prefix">chunking.</span><span className="path-main">combine_text_under_n_chars</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Combine chunks smaller than this size <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-prefix">chunking.</span><span className="path-main">max_characters</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum characters per chunk <div className="default-line default-line-with-docs">Default: <span className="default-value">500</span></div> |
| <div className="path-line"><span className="path-prefix">chunking.</span><span className="path-main">overlap</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Character overlap between chunks <div className="default-line default-line-with-docs">Default: <span className="default-value">0</span></div> |
| <div className="path-line"><span className="path-prefix">chunking.</span><span className="path-main">strategy</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "basic", "by_title" <div className="default-line default-line-with-docs">Default: <span className="default-value">by&#95;title</span></div> |
| <div className="path-line"><span className="path-main">datahub</span></div> <div className="type-name-line"><span className="type-name">DataHubConnectionConfig</span></div> | DataHub connection configuration.  |
| <div className="path-line"><span className="path-prefix">datahub.</span><span className="path-main">server</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | DataHub GMS server URL <div className="default-line default-line-with-docs">Default: <span className="default-value">http://localhost:8080</span></div> |
| <div className="path-line"><span className="path-prefix">datahub.</span><span className="path-main">token</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | DataHub API token for authentication <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-main">document_urns</span></div> <div className="type-name-line"><span className="type-name">One of array, null</span></div> | Specific document URNs to process (if None, process all matching platforms) <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">document_urns.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">embedding</span></div> <div className="type-name-line"><span className="type-name">EmbeddingConfig</span></div> | Embedding generation configuration. <br />  <br /> Default behavior: Fetches configuration from DataHub server automatically. <br /> Override behavior: Validates local config against server when explicitly set.  |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">allow_local_embedding_config</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | BREAK-GLASS: Allow local config without server validation. NOT RECOMMENDED - may break semantic search. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">api_key</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | API key for Cohere (not needed for Bedrock with IAM roles) <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">aws_region</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | AWS region for Bedrock. If not set, loads from server. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Batch size for embedding API calls <div className="default-line default-line-with-docs">Default: <span className="default-value">25</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">input_type</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Input type for Cohere embeddings <div className="default-line default-line-with-docs">Default: <span className="default-value">search&#95;document</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">model</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Model name. If not set, loads from server. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">model_embedding_key</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Storage key for embeddings (e.g., 'cohere_embed_v3'). Required if overriding server config. If not set, loads from server. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">embedding.</span><span className="path-main">provider</span></div> <div className="type-name-line"><span className="type-name">One of Enum, null</span></div> | Embedding provider (bedrock uses AWS, cohere/openai use API key). If not set, loads from server. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-main">event_mode</span></div> <div className="type-name-line"><span className="type-name">EventModeConfig</span></div> | Event-driven mode configuration.  |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">consumer_id</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Consumer ID for offset tracking (defaults to 'datahub-documents-{pipeline_name}') <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable event-driven mode (polls MCL events instead of GraphQL batch) <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">idle_timeout_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Exit after this many seconds with no new events (incremental batch mode) <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">lookback_days</span></div> <div className="type-name-line"><span className="type-name">One of integer, null</span></div> | Number of days to look back for events on first run (None means start from latest) <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">poll_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of events to fetch per poll <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">poll_timeout_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Timeout for each poll request <div className="default-line default-line-with-docs">Default: <span className="default-value">2</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">reset_offsets</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Reset consumer offsets to start from beginning <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.</span><span className="path-main">topics</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Topics to consume for document changes <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;MetadataChangeLog&#95;Versioned&#95;v1&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">event_mode.topics.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">incremental</span></div> <div className="type-name-line"><span className="type-name">IncrementalConfig</span></div> | Incremental processing configuration.  |
| <div className="path-line"><span className="path-prefix">incremental.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Only process documents whose text content has changed (tracks content hash). Uses stateful ingestion when enabled. The state_file_path option is deprecated and ignored when stateful ingestion is enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">incremental.</span><span className="path-main">force_reprocess</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Force reprocess all documents regardless of content hash <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">incremental.</span><span className="path-main">state_file_path</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | [DEPRECATED] Path to state file. This option is ignored when stateful ingestion is enabled. State is now managed through DataHub's stateful ingestion framework. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-main">platform_filter</span></div> <div className="type-name-line"><span className="type-name">One of array, null</span></div> | Filter documents by platforms. Default (None): Process all NATIVE documents (sourceType=NATIVE) regardless of platform. To include external documents from specific platforms, add them here (e.g., ['notion', 'confluence']). This will process NATIVE documents + EXTERNAL documents from the specified platforms. Use ['*'] or ['ALL'] to process all documents regardless of source type or platform. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">platform_filter.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">DocumentChunkingStatefulIngestionConfig</span></div> | Configuration for document chunking stateful ingestion.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "$defs": {
    "ChunkingConfig": {
      "additionalProperties": false,
      "description": "Chunking strategy configuration.",
      "properties": {
        "strategy": {
          "default": "by_title",
          "description": "Chunking strategy to use",
          "enum": [
            "basic",
            "by_title"
          ],
          "title": "Strategy",
          "type": "string"
        },
        "max_characters": {
          "default": 500,
          "description": "Maximum characters per chunk",
          "title": "Max Characters",
          "type": "integer"
        },
        "overlap": {
          "default": 0,
          "description": "Character overlap between chunks",
          "title": "Overlap",
          "type": "integer"
        },
        "combine_text_under_n_chars": {
          "default": 100,
          "description": "Combine chunks smaller than this size",
          "title": "Combine Text Under N Chars",
          "type": "integer"
        }
      },
      "title": "ChunkingConfig",
      "type": "object"
    },
    "DataHubConnectionConfig": {
      "additionalProperties": false,
      "description": "DataHub connection configuration.",
      "properties": {
        "server": {
          "default": "http://localhost:8080",
          "description": "DataHub GMS server URL",
          "title": "Server",
          "type": "string"
        },
        "token": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "DataHub API token for authentication",
          "title": "Token"
        }
      },
      "title": "DataHubConnectionConfig",
      "type": "object"
    },
    "DocumentChunkingStatefulIngestionConfig": {
      "additionalProperties": false,
      "description": "Configuration for document chunking stateful ingestion.",
      "properties": {
        "enabled": {
          "default": false,
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "title": "Enabled",
          "type": "boolean"
        }
      },
      "title": "DocumentChunkingStatefulIngestionConfig",
      "type": "object"
    },
    "EmbeddingConfig": {
      "additionalProperties": false,
      "description": "Embedding generation configuration.\n\nDefault behavior: Fetches configuration from DataHub server automatically.\nOverride behavior: Validates local config against server when explicitly set.",
      "properties": {
        "provider": {
          "anyOf": [
            {
              "enum": [
                "bedrock",
                "cohere",
                "openai"
              ],
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Embedding provider (bedrock uses AWS, cohere/openai use API key). If not set, loads from server.",
          "title": "Provider"
        },
        "model": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Model name. If not set, loads from server.",
          "title": "Model"
        },
        "model_embedding_key": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Storage key for embeddings (e.g., 'cohere_embed_v3'). Required if overriding server config. If not set, loads from server.",
          "title": "Model Embedding Key"
        },
        "aws_region": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "AWS region for Bedrock. If not set, loads from server.",
          "title": "Aws Region"
        },
        "api_key": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "API key for Cohere (not needed for Bedrock with IAM roles)",
          "title": "Api Key"
        },
        "batch_size": {
          "default": 25,
          "description": "Batch size for embedding API calls",
          "title": "Batch Size",
          "type": "integer"
        },
        "input_type": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": "search_document",
          "description": "Input type for Cohere embeddings",
          "title": "Input Type"
        },
        "allow_local_embedding_config": {
          "default": false,
          "description": "BREAK-GLASS: Allow local config without server validation. NOT RECOMMENDED - may break semantic search.",
          "title": "Allow Local Embedding Config",
          "type": "boolean"
        }
      },
      "title": "EmbeddingConfig",
      "type": "object"
    },
    "EventModeConfig": {
      "additionalProperties": false,
      "description": "Event-driven mode configuration.",
      "properties": {
        "enabled": {
          "default": false,
          "description": "Enable event-driven mode (polls MCL events instead of GraphQL batch)",
          "title": "Enabled",
          "type": "boolean"
        },
        "consumer_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Consumer ID for offset tracking (defaults to 'datahub-documents-{pipeline_name}')",
          "title": "Consumer Id"
        },
        "topics": {
          "default": [
            "MetadataChangeLog_Versioned_v1"
          ],
          "description": "Topics to consume for document changes",
          "items": {
            "type": "string"
          },
          "title": "Topics",
          "type": "array"
        },
        "lookback_days": {
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Number of days to look back for events on first run (None means start from latest)",
          "title": "Lookback Days"
        },
        "reset_offsets": {
          "default": false,
          "description": "Reset consumer offsets to start from beginning",
          "title": "Reset Offsets",
          "type": "boolean"
        },
        "idle_timeout_seconds": {
          "default": 30,
          "description": "Exit after this many seconds with no new events (incremental batch mode)",
          "title": "Idle Timeout Seconds",
          "type": "integer"
        },
        "poll_timeout_seconds": {
          "default": 2,
          "description": "Timeout for each poll request",
          "title": "Poll Timeout Seconds",
          "type": "integer"
        },
        "poll_limit": {
          "default": 100,
          "description": "Maximum number of events to fetch per poll",
          "title": "Poll Limit",
          "type": "integer"
        }
      },
      "title": "EventModeConfig",
      "type": "object"
    },
    "IncrementalConfig": {
      "additionalProperties": false,
      "description": "Incremental processing configuration.",
      "properties": {
        "enabled": {
          "default": true,
          "description": "Only process documents whose text content has changed (tracks content hash). Uses stateful ingestion when enabled. The state_file_path option is deprecated and ignored when stateful ingestion is enabled.",
          "title": "Enabled",
          "type": "boolean"
        },
        "state_file_path": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "[DEPRECATED] Path to state file. This option is ignored when stateful ingestion is enabled. State is now managed through DataHub's stateful ingestion framework.",
          "title": "State File Path"
        },
        "force_reprocess": {
          "default": false,
          "description": "Force reprocess all documents regardless of content hash",
          "title": "Force Reprocess",
          "type": "boolean"
        }
      },
      "title": "IncrementalConfig",
      "type": "object"
    }
  },
  "description": "Configuration for DataHub Documents Source.",
  "properties": {
    "stateful_ingestion": {
      "$ref": "#/$defs/DocumentChunkingStatefulIngestionConfig",
      "description": "Stateful ingestion configuration. Enabled by default to support incremental mode (document hash tracking) and event mode (offset tracking)."
    },
    "datahub": {
      "$ref": "#/$defs/DataHubConnectionConfig",
      "description": "DataHub connection configuration"
    },
    "platform_filter": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter documents by platforms. Default (None): Process all NATIVE documents (sourceType=NATIVE) regardless of platform. To include external documents from specific platforms, add them here (e.g., ['notion', 'confluence']). This will process NATIVE documents + EXTERNAL documents from the specified platforms. Use ['*'] or ['ALL'] to process all documents regardless of source type or platform.",
      "title": "Platform Filter"
    },
    "document_urns": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Specific document URNs to process (if None, process all matching platforms)",
      "title": "Document Urns"
    },
    "event_mode": {
      "$ref": "#/$defs/EventModeConfig",
      "description": "Event-driven mode configuration (polls Kafka MCL events)"
    },
    "incremental": {
      "$ref": "#/$defs/IncrementalConfig",
      "description": "Incremental processing configuration (skip unchanged documents)"
    },
    "chunking": {
      "$ref": "#/$defs/ChunkingConfig",
      "description": "Text chunking strategy configuration"
    },
    "embedding": {
      "$ref": "#/$defs/EmbeddingConfig",
      "description": "Embedding generation configuration (LiteLLM with Cohere/Bedrock)"
    },
    "partition_strategy": {
      "const": "markdown",
      "default": "markdown",
      "description": "Text partitioning strategy. Currently only 'markdown' is supported. This field is included in the document hash to trigger reprocessing if the strategy changes.",
      "title": "Partition Strategy",
      "type": "string"
    },
    "skip_empty_text": {
      "default": true,
      "description": "Skip documents with no text content",
      "title": "Skip Empty Text",
      "type": "boolean"
    },
    "min_text_length": {
      "default": 50,
      "description": "Minimum text length in characters to process (shorter documents are skipped)",
      "title": "Min Text Length",
      "type": "integer"
    }
  },
  "title": "DataHubDocumentsSourceConfig",
  "type": "object"
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.datahub_documents.datahub_documents_source.DataHubDocumentsSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/datahub_documents/datahub_documents_source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHubDocuments, feel free to ping us on [our Slack](https://datahub.com/slack).
