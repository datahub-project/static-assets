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
| **v0.15.0** | 2025-01-15 |[Release Notes](#v0-15-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.15.0) |
| **v0.14.1** | 2024-09-17 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.14.1) |
| **v0.14.0.2** | 2024-08-21 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.14.0.2) |
| **v0.14.0** | 2024-08-13 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.14.0) |
| **v0.13.3** | 2024-05-23 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.3) |
| **v0.13.2** | 2024-04-16 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.2) |
| **v0.13.1** | 2024-04-02 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.1) |
| **v0.13.0** | 2024-02-29 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) |
| **v0.12.1** | 2023-12-08 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.12.1) |
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


## [V0.15.0](https://github.com/datahub-project/datahub/releases/tag/v0.15.0) {#v0-15-0}

Released on 2025-01-15 by [@pedro93](https://github.com/pedro93).

### DataHub v0.15.0 Release Notes

#### User Experience

* **Structured Properties**
  * Added comprehensive support for managing structured properties, including creation, editing, deletion, and display preferences. Introduced timestamps for tracking creation and modification. [[#12100](https://github.com/datahub-project/datahub/pull/12100), [#11419](https://github.com/datahub-project/datahub/pull/11419)]
  * Enhanced property display options with badge styling, custom column types, and configurable visibility settings in asset sidebars and schema fields. [[#12111](https://github.com/datahub-project/datahub/pull/12111), [#12052](https://github.com/datahub-project/datahub/pull/12052)]
  * Added structured property filtering in UI with improved aggregation logic and entity metadata display. Introduced new property validators and display settings. [[#12097](https://github.com/datahub-project/datahub/pull/12097), [#12099](https://github.com/datahub-project/datahub/pull/12099)]

* **UI Enhancements**
  * Enhanced container organization with parent hierarchy labels. [[#11705](https://github.com/datahub-project/datahub/pull/11705)] 
  * Added support for markdown in incident descriptions, enabling rich formatting capabilities. [[#11759](https://github.com/datahub-project/datahub/pull/11759)]
  * Improved ingestion reporting with better visibility of successful ingestions with warnings. Enhanced browse paths display for business attributes and schema fields. [[#11704](https://github.com/datahub-project/datahub/pull/11704), [#11585](https://github.com/datahub-project/datahub/pull/11585)]
  * Added support for timeseries aspects in OpenAPI and customizable date range fields for Analytics charts. [[#12096](https://github.com/datahub-project/datahub/pull/12096), [#11366](https://github.com/datahub-project/datahub/pull/11366)]

* **Authorization & Authentication**
  * Enabled authentication and API authorization by default, with support for URN-wildcard-based policies using STARTS_WITH condition. [[#11484](https://github.com/datahub-project/datahub/pull/11484), [#11441](https://github.com/datahub-project/datahub/pull/11441)]
  * Added authorization checks for managing Glossary terms, including privileges for ownership, domain management, and link actions. [[#11337](https://github.com/datahub-project/datahub/pull/11337)]

#### Metadata Ingestion 

##### Ingestion Framework Improvements

* **Enhanced Data Source Support**: Expanded ingestion capabilities for multiple platforms, including Superset (with dataset entities, schema fields, and column-level lineage), Feast (supporting tags and owners ingestion), Neo4j, and Cassandra. Added stateful ingestion support for file sources. [[#11688](https://github.com/datahub-project/datahub/pull/11688), [#11784](https://github.com/datahub-project/datahub/pull/11784), [#11804](https://github.com/datahub-project/datahub/pull/11804), [#11526](https://github.com/datahub-project/datahub/pull/11526), [#11822](https://github.com/datahub-project/datahub/pull/11822)]

* **SQL Processing Improvements**: Replaced vulnerable sqlparse dependency with an in-house SQL parser, optimized CLL generation with reduced memory usage, and added special handling for MSSQL case sensitivity. Enhanced multi-query lineage support for Snowflake temporary tables. [[#11645](https://github.com/datahub-project/datahub/pull/11645), [#11708](https://github.com/datahub-project/datahub/pull/11708), [#11920](https://github.com/datahub-project/datahub/pull/11920), [#12020](https://github.com/datahub-project/datahub/pull/12020)]

* **CLI Enhancements**: Introduced new commands for managing ingestion, including listing source runs with filtering capabilities, undoing soft deletes with platform filtering, and listing structured properties. Added an offline flag to the SQL parser CLI. [[#11740](https://github.com/datahub-project/datahub/pull/11740), [#11980](https://github.com/datahub-project/datahub/pull/11980), [#12012](https://github.com/datahub-project/datahub/pull/12012), [#12283](https://github.com/datahub-project/datahub/pull/12283), [#11635](https://github.com/datahub-project/datahub/pull/11635)]

* **Ownership and Metadata Management**: Extended ownership transformer capabilities across entities, improved glossary sync to preserve custom ownership types, and added support for multiple ownership types in glossaries and terms. Enhanced Forms CLI with additional filters for subtypes, platform instances, owners, tags, and glossary terms. [[#11700](https://github.com/datahub-project/datahub/pull/11700), [#11545](https://github.com/datahub-project/datahub/pull/11545), [#12050](https://github.com/datahub-project/datahub/pull/12050), [#10979](https://github.com/datahub-project/datahub/pull/10979)]

* **Core Infrastructure Improvements**: Implemented unique URN generation for all entities, added support for efficient entity ingestion through `get_entity_as_mcps`, improved empty field handling, and introduced progress reporting during ingestion. Added execution request cleanup job and support for dropping duplicate schema fields. [[#11676](https://github.com/datahub-project/datahub/pull/11676), [#11425](https://github.com/datahub-project/datahub/pull/11425), [#11613](https://github.com/datahub-project/datahub/pull/11613), [#12117](https://github.com/datahub-project/datahub/pull/12117), [#11765](https://github.com/datahub-project/datahub/pull/11765), [#12308](https://github.com/datahub-project/datahub/pull/12308)]

##### Source-Specific Ingestion Improvements

**Airflow**
  * Upgraded infrastructure with support for Airflow 2.10, deprecated versions below 2.3, and improved template handling with Jinja support. Added configuration options for dag patterns and environment variables. [[#11300](https://github.com/datahub-project/datahub/pull/11300), [#11371](https://github.com/datahub-project/datahub/pull/11371), [#11472](https://github.com/datahub-project/datahub/pull/11472), [#11537](https://github.com/datahub-project/datahub/pull/11537), [#11579](https://github.com/datahub-project/datahub/pull/11579), [#12056](https://github.com/datahub-project/datahub/pull/12056)]
  * Enhanced error handling and debugging with improved logging, fixed plugin stability issues on EMR, and added support for AthenaOperator lineage extraction. Introduced ability to disable plugin without restart. [[#11857](https://github.com/datahub-project/datahub/pull/11857), [#11877](https://github.com/datahub-project/datahub/pull/11877), [#11880](https://github.com/datahub-project/datahub/pull/11880), [#12098](https://github.com/datahub-project/datahub/pull/12098)]

**BigQuery**
  * Enhanced data modeling capabilities with support for foreign/primary keys, BigLake tables, and improved handling of external tables. Added support for region qualifiers and partition management. [[#11686](https://github.com/datahub-project/datahub/pull/11686), [#11728](https://github.com/datahub-project/datahub/pull/11728), [#11874](https://github.com/datahub-project/datahub/pull/11874), [#11940](https://github.com/datahub-project/datahub/pull/11940)]
  * Improved lineage tracking with GCS data source support and optimized query performance. Added platform resource entity generation from BigQuery labels. [[#11442](https://github.com/datahub-project/datahub/pull/11442), [#11492](https://github.com/datahub-project/datahub/pull/11492), [#11534](https://github.com/datahub-project/datahub/pull/11534), [#11602](https://github.com/datahub-project/datahub/pull/11602)]
  * Enhanced profiling and performance with better type handling and size limits. Fixed issues with tag synchronization and platform instance settings. [[#11807](https://github.com/datahub-project/datahub/pull/11807), [#12060](https://github.com/datahub-project/datahub/pull/12060)]

**Dagster**
  * Added support for skipping Asset ingestion, fixed input/output value formatting, and improved compatibility with latest Dagster versions (v1.9.6). Deprecated Python 3.8 support. [[#11262](https://github.com/datahub-project/datahub/pull/11262), [#11481](https://github.com/datahub-project/datahub/pull/11481), [#12121](https://github.com/datahub-project/datahub/pull/12121), [#12189](https://github.com/datahub-project/datahub/pull/12189)]

**dbt**
  * Improved performance and functionality with node_name_patterns for faster CLL processing, support for multiple test paths, and better handling of custom owner types. [[#11450](https://github.com/datahub-project/datahub/pull/11450), [#11460](https://github.com/datahub-project/datahub/pull/11460), [#11848](https://github.com/datahub-project/datahub/pull/11848)]
  * Enhanced lineage handling by preventing cycles in SQL parsing and supporting multiple dataset assertions for tests. Added support for dbt Cloud's Explore page. [[#11666](https://github.com/datahub-project/datahub/pull/11666), [#11451](https://github.com/datahub-project/datahub/pull/11451), [#12223](https://github.com/datahub-project/datahub/pull/12223)]

**Snowflake**
  * Expanded support for various table types, including secure, dynamic, and hybrid tables. Enhanced lineage capabilities for renames, swaps, and external tables. [[#11600](https://github.com/datahub-project/datahub/pull/11600), [#12039](https://github.com/datahub-project/datahub/pull/12039), [#12094](https://github.com/datahub-project/datahub/pull/12094), [#12179](https://github.com/datahub-project/datahub/pull/12179)]
  * Improved authentication with OAuth support and token management. Added incremental property processing and structured property support for tags. [[#11888](https://github.com/datahub-project/datahub/pull/11888), [#12048](https://github.com/datahub-project/datahub/pull/12048), [#12080](https://github.com/datahub-project/datahub/pull/12080), [#12285](https://github.com/datahub-project/datahub/pull/12285)]
  * Enhanced error handling and logging with better parse failure reporting and dot handling in table names. [[#12105](https://github.com/datahub-project/datahub/pull/12105), [#12110](https://github.com/datahub-project/datahub/pull/12110), [#12153](https://github.com/datahub-project/datahub/pull/12153)]

**Tableau**
  * Enhanced project management with new path pattern filtering and improved handling of hidden assets. Added support for access roles and group permissions. [[#10855](https://github.com/datahub-project/datahub/pull/10855), [#11157](https://github.com/datahub-project/datahub/pull/11157), [#11559](https://github.com/datahub-project/datahub/pull/11559)]
  * Improved API integration with retry logic for various error codes (502, 504), better authentication handling, and consistent page size application. [[#12213](https://github.com/datahub-project/datahub/pull/12213), [#12216](https://github.com/datahub-project/datahub/pull/12216), [#12233](https://github.com/datahub-project/datahub/pull/12233)]
  * Enhanced reporting and debugging capabilities while maintaining efficient performance and proper permission handling. [[#12015](https://github.com/datahub-project/datahub/pull/12015), [#12024](https://github.com/datahub-project/datahub/pull/12024), [#12175](https://github.com/datahub-project/datahub/pull/12175)]

**PowerBI**
  * Improved M-query parsing with support for comments, better handling of quotes, and DatabricksMultiCloud native query functionality. [[#12177](https://github.com/datahub-project/datahub/pull/12177), [#11743](https://github.com/datahub-project/datahub/pull/11743), [#11756](https://github.com/datahub-project/datahub/pull/11756)]
  * Enhanced workspace management with cross-workspace dataset linking and app ingestion support. Added timeouts for M-query parsing. [[#11560](https://github.com/datahub-project/datahub/pull/11560), [#11629](https://github.com/datahub-project/datahub/pull/11629), [#11753](https://github.com/datahub-project/datahub/pull/11753)]
  * Improved error reporting and performance optimization with reduced type casting and better organization of responsibilities. [[#11763](https://github.com/datahub-project/datahub/pull/11763), [#12004](https://github.com/datahub-project/datahub/pull/12004)]

#### Developer Experience

* **Entity Management**: Introduced entity versioning for Datasets and ML Models, with support for version set linking. Improved timeline functionality with better handling of primary key changes and rename events. Added data transformation logic models to enhance data processing capabilities. [[#11819](https://github.com/datahub-project/datahub/pull/11819), [#11843](https://github.com/datahub-project/datahub/pull/11843), [#12166](https://github.com/datahub-project/datahub/pull/12166), [#12198](https://github.com/datahub-project/datahub/pull/12198)]

* **Enhanced Configuration Management**: Added new customization options through environment variables and Helm charts, including editable dataset names and configurable garbage collection scheduling. The bootstrap process has been optimized to reduce latency during installation. [[#11391](https://github.com/datahub-project/datahub/pull/11391), [#11518](https://github.com/datahub-project/datahub/pull/11518)]

* **Development Environment Updates**: Added Git support to the ingestion-base image, enabling better source control integration for ingestion workflows. [[#11477](https://github.com/datahub-project/datahub/pull/11477)]

* **Security Logging Enhancement**: Improved security audit trails by adding actor URN tracking for unauthorized access attempts. [[#12030](https://github.com/datahub-project/datahub/pull/12030)]

##### NEW: Garbage Collection

* **Comprehensive Metadata Cleanup**: Introduced a new ingestion source: [DataHubGC](https://datahubproject.io/docs/generated/ingestion/sources/datahubgc) to function as a garbage collector for managing dataflows, data jobs, and data process instances, with configurable retention policies and deletion parameters. Added dry run mode for testing cleanup operations. [[#11102](https://github.com/datahub-project/datahub/pull/11102), [#11413](https://github.com/datahub-project/datahub/pull/11413)]

* **Performance Optimizations**: Significantly improved processing speed from 1 hour to 15 minutes by implementing batch processing, optimizing queries, and removing unnecessary operations. Increased default hard delete limit from 10k to 25k entities. [[#11809](https://github.com/datahub-project/datahub/pull/11809), [#12093](https://github.com/datahub-project/datahub/pull/12093), [#12238](https://github.com/datahub-project/datahub/pull/12238)]

* **Reliability Improvements**: Enhanced garbage collection stability with additional validation checks, improved error handling, and better process visibility through ingestion stage reporting. Fixed issues with entity deletion logic and reference handling to preserve critical lineage relationships. [[#12011](https://github.com/datahub-project/datahub/pull/12011), [#12013](https://github.com/datahub-project/datahub/pull/12013), [#12027](https://github.com/datahub-project/datahub/pull/12027), [#12049](https://github.com/datahub-project/datahub/pull/12049), [#12124](https://github.com/datahub-project/datahub/pull/12124), [#12226](https://github.com/datahub-project/datahub/pull/12226)]

#### Thank You to Our Contributors!

##### First-Time Contributors
[@AColocho](https://github.com/AColocho), [@alberttwong](https://github.com/alberttwong), [@Alice-608](https://github.com/Alice-608), [@Bumyu](https://github.com/Bumyu), [@chakru-r](https://github.com/chakru-r), [@chriscc2](https://github.com/chriscc2), [@dejan2609](https://github.com/dejan2609), [@donovan-acryl](https://github.com/donovan-acryl), [@eagle-25](https://github.com/eagle-25), [@hwmarkcheng](https://github.com/hwmarkcheng), [@k-bartlett](https://github.com/k-bartlett), [@kanavnarula](https://github.com/kanavnarula), [@kartikey-visa](https://github.com/kartikey-visa), [@kevinkarchacryl](https://github.com/kevinkarchacryl), [@kousiknandy](https://github.com/kousiknandy), [@kris48k](https://github.com/kris48k), [@llance](https://github.com/llance), [@margaridafernandes-trip](https://github.com/margaridafernandes-trip), [@mikeburke24](https://github.com/mikeburke24), [@raudzis](https://github.com/raudzis), [@ronybony1990](https://github.com/ronybony1990), [@ryota-cloud](https://github.com/ryota-cloud), [@shepherd44](https://github.com/shepherd44), [@siong-tcha](https://github.com/siong-tcha), [@ssidorenko](https://github.com/ssidorenko), [@tanguyantoine](https://github.com/tanguyantoine), [@th0ger](https://github.com/th0ger), [@udays-visa](https://github.com/udays-visa), [@udbhav-hbk](https://github.com/udbhav-hbk), [@vejeta](https://github.com/vejeta)

##### Repeat Contributors
[@aviv-julienjehannet](https://github.com/aviv-julienjehannet), [@bda618](https://github.com/bda618), [@bossenti](https://github.com/bossenti), [@darnaut](https://github.com/darnaut), [@deepgarg-visa](https://github.com/deepgarg-visa), [@DSchmidtDev](https://github.com/DSchmidtDev), [@dushayntAW](https://github.com/dushayntAW), [@eboneil](https://github.com/eboneil), [@ethan-cartwright](https://github.com/ethan-cartwright), [@feldjay](https://github.com/feldjay), [@githendrik](https://github.com/githendrik), [@haeniya](https://github.com/haeniya), [@Jorricks](https://github.com/Jorricks), [@Masterchen09](https://github.com/Masterchen09), [@mkamalas](https://github.com/mkamalas), [@Nbagga14](https://github.com/Nbagga14), [@nicholas-fwang](https://github.com/nicholas-fwang), [@noggi](https://github.com/noggi), [@pankajmahato-visa](https://github.com/pankajmahato-visa), [@pinakipb2](https://github.com/pinakipb2), [@rtekal](https://github.com/rtekal), [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware), [@steffengr](https://github.com/steffengr)

##### DataHub Maintainers
[@acrylJonny](https://github.com/acrylJonny), [@anshbansal](https://github.com/anshbansal), [@asikowitz](https://github.com/asikowitz), [@chriscollins3456](https://github.com/chriscollins3456), [@david-leifker](https://github.com/david-leifker), [@gabe-lyons](https://github.com/gabe-lyons), [@hsheth2](https://github.com/hsheth2), [@jayacryl](https://github.com/jayacryl), [@jjoyce0510](https://github.com/jjoyce0510), [@maggiehays](https://github.com/maggiehays), [@mayurinehate](https://github.com/mayurinehate), [@pedro93](https://github.com/pedro93), [@RyanHolstien](https://github.com/RyanHolstien), [@sakethvarma397](https://github.com/sakethvarma397), [@sgomezvillamor](https://github.com/sgomezvillamor), [@shirshanka](https://github.com/shirshanka), [@sid-acryl](https://github.com/sid-acryl), [@skrydal](https://github.com/skrydal), [@treff7es](https://github.com/treff7es), [@yoonhyejin](https://github.com/yoonhyejin)

#### What's Changed
* fix(ingest): override setdefault in file-backed dict by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11359
* fix(ingest/airflow): simplify env configuration by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11371
* fix(airflow): added support for jinja template for datahub emitter operator by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/11300
* fix(smoke-test): add wait for sync to smoke-test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11405
* fix(customSearch): apply query string interpolation to function score by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11406
* fix(docs): Fix typo in bigquery permissions error by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/11401
* build(deps-dev): bump vite from 4.5.3 to 4.5.5 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11410
* feat(ingest/gc): Add dataflow and soft deleted entities cleanup by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11102
* feat(ingestion): adds env property in ContainerProperties by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/11214
* feat(ingest/gc): Add dry run mode to gc recipe by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11413
* feat(kafka-setup): allow override KAFKA_HEAP_OPTS by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11400
* chore(docs): update release notes v0.14.1 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11408
* Advance search - Added case sensitive flag for wildcard searches by [@kanavnarula](https://github.com/kanavnarula) in https://github.com/datahub-project/datahub/pull/11272
* fix(changeGenerator): fixes schema change generator corner cases v2 by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11386
* feat(docs-site) datahub homepage v2 by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11342
* feat(structuredProps) Add created and lastModified timestamps to structured prop entity by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11419
* feat(docs-site) tours to open in a modal by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11420
* feat(structuredProps) Add delete structured props endpoint and handle null props by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11418
* test(ingest/mcp_diff): Fallback to overwriting file on more complicated diffs by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11407
* feat(docs-site) fixed home paddings on mobile site by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11431
* feat(ingest): add `get_entity_as_mcps` method to client by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11425
* fix(siblings) Combine siblings in embedded search results by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11421
* fix(structuredProps) Fix adding new allowed types in updateStructuredProp endpoint by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11424
* build(deps): bump path-to-regexp from 1.8.0 to 1.9.0 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11356
* chore(bump): bump spring versions by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11435
* chore(bump): pac4j version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11436
* fix(graphql/getDataset): Do not fetch parent for schema fields by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11434
* build: allow gradle daemon by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11437
* fix(ingest/dbt): handle null index values by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11433
* build(deps): bump dompurify from 2.3.8 to 2.5.4 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11387
* build(deps): bump dset from 3.1.3 to 3.1.4 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11361
* fix(ingest/dbt): fix dbt catalog version check by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11350
* Add STARTS_WITH policy condition to allow for URN-wildcard-based policies by [@githendrik](https://github.com/githendrik) in https://github.com/datahub-project/datahub/pull/11441
* fix(restoreIndices): fix bug in urn paginated restoreIndices exit code by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11443
* feat(Analytics) Allow dateRangeField to be configurable for timeSeries chart by [@mkamalas](https://github.com/mkamalas) in https://github.com/datahub-project/datahub/pull/11366
* fix(SearchDocumentTransformer): Use correct variable to update ES by [@pinakipb2](https://github.com/pinakipb2) in https://github.com/datahub-project/datahub/pull/11430
* chore(version): bump protobuf version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11446
* fix(search): restore prefix phrase match on quoted search by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11444
* fix(oidc): apply acr values to redirect url by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11447
* refactor(ui/lineage): Replace FetchedEntities Object with Map by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11440
* feat(ingest/sink): report datahub-rest sink mode by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11422
* docs(ingest): add docs on pydantic compatibility by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11423
* chore: use unique docker log artifact names by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11445
* test(graphql): fix searchFlags in searchAcrossLineage by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11448
* Update pr-labeler.yml by [@donovan-acryl](https://github.com/donovan-acryl) in https://github.com/datahub-project/datahub/pull/11393
* fix(docs): fix layout in documentation after [#11380](https://github.com/datahub-project/datahub/pull/11380) by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/11390
* Group Modal Css fix by [@kanavnarula](https://github.com/kanavnarula) in https://github.com/datahub-project/datahub/pull/11403
* feat(graph): graph index soft-delete support by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11453
* config(reindex): create reindex timeout configuration by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11456
* fix(ingest): sort by last modified not working in the UI by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11343
* feat(data-contracts): support custom assertions in the data contracts builder by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11454
* fix(ingest/sqlglot): Make detach_ctes more robust by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11449
* fix(ingest/mode): add connection timeouts to avoid RemoteDisconnected errors by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11245
* build(gradle): Update gradle.properties by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11458
* build(yarn): increase yarn timeout and version bump by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11461
* fix(ingest/dbt): allow custom owner types for dbt meta by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11460
* doc: fix typo by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11464
* fix(ingestion/looker):  skip personal folder independent looks by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11415
* bump(version): zookeeper by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11465
* fix(ingest): do not cache temporary tables schema resolvers by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11432
* fix(structuredProps) Allow upserting structured props on schema fields that don't exist by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11466
* fix(docs-website): disable dark mode by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11468
* fix: fix broken global style by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11470
* feat(ingest/dbt): speed up dbt CLL with node_name_patterns by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11450
* feat(ingest/dbt): produce multiple assertions for multi-table dbt tests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11451
* feat(ingest): add `git` to ingestion-base image by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11477
* fix(ingest): include platform instance in looker usage urns by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11469
* fix(ingest/openapi): update recipe for DataHub OpenAPI with url_complement and bearer token by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/10980
* docs(aws): Update AWS docs to keep consistency with Docker docs by [@AColocho](https://github.com/AColocho) in https://github.com/datahub-project/datahub/pull/11284
* feat: add second navbar by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11471
* feat: CTA to live demos in cloud section and a few more case studies on home by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11488
* fix(ingest/bq): do not query PARTITIONS for biglake tables by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11463
* config(rest-api): enable authentication and api authorization by default by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11484
* feat(ingest/databricks): add usage perf report by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11480
* feat(ingestion/tableau): introduce project_path_pattern by [@haeniya](https://github.com/haeniya) in https://github.com/datahub-project/datahub/pull/10855
* docs(ingest/dbt): update run result paths examples by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11138
* feat(ingest): support `DATAHUB_INCLUDE_ENV_IN_CONTAINER_PROPERTIES` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11476
* refactor(criterion): refactor criterion construction by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11486
* feat(auth) - Manage Children Glossary term authorization check for Owner, Domain, Remove link by [@mkamalas](https://github.com/mkamalas) in https://github.com/datahub-project/datahub/pull/11337
* fix(ingest/dagster): Fixing path to the dagster logo by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11489
* docker(config): Update docker profiles by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11495
* fix(docs): fix form type by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/11497
* fix(fragments.graphql): values is a correct parameter for FacetFilterInput by [@bda618](https://github.com/bda618) in https://github.com/datahub-project/datahub/pull/11485
* feat: made datahub home page colors more consistent by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11496
* fix(ingest/bigquery): optimise queries v2 session processing by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11492
* feat(ingest/elasticsearch): add api_key auth by [@th0ger](https://github.com/th0ger) in https://github.com/datahub-project/datahub/pull/11475
* fix(doc): Update the documentation for Timeline API by [@sakethvarma397](https://github.com/sakethvarma397) in https://github.com/datahub-project/datahub/pull/11504
* docs(upgrade): add note about downgrade limitation by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11507
* fix(docs-website): corrected minor alignment issues on the home page by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11508
* chore(cleanup): remove legacy bootstrap step by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11494
* docs(search): example of entity weighting by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11511
* feat(businessattribute): filter schema rows on business-attribute pro… by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/11502
* fix(ingest/lookml): missing lineage for looker template -- if prod by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11426
* fix(ingestion/transformer): Add container support for ownership and domains by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11375
* fix(ingestion/nifi): Improve nifi lineage extraction performance by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11490
* fix(dagster-plugin): Fix in/outs format and source config by [@DSchmidtDev](https://github.com/DSchmidtDev) in https://github.com/datahub-project/datahub/pull/11481
* fix(ingest/elasticsearch): detect sub-properties in 'nested' type mapping by [@Bumyu](https://github.com/Bumyu) in https://github.com/datahub-project/datahub/pull/11338
* chore: update case studies by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11520
* feat: visa case study with a text label instead of logo by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11521
* feat(docs-site) added snap logo by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11522
* fix(ingest/looker) : Handle DeserializeError to improve error reporting. by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11457
* build(misc): misc build, config, version updates by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11527
* feat: add miro & foursquare & Deutsche Telekom by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11516
* fix(ingestion/nifi): Fix for incremental lineage ingestion for nifi by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11517
* fix(tests): fix metadata-io tests by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11530
* fix(search): Fix empty description by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11514
* Block http trace method on mce and mce consumers  by [@udays-visa](https://github.com/udays-visa) in https://github.com/datahub-project/datahub/pull/11513
* feat(bootstrap): bootstrap template mcps by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11518
* add new CREATE and UPDATE privileges for USERS_AND_GROUPS by [@githendrik](https://github.com/githendrik) in https://github.com/datahub-project/datahub/pull/11364
* feat(graphql/lineage): Support including ghost entities by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11510
* fix(ingest/sigma): handle members api paginated response by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11535
* fix(metadata-service): Pass editableDatasetNameEnabled feature flag to the config. by [@kris48k](https://github.com/kris48k) in https://github.com/datahub-project/datahub/pull/11391
* Added IEQUAL operator to support case insensitive searches by [@Nbagga14](https://github.com/Nbagga14) in https://github.com/datahub-project/datahub/pull/11501
* build(deps): bump rollup from 3.29.4 to 3.29.5 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11459
* build(deps): bump express from 4.19.2 to 4.20.0 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11357
* build(deps): bump fast-loops from 1.1.3 to 1.1.4 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/10885
* feat(fabric): Add sandbox as a possible environment variable by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/11491
* chore(bump): bump commons, misc versions by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11538
* feat(dataProduct): add data product unset side effect by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11512
* fix(search): Elasticsearch bool query should by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11536
* fix(changeGenerator): fix logic around descriptions and make execution more efficient by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11539
* feat(models): add support for generic platform resources by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11531
* fix(ingest): fix UnboundLocalError in dataproduct transformer by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11528
* fix(ingest): add typeUrn in glossary sync source by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11545
* fix(docs-site) cloud form copy spelling error by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11455
* fix(propagation): show last modified propagated documentation by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11498
* privileges(refactor): consolidate individual sys op privileges by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11549
* feat(website): added built by acryl and linkedin to home hero by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11548
* feat(ingest/bigquery): casing for tmp table check for queries v2 by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11534
* fix(ingestion/powerbi): fix for databricks lineage m-query pattern by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11462
* fix(datahub-gc): set system flag on ingestion source by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11554
* fix(lint): fix yarn lint breakage from [#11498](https://github.com/datahub-project/datahub/pull/11498) by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11553
* chore(ci): bump trivy action version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11555
* feat(docker-profiles): add elasticsearch envs to docker profiles by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11546
* sdk(platform-resource): add entity type for ease of use by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11541
* docs(release): 0.3.6 - docs update by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11506
* fix(datahub-gc):  Update ingestion-datahub-gc.yaml by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11556
* fix(ci): fix cassandra test flake by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11557
* feat(scan): add scanning to setup images by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11563
* Fix data search for fieldType = OBJECT for non-string fields by [@udbhav-hbk](https://github.com/udbhav-hbk) in https://github.com/datahub-project/datahub/pull/11524
* docs(search): add structured search examples for structured properties by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11565
* docs(datahub source): Add urn exclusions to docs by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/11568
* docs(csv-enricher): Add warning for write_semantics by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/11561
* fix(test): fix test specific for single query by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11567
* feat(ingest/bigquery): Add way to reference existing DataHub Tag from a bigquery label by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11544
* chore: remove obsolete attribute from docker by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11573
* fix(cli): update hard delete confirmation message in delete cli by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11550
* feat(ingest/stateful): omit irrelevant urns for deletion by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11558
* feat(ingest): add extra reporting for rest sink ASYNC_BATCH mode by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11562
* feat(models): support dashboards containing dashboards by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11529
* feat(ingest): support `__from_env__` special server value by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11569
* fix(test): Update EbeanAspectDaoTest.java by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11580
* feat(airflow): add a `render_templates` config parameter by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11537
* feat(ingest): add preset source by [@llance](https://github.com/llance) in https://github.com/datahub-project/datahub/pull/10954
* fix(ui): update soft-deletion banner message by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11571
* fix(ingest/looker): handle sdk error for folder_ancestors by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11575
* feat(airflow): add airflow 2.10 to test matrix by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11579
* docs(cypress): Update README.txt by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11588
* fix(trivy): multi-repo, bump trivy version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11590
* fix(trivy): also add alternative java db by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11591
* feat(openapi-v3): generic entities scroll by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11564
* fix: display demo form modal on mobile by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11581
* fix(ingest): ignore irrelevant urns from % change computation by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11583
* feat(ingest/powerbi): fix subTypes and add workspace_type_filter by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11523
* fix(ingest): gracefully handle missing system metadata in client by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11592
* docs(assertions): add example of fetching associated dataset to assertion docs by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/11566
* fix(ingest/sac): handle descriptions which are None correctly by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/11572
* fix(ingest/iceberg): Iceberg table name by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11599
* chore(frontend): force frontend protobuf version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11601
* fix(airflow): add dag AllowDenyPattern config by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/11472
* docs(structured-properties): example to read structured properties fr… by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/11603
* fix(bootstrap): fix early bootstrap mcps by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11605
* fix(spark-lineage-legacy): fix check jar script by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11608
* fix(sdk): platform resource api for non existent resources by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11610
* fix(ingestion/redshift): Fix for Redshift COPY-based lineage by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11552
* fix(ingest/delta-lake): skip file count if require_files is false by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11611
* fix(ingest/superset): parse postgres platform correctly by [@ssidorenko](https://github.com/ssidorenko) in https://github.com/datahub-project/datahub/pull/11540
* feat(openapi-v3): support async and createIfNotExists params on aspect by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11609
* fix(ingest/preset): Add skip_on_failure to root_validator decorator by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11615
* docs(apis): update OpenAPI disclaimer by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11617
* docs: add docs on term suggestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11606
* fix(airflow): fix lint related to dag_run field by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11616
* fix(ingest): drop empty fields by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11613
* fix(ci): ensure py 3.10 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11626
* feat(docs-site) brought back announcement banner by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11618
* fix(search): make graphql query autoCompleteForMultiple to show exact matches first by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/11586
* feat: add contributor pr open comment action by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11487
* docs(ingestion): add architecture diagrams by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11628
* feat(validations): Ingest and metadata schema validators by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11619
* fix(ci): Update contributor-open-pr-comment.yml by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11631
* fix(ci): add runtime limit by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11630
* fix(ci): metadata-io req python by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11632
* feat: add quickstart post by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11623
* feat(ingest/bigquery): Generate platform resource entities for BigQuery labels by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11602
* fix(ingest): add preset deps by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11637
* feat(docker-profiles): allow version override for quickstartDebug by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11643
* feat(ingest/powerbi): link cross workspace dataset into assets by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11560
* docs(custom-plugins): add overview image by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11634
* fix(ci): fix build and test workflow by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11644
* fix(ingest): remove default value from DatahubClientConfig.server by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11570
* chore(ingest): reorganize unit tests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11636
* fix(ingest): run sqllineage in process by default by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11650
* feat(ingest): add offline flag to SQL parser CLI by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11635
* fix(ingest/redshift): reduce sequence limit for LISTAGG by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11621
* fix(ingest/bigquery): Not setting platform instance for bigquery platform resources by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11659
* fix(ingest/dbt): fix bug in CLL pruning by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11614
* fix(ingest/redshift): fix syntax error in temp sql by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11661
* docs(airflow): add known limitations for automatic lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11652
* perf(ingest): streamline CLL generation by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11645
* feat(ingest): ensure sqlite file delete on clean exit by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11612
* fix(sdk): platform resource - support indexed queries when urns are i… by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11660
* fix(ingest/dbt): Prevent lineage cycles when parsing sql of dbt models by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11666
* fix(ingest/dagster): FIx JobSnapshot import is broken by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11672
* feat(ingest/transformer/domain): Add support for on conflict do nothing to dataset domain transformers by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11649
* fix(ingest/looker): Remove bad imports from looker_common by [@feldjay](https://github.com/feldjay) in https://github.com/datahub-project/datahub/pull/11663
* feat(ingest/looker): include project name in model/explore properties by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11664
* feat(ingest/fivetran): protect against high sync volume by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11589
* feat(sdk):platform-resource - complex queries by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11675
* fix(docs): fix businessattributes doc by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/11653
* feat(ingest/fivetran): add safeguards on table/column lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11674
* fix(ui): show DataHub logo for DataHub sources in ingestion souces list by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/11658
* fix(ingest/prefect): Fix prefect mypy errors by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11680
* fix(docs-site): announcement bar responsive behavior by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11681
* fix(misc): misc fixes by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11678
* chore(version): confluent base image by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11689
* feat(ingest): generate urn types for all entities by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11676
* fix(ingest): cache sql is_profiling_enabled method by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11665
* fix(ingest/bigquery): Fix tags urn/name ingestion for BigQuery  by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11691
* doc(bigquery-sync): Add doc for BigQuery sync by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11577
* feat(ingest): use mainline sqlglot by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11693
* fix(ingest): add logging for mcp diff by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11683
* fix(ingestion/glue): manage table names from resource_links from nearest catalog correctly by [@aviv-julienjehannet](https://github.com/aviv-julienjehannet) in https://github.com/datahub-project/datahub/pull/11578
* feat(ingest/fivetran): show connector filter reason by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11695
* feat(ingest/snowflake): support lineage via rename and swap using que… by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11600
* fix(ingest/mongodb): Add Collection Name as Dataset Name in MongoDB by [@pankajmahato-visa](https://github.com/pankajmahato-visa) in https://github.com/datahub-project/datahub/pull/11698
* fix(ui): show structured report context in pre by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11673
* feat(logs): add change event details to log context and improve some logs in MCL/MCP by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11690
* feat(ingest/oracle): retire deprecated cx_oracle library by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11607
* fix(ingest/superset): Don't set schema/db for druid by [@ssidorenko](https://github.com/ssidorenko) in https://github.com/datahub-project/datahub/pull/11682
* fix(ci): remove pip cache by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11702
* feat(ingestion/dagster): Dagster assetless ingestion by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11262
* chore(deps): bump http-proxy-middleware from 2.0.6 to 2.0.7 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11694
* fet(ingest/bigquery): Add support ingesting foreign keys and primary keys for BigQuery tables by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11686
* feat(ingest/fivetran): support overriding destination db by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11701
* feat(ingest/tableau): support ingestion of access roles by [@haeniya](https://github.com/haeniya) in https://github.com/datahub-project/datahub/pull/11157
* fix(logging): minor modifications for logging by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11703
* feat: multi-query lineage for temp upstreams by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11708
* docs(managed/v0.3.6): Add additional release notes for 0.3.6.8 by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11715
* gradle(profiles): create compose base variable by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11716
* fix(log): reduce log volume for ingestion and consumers by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/11714
* misc(gradle): project name parameter by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11717
* refactor(datahub-frontend): upgrade frontend pac4j by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11709
* fix: business attribute empty bubble selection issue by [@kartikey-visa](https://github.com/kartikey-visa) in https://github.com/datahub-project/datahub/pull/11720
* feat(frontend): show browse paths for business attributes related entities - schema fields by [@kartikey-visa](https://github.com/kartikey-visa) in https://github.com/datahub-project/datahub/pull/11585
* feat(bigquery): support config for region qualifiers to fetch jobs by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11728
* feat(docs) steps on handling workspace admin approvals for slack installation by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11726
* feat(docs-site) slack bot scopes by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11727
* feat(docs) steps on how to troubleshoot the slack command not working by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11723
* fix(docs-site) remove free trial notes by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11729
* doc: add missed breaking change note by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11725
* feat(ingest/fivetran): avoid duplicate table lineage entries by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11712
* fix(ingestion/bigquery-gcs-lineage): Add lineage extraction for BigQuery with GCS source by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11442
* feat(ingestion/powerbi): ingest powerbi app by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11629
* feat(ingest/databricks): report unique query count from usage by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11576
* feat(ingest): unpin traitlets by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11731
* feat(ingest/transform): extend ownership transformer to other entities by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11700
* feat(ingest): remove dep on `termcolor` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11733
* fix(ingest/unity): remove redundant check by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11732
* feat(ingest): check ordering in SqlParsingAggregator tests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11735
* feat(docs-website): init solution pages by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11533
* fix(struct-prop): fix unintended struct prop ES mutation by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11751
* fix(openapi-v3): fix mcp alternative validator & test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11744
* fix: add learn more in the homepage by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11752
* docs(dbt-cloud): reference service accounts in docs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11750
* fix(ingestion/powerbi): handle double quotes in M-query by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11743
* fix(ingest/bigquery): add missing path spec deps by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11748
* feat(ingest/datahub): Add way to filter soft deleted entities by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11738
* fix(ingest): pin teradata dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11760
* fix(ingest): reduce asyncio in check_upgrade by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11734
* feat(ingest/powerbi): add timeouts for m-query parsing by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11753
* fix(structuredProperties): fixes underscore behavior in structured property names by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11746
* feat(ui): Support markdown for incident descriptions by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/11759
* feat(ingestion): Add execution request cleanup job by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/11765
* feat(docs-site) polishes and improved responsiveness for the home and solutions pages by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11770
* feat(ingest): unpin looker-sdk dependency by [@chriscc2](https://github.com/chriscc2) in https://github.com/datahub-project/datahub/pull/11755
* feat(forms/cli): add additional filters to the forms CLI (subtypes, platform instances, owners, tags and glossary terms) by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10979
* docs(spark): fix incorrect config option by [@steffengr](https://github.com/steffengr) in https://github.com/datahub-project/datahub/pull/11119
* feat(ingest/powerbi): improve reporting around m-query parser by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11763
* docs(graphql): fix typo in entity.graphql by [@vejeta](https://github.com/vejeta) in https://github.com/datahub-project/datahub/pull/11764
* doc(bigquery): Update setup.md by [@tanguyantoine](https://github.com/tanguyantoine) in https://github.com/datahub-project/datahub/pull/11769
* fix: install servicebell & add condition for markprompt by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11532
* feat(ingest/cli): add undo soft delete command by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11740
* fix(docs-site) improvements to home page by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11783
* Make DatahubGC bootstrap MCP non-optional by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/11785
* fix(ingest/redshift): fix unload lineage in lineage_v2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11620
* fix(ingest/openapi): Fix openapi tests by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11789
* user should be able to pass custom mcp kafka topic by [@ronybony1990](https://github.com/ronybony1990) in https://github.com/datahub-project/datahub/pull/11767
* logging(template-mcp): adding more logging around templating by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11786
* feat(entity-client): batch entity-client ingestProposals by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11787
* feat(ingest/dremio): Dremio Source Ingestion by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11598
* fix(entity-client): switch to caller runs for entity-client by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11791
* bump(cli): Update ingestion-datahub-gc.yaml by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11794
* fix(ingest/powerbi): change default for `use_powerbi_email` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11742
* docs(breaking-changes): datahub-gc by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11808
* fix(doc/bigquery-sync): Update bigquery sync documentation by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11805
* fix(ingest/gc): add limit, add actual loop for iterating over batches by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11809
* fix(ingest/browsePathsV2): Emit Container aspect first, to avoid BrowsePathsV2 generation race condition by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11813
* fix(ingest/fivetran): do not materialise upstream by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11806
* fix(ingest/dremio): update dremio sql query to retrieve queried datasets in sql jobs  by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11801
* fix(ingestion/powerbi): object has no attribute startswith by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11814
* fix(views): fix environment filter for views by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11771
* feat(template-mcps): allow further control for helm by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11816
* fix(timeline): fixes primary key change events by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11819
* fix(ingest): ignore processed query_id from temp upstream by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11798
* feat(ingest): add stateful ingestion support for file source by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11804
* docs(relationship): update relationship docs by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11820
* feat(model): add deprecation aspect to container by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11824
* feat(web-react) improved webpage title generation logic by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11773
* feat(ingest/gx): support gx version 0.18.0 by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11823
* feat(ingestion/powerbi): DatabricksMultiCloud native query support  by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11756
* fix(ci): additional disk clean by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11835
* feat(docs) better oidc setup docs by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11793
* fix(config): add missing package by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11842
* fix(timeline): fixes a renaming corner case by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11843
* fix(ui): show ingested entities in ingestion report when ingestion succeeded with warnings by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/11704
* v0.3.7 release docs by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/11836
* fix(ingest/dbt): handle multiple owners by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11848
* fix(ingest): update GX version having name arg by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11849
* docs(release): helm chart version req 0.3.7 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11850
* refactor(run-id): refactor run id updates by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11834
* fix(ingestion-web) sorting and filtering uses api by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/11844
* docs(automations): Add new doc for Glossary Term Propagation Automation, other docs cleanup by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/11851
* fix(ingest/oracle): fix scheme for sqlalchemy &lt; 2 by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11829
* fix(ingest/partition-executor): Fix deadlock by recomputing ready items by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11853
* fix(ingest/dremio): Dremio software jobs retrieval SQL query fix query error by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11817
* fix(docs): Update v_0_3_7.md by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11861
* fix(doc): fix link to doc, update cli recommendation by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11866
* chore(version): bump netty version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11862
* chore(docs): Minor improvements to transformer docs and java example by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11859
* feat(ingest/cassandra): Add support for Cassandra as a source by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11822
* search(entity-type): make searchable EntityTypeKey by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11868
* docs(search): example tag AND condition by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11870
* Update CSVInfo.tsx by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/11871
* chore(structured-properties): add cli validation for entity types by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11863
* feat(py-sdk): add cli version to ingestion headers by [@githendrik](https://github.com/githendrik) in https://github.com/datahub-project/datahub/pull/11847
* fix(ingest/airflow): Remove seems like not intended force debug mode which caused plugin fail on EMR by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11877
* fix(ingest/airflow): Add log to dag emit by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11880
* feat(ingest/iceberg): Iceberg performance improvement by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11182
* fix(ingest/lookml): replace class variable with instance variable for improved encapsulation by [@raudzis](https://github.com/raudzis) in https://github.com/datahub-project/datahub/pull/11881
* docs(urn): urn encoding by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11884
* fix(ingest/partitionExecutor): Fetch ready items for non-empty batch when _pending is empty by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11885
* fix(ingest): upgrade msal by [@mikeburke24](https://github.com/mikeburke24) in https://github.com/datahub-project/datahub/pull/11883
* refactor(kafka): reconfigure consumers to allow different config by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11869
* Update v_0_3_7.md by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11895
* docs(structured props): fix a typo in structured property docs by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/11887
* feat(mcl-upgrade): implement resume & urn pagination by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11889
* fix(ui) Fix merging siblings schema with mix of v1 & v2 fields by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11837
* fix(ingest): consider sql parsing fallback as failure by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11896
* feat(spark): OpenLineage 1.24.2 upgrade by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11830
* chore(cleanup): remove unused UrnUtils function by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11897
* perf(ingest/redshift): limit copy lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11662
* fix(ingest): add error handling by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11905
* chore(docs): Update restli-overview.md by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11908
* docs: add hudi to integrations by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11901
* Display username while removing the user from the group by [@kanavnarula](https://github.com/kanavnarula) in https://github.com/datahub-project/datahub/pull/11706
* fix(ingest/powerbi): m-query fixes by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11906
* fix(auth)- Fix Redirect url flow in OidcCallback by [@mkamalas](https://github.com/mkamalas) in https://github.com/datahub-project/datahub/pull/11878
* chore(ingest): start using explicit exports by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11899
* chore(ingest): bump black by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11898
* refactor(ingest/snowflake): move oauth config into snowflake dir by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11888
* fix(ingest/bigquery): increase logging in bigquery-queries extractor by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11774
* Update the AWS instructions with EBS CSI and IAM policy instructions by [@alberttwong](https://github.com/alberttwong) in https://github.com/datahub-project/datahub/pull/11872
* fix(ingest/sql): disable patch checker by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11910
* docs(ingest/sac): add additional permission for SAP Analytics Cloud source to docs by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/11903
* chore(ingest): always use urn creation helpers by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11911
* chore: update contributors list by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/11915
* fix(ts): Suppress ts errors on Editor.tsx by [@pinakipb2](https://github.com/pinakipb2) in https://github.com/datahub-project/datahub/pull/11275
* chore(deps): bump cross-spawn from 7.0.3 to 7.0.6 in /smoke-test/tests/cypress by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11890
* chore(deps): bump cross-spawn from 7.0.3 to 7.0.6 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11919
* feat(ingest): handle mssql casing issues in lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11920
* docs(ingest): Raise error on unsupported sqlite version by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11921
* fix(analytics): look at userEditableInfo to populate cells by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/11909
* fix(ingestion/kafka): OAuth callback execution by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11900
* feat(ingest/mssql): include stored procedure lineage by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11912
* fix(ui): use correct docs link for csv enricher by [@bossenti](https://github.com/bossenti) in https://github.com/datahub-project/datahub/pull/11917
* fix(UI): incorrect month showing in MAU by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/11918
* fix(batch-patch): fix patches in batches by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11928
* fix(structuredProps) Add validation that ID and qualifiedName have no… by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11930
* fix(rest.li): fix use of Criterion in rest.li filters by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11932
* fix(validation): improved urn validation logic by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11935
* feat(search): adjust schema field boost by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11933
* fix(ingest/bigquery): ignore include constraints for biglake datasets by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11874
* feat(ingest/kafka): improve error handling of oauth_cb config by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11929
* feat(ingest/oracle): support profile limits for large tables by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11827
* fix: remove ai summit post by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11826
* fix(ui/graphql) Handle groups in institutionalMemory aspect by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11934
* fix(browseDAO): Handle null browse path from ES in BrowseDAO by [@pinakipb2](https://github.com/pinakipb2) in https://github.com/datahub-project/datahub/pull/11875
* fix(airflow): remove trino to presto mapping by [@shepherd44](https://github.com/shepherd44) in https://github.com/datahub-project/datahub/pull/11925
* docs(ingest/bigquery): add partition support capability by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11940
* fix(dataProduct): reduce write fan-out for unset side effect by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11951
* fix(ingest/tableau): handle none database field by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11950
* fix(urn-validator): update urn validation logic by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11952
* feat(ingest): add more logs for kafka polling by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11954
* fix(ingest/sigma): migrate sigma workbooks from container to dashboard by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11939
* fix(ingest/bigquery): Fix performance issue with column profiling ignore by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11807
* docs(cloud): add documentation for Data Product side effect by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/11948
* feat(ingest/mssql): allow filtering by procedure_pattern by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11953
* fix(test): updates a couple tests to disregard list order by [@rtekal](https://github.com/rtekal) in https://github.com/datahub-project/datahub/pull/11840
* fix(dataproduct): optimize data product sideeffect by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11961
* fix(gms/patch): Fix Upstream lineage patching when path contained encoded slash by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11957
* fix(ingest): always send correct data for advanced section by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11960
* feat(schematron): add java capabilities for schema translation by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11963
* fix(shadowJar): fix shadowJar by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11968
* fix(ingest): ensure sentry is initialized with graph tags by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11949
* fix(ingest): more error handling by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11969
* feat(datahub-gc): add truncation days param by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11967
* docs(release): Update v_0_3_7.md by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11937
* fix(ci): fix build-and-test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11974
* refactor(ingest/powerbi): organize code within the module based on responsibilities by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11924
* fix(schematron): fix for jdk8 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11975
* fix(automations docs): Update snowflake-tag-propagation.md to include permissions required for the Automation by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/11977
* chore(bump): bump version of akka for datahub-frontend by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11979
* feat(ingestion): extend feast plugin to ingest tags and owners by [@margaridafernandes-trip](https://github.com/margaridafernandes-trip) in https://github.com/datahub-project/datahub/pull/11784
* fix(validation): additional URN validation adjustments by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11973
* feat(search): Update search_config.yaml by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/11971
* docs(release): update recommended CLI by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11986
* fix(ingest/kafka):add poll for admin client for oauth_cb by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11985
* fix(ingestion/iceberg): Improvements to iceberg source by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/11987
* feat(ingest): standardize sql type mappings by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11982
* feat(ingest): bump typing_extensions dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11965
* feat(ingest): add tests for colon characters in urns by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11976
* feat(ingest/athena): handle partition fetching errors by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11966
* fix: Add option for disabling ownership extraction by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11970
* feat(ingest/dremio): Retrieve default_schema for SQL views by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11832
* fix(docs): fix sample business glossary by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11669
* fix(java-sdk): custom properties patch client by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11984
* fix[ingest/build]: Disable preflight script as it is not needed anymore by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11989
* feat: connector for Neo4j by [@k-bartlett](https://github.com/k-bartlett) in https://github.com/datahub-project/datahub/pull/11526
* fix(ingestion/dremio): Fixed lineage view for dremio EE by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/11990
* fix(ingest/gc): delete invalid dpis by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/11998
* feat(airflow): show dag/task logs in CI by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11981
* chore(ingest): remove deprecated calls to Urn.create_from_string by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11983
* fix(ingest): resolve missing numeric types for profiling by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11991
* fix(docs): Add spark.datahub.stage_metadata_coalescing to recommended configuration for databricks by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11800
* build(coverage): enable code coverage for java and python by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/11992
* chore(docs): Update v_0_3_7.md - v0.3.7.5 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12005
* feat(java-sdk): add utils classes to give equivalence with python uti… by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/12002
* fix(ingest/sagemaker): Gracefully handle missing model group by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12000
* fix(ingest/gc): typo fix, do not delete empty entities by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12011
* fix(ingest/gc): do not cleanup empty job/flow by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12013
* fix(test): fix metadata-io tests by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12006
* fix(ingest/looker): Don't fail on unknown liquid filters by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12014
* feat(docs-website) fix links by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/12019
* fix(ci): fix datahub-client validatePythonEnv by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12023
* test(urn-validation): additional test case by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12001
* feat(hudi): add hudi platform to the list of default platforms by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/11993
* fix(airflow): fix AthenaOperator extraction by [@steffengr](https://github.com/steffengr) in https://github.com/datahub-project/datahub/pull/11857
* feat(tableau): review reporting and debug traces by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12015
* fix(ingest/tableau): make `sites.get_by_id` call optional by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12024
* feat(cli): add platform filter for undo soft delete by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12012
* feat(mcp): add kafka batch processing mode option ([#4449](https://github.com/datahub-project/datahub/pull/4449)) by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12021
* chore: update label for team by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12032
* fix(ui): Adding overflow handling (also goes to oss) by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/12022
* fix(ingest/pulsar): handle missing/invalid schema objects by [@Alice-608](https://github.com/Alice-608) in https://github.com/datahub-project/datahub/pull/11945
* fix(filters) Fix issues with structured properties filters by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/11946
* fix(ingest): avoid bad IPython version by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12035
* feat(ingest/kafka): additional validation for oauth_db signature by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/11996
* fix(ingest/gc): Adding test and more checks to gc source by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12027
* fix(graph-edge): fix graph edge delete exception by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12025
* feat(ingest): add urn validation test files by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12036
* chore(deps): bump cross-spawn from 7.0.3 to 7.0.6 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/11978
* fix(datahub-client): prevent unneeded classes in datahub-client jar by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12037
* fix(entity-service): no-op batches by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12047
* docs(compliance-forms) update guide for creating form via UI by [@maggiehays](https://github.com/maggiehays) in https://github.com/datahub-project/datahub/pull/11936
* feat(snowflake): adding oauth token bypass to snowflake by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/12048
* fix(ingest): avoid shell entities during view lineage generation by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12044
* fix(logs): add actor urn on unauthorised by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12030
* fix(ingest/snowflake): Add handling of Hybrid Table type for Snowflake ingestion by [@siong-tcha](https://github.com/siong-tcha) in https://github.com/datahub-project/datahub/pull/12039
* fix(ingest/powerbi): reduce type cast usage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12004
* refactor(ingest/sql): add _get_view_definition helper method by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12033
* feat(ingest/superset): initial support for superset datasets by [@hwmarkcheng](https://github.com/hwmarkcheng) in https://github.com/datahub-project/datahub/pull/11972
* fix(ingest/sagemaker): Adding option to control retry for any aws source by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/8727
* fix(ingest/gc): Additional dataprocess cleanup fixes by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12049
* feat(tableau): adds more reporting metrics to better understand lineage construction in tableau ingestion by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12008
* feat(ingestion/tableau): hidden asset handling by [@haeniya](https://github.com/haeniya) in https://github.com/datahub-project/datahub/pull/11559
* feat(airflow): drop Airflow &lt; 2.3 support + make plugin v2 the default by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12056
* fix(web) disallow deselecting all degrees on impact analysis view by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/12063
* feat: Add parent container hierarchy label to the container by [@kanavnarula](https://github.com/kanavnarula) in https://github.com/datahub-project/datahub/pull/11705
* fix(py-sdk): DataJobPatchBuilder handling timestamps, output edges by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/12067
* fix(plugin-logging): adjust error logging in plugin registry by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12064
* build(metadata-events): fix shell interpreter mismatch in build script by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12066
* fix(entity-service): handle no-op system-metadata batches by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12055
* build(coverage): rename python coverage reports by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12071
* fix(ingest): replace sqllineage/sqlparse with our SQL parser by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12020
* fix(entity-service): prevent mutation of systemMetdata on prev by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12081
* build(datahub-frontend): enable code-coverage by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12072
* build(ci): codecov integration by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12073
* fix(openapi): adds in previously ignored keep alive value by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/12068
* feat(ui) Add alchemy component library to FE by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12054
* docs(structured properties) add guide by [@maggiehays](https://github.com/maggiehays) in https://github.com/datahub-project/datahub/pull/12070
* feat(ingest): allow max_workers=1 with ASYNC_BATCH rest sink by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12088
* fix(openapi): fix sort criteria parameter by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/12090
* feat(ingest/snowflake): allow option for incremental properties by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12080
* fix(cli): don't use /api in gms url by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12083
* docs(ingest/athena): update recipe with aws key pair example by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12076
* fix(ingest/gc): minor tweak gc source by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12093
* fix(ingest/abs): detect jsonl schema by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11775
* feat(ingest/kafka): Flag for optional schemas ingestion by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12077
* feat(structuredProperties) Add new settings aspect plus graphql changes for structured props by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12052
* fix(ingest/tableau): project_path_pattern use in _is_denied_project by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12010
* feat: Enrich superset ingestion by [@hwmarkcheng](https://github.com/hwmarkcheng) in https://github.com/datahub-project/datahub/pull/11688
* fix(ui) Add backwards compatibility to the UI for old policy filters by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12017
* feat(structuredProps) Add frontend for managing structured props and filtering by them by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12097
* feat(ui) Add full support for structured properties on assets by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12100
* docs(champions): Update directory of DH Champions by [@maggiehays](https://github.com/maggiehays) in https://github.com/datahub-project/datahub/pull/12089
* feat(ingest/snowflake): ingest secure, dynamic, hybrid table metadata by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12094
* feat(spark):OpenLineage 1.25.0 by [@Jorricks](https://github.com/Jorricks) in https://github.com/datahub-project/datahub/pull/12041
* fix(ingest): always resolve platform for browse path v2 by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12045
* fix(ingest/sdk): report recipe correctly by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12101
* feat(cli): add --workers arg in delete command by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12102
* fix(ingest/snowflake): handle dots in snowflake table names by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12105
* fix(ingest/tableau): apply `page_size` regardless of object count by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12026
* docs(ingest/snowflake): update permissions for dynamic tables by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12074
* fix(ingestion/lookml): resolve CLL issue caused by column name casing. by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/11876
* feat(glossary): support multiple ownership types by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/12050
* feat(datahub-client): additionally generates java8 artefacts by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12106
* fix(ui): dereference errors by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12034
* feat(openapi-v3): add minimal timeseries aspect support by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12096
* feat(forms) Clean up form prompts on structured property deletion by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12053
* fix(datahub-client): adds missing archiveAppendix to artifactid when publishing by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12112
* chore(deps): bump nanoid from 3.3.6 to 3.3.8 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/12086
* chore(deps): bump nanoid from 3.3.7 to 3.3.8 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/12114
* feat(structuredProperties): add hide property and show as badge validators by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12099
* fix(ingest/snowflake): further improve dot handling by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12110
* feat(ingest): improve query fingerprinting by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12104
* docs(ingest): add docs on the SQL parser by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12103
* fix(ui): dereference issues by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12109
* fix(datahub-client): avoid parallel execution of publish and publish-java8 by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12120
* fix(ingestion/dremio): Ignore filtered containers in schema allowdeny pattern by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11959
* fix(ingest/kafka-connect): update connection test url, handle api failures by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12082
* fix(ingest/dagster): Fix Dagster build by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12121
* fix(ingest/snowflake): improve warn message by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12125
* fix(dataproduct): creator is assigned as owner by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12127
* fix(mysql): index gap lock deadlock by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12119
* feat(ingest): additional limits on ingestProposalBatch by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12130
* refactor(ingest): cleanup structured properties validation by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12115
* config(docker-profiles): clean-up by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12051
* build(gradle): version change (Gradle and shadow plugin) by [@dejan2609](https://github.com/dejan2609) in https://github.com/datahub-project/datahub/pull/11999
* feat(airflow): add `DatahubRestHook.make_graph` method by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12116
* tests(datahub-client): new tests for the AvroSchemaConverter by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12087
* feat(ingest/snowflake): secure view lineage without owner permissions by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12123
* chore(dep): exclude end of life dependency by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/12007
* chore(version): bump kafka version by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12136
* build(ci): fix vercel setup script by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12143
* feat(ingest/airflow): Add way to disable Airflow plugin without a restart by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12098
* fix(ingestion/tableau): honor the  key projectNameWithin in pagination by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12107
* fix(ingest/datahub): Use server side cursor instead of local one by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12129
* feat(ingestion/tableau): verify role assignment to user in `test_connection`. by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12042
* docs(ingest): fix sink recipe to correct config parameter by [@kousiknandy](https://github.com/kousiknandy) in https://github.com/datahub-project/datahub/pull/12132
* feat(ui) Add finishing touches to the structured props feature by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12111
* feat(ingest/sqlite): Support sqlite &lt; 3.24.0 by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12137
* feat(cli): added cli option for ingestion source by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/11980
* fix(patch): Add Finegrained Lineage patch support for DatajobInputOutput ([#4749](https://github.com/datahub-project/datahub/pull/4749)) by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/12146
* fix(ingest/s3): incorrectly parsing path in s3_uri by [@eagle-25](https://github.com/eagle-25) in https://github.com/datahub-project/datahub/pull/12135
* feat(ingest/datahub): report progress on db ingestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12117
* build(ingest/sqlglot): Bump pin to support snowflake CREATE ... WITH TAG by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12003
* fix(frontend): fix typo datahub-frontend logback.xml by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/12134
* feat(git): add subdir support to GitReference by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12131
* fix(ui) Fix nesting logic in properties tab by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12151
* fix(ingest/snowflake): improve lineage parse failure logging by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12153
* fix(ingest/pulsar): handle Avro schema with missing namespace or name by [@Alice-608](https://github.com/Alice-608) in https://github.com/datahub-project/datahub/pull/12058
* fix(cli/properties): allow structured properties without a graph instance by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12144
* fix(ingest/gc): more logging, error handling, explicit flag by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12124
* fix(ingest/kafka): update dependency, tests by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12159
* feat(api): authorization extended for soft-delete and suspend by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12158
* fix(env) Fix forms hook env var default config by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/12155
* feat(ingest/mlflow): Support configurable base_external_url by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12167
* fix(cli/properties): fix data type validation by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12170
* fix(pgsql): Postgres doesn't support UNION select with FOR UPDATE by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12169
* refactor(ingest/kafka-connect): define interface for new connector impl by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12149
* feat(ingest): add looker meta extractor support in sql parsing by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12062
* feat(ingest/iceberg): Improve iceberg connector by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12163
* feat(python): split out temp wheel builds by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12157
* docs(release): v0.3.7.7 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12091
* fix(docs): Add improvements in examples for PATCH documentation by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/12165
* feat(graphql/ml): Add custom properties to ml entities by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12152
* chore(bump): ingestion-base & actions by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12171
* feat(mssql): platform instance aspect for dataflow and datajob entities by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12180
* fix(tableau): prevents warning in case of site admin creator role by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12175
* fix(tableau): restart server object when reauthenticating by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12182
* fix(dagster): support dagster v1.9.6 by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12189
* fix(graphql): add suspended to corpuserstatus by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/12185
* feat(ingest/snowflake): include external table ddl lineage for queries… by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12179
* fix(gms): Change names of charts in Analytics by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/12192
* fix(ingest/databricks): Fix profiling by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12060
* refactor(ingestion/tableau): mark the `fetch_size` configuration as deprecated. by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12126
* test(ingest/tableau): add test for extract_project_hierarchy scenario by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12079
* docs(structured properties) fix entityTypes in creating structured property by [@nicholas-fwang](https://github.com/nicholas-fwang) in https://github.com/datahub-project/datahub/pull/12187
* chore(bump): bump alpine and dockerize by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12184
* docs update: Update v_0_3_7.md by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12197
* feat(gradle): add quickstartPgDebug option by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12195
* fix(ingest/powerbi): support comments in m-query grammar by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/12177
* feat(ingestion/aws-common): improved instance profile support for ec2, ecs, eks, lambda, beanstalk, app runner and cft roles by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/12139
* feat(ingestion/hive): Add lineage functionality for hive tables from/to file storage by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/11841
* fix(mssql): adds missing containers for dataflow and datajob entities, required for browse paths v2 generation by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12194
* Revert "fix(mssql): adds missing containers for dataflow and datajob entities, required for browse paths v2 generation" by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12201
* chore(bump): bump node version long term support release (build time … by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12199
* fix(ingest): exclude aspect from migration by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12206
* fix(ingest/snowflake): handle empty snowflake column upstreams by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12207
* fix(ui): null dereference by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12193
* fix(ingest): quote asset urns in patch path by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12212
* feat(ingest): add sql parser trace mode by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12210
* fix(ingest): preserve certs when converting emitter to graph by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12211
* fix(ingest/mode): move sql logic to view properties aspect by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12196
* feat: update mlflow-related metadata models by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/12174
* feat(ingest/looker): Do not emit usage for non-ingested dashboards and charts by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/11647
* fix(tableau): retry on InternalServerError 504 by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12213
* fix(ingest/snowflake): always ingest view and external table ddl lineage by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12191
* fix(tableau): fixes wrong argument when reauthenticating by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12216
* fix(ingest/looker): Add flag for Looker metadata extraction by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12205
* fix(ingest/mode): Handle 204 response and invalid json by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12156
* fix(ingest/glue): Add additional checks and logging when specifying catalog_id by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12168
* fix(ingest/gc): misc fixes in gc source by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12226
* Parallelize smoke test by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12225
* chore(bump): spring minor version bump 6.1.14 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12228
* fix(ingest/lookml): emit warnings for resolution failures by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12215
* chore(ingest): remove `enable_logging` helper by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12222
* feat(ingest/dbt): support "Explore" page in dbt cloud by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12223
* feat(ingest/snowflake): support email_as_user_identifier for queries v2 by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12219
* fix(tableau): retry if 502 error code by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12233
* ci: remove qodana by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12227
* chore(tableau): adjust visibility of info message by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12235
* chore(python): test with python 3.11 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/11280
* feat(ingest): add parse_ts_millis helper by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12231
* fix(ingest): use `typing_extensions.Self` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12230
* feat(businessAttribute): generate platform events on association/removal with schemaField by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/12224
* fix(ingest/sql-common): sql_common to use SqlParsingAggregator by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12220
* fix(ingest/gc): reduce logging, remove unnecessary sleeps by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12238
* fix(docs-site) mobile site and artwork polish by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/12237
* feat(data transform): adding dataTransformLogic models by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/12198
* fix(tests): fixing QueryPropertiesMapperTest.java by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/12241
* feat(delete): delete logic non-strict monotonically increasing version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12242
* docs(graphql): create graphql best practices by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12229
* fix(ci): further consolidate NODE_OPTIONS by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12217
* chore: cleanup extra lines by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12248
* fix(docs-site) hero image typo by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/12250
* fix(ingestion/aws_common): update iam role and aws access key tests to complete successfully when executed on EC2 instance by [@acrylJonny](https://github.com/acrylJonny) in https://github.com/datahub-project/datahub/pull/12252
* fix(ingest): json serializable fix by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12246
* fix(ingest/gc): soft deletion loop fix by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12255
* fix(ingest/bigquery): All View generation when queries_v2 is turned off by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12181
* test(ingest/athena): add connector integration tests by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/12256
* chore(ingest): refactor common pytest args by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12240
* fix(sample data): Update timestamps in bootstrap_mce.json to more recent by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/12257
* refactor(sdk/patch): improve patch implementation internals by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12253
* feat(auth): user.props authentication by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12259
* docs(undo_by_filter): Document un-soft-delete commands in delete-metadata.md by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/12251
* fix(tableau): fixes some aspects being emitted multiple times by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12258
* fix(ingestion/redshift): Bumped redshift-connector dependency due to CVE-2024-12745 by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12265
* fix(ingest/gc): logging and stopping fix by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12266
* fix(ingest): consistent fingerprint for sql parsing aggregator by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12239
* docs(queries_v2): set use_queries_v2 to true in snowflake_recipe.yml by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/12269
* feat(ingest/gc): truncate query usage statistics aspect by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12268
* fix(ingest/tableau): retry on auth error for special case by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12264
* fix(ingest/gc): infinite loop query entities by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12274
* fix(ingest/snowflake): use fast query fingerprint for lineage by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/12275
* fix(spark): Finegrained lineage is emitted on the DataJob and not on the emitted Datasets. by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/11956
* docs(tableau): clarify docs around tableau permissions by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12270
* feat(ingest): enable `EnsureAspectSizeProcessor` for all sources by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12262
* fix(ingestion/classifier): temporary measure to avoid deadlocks for classifier by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12261
* feat(ingest/datahub): use stream_results with mysql by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12278
* ci: fix shellcheck warnings, update actions by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12281
* docs(business attribute): clarify support by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12260
* fix(airflow): fix tests with Airflow 2.4 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12279
* fix(ingest): better correctness on the emitter -> graph conversion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12272
* feat(ingest): configurable query generation in combined sources by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12284
* fix(javaEntityClient): correct config parameter by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12287
* ci: upload test coverage to codecov by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12291
* log(elastic/index builder): add est time remaining by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12280
* fix(ingest/glue): don't fail on profile by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12288
* fix(ingest/gc): also query data process instance by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12292
* fix(cli): correct url ending with acryl.io:8080 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12289
* dev: add pre-commit hooks installed by default by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12293
* fix(ingest/file-backed-collections): Properly set _use_sqlite_on_conflict by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12297
* fix(doc): make folder_path_pattern usage more clear by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/12298
* dev: fix pre-commit passing filenames incorrectly by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12304
* feat(sdk): structured properties - add support for listing by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/12283
* chore(tableau): set ingestion stage report and perftimers by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12234
* chore(version): bump jdbc drivers by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12301
* build(coverage): fix carry-forward coverage by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12306
* chore(deps): Migrate EOL vulnerability of javax.mail to jakarta.mail by [@pankajmahato-visa](https://github.com/pankajmahato-visa) in https://github.com/datahub-project/datahub/pull/12282
* chore(alpine): bump alpine images 3.21 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12302
* feat(ingest/datahub): support dropping duplicate schema fields by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12308
* feat(ci): add manual trigger for full build by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12307
* fix(ci): make upload-artifact name unique by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12312
* fix(ingestion/s3): groupby group-splitting issue by [@eagle-25](https://github.com/eagle-25) in https://github.com/datahub-project/datahub/pull/12254
* feat(graphql): adds container aspect for dataflow and datajob entities by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/12236
* docs(ingest/glue): add permissions for glue by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12290
* fix(ingest/gc): add delete limit execution request by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12313
* chore(deps): Migrate CVE-2024-52046 with severity >= 9 (severity = 9.3) vulnerability of org.apache.mina:mina-core:2.2.3 by [@pankajmahato-visa](https://github.com/pankajmahato-visa) in https://github.com/datahub-project/datahub/pull/12305
* fix(ci): fix artifact upload name by [@chakru-r](https://github.com/chakru-r) in https://github.com/datahub-project/datahub/pull/12319
* feat(sdk): support urns in other urn constructors by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12311
* fix(ingest): improve error reporting in `emit_all` by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12309
* docs(ingest): refactor docgen process by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12300
* fix(dockerfile) Remove all references to jetty from the docker file by [@ryota-cloud](https://github.com/ryota-cloud) in https://github.com/datahub-project/datahub/pull/12310
* Add more notifications docs about platform notifications and multiple channels by [@ethan-cartwright](https://github.com/ethan-cartwright) in https://github.com/datahub-project/datahub/pull/10801
* fix(cli/delete): prevent duplicates in delete message by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12323
* feat(ingestion/iceberg): Improve iceberg connector logging by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/12317
* fix(header): prevent clickjack/iframing by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12328
* fix(ingest): tighten Source.create type annotations by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12325
* fix(ci): only upload metadata model on root repo by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12324
* feat(models): update mlflow-related mappers by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/12263
* fix(ingest): support async_flag properly in ingestProposalBatch by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12332
* feat(ingest/snowflake): Support ingesting snowflake tags as structured properties by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/12285
* fix(ingestion) fix snappy inconsistent version in ingestion by [@ryota-cloud](https://github.com/ryota-cloud) in https://github.com/datahub-project/datahub/pull/12321
* Super type dbt redshift by [@kevinkarchacryl](https://github.com/kevinkarchacryl) in https://github.com/datahub-project/datahub/pull/12337
* fix(docker) add new gradle profile for consumer debug purpose by [@ryota-cloud](https://github.com/ryota-cloud) in https://github.com/datahub-project/datahub/pull/12338
* feat(entityVersioning): initial implementation by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/12166
* feat(build): use remote gradle cache by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/12344
* feat(docker-profiles): version mixing & docs by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12342
* docs(async-api): addition to known issues by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/12339
* fix(ingest/gc): fix logging by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/12348
* design: revamp navbar dropdown by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/11864

#### New Contributors
* [@kanavnarula](https://github.com/kanavnarula) made their first contribution in https://github.com/datahub-project/datahub/pull/11272
* [@donovan-acryl](https://github.com/donovan-acryl) made their first contribution in https://github.com/datahub-project/datahub/pull/11393
* [@AColocho](https://github.com/AColocho) made their first contribution in https://github.com/datahub-project/datahub/pull/11284
* [@th0ger](https://github.com/th0ger) made their first contribution in https://github.com/datahub-project/datahub/pull/11475
* [@Bumyu](https://github.com/Bumyu) made their first contribution in https://github.com/datahub-project/datahub/pull/11338
* [@udays-visa](https://github.com/udays-visa) made their first contribution in https://github.com/datahub-project/datahub/pull/11513
* [@kris48k](https://github.com/kris48k) made their first contribution in https://github.com/datahub-project/datahub/pull/11391
* [@udbhav-hbk](https://github.com/udbhav-hbk) made their first contribution in https://github.com/datahub-project/datahub/pull/11524
* [@llance](https://github.com/llance) made their first contribution in https://github.com/datahub-project/datahub/pull/10954
* [@ssidorenko](https://github.com/ssidorenko) made their first contribution in https://github.com/datahub-project/datahub/pull/11540
* [@kartikey-visa](https://github.com/kartikey-visa) made their first contribution in https://github.com/datahub-project/datahub/pull/11720
* [@chriscc2](https://github.com/chriscc2) made their first contribution in https://github.com/datahub-project/datahub/pull/11755
* [@vejeta](https://github.com/vejeta) made their first contribution in https://github.com/datahub-project/datahub/pull/11764
* [@tanguyantoine](https://github.com/tanguyantoine) made their first contribution in https://github.com/datahub-project/datahub/pull/11769
* [@ronybony1990](https://github.com/ronybony1990) made their first contribution in https://github.com/datahub-project/datahub/pull/11767
* [@raudzis](https://github.com/raudzis) made their first contribution in https://github.com/datahub-project/datahub/pull/11881
* [@mikeburke24](https://github.com/mikeburke24) made their first contribution in https://github.com/datahub-project/datahub/pull/11883
* [@alberttwong](https://github.com/alberttwong) made their first contribution in https://github.com/datahub-project/datahub/pull/11872
* [@kevinkarchacryl](https://github.com/kevinkarchacryl) made their first contribution in https://github.com/datahub-project/datahub/pull/11915
* [@shepherd44](https://github.com/shepherd44) made their first contribution in https://github.com/datahub-project/datahub/pull/11925
* [@margaridafernandes-trip](https://github.com/margaridafernandes-trip) made their first contribution in https://github.com/datahub-project/datahub/pull/11784
* [@k-bartlett](https://github.com/k-bartlett) made their first contribution in https://github.com/datahub-project/datahub/pull/11526
* [@chakru-r](https://github.com/chakru-r) made their first contribution in https://github.com/datahub-project/datahub/pull/11992
* [@Alice-608](https://github.com/Alice-608) made their first contribution in https://github.com/datahub-project/datahub/pull/11945
* [@siong-tcha](https://github.com/siong-tcha) made their first contribution in https://github.com/datahub-project/datahub/pull/12039
* [@hwmarkcheng](https://github.com/hwmarkcheng) made their first contribution in https://github.com/datahub-project/datahub/pull/11972
* [@dejan2609](https://github.com/dejan2609) made their first contribution in https://github.com/datahub-project/datahub/pull/11999
* [@kousiknandy](https://github.com/kousiknandy) made their first contribution in https://github.com/datahub-project/datahub/pull/12132
* [@eagle-25](https://github.com/eagle-25) made their first contribution in https://github.com/datahub-project/datahub/pull/12135
* [@ryota-cloud](https://github.com/ryota-cloud) made their first contribution in https://github.com/datahub-project/datahub/pull/12310

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v0.14.1...v0.15.0

## [v0.14.1](https://github.com/datahub-project/datahub/releases/tag/v0.14.1) {#v0-14-1}

Released on 2024-09-17 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.14.1) for v0.14.1 on GitHub.

## [v0.14.0.2](https://github.com/datahub-project/datahub/releases/tag/v0.14.0.2) {#v0-14-0-2}

Released on 2024-08-21 by [@RyanHolstien](https://github.com/RyanHolstien).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.14.0.2) for v0.14.0.2 on GitHub.

## [v0.14.0](https://github.com/datahub-project/datahub/releases/tag/v0.14.0) {#v0-14-0}

Released on 2024-08-13 by [@RyanHolstien](https://github.com/RyanHolstien).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.14.0) for v0.14.0 on GitHub.

## [v0.13.3](https://github.com/datahub-project/datahub/releases/tag/v0.13.3) {#v0-13-3}

Released on 2024-05-23 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.13.3) for v0.13.3 on GitHub.

## [v0.13.2](https://github.com/datahub-project/datahub/releases/tag/v0.13.2) {#v0-13-2}

Released on 2024-04-16 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.13.2) for v0.13.2 on GitHub.

## [v0.13.1](https://github.com/datahub-project/datahub/releases/tag/v0.13.1) {#v0-13-1}

Released on 2024-04-02 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.13.1) for v0.13.1 on GitHub.

## [v0.13.0](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) {#v0-13-0}

Released on 2024-02-29 by [@RyanHolstien](https://github.com/RyanHolstien).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) for v0.13.0 on GitHub.

## [DataHub v0.12.1](https://github.com/datahub-project/datahub/releases/tag/v0.12.1) {#v0-12-1}

Released on 2023-12-08 by [@david-leifker](https://github.com/david-leifker).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.12.1) for DataHub v0.12.1 on GitHub.

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

