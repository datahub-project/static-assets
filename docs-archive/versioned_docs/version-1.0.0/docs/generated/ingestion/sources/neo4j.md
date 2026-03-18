---
sidebar_position: 43
title: Neo4j
slug: /generated/ingestion/sources/neo4j
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/neo4j.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Neo4j
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |



### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
    type: 'neo4j'
    config:
        uri: 'neo4j+ssc://host:7687'
        username: 'neo4j'
        password: 'password'
        env: 'PROD'

sink:
  type: "datahub-rest"
  config:
    server: 'http://localhost:8080'
```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">password</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Neo4j Password  |
| <div className="path-line"><span className="path-main">uri</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The URI for the Neo4j server  |
| <div className="path-line"><span className="path-main">username</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Neo4j Username  |
| <div className="path-line"><span className="path-main">env</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Neo4j env  |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulIngestionConfig</span></div> | Stateful Ingestion Config  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "Neo4jConfig",
  "description": "Any source that produces dataset urns in a single environment should inherit this class",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Stateful Ingestion Config",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulIngestionConfig"
        }
      ]
    },
    "env": {
      "title": "Env",
      "description": "Neo4j env",
      "type": "string"
    },
    "username": {
      "title": "Username",
      "description": "Neo4j Username",
      "type": "string"
    },
    "password": {
      "title": "Password",
      "description": "Neo4j Password",
      "type": "string"
    },
    "uri": {
      "title": "Uri",
      "description": "The URI for the Neo4j server",
      "type": "string"
    }
  },
  "required": [
    "env",
    "username",
    "password",
    "uri"
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
    "StatefulIngestionConfig": {
      "title": "StatefulIngestionConfig",
      "description": "Basic Stateful Ingestion Specific Configuration for any source.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "default": false,
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

## Integration Details

<!-- Plain-language description of what this integration is meant to do.  -->
<!-- Include details about where metadata is extracted from (ie. logs, source API, manifest, etc.)   -->
Neo4j metadata will be ingested into DataHub using 
`CALL apoc.meta.schema() YIELD value UNWIND keys(value) AS key RETURN key, value[key] AS value;`  
The data that is returned will be parsed 
and will be displayed as Nodes and Relationships in DataHub.  Each object will be tagged with describing what kind of DataHub
object it is.  The defaults are 'Node' and 'Relationship'.  These tag values can be overwritten in the recipe.



## Metadata Ingestion Quickstart

### Prerequisites

In order to ingest metadata from Neo4j, you will need:

* Neo4j instance with APOC installed


### Code Coordinates
- Class Name: `datahub.ingestion.source.neo4j.neo4j_source.Neo4jSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/neo4j/neo4j_source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Neo4j, feel free to ping us on [our Slack](https://slack.datahubproject.io).
