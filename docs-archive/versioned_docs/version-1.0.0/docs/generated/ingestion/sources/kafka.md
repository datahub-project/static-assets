---
sidebar_position: 31
title: Kafka
slug: /generated/ingestion/sources/kafka
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/kafka.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Kafka
Extract Topics & Schemas from Apache Kafka or Confluent Cloud.
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Descriptions | ✅ | Set dataset description to top level doc field for Avro schema |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Platform Instance](../../../platform-instances.md) | ✅ | For multiple Kafka clusters, use the platform_instance configuration |
| Schema Metadata | ✅ | Schemas associated with each topic are extracted from the schema registry. Avro and Protobuf (certified), JSON (incubating). Schema references are supported. |


This plugin extracts the following:
- Topics from the Kafka broker
- Schemas associated with each topic from the schema registry (Avro, Protobuf and JSON schemas are supported)


### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: "kafka"
  config:
    platform_instance: "YOUR_CLUSTER_ID"
    connection:
      bootstrap: "broker:9092"
      schema_registry_url: http://localhost:8081

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
| <div className="path-line"><span className="path-main">convert_urns_to_lowercase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to convert dataset urns to lowercase. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">disable_topic_record_naming_strategy</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Disables the utilization of the TopicRecordNameStrategy for Schema Registry subjects. For more information, visit: https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html#handling-differences-between-preregistered-and-client-derived-schemas:~:text=io.confluent.kafka.serializers.subject.TopicRecordNameStrategy <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">enable_meta_mapping</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, applies the mappings that are defined through the meta_mapping directives. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">field_meta_mapping</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | mapping rules that will be executed against field-level schema properties. Refer to the section below on meta automated mappings. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-main">ignore_warnings_on_schema_type</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Disables warnings reported for non-AVRO/Protobuf value or key schemas if set. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">ingest_schemas_as_entities</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enables ingesting schemas from schema registry as separate entities, in addition to the topics <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">meta_mapping</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | mapping rules that will be executed against top-level schema properties. Refer to the section below on meta automated mappings. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">schema_registry_class</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fully qualified implementation class(custom) that implements the KafkaSchemaRegistryBase interface. <div className="default-line default-line-with-docs">Default: <span className="default-value">datahub.ingestion.source.confluent&#95;schema&#95;registry...</span></div> |
| <div className="path-line"><span className="path-main">schema_tags_field</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The field name in the schema metadata that contains the tags to be added to the dataset. <div className="default-line default-line-with-docs">Default: <span className="default-value">tags</span></div> |
| <div className="path-line"><span className="path-main">strip_user_ids_from_email</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to strip email id while adding owners using meta mappings. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">tag_prefix</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Prefix added to tags during ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-main">topic_subject_map</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">connection</span></div> <div className="type-name-line"><span className="type-name">KafkaConsumerConnectionConfig</span></div> |  <div className="default-line ">Default: <span className="default-value">&#123;&#x27;bootstrap&#x27;: &#x27;localhost:9092&#x27;, &#x27;schema&#95;registry&#95;u...</span></div> |
| <div className="path-line"><span className="path-prefix">connection.</span><span className="path-main">bootstrap</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">localhost:9092</span></div> |
| <div className="path-line"><span className="path-prefix">connection.</span><span className="path-main">client_timeout_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The request timeout used when interacting with the Kafka APIs. <div className="default-line default-line-with-docs">Default: <span className="default-value">60</span></div> |
| <div className="path-line"><span className="path-prefix">connection.</span><span className="path-main">consumer_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra consumer config serialized as JSON. These options will be passed into Kafka's DeserializingConsumer. See https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#deserializingconsumer and https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md .  |
| <div className="path-line"><span className="path-prefix">connection.</span><span className="path-main">schema_registry_config</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Extra schema registry config serialized as JSON. These options will be passed into Kafka's SchemaRegistryClient. https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html?#schemaregistryclient  |
| <div className="path-line"><span className="path-prefix">connection.</span><span className="path-main">schema_registry_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">http://localhost:8080/schema-registry/api/</span></div> |
| <div className="path-line"><span className="path-main">domain</span></div> <div className="type-name-line"><span className="type-name">map(str,AllowDenyPattern)</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">domain.`key`.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">topic_patterns</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> |  <div className="default-line ">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#x27;^&#95;.&#42;&#x27;&#93;, &#x27;ignoreCase&#x27;: ...</span></div> |
| <div className="path-line"><span className="path-prefix">topic_patterns.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">topic_patterns.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">topic_patterns.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">topic_patterns.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">topic_patterns.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "KafkaSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "convert_urns_to_lowercase": {
      "title": "Convert Urns To Lowercase",
      "description": "Whether to convert dataset urns to lowercase.",
      "default": false,
      "type": "boolean"
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "connection": {
      "title": "Connection",
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
    "topic_patterns": {
      "title": "Topic Patterns",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [
          "^_.*"
        ],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "domain": {
      "title": "Domain",
      "description": "A map of domain names to allow deny patterns. Domains can be urn-based (urn:li:domain:13ae4d85-d955-49fc-8474-9004c663a810) or bare (`13ae4d85-d955-49fc-8474-9004c663a810`).",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/AllowDenyPattern"
      }
    },
    "topic_subject_map": {
      "title": "Topic Subject Map",
      "description": "Provides the mapping for the `key` and the `value` schemas of a topic to the corresponding schema registry subject name. Each entry of this map has the form `<topic_name>-key`:`<schema_registry_subject_name_for_key_schema>` and `<topic_name>-value`:`<schema_registry_subject_name_for_value_schema>` for the key and the value schemas associated with the topic, respectively. This parameter is mandatory when the [RecordNameStrategy](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html#how-the-naming-strategies-work) is used as the subject naming strategy in the kafka schema registry. NOTE: When provided, this overrides the default subject name resolution even when the `TopicNameStrategy` or the `TopicRecordNameStrategy` are used.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "schema_registry_class": {
      "title": "Schema Registry Class",
      "description": "The fully qualified implementation class(custom) that implements the KafkaSchemaRegistryBase interface.",
      "default": "datahub.ingestion.source.confluent_schema_registry.ConfluentSchemaRegistry",
      "type": "string"
    },
    "schema_tags_field": {
      "title": "Schema Tags Field",
      "description": "The field name in the schema metadata that contains the tags to be added to the dataset.",
      "default": "tags",
      "type": "string"
    },
    "enable_meta_mapping": {
      "title": "Enable Meta Mapping",
      "description": "When enabled, applies the mappings that are defined through the meta_mapping directives.",
      "default": true,
      "type": "boolean"
    },
    "meta_mapping": {
      "title": "Meta Mapping",
      "description": "mapping rules that will be executed against top-level schema properties. Refer to the section below on meta automated mappings.",
      "default": {},
      "type": "object"
    },
    "field_meta_mapping": {
      "title": "Field Meta Mapping",
      "description": "mapping rules that will be executed against field-level schema properties. Refer to the section below on meta automated mappings.",
      "default": {},
      "type": "object"
    },
    "strip_user_ids_from_email": {
      "title": "Strip User Ids From Email",
      "description": "Whether or not to strip email id while adding owners using meta mappings.",
      "default": false,
      "type": "boolean"
    },
    "tag_prefix": {
      "title": "Tag Prefix",
      "description": "Prefix added to tags during ingestion.",
      "default": "",
      "type": "string"
    },
    "ignore_warnings_on_schema_type": {
      "title": "Ignore Warnings On Schema Type",
      "description": "Disables warnings reported for non-AVRO/Protobuf value or key schemas if set.",
      "default": false,
      "type": "boolean"
    },
    "disable_topic_record_naming_strategy": {
      "title": "Disable Topic Record Naming Strategy",
      "description": "Disables the utilization of the TopicRecordNameStrategy for Schema Registry subjects. For more information, visit: https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html#handling-differences-between-preregistered-and-client-derived-schemas:~:text=io.confluent.kafka.serializers.subject.TopicRecordNameStrategy",
      "default": false,
      "type": "boolean"
    },
    "ingest_schemas_as_entities": {
      "title": "Ingest Schemas As Entities",
      "description": "Enables ingesting schemas from schema registry as separate entities, in addition to the topics",
      "default": false,
      "type": "boolean"
    }
  },
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

:::note
Stateful Ingestion is available only when a Platform Instance is assigned to this source.
:::

### Connecting to Confluent Cloud

If using Confluent Cloud you can use a recipe like this. In this `consumer_config.sasl.username` and `consumer_config.sasl.password` are the API credentials that you get (in the Confluent UI) from your cluster -> Data Integration -> API Keys. `schema_registry_config.basic.auth.user.info` has API credentials for Confluent schema registry which you get (in Confluent UI) from Schema Registry -> API credentials.

When creating API Key for the cluster ensure that the ACLs associated with the key are set like below. This is required for DataHub to read topic metadata from topics in Confluent Cloud.

```
Topic Name = *
Permission = ALLOW
Operation = DESCRIBE
Pattern Type = LITERAL
```

```yml
source:
  type: "kafka"
  config:
    platform_instance: "YOUR_CLUSTER_ID"
    connection:
      bootstrap: "abc-defg.eu-west-1.aws.confluent.cloud:9092"
      consumer_config:
        security.protocol: "SASL_SSL"
        sasl.mechanism: "PLAIN"
        sasl.username: "${CLUSTER_API_KEY_ID}"
        sasl.password: "${CLUSTER_API_KEY_SECRET}"
      schema_registry_url: "https://abc-defgh.us-east-2.aws.confluent.cloud"
      schema_registry_config:
        basic.auth.user.info: "${REGISTRY_API_KEY_ID}:${REGISTRY_API_KEY_SECRET}"

sink:
  # sink configs
```

If you are trying to add domains to your topics you can use a configuration like below.

```yml
source:
  type: "kafka"
  config:
    # ...connection block
    domain:
      "urn:li:domain:13ae4d85-d955-49fc-8474-9004c663a810":
        allow:
          - ".*"
      "urn:li:domain:d6ec9868-6736-4b1f-8aa6-fee4c5948f17":
        deny:
          - ".*"
```

Note that the `domain` in config above can be either an _urn_ or a domain _id_ (i.e. `urn:li:domain:13ae4d85-d955-49fc-8474-9004c663a810` or simply `13ae4d85-d955-49fc-8474-9004c663a810`). The Domain should exist in your DataHub instance before ingesting data into the Domain. To create a Domain on DataHub, check out the [Domains User Guide](/docs/domains/).

If you are using a non-default subject naming strategy in the schema registry, such as [RecordNameStrategy](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html#how-the-naming-strategies-work), the mapping for the topic's key and value schemas to the schema registry subject names should be provided via `topic_subject_map` as shown in the configuration below.

```yml
source:
  type: "kafka"
  config:
    # ...connection block
    # Defines the mapping for the key & value schemas associated with a topic & the subject name registered with the
    # kafka schema registry.
    topic_subject_map:
      # Defines both key & value schema for topic 'my_topic_1'
      "my_topic_1-key": "io.acryl.Schema1"
      "my_topic_1-value": "io.acryl.Schema2"
      # Defines only the value schema for topic 'my_topic_2' (the topic doesn't have a key schema).
      "my_topic_2-value": "io.acryl.Schema3"
```

### Custom Schema Registry

The Kafka Source uses the schema registry to figure out the schema associated with both `key` and `value` for the topic.
By default it uses the [Confluent's Kafka Schema registry](https://docs.confluent.io/platform/current/schema-registry/index.html)
and supports the `AVRO` and `PROTOBUF` schema types.

If you're using a custom schema registry, or you are using schema type other than `AVRO` or `PROTOBUF`, then you can provide your own
custom implementation of the `KafkaSchemaRegistryBase` class, and implement the `get_schema_metadata(topic, platform_urn)` method that
given a topic name would return object of `SchemaMetadata` containing schema for that topic. Please refer
`datahub.ingestion.source.confluent_schema_registry::ConfluentSchemaRegistry` for sample implementation of this class.

```python
class KafkaSchemaRegistryBase(ABC):
    @abstractmethod
    def get_schema_metadata(
        self, topic: str, platform_urn: str
    ) -> Optional[SchemaMetadata]:
        pass
```

The custom schema registry class can be configured using the `schema_registry_class` config param of the `kafka` source as shown below.

```YAML
source:
  type: "kafka"
  config:
    # Set the custom schema registry implementation class
    schema_registry_class: "datahub.ingestion.source.confluent_schema_registry.ConfluentSchemaRegistry"
    # Coordinates
    connection:
      bootstrap: "broker:9092"
      schema_registry_url: http://localhost:8081
```

### OAuth Callback 
The OAuth callback function can be set up using `config.connection.consumer_config.oauth_cb`.

You need to specify a Python function reference in the format &lt;python-module&gt;:&lt;function-name&gt;.

For example, in the configuration `oauth:create_token`, `create_token` is a function defined in `oauth.py`, and `oauth.py` must be accessible in the PYTHONPATH.

```YAML
source:
  type: "kafka"
  config:
    # Set the custom schema registry implementation class
    schema_registry_class: "datahub.ingestion.source.confluent_schema_registry.ConfluentSchemaRegistry"
    # Coordinates
    connection:
      bootstrap: "broker:9092"
      schema_registry_url: http://localhost:8081
      consumer_config:
        security.protocol: "SASL_PLAINTEXT"
        sasl.mechanism: "OAUTHBEARER"
        oauth_cb: "oauth:create_token"
# sink configs
```

### Limitations of `PROTOBUF` schema types implementation

The current implementation of the support for `PROTOBUF` schema type has the following limitations:

- Recursive types are not supported.
- If the schemas of different topics define a type in the same package, the source would raise an exception.

In addition to this, maps are represented as arrays of messages. The following message,

```
message MessageWithMap {
  map<int, string> map_1 = 1;
}
```

becomes:

```
message Map1Entry {
  int key = 1;
  string value = 2/
}
message MessageWithMap {
  repeated Map1Entry map_1 = 1;
}
```

### Enriching DataHub metadata with automated meta mapping

:::note
Meta mapping is currently only available for Avro schemas, and requires that those Avro schemas are pushed to the schema registry.
:::

Avro schemas are permitted to have additional attributes not defined by the specification as arbitrary metadata. A common pattern is to utilize this for business metadata. The Kafka source has the ability to transform this directly into DataHub Owners, Tags and Terms.

#### Simple tags

If you simply have a list of tags embedded into an Avro schema (either at the top-level or for an individual field), you can use the `schema_tags_field` config.

Example Avro schema:

```json
{
  "name": "sampleRecord",
  "type": "record",
  "tags": ["tag1", "tag2"],
  "fields": [
    {
      "name": "field_1",
      "type": "string",
      "tags": ["tag3", "tag4"]
    }
  ]
}
```

The name of the field containing a list of tags can be configured with the `schema_tags_field` property:

```yaml
config:
  schema_tags_field: tags
```

#### meta mapping

You can also map specific Avro fields into Owners, Tags and Terms using meta
mapping.

Example Avro schema:

```json
{
  "name": "sampleRecord",
  "type": "record",
  "owning_team": "@Data-Science",
  "data_tier": "Bronze",
  "fields": [
    {
      "name": "field_1",
      "type": "string",
      "gdpr": {
        "pii": true
      }
    }
  ]
}
```

This can be mapped to DataHub metadata with `meta_mapping` config:

```yaml
config:
  meta_mapping:
    owning_team:
      match: "^@(.*)"
      operation: "add_owner"
      config:
        owner_type: group
    data_tier:
      match: "Bronze|Silver|Gold"
      operation: "add_term"
      config:
        term: "{{ $match }}"
  field_meta_mapping:
    gdpr.pii:
      match: true
      operation: "add_tag"
      config:
        tag: "pii"
```

The underlying implementation is similar to [dbt meta mapping](/docs/generated/ingestion/sources/dbt#dbt-meta-automated-mappings), which has more detailed examples that can be used for reference.

### Code Coordinates
- Class Name: `datahub.ingestion.source.kafka.kafka.KafkaSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/kafka/kafka.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Kafka, feel free to ping us on [our Slack](https://slack.datahubproject.io).
