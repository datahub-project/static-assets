---
title: DataHub Releases
sidebar_label: Releases
slug: /releases
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs-website/generateDocsDir.ts
---

# DataHub Releases

## Summary

| Version | Release Date | Links |
| ------- | ------------ | ----- |
| **v1.5.0.1** | 2026-03-25 |[Release Notes](#v1-5-0-1), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.5.0.1) |
| **v1.5.0** | 2026-03-24 |[Release Notes](#v1-5-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.5.0) |
| **v1.4.0.3** | 2026-02-19 |[Release Notes](#v1-4-0-3), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.4.0.3) |
| **v1.4.0.2** | 2026-02-10 |[Release Notes](#v1-4-0-2), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.4.0.2) |
| **v1.4.0** | 2026-02-06 |[Release Notes](#v1-4-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.4.0) |
| **v1.3.0.1** | 2025-11-12 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.3.0.1) |
| **v1.3.0** | 2025-10-06 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.3.0) |


## [v1.5.0.1](https://github.com/datahub-project/datahub/releases/tag/v1.5.0.1) {#v1-5-0-1}

Released on 2026-03-25 by [@david-leifker](https://github.com/david-leifker).

### Changes

Include bundled venvs for datahub-gc, datahub-documents

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v1.5.0...v1.5.0.1

## [v1.5.0](https://github.com/datahub-project/datahub/releases/tag/v1.5.0) {#v1-5-0}

Released on 2026-03-24 by [@david-leifker](https://github.com/david-leifker).

### **DataHub v1.5.0 Release Notes**

**Helm Chart Requirement:** `0.9.2`
 **Full technical release notes:** [Updating DataHub](https://github.com/datahub-project/datahub/blob/master/docs/how/updating-datahub.md)

**Product Features**

* **V1 UI officially sunset.** All development targets V2 UI going forward. Ensure `THEME_V2_ENABLED=true` and `THEME_V2_DEFAULT=true`.  
* **Multiple data products per asset** (backend and UI).  
* **Policy targeting by Glossary Terms and Groups.**  
* **Domain-scoped policies** now include child domain assets.  
* **`datahub search` CLI** with semantic search, query projection, and agent-context integration.

#### **Platform**

* **Java 17 runtime required.** Spark upgraded to 3.3.4, Hadoop to 3.3.6. Spark lineage users must be on Spark 3.3.0+.  
* **Default token signing key & salt removed.** Operators must explicitly set `DATAHUB_TOKEN_SERVICE_SIGNING_KEY` and `DATAHUB_TOKEN_SERVICE_SALT`. Helm users are unaffected.  
* **Retention service disabled \= no version history.** Only the current version (v0) is retained when the retention service is not enabled.  
* **TLS 1.0/1.1 disabled** on frontend custom truststores.  
* **Elasticsearch reindex/index-creation retries** for improved upgrade resilience.  
* **Kubernetes optional scale-down during system-update** for blocking upgrades like reindexing. Disabled by default.  
* **SDK: `emit_mcps()` now returns `List[TraceData]`** instead of `int`. Trace IDs exposed for `SYNC_PRIMARY` and `ASYNC` modes.  
* **Reproducible ingestion Docker builds** via pinned transitive dependencies (`uv.lock`, `constraints.txt`).  
* **Python deps migrating** from `setup.py` to `pyproject.toml` (PEP 621); `setup.py` still the editing source for now.

#### **Ingestion**

##### **New Connectors**

* **RDF**, **Snowplow**, **Apache Doris**

##### **Breaking Changes (see migration guide for details)**

* **PowerBI M-Query lineage** rewritten using Microsoft's official parser. `native_query_parsing: false` behavior changed.  
* **SQL view query IDs** now use SHA-256 hashes — old query entities become orphaned. Use stateful ingestion to clean up.  
* **Oracle multitenant URNs** now use PDB name instead of CDB name when connecting via `service_name`.  
* **Fabric OneLake** workspace containers moved to `fabric` platform (from `fabric-onelake`).  
* **Vertex AI** pipeline URNs restructured for stable DataFlow entities; ML Metadata extraction enabled by default (requires additional GCP permissions).  
* **DataHub source** now uses URN pattern filtering to exclude secrets, ingestion sources, and execution requests by default.  
* **Kafka Connect Debezium SQL Server** platform changed from `sqlserver` to `mssql`.

##### **Enhancements**

* **dbt:** Semantic model and exposures ingestion; `convert_urns_to_lowercase` option for case-insensitive platforms.  
* **Snowflake:** Metadata pattern pushdown, table type filtering, external DMF assertion ingestion.  
* **Power BI:** Column-level lineage enabled by default.  
* **Kafka Connect:** Debezium and Confluent JDBC sink connector support; bundled JVM removes system Java requirement.  
* **SQL parsing:** Major CTE/subquery join resolution performance improvements across all SQL-based connectors.  
* **Mode:** Concurrent API fetching, response caching, SQL parsing optimizations.  
* **Trino:** Column-level lineage on upstream datasets.  
* **Iceberg:** Ingestion-time domain assignment.  
* **Azure Data Factory:** Column lineage for Copy activity.  
* **Airflow plugin:** Multi-statement SQL parsing for lineage.  
* **Sigma:** Workbook filtering.  
* **BigQuery:** `convert_column_urns_to_lowercase` option.  
* **Kafka source:** Option to disable Avro schema name validation.  
* **Great Expectations & SQLAlchemy profilers** brought to feature parity.  
* **Browse paths:** DataFlow/DataJob entities get `browsePathsV2` with platform instance when configured.  
* **Vertex AI:** Cross-platform lineage, hierarchical UI folders, stateful ingestion for large projects.  
* **Oracle:** Fixed container naming with `service_name`.  
* **Configurable report sample sizes** and richer failure logging.

#### **Deprecations**

* **Vertex AI:** `region` → `regions`, `project_id` → `project_ids`. Old fields still work.  
* **Vertex AI:** `normalize_external_dataset_paths` will default to `true` in the next major version.



**Full Changelog**: https://github.com/datahub-project/datahub/compare/v1.4.0.3...v1.5.0

## [v1.4.0.3](https://github.com/datahub-project/datahub/releases/tag/v1.4.0.3) {#v1-4-0-3}

Released on 2026-02-19 by [@jjoyce0510](https://github.com/jjoyce0510).

### Release Highlights

- This minor release addresses a bug in Semantic Search configuration where the modelId was not respecting the environment variables for OpenAI + Cohere (Non-Bedrock embeddings model). Please use this release if you intend to leverage the Documents & semantic search capabilities in DataHub.

#### What's Changed
* [semantic-search] semantic search improvements for clarity ([#16250](https://github.com/datahub-project/datahub/pull/16250)) by [@nwadams](https://github.com/nwadams) in https://github.com/datahub-project/datahub/pull/16267
* [v1.4.0.3] bump default cli version ([#16268](https://github.com/datahub-project/datahub/pull/16268)) by [@nwadams](https://github.com/nwadams) in https://github.com/datahub-project/datahub/pull/16269
* fix(ingest): constrain setuptools&lt;82 to fix pkg_resources runtime error by [@kyungsoo-datahub](https://github.com/kyungsoo-datahub) in https://github.com/datahub-project/datahub/pull/16283
* fix(semanticsearchretry): ensure retry for semanticsearch ([#16281](https://github.com/datahub-project/datahub/pull/16281)) by [@nwadams](https://github.com/nwadams) in https://github.com/datahub-project/datahub/pull/16286


**Full Changelog**: https://github.com/datahub-project/datahub/compare/v1.4.0.2...v1.4.0.3

## [v1.4.0.2](https://github.com/datahub-project/datahub/releases/tag/v1.4.0.2) {#v1-4-0-2}

Released on 2026-02-10 by [@david-leifker](https://github.com/david-leifker).

There is no version `v1.4.0.1`, moving to `v1.4.0.2` to be consistent with the CLI version for this release.

Changes:
* Bump default CLI version

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v1.4.0...v1.4.0.2

## [v1.4.0](https://github.com/datahub-project/datahub/releases/tag/v1.4.0) {#v1-4-0}

Released on 2026-02-06 by [@jjoyce0510](https://github.com/jjoyce0510).

> Notice: If you're interested in configuring the document cataloging & semantic search features, please upgrade to v1.4.0.3 which includes some small improvements & fixes for the configuration experience for semantic search. 

### Release Highlights

DataHub v1.4.0 is packed with exciting updates, including:

- **AI & Context:** Introducing Context Documents for bringing organizational knowledge to DataHub. Create context documents directly on DataHub, or import them from Notion & Confluence. Curate, refine, and semantically search across your documents using [DataHub MCP Server](https://github.com/acryldata/mcp-server-datahub) & [Agent Context Kit](https://docs.datahub.com/docs/dev-guides/agent-context/agent-context). Requires admin configuration.

- **Major UI Improvements:** Redesigned ingestion source creation workflow with guided step-by-step experience, modernized login/signup pages, support for Service Accounts, new asset “Summary” profile tab with modular layout, and ability to upload files to asset documentation. Read more below!

- **New Ingestion Connectors:** New connectors for Google Dataplex, Azure Data Factory, IBM Db2, Notion, & Confluence. Major enhancements include Airflow 3.x support, Snowflake Streamlit apps and Semantic Views ingestion, Databricks OAuth authentication, and Kafka Connect Confluent Cloud integration.

- **SDK Features:** New Java SDK V2 with fluent builder API, Python SDK Tag entity support, parametrized assertion runs, and full Pydantic v2 migration.

- **Platform Improvements:** Elasticsearch 8 support with multi-client shim and semantic search infrastructure.

---

### User Experience

This release includes significant improvements to the user interface and user experience:

#### Improved Experiences: Home Page, Lineage Explorer, Entity Profiles, & More

**Simplified Home Page**

DataHub’s simplified, modular home page experience is now enabled by default for all DataHub instances. 

Learn more about the new Home Page [here](https://docs.datahub.com/docs/features/feature-guides/custom-home-page). 

&lt;img width="1725" height="878" alt="Screenshot 2026-02-03 at 7 05 21 PM" src="https://github.com/user-attachments/assets/6fff44da-a4cf-4937-b2df-5abf038ed137" />

Support for the old home page will be dropped in an upcoming release. Until that time, you may revert to the previous home page by setting following environment variable in the `datahub-gms`:

- `SHOW_HOME_PAGE_REDESIGN` to `false`

**Entity Profile Summary Tabs**

Check out the new summary tabs available on Domain, Glossary Term, & Data Product profile pages. Summaries provide an overview of the key details about each entity at a glance. 

&lt;img width="1663" height="873" alt="Screenshot 2026-02-03 at 7 05 45 PM" src="https://github.com/user-attachments/assets/cdffc796-f50f-4e71-883e-7ff6f443ac54" />

**Streamlined Data Lineage Explorer**

Experience the most seamless version of data lineage yet. Seamlessly navigate across data dependencies with the redesigned lineage navigator. Behavior should largely remain the same as with the old lineage UI. In a future release, the old UI will be removed. For now, you can revert to it by setting following environment variable in the `datahub-gms`:

- `LINEAGE_GRAPH_V3` to `false`

&lt;img width="1721" height="887" alt="Screenshot 2026-02-03 at 7 08 56 PM" src="https://github.com/user-attachments/assets/01a05afa-9308-4d85-a7a2-5e423b24fe10" />

**Other UX Improvements**

We’ve also included modernized Ingestion, Login, Sign Up, and Analytics pages in this release. Check them out and let us know what you think! 

**Important**: Note that we’ve disabled the legacy UI for DataHub by default as of this release. You’ll no longer be able to toggle between the legacy UI & new UI in settings - the new UI will be visible by default. In future releases, the legacy UI will be removed from the UI codebase completely. 

#### Context Documents & Semantic Search

Introducing Context Documents V1, a new feature that allows adding AI-related context and documentation to assets, & optional configurability for semantic search (beta). 

- Added models and APIs for Context Documents [[#15280](https://github.com/datahub-project/datahub/pull/15280)]
- Introduced UI flows for Context Documents. [[#15279](https://github.com/datahub-project/datahub/pull/15279)]
- Various UI improvements for Context Documents. [[#15413](https://github.com/datahub-project/datahub/pull/15413)]
- Support viewing and adding related context to all asset types. [[#15453](https://github.com/datahub-project/datahub/pull/15453)]
- Support for ingesting external context documents from [Notion](https://docs.datahub.com/docs/generated/ingestion/sources/notion) & [Confluence](https://docs.datahub.com/docs/generated/ingestion/sources/confluence) (see Ingestion Updates below).
- Support for configuring semantic indexing of document contents, and semantic search via the `semanticSearchAcrossEntities` GraphQL resolver, through [DataHub MCP Server](https://github.com/acryldata/mcp-server-datahub), and via the [Agent Context Kit](https://docs.datahub.com/docs/dev-guides/agent-context/agent-context) document search tools.
    - Note that semantic search must happen via Ingestion Recipes ([Notion](https://docs.datahub.com/docs/generated/ingestion/sources/notion), [Confluence](https://docs.datahub.com/docs/generated/ingestion/sources/confluence), or [DataHub Documents](https://docs.datahub.com/docs/generated/ingestion/sources/datahub-documents) ingestion source). For more details, see [Semantic Search Configuration](https://docs.datahub.com/docs/how-to/semantic-search-configuration).
    - Semantic Search is only supported if you are using OpenSearch version 2.19.3+. It is NOT currently supported for Elasticsearch deployments.

This feature is enabled by default, but can be disabled by setting the following environment variable in the `datahub-gms`:

- `CONTEXT_DOCUMENTS_ENABLED`  to `false`

Read more about Context Documents [here](https://docs.datahub.com/docs/features/feature-guides/context/context-documents). And read about configuring platform capabilities required for semantic search [here](https://docs.datahub.com/docs/how-to/semantic-search-configuration). 

#### Agent Context Kit: Snowflake, LangChain, MCP Server

As of v1.4.0, DataHub is publishing a new [Agent Context Kit](https://docs.datahub.com/docs/dev-guides/agent-context/agent-context) Python library.

Shipped in this release:

- **Snowflake**: Providing a new `datahub agent` CLI command that enables you to provision a Snowflake Cortex Agent that automatically has access to various DataHub tools for searching assets, documents, retrieving lineage, sample queries, and more. Learn more [here](https://docs.datahub.com/docs/dev-guides/agent-context/snowflake).
- **LangChain**: Providing a Python tools library that enables you to easily build LangChain Agents with access to DataHub assets & metadata. Learn more [here](https://docs.datahub.com/docs/dev-guides/agent-context/langchain).

In addition, we’ve also made some important additions to the [DataHub MCP Server](https://github.com/acryldata/mcp-server-datahub) to add a host of new tools:

- **Mutation Tools:** Edit tags, terms, owners, descriptions, structured properties, domains, & more.
- **Document Tools**: Search (keyword OR semantic) across context documents, create new documents in the “Shared” space.

Which will be available in the `v0.5.0` version of DataHub MCP Server. 

#### Service Accounts

Support for creating named service accounts, generating API access tokens, and granting permissions via DataHub’s [Access Policies](https://docs.datahub.com/docs/authorization/access-policies-guide/) system. Useful for creating dedicated 

- Add support for service accounts in DataHub [[#52765](https://github.com/datahub-project/datahub/pull/52765)]

This feature is enabled by default. Read more about service accounts [here](https://docs.datahub.com/docs/features/feature-guides/service-accounts). 

#### Upload Files to Asset Documentation

New capability to upload and download files when documenting any types of assets in DataHub using configurable S3 storage backend. Requires configuring DataHub’s backend server to be able to read and write from a particular S3 bucket. 

- File upload to S3 extension in UI. [[#15061](https://github.com/datahub-project/datahub/pull/15061)]
- Presigned upload URL endpoint. [[#14943](https://github.com/datahub-project/datahub/pull/14943)]
- Inline previews for text, PDF, and video files. [[#15182](https://github.com/datahub-project/datahub/pull/15182)]
- Support for schema field and asset documentation. [[#15055](https://github.com/datahub-project/datahub/pull/15055)]
- Permission checks for file downloads. [[#15059](https://github.com/datahub-project/datahub/pull/15059)]

This feature is disabled by default, and can be enabled by setting various environment variable in the `datahub-gms` container: 

- `DOCUMENTATION_FILE_UPLOAD_V1`  to `true`
- And S3 configs:
    
    ```
    DATAHUB_BUCKET_NAME: # The S3 bucket name to use for storing data
    DATAHUB_ROLE_ARN: # The AWS IAM role ARN to assume for S3 reads and writes
    ```
    

Note that this assumes AWS credentials with permission to read & write to the specified bucket are available & mounted in the environment where DataHub is running. 

##### Other Improvements

- Support linking multiple Applications to entities. [[#15160](https://github.com/datahub-project/datahub/pull/15160)]
- Structured properties infinite scroll with backend search. [[#14991](https://github.com/datahub-project/datahub/pull/14991)]
- Option to hide structured properties with empty values. [[#14872](https://github.com/datahub-project/datahub/pull/14872)]
- Model signature table for MLModel summary tab. [[#15205](https://github.com/datahub-project/datahub/pull/15205)]
- Improved More Filters UX. [[#15794](https://github.com/datahub-project/datahub/pull/15794)]
- Role selector with pagination and search. [[#15858](https://github.com/datahub-project/datahub/pull/15858)]
- Tag editing updates with new menu. [[#14884](https://github.com/datahub-project/datahub/pull/14884)]
- Show all views in settings. [[#14971](https://github.com/datahub-project/datahub/pull/14971)]
- Runs tab for DataFlow entities. [[#15775](https://github.com/datahub-project/datahub/pull/15775)]

---

#### Metadata Ingestion

We're continuously improving our integrations to add new capabilities and squash bugs.

##### New Sources

- **Google Dataplex:** New connector for Google Dataplex metadata ingestion. In incubation. [[#15379](https://github.com/datahub-project/datahub/pull/15379)]
- **Azure Data Factory:** New connector for Azure Data Factory pipelines and datasets.  In incubation. [[#15499](https://github.com/datahub-project/datahub/pull/15499)]
- **Microsoft Fabric OneLake:** New connector to ingest from Fabric workspaces, lakehouses, warehouses, schema, and tables.
- **IBM Db2:** New source for IBM Db2 databases. Incubating.. [[#14968](https://github.com/datahub-project/datahub/pull/14968)]
- **[Notion](https://docs.datahub.com/docs/generated/ingestion/sources/notion):** Added as ingestion source for Context Documents. In incubation. [[#15970](https://github.com/datahub-project/datahub/pull/15970)]
- **[Confluence](https://docs.datahub.com/docs/generated/ingestion/sources/confluence):** Added as an ingestion source for Context Documents. In incubation. [[#15970](https://github.com/datahub-project/datahub/pull/15970)]

##### Existing Sources

**Airflow:**

- Full Airflow 3.x support. [[#13790](https://github.com/datahub-project/datahub/pull/13790)]
- Teradata operator support for Airflow plugin. [[#15418](https://github.com/datahub-project/datahub/pull/15418)]
- DataFlow emission from task handler in distributed deployments. [[#15875](https://github.com/datahub-project/datahub/pull/15875)]

**Snowflake:**

- Streamlit apps ingestion support. [[#15272](https://github.com/datahub-project/datahub/pull/15272)]
- Semantic View ingestion support. [[#15395](https://github.com/datahub-project/datahub/pull/15395)]
- Stateful time window ingestion for queries v2 with bucket alignment. [[#15040](https://github.com/datahub-project/datahub/pull/15040)]
- Classification library added to dependencies. [[#15407](https://github.com/datahub-project/datahub/pull/15407)]

**Databricks/Unity Catalog:**

- Azure OAuth support. [[#15117](https://github.com/datahub-project/datahub/pull/15117)]
- OAuth and unified auth support. [[#15824](https://github.com/datahub-project/datahub/pull/15824)]
- ML model signature and run details support. [[#15177](https://github.com/datahub-project/datahub/pull/15177)]
- SQL-based query history extraction for usage. [[#14953](https://github.com/datahub-project/datahub/pull/14953)]
- Migration from deprecated SqlParsingBuilder to SqlParsingAggregator. [[#15005](https://github.com/datahub-project/datahub/pull/15005)]

**Kafka Connect:**

- Confluent Cloud connector and transform pipeline support. [[#14575](https://github.com/datahub-project/datahub/pull/14575)]
- Lineage inference from DataHub. [[#15234](https://github.com/datahub-project/datahub/pull/15234)]

**Fivetran:**

- Introducing support for Databricks. [[#14897](https://github.com/datahub-project/datahub/pull/14897)]
- Introducing support for Google Sheets and API client integration. [[#15007](https://github.com/datahub-project/datahub/pull/15007)]
- Improved REST API error handling. [[#15323](https://github.com/datahub-project/datahub/pull/15323)]

**dbt:**

- Semantic view support. [[#15411](https://github.com/datahub-project/datahub/pull/15411)]
- Bulk job ingestion for DBT Cloud. [[#15264](https://github.com/datahub-project/datahub/pull/15264)]
- Freshness tests now ingested as Freshness Assertions. [[#15885](https://github.com/datahub-project/datahub/pull/15885)]

**Hive Metastore:**

- Thrift connection mode with Kerberos support. [[#15691](https://github.com/datahub-project/datahub/pull/15691)]
- Upstream lineage support. [[#15435](https://github.com/datahub-project/datahub/pull/15435)]

**Oracle:**

- Support for materialized views, stored procedures, and usage. [[#15118](https://github.com/datahub-project/datahub/pull/15118)]

**PostgreSQL/MySQL:**

- IAM auth support for MySQL and PostgreSQL sources. [[#14899](https://github.com/datahub-project/datahub/pull/14899)]

**PowerBI:**

- Amazon Athena lineage support. [[#15728](https://github.com/datahub-project/datahub/pull/15728)]
- ODBC upstream lineage mapping and SQL parsing fixes. [[#15756](https://github.com/datahub-project/datahub/pull/15756)]
- Introduces DirectLake lineage extraction from PowerBI tables to Fabric OneLake tables [[#15927](https://github.com/datahub-project/datahub/pull/15927)]

**LookML:**

- Use Looker API to get fields of a View. [[#15060](https://github.com/datahub-project/datahub/pull/15060)]
- Updated recipe and UI enhancements. [[#15086](https://github.com/datahub-project/datahub/pull/15086)]

**Tableau:**

- Exponential backoff retry logic for InternalServerError. [[#15828](https://github.com/datahub-project/datahub/pull/15828)]

**Redshift:**

- Query tagging identifiying DataHub workload in the AWS Service Ready Program. [[#15676](https://github.com/datahub-project/datahub/pull/15676)]
- Fix lineage extraction ignoring disabled flags. [[#15545](https://github.com/datahub-project/datahub/pull/15545)]

**BigQuery:**

- Performance optimizations to minimize unnecessary API calls and improved performance for date-sharded tables [[#15945](https://github.com/datahub-project/datahub/pull/15945), [#15978](https://github.com/datahub-project/datahub/pull/15978)]
- Pushdown deny/allow usernames for server-side user filtering. [[#15699](https://github.com/datahub-project/datahub/pull/15699)]
- Case normalization for temp table inference. [[#15252](https://github.com/datahub-project/datahub/pull/15252)]

**Dremio:**

- Custom schema resolver for non-standard URI length. [[#15514](https://github.com/datahub-project/datahub/pull/15514)]
- OOM error handling for large metadata ingestion. [[#14883](https://github.com/datahub-project/datahub/pull/14883)]

**Grafana:**

- Option to pass user email as dashboard owner. [[#15489](https://github.com/datahub-project/datahub/pull/15489)]
- Fix for text panels causing ingestion failures. [[#15291](https://github.com/datahub-project/datahub/pull/15291)]

**Iceberg:**

- Role assumption support. [[#15288](https://github.com/datahub-project/datahub/pull/15288)]

**MSSQL:**

- Auto-enable use_odbc for mssql-odbc source type. [[#15702](https://github.com/datahub-project/datahub/pull/15702)]
- Stored procedure lineage extraction fix. [[#15340](https://github.com/datahub-project/datahub/pull/15340)]
- Statement splitting fix for expressions ending with parentheses. [[#15730](https://github.com/datahub-project/datahub/pull/15730)]

**Metabase:**

- Legacy-mbql parameter for Metabase 0.57+ compatibility. [[#15709](https://github.com/datahub-project/datahub/pull/15709)]

**MongoDB:**

- Fix handling of arrays containing complex structures. [[#15026](https://github.com/datahub-project/datahub/pull/15026)]

**Qlik Sense:**

- Scoped ingestion to eliminate full environment scans. [[#15837](https://github.com/datahub-project/datahub/pull/15837)]

##### Misc. Ingestion Improvements

- Postgres: now supports automated lineage extraction from query history [[#15924](https://github.com/datahub-project/datahub/pull/15924)]
- Secret masking framework for sensitive data. [[#15188](https://github.com/datahub-project/datahub/pull/15188)]
- Recording and replay system for debugging ingestion runs. [[#15480](https://github.com/datahub-project/datahub/pull/15480)]
- S3 performance improvements for get_dir_to_process and get_folder_info. [[#14709](https://github.com/datahub-project/datahub/pull/14709)]
- Tags to structured properties transformer. [[#15423](https://github.com/datahub-project/datahub/pull/15423)]
- Configurable SQL parse cache size via environment variable. [[#15977](https://github.com/datahub-project/datahub/pull/15977)]
- OAuth callback support for Kafka producers/sinks. [[#15420](https://github.com/datahub-project/datahub/pull/15420), [#15673](https://github.com/datahub-project/datahub/pull/15673)]
- Lightweight Kafka connectivity validation. [[#15472](https://github.com/datahub-project/datahub/pull/15472)]
- Convert to lowercase option for S3. [[#15475](https://github.com/datahub-project/datahub/pull/15475)]
- Upper bounds added to dependency versions. [[#15813](https://github.com/datahub-project/datahub/pull/15813)]
- Regex pattern compilation for ingestion filtering hot path. [[#15463](https://github.com/datahub-project/datahub/pull/15463)]

---

#### DataHub Python SDK

Improvements and new features for the DataHub SDK:

- Full Pydantic v2 migration with v1 legacy code removed. [[#15261](https://github.com/datahub-project/datahub/pull/15261)]
- Tag entity support in SDK v2. [[#14791](https://github.com/datahub-project/datahub/pull/14791)]
- Parametrized Assertion Run support. [[#15447](https://github.com/datahub-project/datahub/pull/15447)]
- DataProduct output ports support. [[#15000](https://github.com/datahub-project/datahub/pull/15000)]
- DataJob environment defaults to PROD when using flow_urn. [[#15388](https://github.com/datahub-project/datahub/pull/15388)]
- GraphQL CLI command. [[#14781](https://github.com/datahub-project/datahub/pull/14781)]
- User add CLI command. [[#15011](https://github.com/datahub-project/datahub/pull/15011)]
- Agent-friendly `datahub init` with non-interactive mode, environment variable support, and configurable token duration. [[#16038](https://github.com/datahub-project/datahub/pull/16038)]
- `-env` option for ingest deploy command. [[#15518](https://github.com/datahub-project/datahub/pull/15518)]
- Support for extra-pip and extra-env options in config file. [[#15800](https://github.com/datahub-project/datahub/pull/15800)]
- MCE Topic optional in Kafka sink. [[#14150](https://github.com/datahub-project/datahub/pull/14150)]
- Environment variables extracted into single file. [[#15021](https://github.com/datahub-project/datahub/pull/15021)]

---

#### DataHub Java SDK

New Java SDK V2 with modern API design:

- Fluent builder API with entity support. [[#15307](https://github.com/datahub-project/datahub/pull/15307)]
- Ensure full aspect writes complete before patches. [[#15522](https://github.com/datahub-project/datahub/pull/15522)]

---

#### Platform & Backend

Platform improvements and backend enhancements:

##### Elasticsearch 8 Support

- Multi-client search engine shim for ES8 support. [[#14904](https://github.com/datahub-project/datahub/pull/14904)]

##### Search Enhancements

- Semantic search infrastructure. [[#15743](https://github.com/datahub-project/datahub/pull/15743)]
- Semantic search configuration GraphQL API. [[#15959](https://github.com/datahub-project/datahub/pull/15959)]

##### System Update Improvements

- Consolidated setup jobs
    - SQL setup replacement for MySQL/Postgres. [[#15044](https://github.com/datahub-project/datahub/pull/15044)]
    - Elasticsearch setup replacement. [[#15058](https://github.com/datahub-project/datahub/pull/15058)]
- Improved IAM setup support. [[#15143](https://github.com/datahub-project/datahub/pull/15143)]
- Consistency checks API and upgrade validation. [[#15766](https://github.com/datahub-project/datahub/pull/15766)]

##### Kafka Improvements

- Consumer lag monitoring. [[#15769](https://github.com/datahub-project/datahub/pull/15769)]
- Automatic topic partition upsizing (opt-in). [[#15714](https://github.com/datahub-project/datahub/pull/15714)]
- Split consumer/producer configuration. [[#15751](https://github.com/datahub-project/datahub/pull/15751)]
- Events Kafka pool and client retry improvements. [[#15429](https://github.com/datahub-project/datahub/pull/15429)]

##### OpenAPI Enhancements

- Improved scroll API with advanced pagination and facets. [[#14877](https://github.com/datahub-project/datahub/pull/14877)]
- Sorting customization on missing value handling. [[#15383](https://github.com/datahub-project/datahub/pull/15383)]

##### GraphQL Enhancements

- Comprehensive entity patching functionality. [[#14823](https://github.com/datahub-project/datahub/pull/14823)]

##### Other Platform Changes

- HTTPS support with option to disable HTTP in frontend. [[#15757](https://github.com/datahub-project/datahub/pull/15757)]
- OpenSearch upgrade to 2.19.3. [[#15047](https://github.com/datahub-project/datahub/pull/15047)]
- Dependency locking for Gradle. [[#15303](https://github.com/datahub-project/datahub/pull/15303)]

---

#### AI

New capabilities for organizational knowledge and AI-powered features:

##### Context Documents

- Context Base V1 models and APIs. [[#15280](https://github.com/datahub-project/datahub/pull/15280)]
- UI flows for viewing and adding context to assets. [[#15279](https://github.com/datahub-project/datahub/pull/15279)]
- Support for all asset types. [[#15453](https://github.com/datahub-project/datahub/pull/15453)]
- Python APIs and documentation. [[#15319](https://github.com/datahub-project/datahub/pull/15319)]

##### Semantic Search

- Backend infrastructure for semantic search on Context Documents. [[#15743](https://github.com/datahub-project/datahub/pull/15743)]
- GraphQL configuration API to enable ingestion to share configs. [[#15959](https://github.com/datahub-project/datahub/pull/15959)]

##### Document Ingestion

- New datahub-documents source with chunking and embedding support. [[#15975](https://github.com/datahub-project/datahub/pull/15975)]

---

#### Documentation

Documentation updates and improvements:

- Context Documents and Ask DataHub user docs. [[#15695](https://github.com/datahub-project/datahub/pull/15695)]
- Smart SQL assertions documentation. [[#15187](https://github.com/datahub-project/datahub/pull/15187)]
- Custom SQL in column value assertions. [[#15192](https://github.com/datahub-project/datahub/pull/15192)]
- Query attribution documentation. [[#15879](https://github.com/datahub-project/datahub/pull/15879)]
- Logical datasets and bulk relationship removal. [[#15029](https://github.com/datahub-project/datahub/pull/15029)]
- Metadata model entity documentation with field tables and SDK examples. [[#15095](https://github.com/datahub-project/datahub/pull/15095)]
- MCP server setup instructions. [[#15484](https://github.com/datahub-project/datahub/pull/15484)]
- Guidelines to avoid AI test anti-patterns. [[#15073](https://github.com/datahub-project/datahub/pull/15073)]
- Ingestion security guidelines. [[#15729](https://github.com/datahub-project/datahub/pull/15729)]
- Microfrontend usage and build instructions. [[#15713](https://github.com/datahub-project/datahub/pull/15713)]
- CDC mode configuration improvements. [[#15496](https://github.com/datahub-project/datahub/pull/15496)]
- Search access controls for DataHub Cloud. [[#15513](https://github.com/datahub-project/datahub/pull/15513)]

---

#### Breaking Changes

- **Pydantic v2 Migration:** Pydantic v1 legacy code has been removed. All custom code using the SDK must migrate to Pydantic v2. [[#15261](https://github.com/datahub-project/datahub/pull/15261)]
- **Fivetran:** Database and schema names handling changed to use quoted identifiers. [[#15321](https://github.com/datahub-project/datahub/pull/15321)]
- **LookML/Looker:** See documented breaking changes. [[#14947](https://github.com/datahub-project/datahub/pull/14947)]
- **Python 3.9 EOL**: Python 3.9 support has been removed as this version is EOL [[#15984](https://github.com/datahub-project/datahub/pull/15984)]

#### Security Notes

- DataHub is aware of urllib3 DoS vulnerabilities CVE-2025-66418,
CVE-2025-66471, and CVE-2026-21441. These vulnerabilities slightly
increase DoS risk but do not change DataHub's threat model. Users
should configure ingestion from trusted sources only. urllib3 will
be upgraded when botocore supports versions >2.5.x.

## [v1.3.0.1](https://github.com/datahub-project/datahub/releases/tag/v1.3.0.1) {#v1-3-0-1}

Released on 2025-11-12 by [@chakru-r](https://github.com/chakru-r).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v1.3.0.1) for v1.3.0.1 on GitHub.

## [v1.3.0](https://github.com/datahub-project/datahub/releases/tag/v1.3.0) {#v1-3-0}

Released on 2025-10-06 by [@RyanHolstien](https://github.com/RyanHolstien).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v1.3.0) for v1.3.0 on GitHub.

