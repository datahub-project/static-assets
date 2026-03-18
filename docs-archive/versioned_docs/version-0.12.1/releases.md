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
| **v0.12.1** | 2023-12-08 |[Release Notes](#v0-12-1), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.12.1) |
| **v0.12.0** | 2023-10-25 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.12.0) |
| **v0.11.0** | 2023-09-08 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.11.0) |
| **v0.10.5** | 2023-08-02 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.5) |
| **v0.10.4** | 2023-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.4) |
| **v0.10.3** | 2023-05-25 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.3) |
| **v0.10.2** | 2023-04-13 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.2) |
| **v0.10.1** | 2023-03-23 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.1) |
| **v0.10.0** | 2023-02-07 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.10.0) |
| **v0.9.6.1** | 2023-01-31 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.6.1) |
| **v0.9.6** | 2023-01-13 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.6) |
| **v0.9.5** | 2022-12-23 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.5) |
| **v0.9.4** | 2022-12-20 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.4) |
| **v0.9.3** | 2022-11-30 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.3) |
| **v0.9.2** | 2022-11-04 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.2) |
| **v0.9.1** | 2022-10-31 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.1) |
| **v0.9.0** | 2022-10-11 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.9.0) |
| **v0.8.45** | 2022-09-23 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.45) |
| **v0.8.44** | 2022-09-01 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.44) |
| **v0.8.43** | 2022-08-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.43) |
| **v0.8.42** | 2022-08-03 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.42) |
| **v0.8.41** | 2022-07-15 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.41) |
| **v0.8.40** | 2022-06-30 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.40) |
| **v0.8.39** | 2022-06-24 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.39) |
| **v0.8.38** | 2022-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.38) |
| **v0.8.37** | 2022-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.37) |
| **v0.8.36** | 2022-06-02 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.36) |
| **v0.8.35** | 2022-05-18 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.35) |
| **v0.8.34** | 2022-05-04 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.34) |


## [DataHub v0.12.1](https://github.com/datahub-project/datahub/releases/tag/v0.12.1) {#v0-12-1}

Released on 2023-12-08 by [@david-leifker](https://github.com/david-leifker).

### Release Highlights
#### New Features
SQLAlchemy Source Enhancements: Support for view lineage across all SQLAlchemy sources (PR [#9039](https://github.com/datahub-project/datahub/pull/9039)).
Airflow Integration: Retry callback and support for ExternalTaskSensor subclasses added (PR [#8514](https://github.com/datahub-project/datahub/pull/8514)).
Kafka Enhancements: Increased Kafka message size and enabled compression (PR [#9038](https://github.com/datahub-project/datahub/pull/9038)).
JSONSchema Ingestion: Enabled schema-aware JsonSchemaTranslator (PR [#8971](https://github.com/datahub-project/datahub/pull/8971)).
Search Bar Improvements: Added a flag to hide/display the autocomplete query (PR [#9104](https://github.com/datahub-project/datahub/pull/9104)).
SQL Parser Performance: Enhancements and asyncio fixes (PR [#9119](https://github.com/datahub-project/datahub/pull/9119)).
MongoDB Ingestion: Support for stateful ingestion and improved schema inference for lists (PR [#9118](https://github.com/datahub-project/datahub/pull/9118), PR [#9145](https://github.com/datahub-project/datahub/pull/9145)).
Policy Engine Updates: Refactoring and enhancements, including support for 10k+ policies (PR [#9163](https://github.com/datahub-project/datahub/pull/9163), PR [#9177](https://github.com/datahub-project/datahub/pull/9177)).
UI Enhancements: Numerous improvements including command-k icons in the search bar, updated Apollo cache, and auto-complete debounce in the search bar (PR [#9194](https://github.com/datahub-project/datahub/pull/9194), PR [#9193](https://github.com/datahub-project/datahub/pull/9193), PR [#9205](https://github.com/datahub-project/datahub/pull/9205)).
Fivetran Integration: Connector integration for Fivetran (PR [#9018](https://github.com/datahub-project/datahub/pull/9018)).
Neo4j Database Support: Connection to specific Neo4j databases now supported (PR [#9179](https://github.com/datahub-project/datahub/pull/9179)).
Chart Subtypes in UI: Support for chart subtypes (PR [#9186](https://github.com/datahub-project/datahub/pull/9186)).

#### Fixes and Improvements
BigQuery Fixes: Resolved issues with lineage filter query, and fixed extracting comments from complex types (PR [#9114](https://github.com/datahub-project/datahub/pull/9114), PR [#8950](https://github.com/datahub-project/datahub/pull/8950)).
MongoDB Refactoring: Platform instance addition to MongoDB (PR [#8663](https://github.com/datahub-project/datahub/pull/8663)).
Kafka Setup: Adjusted truststore settings for PEM files (PR [#8656](https://github.com/datahub-project/datahub/pull/8656)).
REST API Authorization: Fixed rollback failure when authorization is enabled (PR [#9092](https://github.com/datahub-project/datahub/pull/9092)).
Java Exception Handling: Addressed java.util.ConcurrentModificationException (PR [#9090](https://github.com/datahub-project/datahub/pull/9090)).
UI and Documentation: Fixed filtering logic in UI, corrected documentation errors, and added feature guides (PR [#9116](https://github.com/datahub-project/datahub/pull/9116), PR [#9125](https://github.com/datahub-project/datahub/pull/9125), PR [#9124](https://github.com/datahub-project/datahub/pull/9124), PR [#9126](https://github.com/datahub-project/datahub/pull/9126), PR [#9134](https://github.com/datahub-project/datahub/pull/9134), PR [#9137](https://github.com/datahub-project/datahub/pull/9137), PR [#9122](https://github.com/datahub-project/datahub/pull/9122), PR [#9068](https://github.com/datahub-project/datahub/pull/9068)).
SQL Server and Snowflake Ingestion: Updated queries and fixed missing view downstream call (PR [#9127](https://github.com/datahub-project/datahub/pull/9127), PR [#8966](https://github.com/datahub-project/datahub/pull/8966)).
ClickHouse and DB2 Ingestion: Addressed column reflection regression and table properties handling (PR [#9143](https://github.com/datahub-project/datahub/pull/9143), PR [#9128](https://github.com/datahub-project/datahub/pull/9128)).
Ingestion Improvements: Numerous fixes and enhancements across various ingestion sources (PR [#9153](https://github.com/datahub-project/datahub/pull/9153), PR [#9155](https://github.com/datahub-project/datahub/pull/9155), PR [#9141](https://github.com/datahub-project/datahub/pull/9141), PR [#9157](https://github.com/datahub-project/datahub/pull/9157), PR [#9123](https://github.com/datahub-project/datahub/pull/9123)).
CI and Build Process: Tweaked workflows, increased gradle retries, and addressed CI errors (PR [#9052](https://github.com/datahub-project/datahub/pull/9052), PR [#9091](https://github.com/datahub-project/datahub/pull/9091), PR [#9160](https://github.com/datahub-project/datahub/pull/9160)).
Security Updates: Addressed a zookeeper CVE and other security concerns (PR [#9190](https://github.com/datahub-project/datahub/pull/9190)).
UI Refactoring: Improved entity page loading indicators and renamed button texts (PR [#9195](https://github.com/datahub-project/datahub/pull/9195), PR [#9196](https://github.com/datahub-project/datahub/pull/9196)).
Policy and Auth Enhancements: Refactored policy locking and added roles to policy engine validation logic (PR [#9178](https://github.com/datahub-project/datahub/pull/9178)).

#### Testing and Continuous Integration
API Testing: Added tests for managing secrets, access token privilege, and flaky tests fix (PR [#9121](https://github.com/datahub-project/datahub/pull/9121), PR [#9167](https://github.com/datahub-project/datahub/pull/9167), PR [#9132](https://github.com/datahub-project/datahub/pull/9132), PR [#9175](https://github.com/datahub-project/datahub/pull/9175)).
Cypress Test Fixes: Addressed glossary navigation and download_lineage_results tests (PR [#9175](https://github.com/datahub-project/datahub/pull/9175), PR [#9132](https://github.com/datahub-project/datahub/pull/9132)).
Cleanup and Refactoring
Ingestion Cleanup: Removed legacy memory_leak_detector and refactored ingestion sources (PR [#9158](https://github.com/datahub-project/datahub/pull/9158), PR [#9135](https://github.com/datahub-project/datahub/pull/9135), PR [#9120](https://github.com/datahub-project/datahub/pull/9120), PR [#9105](https://github.com/datahub-project/datahub/pull/9105)).
PDL Refactoring: Refactored Assertion model enums (PR [#9191](https://github.com/datahub-project/datahub/pull/9191)).
Build and Deployment
Release Preparation: Updated files for the 0.12.0 release (PR [#9130](https://github.com/datahub-project/datahub/pull/9130)).

### What's Changed
* feat(ingest): support view lineage for all sqlalchemy sources by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9039
* fix(ingest/bigquery): Fixing lineage filter query by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9114
* refactor(ingestion/mongodb): Add platform_instance to mongodb by [@nicholas-fwang](https://github.com/nicholas-fwang) in https://github.com/datahub-project/datahub/pull/8663
* fix(kafka-setup): Don't set truststore pass for PEM files by [@mmmeeedddsss](https://github.com/mmmeeedddsss) in https://github.com/datahub-project/datahub/pull/8656
* fix(ingest): Fix roll back failure when REST_API_AUTHORIZATION_ENABLED is set to true by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9092
* (fix): Avoid java.util.ConcurrentModificationException by [@rtekal](https://github.com/rtekal) in https://github.com/datahub-project/datahub/pull/9090
* Fix(ingest/bigquery): fix extracting comments from complex types by [@maaaikoool](https://github.com/maaaikoool) in https://github.com/datahub-project/datahub/pull/8950
* docs: add versions 0.12.0 by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9125
* fix(ui) Fix filtering logic for everwhere generating OR filters by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9116
* build(release): Update files for 0.12.0 release by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9130
* fix(ingest/sql-server): update queries to use escaped procedure name by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9127
* feat(airflow): retry callback, support ExternalTaskSensor subclasses by [@richenc](https://github.com/richenc) in https://github.com/datahub-project/datahub/pull/8514
* docs: fix saasonly flags for some pages by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9124
* fix(ingest/snowflake): missing view downstream cll if platform instance is set by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/8966
* feat: Add flag to hide/display the autocomplete query for search bar by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9104
* docs(timeline): correct markdown heading level by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9126
* docs(graphql) Correct mutation -> query for searchAcrossLineage examples by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9134
* feat(kafka): increase kafka message size and enable compression by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9038
* feat(ingest/jsonschema) enable schema-aware `JsonSchemaTranslator` by [@KulykDmytro](https://github.com/KulykDmytro) in https://github.com/datahub-project/datahub/pull/8971
* fix(metadata-ingestion): adds default value to _resolved_domain_urn i… by [@alexklavensnyt](https://github.com/alexklavensnyt) in https://github.com/datahub-project/datahub/pull/9115
* ci: tweak to only run relevant workflows by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9052
* Fix for flaky download_lineage_results cypress test by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9132
* docs: Update updating-datahub.md by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9131
* fix(ingest/clickhouse): pin version to solve column reflection regression by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9143
* feat(ingest/looker): cleanup error handling by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9135
* feat(ingest): add `entity_supports_aspect` helper by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9120
* feat(sqlparser): support more update syntaxes + fix bug with subqueries by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9105
* docs: correct broken doc links by [@sachinsaju](https://github.com/sachinsaju) in https://github.com/datahub-project/datahub/pull/9137
* feat(ingest): sql parser perf + asyncio fixes by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9119
* feat(quickstart): fix broker InconsistentClusterIdException issues by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9148
* fix(policies): remove non-existent policies, fix name by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9150
* Fix for a test that passed on Oss and failed on Saas by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9147
* docs(teradata): teradata doc external link 404 fix by [@sachinsaju](https://github.com/sachinsaju) in https://github.com/datahub-project/datahub/pull/9152
* fix(datahub-client): Include relocation for snakeyaml dependency. by [@jiateoh](https://github.com/jiateoh) in https://github.com/datahub-project/datahub/pull/8911
* fix(ingest): cleanup large images in CI by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9153
* build: increase gradle retries by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9091
* feat(ingest): bump sqlglot parser by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9155
* feat(ingest/mongodb): support stateful ingestion by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9118
* API test for managing secrets privilege by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9121
* fix(ingest): handle exceptions in min, max, mean profiling by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9129
* feat: rename Assets tab to Owner Of by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9141
* fix(ingest/mongodb): fix schema inference for lists of values by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9145
* fix(ingest/db2): fix handling for table properties by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/9128
* fix(ingest): fully support MCPs in urn_iter primitive by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9157
* fix(ingest/bigquery): use correct row count in null count profiling c… by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9123
* docs: add feature guides for subscriptions and notifications by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9122
* docs: unify oidc guides using tabs by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9068
* chore(ingest): remove legacy memory_leak_detector by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9158
* feat(ingest/looker): support emitting unused explores by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9159
* refactor(policy): refactor policy locking, no functional difference by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9163
* API test for managing access token privilege by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9167
* fix(mysql-setup): quote database name by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9169
* fix(health): fix health check url authentication by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9117
* fix(elasticsearch): fix elasticsearch-setup for dropped 000001 index by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9074
* Origin/fix flaky glossary navigation cypress test by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9175
* fix: bad lineage link in `LineageGraphOnboardingConfig.tsx` by [@walter9388](https://github.com/walter9388) in https://github.com/datahub-project/datahub/pull/9162
* OBS-191 | Viewing domains page should not require Manage Domains priv… by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9156
* fix: expand the stats row in search preview cards by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9140
* docs(ingest): clarify adding source guide by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9161
* chore: stop ingestion-smoke CI errors on forks by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9160
* docs(ingest): inherit capabilities from superclasses by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9174
* fix(ingest/datahub-source): Order by version in memory by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9185
* lint(frontend): fix HeaderLinks lint error by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9189
* refactor(ui): Refactor entity page loading indicators  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9195
* fix(security): fix for zookeeper CVE-2023-44981 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9190
* refactor(ui): Rename "dataset details" button text to "view details" on lineage sidebar profile by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9196
* feat(ui): Add command-k icons to search bar  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9194
* feat(ui) Update Apollo cache to work with union types by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9193
* feat(policy): enable support for 10k+ policies by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9177
* feat(browsepathv2): Allow system-update to reprocess browse paths v2 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9200
* feat(integration/fivetran): Fivetran connector integration by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9018
* feat(neo4j): Allow datahub to connect to specific neo4j database by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/9179
* feat(subtypes): support subtypes for charts in the UI by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/9186
* feat(ui) Debounce auto-complete in search bar by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9205
* fix(lineage): magical lineage layout fix by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/9187
* refactor(pdl): Refactoring Assertion model enums out  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9191
* feat(auth): Add roles to policy engine validation logic by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9178
* style(ingest/tableau): Rename tableau_constant to c by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9207
* docs: update broken link in metadata-modelling by [@sachinsaju](https://github.com/sachinsaju) in https://github.com/datahub-project/datahub/pull/9184
* Test policy to create and manage privileges by [@kkorchak](https://github.com/kkorchak) in https://github.com/datahub-project/datahub/pull/9173
* docs(security): add security doc to website by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9209
* docs(java-sdk-dataset): add dataset via java sdk example by [@sachinsaju](https://github.com/sachinsaju) in https://github.com/datahub-project/datahub/pull/9136
* doc(java-sdk-example):example to create tag via java-sdk by [@sachinsaju](https://github.com/sachinsaju) in https://github.com/datahub-project/datahub/pull/9151
* fix(ingest/powerbi): use dataset workspace id as key for parent container by [@looppi](https://github.com/looppi) in https://github.com/datahub-project/datahub/pull/8994
* refactor(schema tab): Remove last observed timestamps from schema tab by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9188
* docs: adjust sidebar & create new admin section by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9064
* fix(metadata-io): in Neo4j service use proper algorithm to get lineage by [@lix-mms](https://github.com/lix-mms) in https://github.com/datahub-project/datahub/pull/8687
* Managed Ingestion UX Improvements by [@purnimagarg1](https://github.com/purnimagarg1) in https://github.com/datahub-project/datahub/pull/9216
* chore(ingest): start working on pydantic v2 support by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9220
* feat(ingestion): file-based state checkpoint provider by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9029
* feat(ingestion/airflow): support datajobs as task inlets by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9211
* fix(build): set `[@cliMajorVersion](https://github.com/cliMajorVersion)@` correctly by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9228
* fix(datahub-ingestion): remove old jars, sync pyspark version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9217
* fix: add security.md to sidebar by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9229
* feat(policies): reduce default access for all users by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9067
* Update add new company s7 airlines by [@YuriyGavrilov](https://github.com/YuriyGavrilov) in https://github.com/datahub-project/datahub/pull/9019
* docs(debug): add debug information for cli by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9208
* fix(datahub-ingestion): prevent transitive deps, bump addtional pyspa… by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9233
* feat(ingest/dbt): dbt column-level lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/8991
* chore(ingest): cleanup various methods by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9221
* docs: clarify how to disable telemetry by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9236
* feat(ingest/mongodb): support AWS DocumentDB for MongoDB by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9201
* feat(airflow): make RUN_IN_THREAD configurable by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9226
* fix(signup): prevent invalid email signup by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9234
* chore(security): version adjustments for security vulns by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9243
* docs(ingest): fix typo in snowflake ingestion docs by [@PGuiv](https://github.com/PGuiv) in https://github.com/datahub-project/datahub/pull/9239
* chore(security): jre to headless, removes x11 dependency by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9245
* feat(recomendations): Make top platforms account only for searchable entities by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9240
* Feature/prd 770 by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9224
* fix:fix search on paginated lists by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9198
* fix: increase the search bar highlight border to double the width by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9251
* feat: Add loading indicator to Manage Domains sidebar by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9142
* fix(ui): show external url also in entity profile of containers by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/8834
* feat(ingest/unity): Support specifying catalogs directly; pass env correctly by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9110
* refactor(datahub-web-react): allows proxying to external datahub-frontend servers by [@PatrickfBraz](https://github.com/PatrickfBraz) in https://github.com/datahub-project/datahub/pull/9250
* chore(node): update node to non-EOL version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9252
* fix(ingest): drop redshift-legacy and redshift-usage-legacy sources by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9244
* feat(ingest): support advanced configs for aws by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9237
* fix(sql-parser): convert platform instance to lowercase when building table urns by [@Starkie](https://github.com/Starkie) in https://github.com/datahub-project/datahub/pull/9181
* test(ingest/unity): Update goldens by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9254
* build(ingest/hive): Update thrift pin by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/8964
* docs(airflow): update plugin setup docs to include UI setup approach by [@jiateoh](https://github.com/jiateoh) in https://github.com/datahub-project/datahub/pull/9253
* feat(usageclient): updates for usageclient by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9255
* fix(graphql): prevent duplicate index queries for dataproducts by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9260
* logging(search): log level highlight value urn detection by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9262
* Add Python version in Developer README by [@kevin1chun](https://github.com/kevin1chun) in https://github.com/datahub-project/datahub/pull/9268
* Sync datahub-head on merge by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/9267
* PRD-742/fix:Settings tab should have 2 scrollable sections by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9218
* feat: add ingestion overview pages  by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9210
* fix(ingest/athena): detect decimal type correctly by [@bossenti](https://github.com/bossenti) in https://github.com/datahub-project/datahub/pull/9270
* Fix/prd 787 by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9261
* build(deps): bump [@babel](https://github.com/babel)/traverse from 7.22.11 to 7.23.2 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9022
* fix(gha): fix gha for single tag by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9283
* fix(node): fix node_options by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9281
* fix: Revamp features page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/8839
* docs(acryl cloud): release notes 0.2.13 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9291
* fix: stats are spaced out too far by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9292
* feat(mysql): upgrade to version 8.2 for quickstart by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9241
* feat: add townhall RSVP link on the main page  by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9277
* fix(ingest/snowflake): Apply email filter on all usage metrics by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9269
* docs(ingestion): Added mention of host without protocol by [@SimonOsipov](https://github.com/SimonOsipov) in https://github.com/datahub-project/datahub/pull/9301
* fix(ingest/teradata): Teradata speed up changes by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9059
* fix(kafka): fix consumer properties on due consumer by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9304
* fix(dbt-cloud): do not pass macros to sorting nodes by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9302
* fix(ingest/lookml): emit all views with same name and different file path by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9279
* fix(deprecation): bring frontend in-sync with model by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9303
* fix: fix the settings height when there are not many items by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9294
* docs: update recommended CLI by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9307
* feat(ui): bump frontend dependencies by [@ngamanda](https://github.com/ngamanda) in https://github.com/datahub-project/datahub/pull/8353
* fix(java) Fixes NPE ES service by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9311
* feat(config): Configurable bootstrap of ownership types by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/9308
* feat: update the "json-schema" version from package.json to solve json-schema vulnerability by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9289
* fix(ingest/mssql): Add MONEY and SMALLMONEY data types as Number by [@terratrue-daniel](https://github.com/terratrue-daniel) in https://github.com/datahub-project/datahub/pull/9313
* fix(ingest): drop deprecated database_alias from sql sources by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9299
* Make repositories configurable for enterprise developers by [@githendrik](https://github.com/githendrik) in https://github.com/datahub-project/datahub/pull/9230
* fix(ingest/sql): improve handling of views with dots in their names by [@Starkie](https://github.com/Starkie) in https://github.com/datahub-project/datahub/pull/9183
* docs(ingest): update docs on adding stateful ingestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9327
* fix(docker): docker compose health checks port fix by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9326
* fix : vulnerability (React): Inefficient Regular Expression Complexit… by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9324
* fix(ui) Fix UI glitch in policies creator by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9266
* fix(sidebar): remove a space reserved for scroll bars when sidebar is collapsed by [@allizex](https://github.com/allizex) in https://github.com/datahub-project/datahub/pull/9322
* feat(ingest/mssql): enable TLS encryption for SQLServer using pytds by [@terratrue-daniel](https://github.com/terratrue-daniel) in https://github.com/datahub-project/datahub/pull/9256
* fix(datahub-frontend): Add playCaffeine as replacement for removed playEhcache dependency by [@MideO](https://github.com/MideO) in https://github.com/datahub-project/datahub/pull/8344
* fix(ingest): bump pyhive to fix headers issue by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9328
* feat(gradle): quickstart postgres gradle task by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9329
* Upload metadata model to s3 by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/9325
* fix(ui) Set explicit height on logo images to fix render bug by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9344
* fix(ingest/browse): Re-emit browse path v2 aspects to avoid race condition by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9227
* feat(ingest/ldap): make ingestion robust to string departmentId by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9258
* doc(ingest/teradata): Adding Teradata to list of Integrations by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9336
* Complexity in chalk/ansi-regex  and minimatch ReDoS  Vulnerability solution by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9323
* build(deps): bump tmpl from 1.0.4 to 1.0.5 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9345
* fix:Address [@babel](https://github.com/babel)/traverse vulnerabilities by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9343
* docs(ingest/looker): mark platform instance as a supported capability by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9347
* fix:Address HIGH vulnerability with Axios by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9353
* fix: show formatted total result count in Search by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9356
* feat(sdk): autogenerate urn types by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9257
* fix(airflow): support inlet datajobs correctly in v1 plugin by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9331
* feat(ingest): clean up DataHubRestEmitter return type by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9286
* feat(ingest/dbt): support custom ownership types in dbt meta by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9332
* docs(ingest/lookml): clarify that ssh key has no passphrase by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9348
* fix(migrate): connect with token without dry-run by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9317
* fix(ui): Minor: fix unnecessary lineage tab scroll by removing -1 margin on lists by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9364
* Prd 196 dynamic tabname by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9352
* docs: add setup instructions for mac dependencies by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9346
* feat(ui): Add caching to search, entity profile for better UX by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9362
* refactor(ui): Remove primary color for sort selector + add t… by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9363
* feat(ui): Supporting subtypes for data jobs by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9361
* fix(ingest/bigquery): Fix format arguments for table lineage test ([#9340](https://github.com/datahub-project/datahub/pull/9340)) by [@middagj](https://github.com/middagj) in https://github.com/datahub-project/datahub/pull/9341
* fix(siblingsHook): add logic to account for non dbt upstreams by [@ethan-cartwright](https://github.com/ethan-cartwright) in https://github.com/datahub-project/datahub/pull/9154
* feat: Support CSV ingestion through the UI by [@purnimagarg1](https://github.com/purnimagarg1) in https://github.com/datahub-project/datahub/pull/9280
* fix: node-fetch forwards secure headers to untrusted sites by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9375
* fix(ingest/powerbi): Allow old parser to parse [db].[schema].[table] table references by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9360
* feat(ingest): support stdin in `datahub put` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9359
* fix(ingest): resolve issue with caplog and asyncio by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9377
* fix(ingest/airflow): compat with pluggy 1.0 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9365
* feat(ingest/athena): Enable Athena view ingestion and view lineage by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9354
* fix(ingest/redshift): Identify materialized views properly + fix connection args support by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9368
* test(ingest/unity): Unity catalog data generation by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/8949
* fix(elasticsearch): set datahub usage events shard & replica count by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9388
* feat(gms/search): Adding support for DOUBLE Searchable type by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/9369
* feat(lint): add spotless for java lint by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9373
* feat(ci): split no cypress test suite by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9387
* fix(ingest/redshift): too many values unpack by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9394
* fix(ingest/redshift): Fix psycopg2 removal from Redshift Source by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9395
* fix(ui): fixed font src spelling mistake by [@accso-jo](https://github.com/accso-jo) in https://github.com/datahub-project/datahub/pull/9204
* feat(ingest/unity): GE Profiling by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/8951
* feat(ui/last-updated): Calculate last updated time as max(properties time, operation time) by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9242
* docs: add youtube link to townhall button on docs by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9381
* fix: set new sidebar section by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9393
* fix(json-schema): take into account environment by [@matthiasdg](https://github.com/matthiasdg) in https://github.com/datahub-project/datahub/pull/9385
* feat(datahub-frontend): make Java memory options configurable via ENV variable by [@haeniya](https://github.com/haeniya) in https://github.com/datahub-project/datahub/pull/9215
* docs(ingest/sql-queries): Add documentation by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9406
* docs: fix duplicated overview link for api section by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9402
* feat(glossary): add toggle sidebar button and functionality to Busine… by [@olgadimova](https://github.com/olgadimova) in https://github.com/datahub-project/datahub/pull/9222
* refactor(ui): Refactor entity registry to be inside App Providers by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9399
* feat(ui): handle content prop changes in Editor component by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9400
* fix(ingest/profiling): Add back db_name to sql_generic_profiler methods by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9407
* feat(observability): add actor urn to GraphQL spans by [@ngamanda](https://github.com/ngamanda) in https://github.com/datahub-project/datahub/pull/9382
* fix(ingest/lookml): make deploy key optional by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9378
* fix(ingest/powerbi): fix powerbi chart input handling by [@looppi](https://github.com/looppi) in https://github.com/datahub-project/datahub/pull/9415
* fix(ingest): fix metadata for custom python packages by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9391
* fix(ingest): bug fixes and docs updates by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9422
* Pin alpine base image version to 3.18 by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/9421
* fix(cypress) Fix flakiness of cypress test for glossary navigation by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9410

### New Contributors
* [@nicholas-fwang](https://github.com/nicholas-fwang) made their first contribution in https://github.com/datahub-project/datahub/pull/8663
* [@richenc](https://github.com/richenc) made their first contribution in https://github.com/datahub-project/datahub/pull/8514
* [@kushagra-apptware](https://github.com/kushagra-apptware) made their first contribution in https://github.com/datahub-project/datahub/pull/9104
* [@alexklavensnyt](https://github.com/alexklavensnyt) made their first contribution in https://github.com/datahub-project/datahub/pull/9115
* [@sachinsaju](https://github.com/sachinsaju) made their first contribution in https://github.com/datahub-project/datahub/pull/9137
* [@jiateoh](https://github.com/jiateoh) made their first contribution in https://github.com/datahub-project/datahub/pull/8911
* [@deepgarg-visa](https://github.com/deepgarg-visa) made their first contribution in https://github.com/datahub-project/datahub/pull/9128
* [@darnaut](https://github.com/darnaut) made their first contribution in https://github.com/datahub-project/datahub/pull/9169
* [@walter9388](https://github.com/walter9388) made their first contribution in https://github.com/datahub-project/datahub/pull/9162
* [@sumitappt](https://github.com/sumitappt) made their first contribution in https://github.com/datahub-project/datahub/pull/9156
* [@gaurav2733](https://github.com/gaurav2733) made their first contribution in https://github.com/datahub-project/datahub/pull/9140
* [@purnimagarg1](https://github.com/purnimagarg1) made their first contribution in https://github.com/datahub-project/datahub/pull/9216
* [@YuriyGavrilov](https://github.com/YuriyGavrilov) made their first contribution in https://github.com/datahub-project/datahub/pull/9019
* [@PGuiv](https://github.com/PGuiv) made their first contribution in https://github.com/datahub-project/datahub/pull/9239
* [@Salman-Apptware](https://github.com/Salman-Apptware) made their first contribution in https://github.com/datahub-project/datahub/pull/9198
* [@kevin1chun](https://github.com/kevin1chun) made their first contribution in https://github.com/datahub-project/datahub/pull/9268
* [@noggi](https://github.com/noggi) made their first contribution in https://github.com/datahub-project/datahub/pull/9267
* [@SimonOsipov](https://github.com/SimonOsipov) made their first contribution in https://github.com/datahub-project/datahub/pull/9301
* [@terratrue-daniel](https://github.com/terratrue-daniel) made their first contribution in https://github.com/datahub-project/datahub/pull/9313
* [@allizex](https://github.com/allizex) made their first contribution in https://github.com/datahub-project/datahub/pull/9322
* [@MideO](https://github.com/MideO) made their first contribution in https://github.com/datahub-project/datahub/pull/8344
* [@middagj](https://github.com/middagj) made their first contribution in https://github.com/datahub-project/datahub/pull/9341
* [@accso-jo](https://github.com/accso-jo) made their first contribution in https://github.com/datahub-project/datahub/pull/9204
* [@matthiasdg](https://github.com/matthiasdg) made their first contribution in https://github.com/datahub-project/datahub/pull/9385
* [@haeniya](https://github.com/haeniya) made their first contribution in https://github.com/datahub-project/datahub/pull/9215
* [@olgadimova](https://github.com/olgadimova) made their first contribution in https://github.com/datahub-project/datahub/pull/9222

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v0.12.0...v0.12.1

## [v0.12.1rc2](https://github.com/datahub-project/datahub/releases/tag/v0.12.1rc2) {#v0-12-1rc2}

Released on 2023-11-28 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.12.1rc2) for v0.12.1rc2 on GitHub.

## [v0.12.0](https://github.com/datahub-project/datahub/releases/tag/v0.12.0) {#v0-12-0}

Released on 2023-10-25 by [@pedro93](https://github.com/pedro93).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.12.0) for v0.12.0 on GitHub.

## [v0.11.0](https://github.com/datahub-project/datahub/releases/tag/v0.11.0) {#v0-11-0}

Released on 2023-09-08 by [@iprentic](https://github.com/iprentic).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.11.0) for v0.11.0 on GitHub.

## [v0.10.5](https://github.com/datahub-project/datahub/releases/tag/v0.10.5) {#v0-10-5}

Released on 2023-08-02 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.5) for v0.10.5 on GitHub.

## [v0.10.4](https://github.com/datahub-project/datahub/releases/tag/v0.10.4) {#v0-10-4}

Released on 2023-06-09 by [@pedro93](https://github.com/pedro93).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.4) for v0.10.4 on GitHub.

## [v0.10.3](https://github.com/datahub-project/datahub/releases/tag/v0.10.3) {#v0-10-3}

Released on 2023-05-25 by [@iprentic](https://github.com/iprentic).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.3) for v0.10.3 on GitHub.

## [DataHub v0.10.2](https://github.com/datahub-project/datahub/releases/tag/v0.10.2) {#v0-10-2}

Released on 2023-04-13 by [@iprentic](https://github.com/iprentic).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.2) for DataHub v0.10.2 on GitHub.

## [DataHub v0.10.1](https://github.com/datahub-project/datahub/releases/tag/v0.10.1) {#v0-10-1}

Released on 2023-03-23 by [@aditya-radhakrishnan](https://github.com/aditya-radhakrishnan).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.1) for DataHub v0.10.1 on GitHub.

## [DataHub v0.10.0](https://github.com/datahub-project/datahub/releases/tag/v0.10.0) {#v0-10-0}

Released on 2023-02-07 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.10.0) for DataHub v0.10.0 on GitHub.

## [DataHub v0.9.6.1](https://github.com/datahub-project/datahub/releases/tag/v0.9.6.1) {#v0-9-6-1}

Released on 2023-01-31 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.6.1) for DataHub v0.9.6.1 on GitHub.

## [DataHub v0.9.6](https://github.com/datahub-project/datahub/releases/tag/v0.9.6) {#v0-9-6}

Released on 2023-01-13 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.6) for DataHub v0.9.6 on GitHub.

## [DataHub v0.9.5](https://github.com/datahub-project/datahub/releases/tag/v0.9.5) {#v0-9-5}

Released on 2022-12-23 by [@jjoyce0510](https://github.com/jjoyce0510).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.5) for DataHub v0.9.5 on GitHub.

## [[Known Issues] DataHub v0.9.4](https://github.com/datahub-project/datahub/releases/tag/v0.9.4) {#v0-9-4}

Released on 2022-12-20 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.4) for [Known Issues] DataHub v0.9.4 on GitHub.

## [DataHub v0.9.3](https://github.com/datahub-project/datahub/releases/tag/v0.9.3) {#v0-9-3}

Released on 2022-11-30 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.3) for DataHub v0.9.3 on GitHub.

## [DataHub v0.9.2](https://github.com/datahub-project/datahub/releases/tag/v0.9.2) {#v0-9-2}

Released on 2022-11-04 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.2) for DataHub v0.9.2 on GitHub.

## [DataHub v0.9.1](https://github.com/datahub-project/datahub/releases/tag/v0.9.1) {#v0-9-1}

Released on 2022-10-31 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.1) for DataHub v0.9.1 on GitHub.

## [DataHub v0.9.0](https://github.com/datahub-project/datahub/releases/tag/v0.9.0) {#v0-9-0}

Released on 2022-10-11 by [@szalai1](https://github.com/szalai1).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.9.0) for DataHub v0.9.0 on GitHub.

## [DataHub v0.8.45](https://github.com/datahub-project/datahub/releases/tag/v0.8.45) {#v0-8-45}

Released on 2022-09-23 by [@gabe-lyons](https://github.com/gabe-lyons).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.45) for DataHub v0.8.45 on GitHub.

## [DataHub v0.8.44](https://github.com/datahub-project/datahub/releases/tag/v0.8.44) {#v0-8-44}

Released on 2022-09-01 by [@jjoyce0510](https://github.com/jjoyce0510).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.44) for DataHub v0.8.44 on GitHub.

## [DataHub v0.8.43](https://github.com/datahub-project/datahub/releases/tag/v0.8.43) {#v0-8-43}

Released on 2022-08-09 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.43) for DataHub v0.8.43 on GitHub.

## [v0.8.42](https://github.com/datahub-project/datahub/releases/tag/v0.8.42) {#v0-8-42}

Released on 2022-08-03 by [@gabe-lyons](https://github.com/gabe-lyons).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.42) for v0.8.42 on GitHub.

## [v0.8.41](https://github.com/datahub-project/datahub/releases/tag/v0.8.41) {#v0-8-41}

Released on 2022-07-15 by [@anshbansal](https://github.com/anshbansal).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.41) for v0.8.41 on GitHub.

## [v0.8.40](https://github.com/datahub-project/datahub/releases/tag/v0.8.40) {#v0-8-40}

Released on 2022-06-30 by [@gabe-lyons](https://github.com/gabe-lyons).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.40) for v0.8.40 on GitHub.

## [v0.8.39](https://github.com/datahub-project/datahub/releases/tag/v0.8.39) {#v0-8-39}

Released on 2022-06-24 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.39) for v0.8.39 on GitHub.

## [[!] DataHub v0.8.38](https://github.com/datahub-project/datahub/releases/tag/v0.8.38) {#v0-8-38}

Released on 2022-06-09 by [@jjoyce0510](https://github.com/jjoyce0510).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.38) for [!] DataHub v0.8.38 on GitHub.

## [[!] DataHub v0.8.37](https://github.com/datahub-project/datahub/releases/tag/v0.8.37) {#v0-8-37}

Released on 2022-06-09 by [@jjoyce0510](https://github.com/jjoyce0510).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.37) for [!] DataHub v0.8.37 on GitHub.

## [DataHub V0.8.36](https://github.com/datahub-project/datahub/releases/tag/v0.8.36) {#v0-8-36}

Released on 2022-06-02 by [@treff7es](https://github.com/treff7es).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.36) for DataHub V0.8.36 on GitHub.

## [[!] DataHub v0.8.35](https://github.com/datahub-project/datahub/releases/tag/v0.8.35) {#v0-8-35}

Released on 2022-05-18 by [@dexter-mh-lee](https://github.com/dexter-mh-lee).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.35) for [!] DataHub v0.8.35 on GitHub.

## [v0.8.34](https://github.com/datahub-project/datahub/releases/tag/v0.8.34) {#v0-8-34}

Released on 2022-05-04 by [@maggiehays](https://github.com/maggiehays).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.8.34) for v0.8.34 on GitHub.

