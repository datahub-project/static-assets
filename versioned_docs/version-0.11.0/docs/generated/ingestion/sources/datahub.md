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
Migrate data from one DataHub instance to another.

Requires direct access to the database, kafka broker, and kafka schema registry
of the source DataHub instance.
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


### Overview

This source pulls data from two locations:
- The DataHub database, containing a single table holding all versioned aspects
- The DataHub Kafka cluster, reading from the [MCL Log](../../../../docs/what/mxe.md#metadata-change-log-mcl)
topic for timeseries aspects.

All data is first read from the database, before timeseries data is ingested from kafka.
To prevent this source from potentially running forever, it will not ingest data produced after the
datahub_source ingestion job is started. This `stop_time` is reflected in the report.

Data from the database and kafka are read in chronological order, specifically by the
createdon timestamp in the database and by kafka offset per partition. In order to
properly read from the database, please ensure that the `createdon` column is indexed.
Newly created databases should have this index, named `timeIndex`, by default, but older
ones you may have to create yourself, with the statement:

```
CREATE INDEX timeIndex ON metadata_aspect_v2 (createdon);
```

*If you do not have this index, the source may run incredibly slowly and produce
significant database load.*

#### Stateful Ingestion
On first run, the source will read from the earliest data in the database and the earliest
kafka offsets. Every `commit_state_interval` (default 1000) records, the source will store
a checkpoint to remember its place, i.e. the last createdon timestamp and kafka offsets.
This allows you to stop and restart the source without losing much progress, but note that
you will re-ingest some data at the start of the new run.

If any errors are encountered in the ingestion process, e.g. we are unable to emit an aspect
due to network errors, the source will keep running, but will stop committing checkpoints,
unless `commit_with_parse_errors` (default `false`) is set. Thus, if you re-run the ingestion,
you can re-ingest the data that was missed, but note it will all re-ingest all subsequent data.

If you want to re-ingest all data, you can set a different `pipeline_name` in your recipe,
or set `stateful_ingestion.ignore_old_state`:

```yaml
source:
  config:
    # ... connection config, etc.
    stateful_ingestion:
      enabled: true
      ignore_old_state: true
```

#### Limitations
- Can only pull timeseries aspects retained by Kafka, which by default lasts 90 days.
- Does not detect hard timeseries deletions, e.g. if via a `datahub delete` command using the CLI.
Therefore, if you deleted data in this way, it will still exist in the destination instance.
- If you have a significant amount of aspects with the exact same `createdon` timestamp,
stateful ingestion will not be able to save checkpoints partially through that timestamp.
On a subsequent run, all aspects for that timestamp will be ingested.

#### Performance
On your destination DataHub instance, we suggest the following settings:
- Enable [async ingestion](../../../../docs/deploy/environment-vars.md#ingestion)
- Use standalone consumers
([mae-consumer](../../../../metadata-jobs/mae-consumer-job/README.md)
and [mce-consumer](../../../../metadata-jobs/mce-consumer-job/README.md))
  * If you are migrating large amounts of data, consider scaling consumer replicas.
- Increase the number of gms pods to add redundancy and increase resilience to node evictions
  * If you are migrating large amounts of data, consider increasing elasticsearch's
  thread count via the `ELASTICSEARCH_THREAD_COUNT` environment variable.

### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[datahub]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
pipeline_name: datahub_source_1
datahub_api:
  server: "http://localhost:8080"  # Migrate data from DataHub instance on localhost:8080
  token: "<token>"
source:
  type: datahub
  config:
    include_all_versions: false
    database_connection:
      scheme: "mysql+pymysql"  # or "postgresql+psycopg2" for Postgres
      host_port: "<database_host>:<database_port>"
      username: "<username>"
      password: "<password>"
      database: "<database>"
    kafka_connection:
      bootstrap: "<boostrap_url>:9092"
      schema_registry_url: "<schema_registry_url>:8081"
    stateful_ingestion:
      enabled: true
      ignore_old_state: false
  extractor_config:
    set_system_metadata: false  # Replicate system metadata

# Here, we write to a DataHub instance
# You can also use a different sink, e.g. to write the data to a file instead
sink:
  type: datahub
  config:
    server: "<destination_gms_url>"
    token: "<token>"

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
| <div className="path-line"><span className="path-main">database_query_batch_size</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of records to fetch from the database at a time <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |
| <div className="path-line"><span className="path-main">database_table_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of database table containing all versioned aspects <div className="default-line default-line-with-docs">Default: <span className="default-value">metadata&#95;aspect&#95;v2</span></div> |
| <div className="path-line"><span className="path-main">include_all_versions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | If enabled, include all versions of each aspect. Otherwise, only include the latest version of each aspect.  <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">kafka_topic_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Name of kafka topic containing timeseries MCLs <div className="default-line default-line-with-docs">Default: <span className="default-value">MetadataChangeLog&#95;Timeseries&#95;v1</span></div> |
| <div className="path-line"><span className="path-main">database_connection</span></div> <div className="type-name-line"><span className="type-name">SQLAlchemyConnectionConfig</span></div> | Database connection config  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">host_port</span>&nbsp;<abbr title="Required if database_connection is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | host URL  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">scheme</span>&nbsp;<abbr title="Required if database_connection is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | scheme  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">database</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | database (catalog)  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">database_alias</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | [Deprecated] Alias to apply to database when ingesting.  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | password  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">sqlalchemy_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | URI of database to connect to. See https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls. Takes precedence over other connection parameters.  |
| <div className="path-line"><span className="path-prefix">database_connection.</span><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | username  |
| <div className="path-line"><span className="path-main">kafka_connection</span></div> <div className="type-name-line"><span className="type-name">KafkaConsumerConnectionConfig</span></div> | Kafka connection config  |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">bootstrap</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">localhost:9092</span></div> |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">client_timeout_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The request timeout used when interacting with the Kafka APIs. <div className="default-line default-line-with-docs">Default: <span className="default-value">60</span></div> |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">consumer_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra consumer config serialized as JSON. These options will be passed into Kafka's DeserializingConsumer. See https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#deserializingconsumer and https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md .  |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">schema_registry_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra schema registry config serialized as JSON. These options will be passed into Kafka's SchemaRegistryClient. https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html?#schemaregistryclient  |
| <div className="path-line"><span className="path-prefix">kafka_connection.</span><span className="path-main">schema_registry_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">http://localhost:8080/schema-registry/api/</span></div> |
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
    "database_connection": {
      "title": "Database Connection",
      "description": "Database connection config",
      "allOf": [
        {
          "$ref": "#/definitions/SQLAlchemyConnectionConfig"
        }
      ]
    },
    "kafka_connection": {
      "title": "Kafka Connection",
      "description": "Kafka connection config",
      "allOf": [
        {
          "$ref": "#/definitions/KafkaConsumerConnectionConfig"
        }
      ]
    },
    "include_all_versions": {
      "title": "Include All Versions",
      "description": "If enabled, include all versions of each aspect. Otherwise, only include the latest version of each aspect. ",
      "default": false,
      "type": "boolean"
    },
    "database_query_batch_size": {
      "title": "Database Query Batch Size",
      "description": "Number of records to fetch from the database at a time",
      "default": 10000,
      "type": "integer"
    },
    "database_table_name": {
      "title": "Database Table Name",
      "description": "Name of database table containing all versioned aspects",
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
    "SQLAlchemyConnectionConfig": {
      "title": "SQLAlchemyConnectionConfig",
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
          "description": "host URL",
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
          "description": "scheme",
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
      "required": [
        "host_port",
        "scheme"
      ],
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
