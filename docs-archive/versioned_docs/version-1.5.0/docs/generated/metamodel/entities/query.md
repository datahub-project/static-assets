---
sidebar_position: 32
title: Query
slug: /generated/metamodel/entities/query
custom_edit_url: null
---
# Query

The query entity represents SQL queries (or queries in other languages) that have been executed against one or more data assets such as datasets, tables, or views. Query entities capture both manually created queries and queries discovered through automated crawling of query logs from data platforms like BigQuery, Snowflake, Redshift, and others.

Queries are powerful building blocks for understanding data lineage, usage patterns, and relationships between datasets. When DataHub ingests query logs from data warehouses, it automatically creates query entities that capture the SQL statements, the datasets they reference, execution statistics, and usage patterns over time.

## Identity

Query entities are identified by a single piece of information:

- A unique identifier (`id`) that serves as the key for the query entity. This identifier is typically generated as a hash of the normalized query text, ensuring that identical queries are deduplicated and treated as the same entity.

An example of a query identifier is `urn:li:query:3b8d7b8c7e4e8b4e3c2e1a5c6d7e8f9a`. The identifier is a unique string that can be generated through various means:

- A hash of the normalized SQL query text (common for system-discovered queries)
- A user-provided identifier (for manually created queries)
- A platform-specific query identifier

## Important Capabilities

### Query Properties

The `queryProperties` aspect contains the core information about a query:

- **Statement**: The actual query text and its language (SQL, or UNKNOWN)
- **Source**: How the query was discovered (`MANUAL` for user-entered queries via UI, or `SYSTEM` for queries discovered by crawlers)
- **Name**: Optional display name to identify the query in a human-readable way
- **Description**: Optional description providing context about what the query does
- **Created/Modified**: Audit stamps tracking who created and last modified the query, along with timestamps
- **Origin**: The source entity that this query came from (e.g., a View, Stored Procedure, dbt Model, etc.)
- **Custom Properties**: Additional key-value pairs for platform-specific metadata

The following code snippet shows you how to create a query entity with properties.

<details>
<summary>Python SDK: Create a query with properties</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_create.py
# metadata-ingestion/examples/library/query_create.py
import logging
import os
import time

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.metadata.schema_classes import (
    AuditStampClass,
    QueryLanguageClass,
    QueryPropertiesClass,
    QuerySourceClass,
    QueryStatementClass,
    QuerySubjectClass,
    QuerySubjectsClass,
)
from datahub.metadata.urns import CorpUserUrn, DatasetUrn, QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_id = "my-unique-query-id"
query_urn = QueryUrn(query_id)

current_timestamp = int(time.time() * 1000)
actor_urn = CorpUserUrn("datahub")

query_properties = QueryPropertiesClass(
    statement=QueryStatementClass(
        value="SELECT customer_id, order_total FROM orders WHERE order_date >= '2024-01-01'",
        language=QueryLanguageClass.SQL,
    ),
    source=QuerySourceClass.MANUAL,
    name="Customer Orders Q1 2024",
    description="Query to retrieve all customer orders from Q1 2024 for reporting",
    created=AuditStampClass(time=current_timestamp, actor=actor_urn.urn()),
    lastModified=AuditStampClass(time=current_timestamp, actor=actor_urn.urn()),
)

dataset_urn = DatasetUrn.from_string(
    "urn:li:dataset:(urn:li:dataPlatform:postgres,public.orders,PROD)"
)
query_subjects = QuerySubjectsClass(
    subjects=[
        QuerySubjectClass(entity=dataset_urn.urn()),
    ]
)

gms_server = os.getenv("DATAHUB_GMS_URL", "http://localhost:8080")
token = os.getenv("DATAHUB_GMS_TOKEN")
rest_emitter = DatahubRestEmitter(gms_server=gms_server, token=token)

mcpw_properties = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=query_properties,
)
rest_emitter.emit(mcpw_properties)

mcpw_subjects = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=query_subjects,
)
rest_emitter.emit(mcpw_subjects)

log.info(f"Created query {query_urn}")

```

</details>

You can also update specific properties of an existing query:

<details>
<summary>Python SDK: Update query properties</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_update_properties.py
# metadata-ingestion/examples/library/query_update_properties.py
import logging
import time

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DataHubGraphConfig
from datahub.metadata.schema_classes import (
    AuditStampClass,
    QueryPropertiesClass,
)
from datahub.metadata.urns import CorpUserUrn, QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_urn = QueryUrn("my-unique-query-id")

graph = DataHubGraph(DataHubGraphConfig(server="http://localhost:8080"))
emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

existing_properties = graph.get_aspect(
    entity_urn=query_urn.urn(),
    aspect_type=QueryPropertiesClass,
)

if not existing_properties:
    log.error(f"Query {query_urn} does not exist or has no properties")
    exit(1)

current_timestamp = int(time.time() * 1000)
actor_urn = CorpUserUrn("datahub")

existing_properties.name = "Updated Query Name"
existing_properties.description = "This query has been updated with new documentation"
existing_properties.lastModified = AuditStampClass(
    time=current_timestamp, actor=actor_urn.urn()
)

event = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=existing_properties,
)

emitter.emit(event)
log.info(f"Updated properties for query {query_urn}")

```

</details>

### Query Subjects

The `querySubjects` aspect captures the data assets that are referenced by a query. These are the datasets, tables, views, or other entities that the query reads from or writes to.

In single-asset queries (e.g., `SELECT * FROM table`), the subjects will contain a single table reference. In multi-asset queries (e.g., joins across multiple tables), the subjects may contain multiple table references.

<details>
<summary>Python SDK: Add subjects to a query</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_add_subjects.py
# metadata-ingestion/examples/library/query_add_subjects.py
import logging

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DataHubGraphConfig
from datahub.metadata.schema_classes import QuerySubjectClass, QuerySubjectsClass
from datahub.metadata.urns import DatasetUrn, QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_urn = QueryUrn("my-unique-query-id")

graph = DataHubGraph(DataHubGraphConfig(server="http://localhost:8080"))
emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

existing_subjects = graph.get_aspect(
    entity_urn=query_urn.urn(),
    aspect_type=QuerySubjectsClass,
)

subjects = existing_subjects.subjects if existing_subjects else []

new_dataset_urn = DatasetUrn.from_string(
    "urn:li:dataset:(urn:li:dataPlatform:postgres,public.customers,PROD)"
)
new_subject = QuerySubjectClass(entity=new_dataset_urn.urn())

if new_subject not in subjects:
    subjects.append(new_subject)

query_subjects_aspect = QuerySubjectsClass(subjects=subjects)

event = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=query_subjects_aspect,
)

emitter.emit(event)
log.info(f"Added subject to query {query_urn}")

```

</details>

### Query Usage Statistics

The `queryUsageStatistics` aspect is a timeseries aspect that tracks execution statistics and usage patterns for queries over time. This includes:

- **Query Count**: Total number of times the query was executed in a time bucket
- **Query Cost**: The compute cost associated with executing the query (platform-specific)
- **Last Executed At**: Timestamp of the most recent execution
- **Unique User Count**: Number of distinct users who executed the query
- **User Counts**: Breakdown of execution counts by individual users

This aspect is typically populated automatically by ingestion connectors that process query logs from data platforms. The timeseries nature allows for tracking trends and patterns in query usage over time.

### Tags and Glossary Terms

Like other DataHub entities, queries can have Tags or Terms attached to them. Tags are informal labels for categorizing queries (e.g., "production", "experimental", "deprecated"), while Terms are formal vocabulary from a business glossary (e.g., "Customer Data", "Financial Reporting").

#### Adding Tags to a Query

Tags are added to queries using the `globalTags` aspect.

<details>
<summary>Python SDK: Add a tag to a query</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_add_tag.py
# metadata-ingestion/examples/library/query_add_tag.py
import logging

from datahub.emitter.mce_builder import make_tag_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DataHubGraphConfig
from datahub.metadata.schema_classes import GlobalTagsClass, TagAssociationClass
from datahub.metadata.urns import QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_urn = QueryUrn("my-unique-query-id")

graph = DataHubGraph(DataHubGraphConfig(server="http://localhost:8080"))
emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

existing_tags = graph.get_aspect(
    entity_urn=query_urn.urn(),
    aspect_type=GlobalTagsClass,
)

tags_to_add = existing_tags.tags if existing_tags else []

tags_to_add.append(
    TagAssociationClass(tag=make_tag_urn("production"), context="Query categorization")
)

global_tags_aspect = GlobalTagsClass(tags=tags_to_add)

event = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=global_tags_aspect,
)

emitter.emit(event)
log.info(f"Added tag to query {query_urn}")

```

</details>

#### Adding Glossary Terms to a Query

Terms are added using the `glossaryTerms` aspect.

<details>
<summary>Python SDK: Add a term to a query</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_add_term.py
# metadata-ingestion/examples/library/query_add_term.py
import logging

from datahub.emitter.mce_builder import make_term_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DataHubGraphConfig
from datahub.metadata.schema_classes import (
    AuditStampClass,
    GlossaryTermAssociationClass,
    GlossaryTermsClass,
)
from datahub.metadata.urns import QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_urn = QueryUrn("my-unique-query-id")

graph = DataHubGraph(DataHubGraphConfig(server="http://localhost:8080"))
emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

existing_terms = graph.get_aspect(
    entity_urn=query_urn.urn(),
    aspect_type=GlossaryTermsClass,
)

terms_to_add = existing_terms.terms if existing_terms else []

terms_to_add.append(
    GlossaryTermAssociationClass(
        urn=make_term_urn("CustomerData"), context="Query subject area"
    )
)

glossary_terms_aspect = GlossaryTermsClass(
    terms=terms_to_add,
    auditStamp=AuditStampClass(time=0, actor="urn:li:corpuser:datahub"),
)

event = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=glossary_terms_aspect,
)

emitter.emit(event)
log.info(f"Added glossary term to query {query_urn}")

```

</details>

### Ownership

Ownership is associated to a query using the `ownership` aspect. Owners can be of different types such as `TECHNICAL_OWNER`, `BUSINESS_OWNER`, `DATA_STEWARD`, etc. Ownership helps identify who is responsible for maintaining and understanding specific queries.

<details>
<summary>Python SDK: Add an owner to a query</summary>

```python
# Inlined from /metadata-ingestion/examples/library/query_add_owner.py
# metadata-ingestion/examples/library/query_add_owner.py
import logging

from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.ingestion.graph.client import DataHubGraph, DataHubGraphConfig
from datahub.metadata.schema_classes import (
    OwnerClass,
    OwnershipClass,
    OwnershipTypeClass,
)
from datahub.metadata.urns import CorpUserUrn, QueryUrn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

query_urn = QueryUrn("my-unique-query-id")

graph = DataHubGraph(DataHubGraphConfig(server="http://localhost:8080"))
emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

existing_ownership = graph.get_aspect(
    entity_urn=query_urn.urn(),
    aspect_type=OwnershipClass,
)

owners = existing_ownership.owners if existing_ownership else []

new_owner = OwnerClass(
    owner=CorpUserUrn("jdoe").urn(),
    type=OwnershipTypeClass.TECHNICAL_OWNER,
)

if new_owner not in owners:
    owners.append(new_owner)

ownership_aspect = OwnershipClass(
    owners=owners,
)

event = MetadataChangeProposalWrapper(
    entityUrn=query_urn.urn(),
    aspect=ownership_aspect,
)

emitter.emit(event)
log.info(f"Added owner to query {query_urn}")

```

</details>

### Platform Instance

The `dataPlatformInstance` aspect allows you to specify which specific instance of a data platform the query is associated with. This is useful when you have multiple instances of the same platform (e.g., multiple Snowflake accounts or BigQuery projects).

## Integration Points

### Relationship with Datasets

Queries have a fundamental relationship with dataset entities through the `querySubjects` aspect. Each subject in a query references a dataset URN, creating a bidirectional relationship that allows you to:

- Navigate from a query to the datasets it references
- Navigate from a dataset to all queries that reference it

This relationship is crucial for understanding dataset usage and query-based lineage.

### Lineage Integration

Queries play a central role in DataHub's lineage capabilities:

- **Query-based Lineage**: When DataHub processes SQL queries (either from query logs or manually provided), it performs SQL parsing to extract column-level lineage information. This lineage is then attached to datasets, showing how data flows from source columns to destination columns through SQL transformations.

- **Fine-grained Lineage**: Queries can be referenced in fine-grained lineage edges on datasets, providing the SQL context for how specific columns are derived. The query URN is stored in the `query` field of fine-grained lineage information.

- **Origin Tracking**: Queries can have an `origin` field pointing to the entity they came from (e.g., a View or Stored Procedure), creating a traceable chain from the query execution back to its source definition.

### Ingestion Sources

Several DataHub ingestion connectors automatically discover and create query entities:

- **BigQuery**: Extracts queries from audit logs and information schema
- **Snowflake**: Processes query history from account usage views
- **Redshift**: Reads from system tables like `STL_QUERY` and `SVL_QUERY`
- **SQL Queries Source**: A generic connector that can process query logs from any SQL database
- **Mode**: Extracts queries from Mode reports and analyses
- **Hex**: Discovers queries from Hex notebook cells

These connectors typically:

1. Fetch query logs with SQL statements and metadata
2. Parse the SQL to identify referenced tables
3. Create query entities with appropriate properties and subjects
4. Generate usage statistics as timeseries data
5. Emit column-level lineage derived from SQL parsing

### GraphQL API

Queries can be created, updated, and deleted through the DataHub GraphQL API:

- **createQuery**: Creates a new query with specified properties and subjects
- **updateQuery**: Updates an existing query's name, description, or statement
- **deleteQuery**: Soft-deletes a query entity

These mutations are available through the GraphQL endpoint and are used by the DataHub UI for manual query management.

### Usage Analytics

Query entities contribute to dataset usage analytics. When query usage statistics are ingested, they:

- Increment the dataset's usage counts
- Track which users are querying which datasets
- Provide insights into query patterns and frequency
- Help identify high-value datasets based on query activity

## Notable Exceptions

### Query Deduplication

Queries are automatically deduplicated based on their normalized query text. This means that:

- Whitespace differences are ignored
- Comments are typically removed during normalization
- Identical queries from different users or time periods are merged into a single query entity
- Usage statistics are aggregated across all executions of the same normalized query

This deduplication is essential for managing the volume of queries in large-scale deployments.

### Temporary Tables

When processing queries that involve temporary tables, the SQL parsing aggregator maintains session context to:

- Track temporary table creation and usage within a session
- Resolve lineage through temporary tables to underlying permanent tables
- Avoid creating query subjects that reference ephemeral temporary tables

This ensures that query lineage reflects the actual data dependencies rather than intermediate temporary structures.

### Query Size Limits

Very large query statements (e.g., generated queries with thousands of lines) may be truncated or rejected to maintain system performance. The exact limits depend on the backend configuration and the storage layer.

### Language Support

Currently, query entities primarily support SQL as the query language. While there is an `UNKNOWN` language option, DataHub's SQL parsing and lineage extraction capabilities are specifically designed for SQL dialects. Other query languages (e.g., Cypher, SPARQL, or proprietary query languages) can be stored but will not benefit from automatic lineage extraction.

### Manual vs System Queries

Queries can have two sources:

- `MANUAL`: Queries created by users through the DataHub UI or API
- `SYSTEM`: Queries discovered automatically by ingestion connectors

This distinction helps differentiate between user-curated queries (which might be documented and named) and the potentially large volume of queries automatically discovered from query logs.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Technical Reference Guide

The sections above provide an overview of how to use this entity. The following sections provide detailed technical information about how metadata is stored and represented in DataHub.

**Aspects** are the individual pieces of metadata that can be attached to an entity. Each aspect contains specific information (like ownership, tags, or properties) and is stored as a separate record, allowing for flexible and incremental metadata updates.

**Relationships** show how this entity connects to other entities in the metadata graph. These connections are derived from the fields within each aspect and form the foundation of DataHub's knowledge graph.

### Reading the Field Tables

Each aspect's field table includes an **Annotations** column that provides additional metadata about how fields are used:

- **⚠️ Deprecated**: This field is deprecated and may be removed in a future version. Check the description for the recommended alternative
- **Searchable**: This field is indexed and can be searched in DataHub's search interface
- **Searchable (fieldname)**: When the field name in parentheses is shown, it indicates the field is indexed under a different name in the search index. For example, `dashboardTool` is indexed as `tool`
- **→ RelationshipName**: This field creates a relationship to another entity. The arrow indicates this field contains a reference (URN) to another entity, and the name indicates the type of relationship (e.g., `→ Contains`, `→ OwnedBy`)

Fields with complex types (like `Edge`, `AuditStamp`) link to their definitions in the [Common Types](#common-types) section below.

### Aspects

#### queryProperties
Information about a Query against one or more data assets (e.g. Tables or Views).

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| customProperties | map | ✓ | Custom property bag. | Searchable |
| statement | QueryStatement | ✓ | The Query Statement. |  |
| source | QuerySource | ✓ | The source of the Query | Searchable |
| name | string |  | Optional display name to identify the query. | Searchable |
| description | string |  | The Query description. |  |
| created | [AuditStamp](#auditstamp) | ✓ | Audit stamp capturing the time and actor who created the Query. | Searchable |
| lastModified | [AuditStamp](#auditstamp) | ✓ | Audit stamp capturing the time and actor who last modified the Query. | Searchable |
| origin | string |  | The origin of the Query. This is the source of the Query (e.g. a View, Stored Procedure, dbt Mode... | Searchable |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "queryProperties"
  },
  "name": "QueryProperties",
  "namespace": "com.linkedin.query",
  "fields": [
    {
      "Searchable": {
        "/*": {
          "fieldType": "TEXT",
          "queryByDefault": true
        }
      },
      "type": {
        "type": "map",
        "values": "string"
      },
      "name": "customProperties",
      "default": {},
      "doc": "Custom property bag."
    },
    {
      "type": {
        "type": "record",
        "name": "QueryStatement",
        "namespace": "com.linkedin.query",
        "fields": [
          {
            "type": "string",
            "name": "value",
            "doc": "The query text"
          },
          {
            "type": {
              "type": "enum",
              "symbolDocs": {
                "SQL": "A SQL Query",
                "UNKNOWN": "Unknown query language"
              },
              "name": "QueryLanguage",
              "namespace": "com.linkedin.query",
              "symbols": [
                "SQL",
                "UNKNOWN"
              ]
            },
            "name": "language",
            "default": "SQL",
            "doc": "The language of the Query, e.g. SQL."
          }
        ],
        "doc": "A query statement against one or more data assets."
      },
      "name": "statement",
      "doc": "The Query Statement."
    },
    {
      "Searchable": {},
      "type": {
        "type": "enum",
        "symbolDocs": {
          "MANUAL": "The query was entered manually by a user (via the UI).",
          "SYSTEM": "The query was discovered by a crawler."
        },
        "name": "QuerySource",
        "namespace": "com.linkedin.query",
        "symbols": [
          "MANUAL",
          "SYSTEM"
        ]
      },
      "name": "source",
      "doc": "The source of the Query"
    },
    {
      "Searchable": {
        "boostScore": 10.0,
        "enableAutocomplete": true,
        "fieldType": "WORD_GRAM"
      },
      "type": [
        "null",
        "string"
      ],
      "name": "name",
      "default": null,
      "doc": "Optional display name to identify the query."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "description",
      "default": null,
      "doc": "The Query description."
    },
    {
      "Searchable": {
        "/actor": {
          "fieldName": "createdBy",
          "fieldType": "URN"
        },
        "/time": {
          "fieldName": "createdAt",
          "fieldType": "DATETIME"
        }
      },
      "type": {
        "type": "record",
        "name": "AuditStamp",
        "namespace": "com.linkedin.common",
        "fields": [
          {
            "type": "long",
            "name": "time",
            "doc": "When did the resource/association/sub-resource move into the specific lifecycle stage represented by this AuditEvent."
          },
          {
            "java": {
              "class": "com.linkedin.common.urn.Urn"
            },
            "type": "string",
            "name": "actor",
            "doc": "The entity (e.g. a member URN) which will be credited for moving the resource/association/sub-resource into the specific lifecycle stage. It is also the one used to authorize the change."
          },
          {
            "java": {
              "class": "com.linkedin.common.urn.Urn"
            },
            "type": [
              "null",
              "string"
            ],
            "name": "impersonator",
            "default": null,
            "doc": "The entity (e.g. a service URN) which performs the change on behalf of the Actor and must be authorized to act as the Actor."
          },
          {
            "type": [
              "null",
              "string"
            ],
            "name": "message",
            "default": null,
            "doc": "Additional context around how DataHub was informed of the particular change. For example: was the change created by an automated process, or manually."
          }
        ],
        "doc": "Data captured on a resource/association/sub-resource level giving insight into when that resource/association/sub-resource moved into a particular lifecycle stage, and who acted to move it into that specific lifecycle stage."
      },
      "name": "created",
      "doc": "Audit stamp capturing the time and actor who created the Query."
    },
    {
      "Searchable": {
        "/actor": {
          "fieldName": "lastModifiedBy",
          "fieldType": "URN"
        },
        "/time": {
          "fieldName": "lastModifiedAt",
          "fieldType": "DATETIME"
        }
      },
      "type": "com.linkedin.common.AuditStamp",
      "name": "lastModified",
      "doc": "Audit stamp capturing the time and actor who last modified the Query."
    },
    {
      "Searchable": {
        "addToFilters": false,
        "fieldType": "URN",
        "queryByDefault": false
      },
      "java": {
        "class": "com.linkedin.common.urn.Urn"
      },
      "type": [
        "null",
        "string"
      ],
      "name": "origin",
      "default": null,
      "doc": "The origin of the Query.\nThis is the source of the Query (e.g. a View, Stored Procedure, dbt Model, etc.) that the Query was created from."
    }
  ],
  "doc": "Information about a Query against one or more data assets (e.g. Tables or Views)."
}
```

</TabItem>
</Tabs>


#### querySubjects
Information about the subjects of a particular Query, i.e. the assets
being queried.

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| subjects | QuerySubject[] | ✓ | One or more subjects of the query.  In single-asset queries (e.g. table select), this will contai... |  |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "querySubjects"
  },
  "name": "QuerySubjects",
  "namespace": "com.linkedin.query",
  "fields": [
    {
      "type": {
        "type": "array",
        "items": {
          "type": "record",
          "name": "QuerySubject",
          "namespace": "com.linkedin.query",
          "fields": [
            {
              "Searchable": {
                "fieldName": "entities",
                "fieldType": "KEYWORD"
              },
              "java": {
                "class": "com.linkedin.common.urn.Urn"
              },
              "type": "string",
              "name": "entity",
              "doc": "An entity which is the subject of a query."
            }
          ],
          "doc": "A single subject of a particular query.\nIn the future, we may evolve this model to include richer details\nabout the Query Subject in relation to the query."
        }
      },
      "name": "subjects",
      "doc": "One or more subjects of the query.\n\nIn single-asset queries (e.g. table select), this will contain the Table reference\nand optionally schema field references.\n\nIn multi-asset queries (e.g. table joins), this may contain multiple Table references\nand optionally schema field references."
    }
  ],
  "doc": "Information about the subjects of a particular Query, i.e. the assets\nbeing queried."
}
```

</TabItem>
</Tabs>


#### status
The lifecycle status metadata of an entity, e.g. dataset, metric, feature, etc.
This aspect is used to represent soft deletes conventionally.

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| removed | boolean | ✓ | Whether the entity has been removed (soft-deleted). | Searchable |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "status"
  },
  "name": "Status",
  "namespace": "com.linkedin.common",
  "fields": [
    {
      "Searchable": {
        "fieldType": "BOOLEAN"
      },
      "type": "boolean",
      "name": "removed",
      "default": false,
      "doc": "Whether the entity has been removed (soft-deleted)."
    }
  ],
  "doc": "The lifecycle status metadata of an entity, e.g. dataset, metric, feature, etc.\nThis aspect is used to represent soft deletes conventionally."
}
```

</TabItem>
</Tabs>


#### dataPlatformInstance
The specific instance of the data platform that this entity belongs to

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| platform | string | ✓ | Data Platform | Searchable |
| instance | string |  | Instance of the data platform (e.g. db instance) | Searchable (platformInstance) |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "dataPlatformInstance"
  },
  "name": "DataPlatformInstance",
  "namespace": "com.linkedin.common",
  "fields": [
    {
      "Searchable": {
        "addToFilters": true,
        "fieldType": "URN",
        "filterNameOverride": "Platform"
      },
      "java": {
        "class": "com.linkedin.common.urn.Urn"
      },
      "type": "string",
      "name": "platform",
      "doc": "Data Platform"
    },
    {
      "Searchable": {
        "addToFilters": true,
        "fieldName": "platformInstance",
        "fieldType": "URN",
        "filterNameOverride": "Platform Instance"
      },
      "java": {
        "class": "com.linkedin.common.urn.Urn"
      },
      "type": [
        "null",
        "string"
      ],
      "name": "instance",
      "default": null,
      "doc": "Instance of the data platform (e.g. db instance)"
    }
  ],
  "doc": "The specific instance of the data platform that this entity belongs to"
}
```

</TabItem>
</Tabs>


#### subTypes
Sub Types. Use this aspect to specialize a generic Entity
e.g. Making a Dataset also be a View or also be a LookerExplore

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| typeNames | string[] | ✓ | The names of the specific types. | Searchable |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "subTypes"
  },
  "name": "SubTypes",
  "namespace": "com.linkedin.common",
  "fields": [
    {
      "Searchable": {
        "/*": {
          "addToFilters": true,
          "fieldType": "KEYWORD",
          "filterNameOverride": "Sub Type",
          "queryByDefault": false
        }
      },
      "type": {
        "type": "array",
        "items": "string"
      },
      "name": "typeNames",
      "doc": "The names of the specific types."
    }
  ],
  "doc": "Sub Types. Use this aspect to specialize a generic Entity\ne.g. Making a Dataset also be a View or also be a LookerExplore"
}
```

</TabItem>
</Tabs>


#### queryUsageStatistics (Timeseries)
Stats corresponding to dataset's usage.

<Tabs>
<TabItem value="fields" label="Fields" default>


| Field | Type | Required | Description | Annotations |
|-------|------|----------|-------------|-------------|
| timestampMillis | long | ✓ | The event timestamp field as epoch at UTC in milli seconds. |  |
| eventGranularity | TimeWindowSize |  | Granularity of the event if applicable |  |
| partitionSpec | PartitionSpec |  | The optional partition specification. |  |
| messageId | string |  | The optional messageId, if provided serves as a custom user-defined unique identifier for an aspe... |  |
| queryCount | int |  | Total query count in this bucket |  |
| queryCost | double |  | Query cost for this query and bucket |  |
| lastExecutedAt | long |  | Last executed timestamp |  |
| uniqueUserCount | int |  | Unique user count |  |
| userCounts | DatasetUserUsageCounts[] |  | Users within this bucket, with frequency counts |  |

</TabItem>
<TabItem value="raw" label="Raw Schema">

```javascript
{
  "type": "record",
  "Aspect": {
    "name": "queryUsageStatistics",
    "type": "timeseries"
  },
  "name": "QueryUsageStatistics",
  "namespace": "com.linkedin.query",
  "fields": [
    {
      "type": "long",
      "name": "timestampMillis",
      "doc": "The event timestamp field as epoch at UTC in milli seconds."
    },
    {
      "type": [
        "null",
        {
          "type": "record",
          "name": "TimeWindowSize",
          "namespace": "com.linkedin.timeseries",
          "fields": [
            {
              "type": {
                "type": "enum",
                "name": "CalendarInterval",
                "namespace": "com.linkedin.timeseries",
                "symbols": [
                  "SECOND",
                  "MINUTE",
                  "HOUR",
                  "DAY",
                  "WEEK",
                  "MONTH",
                  "QUARTER",
                  "YEAR"
                ]
              },
              "name": "unit",
              "doc": "Interval unit such as minute/hour/day etc."
            },
            {
              "type": "int",
              "name": "multiple",
              "default": 1,
              "doc": "How many units. Defaults to 1."
            }
          ],
          "doc": "Defines the size of a time window."
        }
      ],
      "name": "eventGranularity",
      "default": null,
      "doc": "Granularity of the event if applicable"
    },
    {
      "type": [
        {
          "type": "record",
          "name": "PartitionSpec",
          "namespace": "com.linkedin.timeseries",
          "fields": [
            {
              "TimeseriesField": {},
              "type": "string",
              "name": "partition",
              "doc": "A unique id / value for the partition for which statistics were collected,\ngenerated by applying the key definition to a given row."
            },
            {
              "type": [
                "null",
                {
                  "type": "record",
                  "name": "TimeWindow",
                  "namespace": "com.linkedin.timeseries",
                  "fields": [
                    {
                      "type": "long",
                      "name": "startTimeMillis",
                      "doc": "Start time as epoch at UTC."
                    },
                    {
                      "type": "com.linkedin.timeseries.TimeWindowSize",
                      "name": "length",
                      "doc": "The length of the window."
                    }
                  ]
                }
              ],
              "name": "timePartition",
              "default": null,
              "doc": "Time window of the partition, if we are able to extract it from the partition key."
            },
            {
              "deprecated": true,
              "type": {
                "type": "enum",
                "name": "PartitionType",
                "namespace": "com.linkedin.timeseries",
                "symbols": [
                  "FULL_TABLE",
                  "QUERY",
                  "PARTITION"
                ]
              },
              "name": "type",
              "default": "PARTITION",
              "doc": "Unused!"
            }
          ],
          "doc": "A reference to a specific partition in a dataset."
        },
        "null"
      ],
      "name": "partitionSpec",
      "default": {
        "partition": "FULL_TABLE_SNAPSHOT",
        "type": "FULL_TABLE",
        "timePartition": null
      },
      "doc": "The optional partition specification."
    },
    {
      "type": [
        "null",
        "string"
      ],
      "name": "messageId",
      "default": null,
      "doc": "The optional messageId, if provided serves as a custom user-defined unique identifier for an aspect value."
    },
    {
      "TimeseriesField": {},
      "type": [
        "null",
        "int"
      ],
      "name": "queryCount",
      "default": null,
      "doc": "Total query count in this bucket"
    },
    {
      "TimeseriesField": {},
      "type": [
        "null",
        "double"
      ],
      "name": "queryCost",
      "default": null,
      "doc": "Query cost for this query and bucket"
    },
    {
      "TimeseriesField": {},
      "type": [
        "null",
        "long"
      ],
      "name": "lastExecutedAt",
      "default": null,
      "doc": "Last executed timestamp"
    },
    {
      "TimeseriesField": {},
      "type": [
        "null",
        "int"
      ],
      "name": "uniqueUserCount",
      "default": null,
      "doc": "Unique user count"
    },
    {
      "TimeseriesFieldCollection": {
        "key": "user"
      },
      "type": [
        "null",
        {
          "type": "array",
          "items": {
            "type": "record",
            "name": "DatasetUserUsageCounts",
            "namespace": "com.linkedin.dataset",
            "fields": [
              {
                "java": {
                  "class": "com.linkedin.common.urn.Urn"
                },
                "type": "string",
                "name": "user",
                "doc": "The unique id of the user."
              },
              {
                "TimeseriesField": {},
                "type": "int",
                "name": "count",
                "doc": "Number of times the dataset has been used by the user."
              },
              {
                "TimeseriesField": {},
                "type": [
                  "null",
                  "string"
                ],
                "name": "userEmail",
                "default": null,
                "doc": "If user_email is set, we attempt to resolve the user's urn upon ingest"
              }
            ],
            "doc": "Records a single user's usage counts for a given resource"
          }
        }
      ],
      "name": "userCounts",
      "default": null,
      "doc": "Users within this bucket, with frequency counts"
    }
  ],
  "doc": "Stats corresponding to dataset's usage."
}
```

</TabItem>
</Tabs>


### Common Types

These types are used across multiple aspects in this entity.

#### AuditStamp

Data captured on a resource/association/sub-resource level giving insight into when that resource/association/sub-resource moved into a particular lifecycle stage, and who acted to move it into that specific lifecycle stage.

**Fields:**

- `time` (long): When did the resource/association/sub-resource move into the specific lifecyc...
- `actor` (string): The entity (e.g. a member URN) which will be credited for moving the resource...
- `impersonator` (string?): The entity (e.g. a service URN) which performs the change on behalf of the Ac...
- `message` (string?): Additional context around how DataHub was informed of the particular change. ...


### Relationships

### [Global Metadata Model](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)
![Global Graph](https://github.com/datahub-project/static-assets/raw/main/imgs/datahub-metadata-model.png)


:::note 💡 **Contributing to this documentation**
This page is auto-generated from the underlying source code. To make changes, please edit the relevant source files in the [metadata-models](https://github.com/datahub-project/datahub/tree/master/metadata-models) directory. 

**Tip:** For quick typo fixes or documentation updates, you can click the ✏️ **Edit** icon directly in the GitHub UI to open a Pull Request. For larger changes and PR naming conventions, please refer to our [Contributing Guide](/docs/contributing).
:::
