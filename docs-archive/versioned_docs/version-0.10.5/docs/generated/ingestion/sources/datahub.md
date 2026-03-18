---
sidebar_position: 8
title: DataHub
slug: /generated/ingestion/sources/datahub
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahub.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHub
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)



### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[datahub]'
```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">commit_state_interval</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of records to process before committing state <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-main">commit_with_parse_errors</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to update createdon timestamp and kafka offset despite parse errors. Enable if you want to ignore the errors. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">include_all_versions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, include all versions of each aspect. Otherwise, only include the latest version of each aspect. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">kafka_topic_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of kafka topic containing timeseries MCLs <div className="default-line default-line-with-docs">Default: <span className="default-value">MetadataChangeLog&#95;Timeseries&#95;v1</span></div> |
| <div className="path-line"><span className="path-main">mysql_batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of records to fetch from MySQL at a time <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-main">mysql_table_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of MySQL table containing all versioned aspects <div className="default-line default-line-with-docs">Default: <span className="default-value">metadata&#95;aspect&#95;v2</span></div> |
| <div className="path-line"><span className="path-main">kafka_connection</span></div> <div className="type-name-line"><span className="type-name">KafkaConsumerConnectionConfig</span></div> | Kafka connection config <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;bootstrap&#x27;: &#x27;localhost:9092&#x27;, &#x27;schema&#95;registry&#95;u...</span></div> |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">bootstrap</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">localhost:9092</span></div> |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">client_timeout_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The request timeout used when interacting with the Kafka APIs. <div className="default-line default-line-with-docs">Default: <span className="default-value">60</span></div> |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">consumer_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra consumer config serialized as JSON. These options will be passed into Kafka's DeserializingConsumer. See https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#deserializingconsumer and https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md .  |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">schema_registry_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra schema registry config serialized as JSON. These options will be passed into Kafka's SchemaRegistryClient. https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html?#schemaregistryclient  |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">schema_registry_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">http://localhost:8080/schema-registry/api/</span></div> |
| <div className="path-line"><span className="path-main">mysql_connection</span></div> <div className="type-name-line"><span className="type-name">MySQLConnectionConfig</span></div> | MySQL connection config <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;username&#x27;: None, &#x27;host&#95;port&#x27;: &#x27;localhost:3306&#x27;, ...</span></div> |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">database</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | database (catalog)  |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">database_alias</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | [Deprecated] Alias to apply to database when ingesting.  |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">host_port</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | MySQL host URL. <div className="default-line default-line-with-docs">Default: <span className="default-value">localhost:3306</span></div> |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | password  |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">mysql+pymysql</span></div> |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">sqlalchemy_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | URI of database to connect to. See https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls. Takes precedence over other connection parameters.  |
| <div className="path-line"><span className="path-prefix">mysql_connection.</span><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | username  |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulIngestionConfig</span></div> | Stateful Ingestion Config <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;enabled&#x27;: True, &#x27;max&#95;checkpoint&#95;state&#95;size&#x27;: 167...</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | The type of the ingestion state provider registered with datahub. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataHubSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Stateful Ingestion Config",
      "default": {
        "enabled": true,
        "max_checkpoint_state_size": 16777216,
        "state_provider": {
          "type": "datahub",
          "config": null
        },
        "ignore_old_state": false,
        "ignore_new_state": false
      },
      "allOf": [
        {
          "$ref": "#/definitions/StatefulIngestionConfig"
        }
      ]
    },
    "mysql_connection": {
      "title": "Mysql Connection",
      "description": "MySQL connection config",
      "default": {
        "username": null,
        "host_port": "localhost:3306",
        "database": null,
        "database_alias": null,
        "scheme": "mysql+pymysql",
        "sqlalchemy_uri": null,
        "options": {}
      },
      "allOf": [
        {
          "$ref": "#/definitions/MySQLConnectionConfig"
        }
      ]
    },
    "kafka_connection": {
      "title": "Kafka Connection",
      "description": "Kafka connection config",
      "default": {
        "bootstrap": "localhost:9092",
        "schema_registry_url": "http://localhost:8080/schema-registry/api/",
        "schema_registry_config": {},
        "client_timeout_seconds": 60,
        "consumer_config": {}
      },
      "allOf": [
        {
          "$ref": "#/definitions/KafkaConsumerConnectionConfig"
        }
      ]
    },
    "include_all_versions": {
      "title": "Include All Versions",
      "description": "If enabled, include all versions of each aspect. Otherwise, only include the latest version of each aspect.",
      "default": false,
      "type": "boolean"
    },
    "mysql_batch_size": {
      "title": "Mysql Batch Size",
      "description": "Number of records to fetch from MySQL at a time",
      "default": 10000,
      "type": "integer"
    },
    "mysql_table_name": {
      "title": "Mysql Table Name",
      "description": "Name of MySQL table containing all versioned aspects",
      "default": "metadata_aspect_v2",
      "type": "string"
    },
    "kafka_topic_name": {
      "title": "Kafka Topic Name",
      "description": "Name of kafka topic containing timeseries MCLs",
      "default": "MetadataChangeLog_Timeseries_v1",
      "type": "string"
    },
    "commit_state_interval": {
      "title": "Commit State Interval",
      "description": "Number of records to process before committing state",
      "default": 1000,
      "type": "integer"
    },
    "commit_with_parse_errors": {
      "title": "Commit With Parse Errors",
      "description": "Whether to update createdon timestamp and kafka offset despite parse errors. Enable if you want to ignore the errors.",
      "default": false,
      "type": "boolean"
    }
  },
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
    "StatefulIngestionConfig": {
      "title": "StatefulIngestionConfig",
      "description": "Basic Stateful Ingestion Specific Configuration for any source.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "The type of the ingestion state provider registered with datahub.",
          "default": false,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "MySQLConnectionConfig": {
      "title": "MySQLConnectionConfig",
      "type": "object",
      "properties": {
        "username": {
          "title": "Username",
          "description": "username",
          "type": "string"
        },
        "password": {
          "title": "Password",
          "description": "password",
          "type": "string",
          "writeOnly": true,
          "format": "password"
        },
        "host_port": {
          "title": "Host Port",
          "description": "MySQL host URL.",
          "default": "localhost:3306",
          "type": "string"
        },
        "database": {
          "title": "Database",
          "description": "database (catalog)",
          "type": "string"
        },
        "database_alias": {
          "title": "Database Alias",
          "description": "[Deprecated] Alias to apply to database when ingesting.",
          "type": "string"
        },
        "scheme": {
          "title": "Scheme",
          "default": "mysql+pymysql",
          "type": "string"
        },
        "sqlalchemy_uri": {
          "title": "Sqlalchemy Uri",
          "description": "URI of database to connect to. See https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls. Takes precedence over other connection parameters.",
          "type": "string"
        },
        "options": {
          "title": "Options",
          "description": "Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.",
          "type": "object"
        }
      },
      "additionalProperties": false
    },
    "KafkaConsumerConnectionConfig": {
      "title": "KafkaConsumerConnectionConfig",
      "description": "Configuration class for holding connectivity information for Kafka consumers",
      "type": "object",
      "properties": {
        "bootstrap": {
          "title": "Bootstrap",
          "default": "localhost:9092",
          "type": "string"
        },
        "schema_registry_url": {
          "title": "Schema Registry Url",
          "default": "http://localhost:8080/schema-registry/api/",
          "type": "string"
        },
        "schema_registry_config": {
          "title": "Schema Registry Config",
          "description": "Extra schema registry config serialized as JSON. These options will be passed into Kafka's SchemaRegistryClient. https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html?#schemaregistryclient",
          "type": "object"
        },
        "client_timeout_seconds": {
          "title": "Client Timeout Seconds",
          "description": "The request timeout used when interacting with the Kafka APIs.",
          "default": 60,
          "type": "integer"
        },
        "consumer_config": {
          "title": "Consumer Config",
          "description": "Extra consumer config serialized as JSON. These options will be passed into Kafka's DeserializingConsumer. See https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#deserializingconsumer and https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md .",
          "type": "object"
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
- Class Name: `datahub.ingestion.source.datahub.datahub_source.DataHubSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/datahub/datahub_source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHub, feel free to ping us on [our Slack](https://slack.datahubproject.io).
