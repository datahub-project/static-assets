---
sidebar_position: 42
title: Neo4j
slug: /generated/ingestion/sources/neo4j
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/neo4j.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Neo4j
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)



### CLI based Ingestion

#### Install the Plugin
The `neo4j` source works out of the box with `acryl-datahub`.

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
  "additionalProperties": false
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
