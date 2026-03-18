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
| **v0.13.1** | 2024-04-02 |[Release Notes](#v0-13-1), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.1) |
| **v0.13.0** | 2024-02-29 |[Release Notes](#v0-13-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) |
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
| **v0.8.41** | 2022-07-15 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.41) |
| **v0.8.40** | 2022-06-30 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.40) |
| **v0.8.39** | 2022-06-24 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.39) |
| **v0.8.38** | 2022-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.38) |
| **v0.8.37** | 2022-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.37) |
| **v0.8.36** | 2022-06-02 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.36) |


## [v0.13.1](https://github.com/datahub-project/datahub/releases/tag/v0.13.1) {#v0-13-1}

Released on 2024-04-02 by [@david-leifker](https://github.com/david-leifker).

### DataHub Release Notes

#### User Experience
- **Capture and Manage Common Joins between Datasets**: Users can now view and manage common join relationships between datasets, making it easier than ever to capture best practices and bespoke join logic. Watch the walkthrough [here](https://youtu.be/NuLLc88ij-s?si=_0eIKiPLqZVzFfqw)! [8325](https://github.com/datahub-project/datahub/pull/8325)
  - *Head's up: you'll need to enable the `ER_MODEL_RELATIONSHIP_FEATURE_ENABLED` env variable to use this feature!*
- **Enhanced UI Interactions**: Users can now enjoy an improved markdown editor and filter policies by active/inactive statuses, resulting in a more intuitive and manageable interface. [9949](https://github.com/datahub-project/datahub/pull/9949), [9958](https://github.com/datahub-project/datahub/pull/9958)
- **Visual Context for Groups**: You can now include picture links for groups in the UI, adding a richer visual context and enhancing the navigational experience. [9882](https://github.com/datahub-project/datahub/pull/9882)
- **Improved Error Visibility**: The UI now displays error messages related to data size limitations, allowing for better troubleshooting and user experience. [10038](https://github.com/datahub-project/datahub/pull/10038)

#### Developer Experience
- **Enhanced Kafka Compatibility**: Updated client version for Kafka setup ensures better compatibility and functionality for developers. [9962](https://github.com/datahub-project/datahub/pull/9962)
- **Optimized Docker Build**: Docker setups now respect pip mirrors, optimizing the build process especially in restricted network environments. [9963](https://github.com/datahub-project/datahub/pull/9963)
- **Advanced Error Handling**: New error handling for duplicate class names and improved `fspath` lint error management enhance the code reliability and quality. [9960](https://github.com/datahub-project/datahub/pull/9960), [9976](https://github.com/datahub-project/datahub/pull/9976)
- **Latest OpenSearch Image**: Incorporation of OpenSearch image version 2.11.0 aligns with the latest stable releases, boosting performance and security. [9984](https://github.com/datahub-project/datahub/pull/9984)

#### Metadata Ingestion
- **NEW: Dagster Integration**: You can now seamlessly ingest your Dagter Pipelines, Jobs, Ops, and lineage into DataHub. [10071](https://github.com/datahub-project/datahub/pull/10071)
- **Expanded Field Classification Support**: This release introduces support for field-level classification during ingestion for Redshift, BigQuery, DynamoDB, and SQL Sources. [10013](https://github.com/datahub-project/datahub/pull/10013), [10031](https://github.com/datahub-project/datahub/pull/10031)
- **Enhanced Ingestion Capabilities**: DataHub now offers stateful ingestion by default, optimizing routines for REST sinks and improving metadata accuracy across diverse sources like dbt and BigQuery. [9934](https://github.com/datahub-project/datahub/pull/9934), [10158](https://github.com/datahub-project/datahub/pull/10158), [10080](https://github.com/datahub-project/datahub/pull/10080)
- **Better Data Lineage**: This release introduced support for Openlineage in service of the Spark Lineage Beta Plugin; additionally, we now support incremental Column-Level Lineage, improving the accuracy of detecting column-level relationships during ingestion.[9870](https://github.com/datahub-project/datahub/pull/9870), [9967](https://github.com/datahub-project/datahub/pull/9967), [10090](https://github.com/datahub-project/datahub/pull/10090)
- **Schema Clarity**: New descriptions support for JSON schema arrays and a mechanism to escape special characters in BigQuery table descriptions aid in clearer schema validation and ingestion processes. Databricks ingestion now supports Hive Metastore schemas with special characters. [9757](https://github.com/datahub-project/datahub/pull/9757), [9932](https://github.com/datahub-project/datahub/pull/9932), [10049](https://github.com/datahub-project/datahub/pull/10049)

#### Version Upgrades
- Kafka client and OpenSearch image were updated to the latest versions.

#### Breaking Changes
This release introduces default settings for stateful ingestion and updates in handling dbt ingestion. For details on all breaking changes, view the full documentation [here](https://github.com/datahub-project/datahub/blob/master/docs/how/updating-datahub.md).

#### Contributors
MASSIVE shoutout to our contributors!

##### First-Time Contributors
[akarsh991](https://github.com/akarsh991), [alexs-101](https://github.com/alexs-101), [AvaniSiddhapuraAPT](https://github.com/AvaniSiddhapuraAPT), [diegmonti](https://github.com/diegmonti), [dushayntAW](https://github.com/dushayntAW), [filipe-caetano-ovo](https://github.com/filipe-caetano-ovo), [HuanjieGuo](https://github.com/HuanjieGuo), [jayacryl](https://github.com/jayacryl), [k7ragav](https://github.com/k7ragav), [kopax-polyconseil](https://github.com/kopax-polyconseil), [LePuppy](https://github.com/LePuppy), [Nelvin73](https://github.com/Nelvin73), [pinakipb2](https://github.com/pinakipb2), [poorvi767](https://github.com/poorvi767), [rae89](https://github.com/rae89), [trialiya](https://github.com/trialiya), [valeral](https://github.com/valeral).

##### Repeat Contributors
[ANich](https://github.com/ANich), [shubhamjagtap639](https://github.com/shubhamjagtap639), [sgomezvillamor](https://github.com/sgomezvillamor), [siladitya2](https://github.com/siladitya2), [skrydal](https://github.com/skrydal), [sumitappt](https://github.com/sumitappt), [Masterchen09](https://github.com/Masterchen09), [mayurinehate](https://github.com/mayurinehate), [ngamanda](https://github.com/ngamanda), [gaurav2733](https://github.com/gaurav2733), [githendrik](https://github.com/githendrik), [jayasimhankv](https://github.com/jayasimhankv).

##### DataHub Maintainers
[anshbansal](https://github.com/anshbansal), [asikowitz](https://github.com/asikowitz), [chriscollins3456](https://github.com/chriscollins3456), [darnaut](https://github.com/darnaut), [david-leifker](https://github.com/david-leifker), [eboneil](https://github.com/eboneil), [ethan-cartwright](https://github.com/ethan-cartwright), [gabe-lyons](https://github.com/gabe-lyons), [hsheth2](https://github.com/hsheth2), [pedro93](https://github.com/pedro93), [RyanHolstien](https://github.com/RyanHolstien), [treff7es](https://github.com/treff7es), [yoonhyejin](https://github.com/yoonhyejin).

### What's Changed
* bump(kafka-setup): client version bump by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9962
* feat(ingest): throw codegen error on duplicate class names by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9960
* feat(docker): respect pip mirrors with uv by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9963
* Openlineage endpoint and Spark Lineage Beta Plugin by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9870
* fix(ingest/json-schema): adding support descriptions for array by [@AvaniSiddhapuraAPT](https://github.com/AvaniSiddhapuraAPT) in https://github.com/datahub-project/datahub/pull/9757
* fix(ingest/redshift): fix bug in lineage v2 table renames by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9967
* feat(ingest): speed up to_obj() and validate() by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9969
* feat(ingest): fix fspath lint error by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9976
* docs: archive old version before 0.12.0 & fix broken links by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9957
* fix(ui/markdown-editor): arrows change field when editing description… by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9949
* feat(ui/policies): add filter for Active/Inactive/All on policy page by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9958
* feat(ui): add option to add picture link for groups by [@akarsh991](https://github.com/akarsh991) in https://github.com/datahub-project/datahub/pull/9882
* feat(ingest): add Looks subtype + stop reemitting browsePathV2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9978
* fix(ingest/bigquery): escape special characters for table descriptions by [@AvaniSiddhapuraAPT](https://github.com/AvaniSiddhapuraAPT) in https://github.com/datahub-project/datahub/pull/9932
* feat(ui): add loading spin to access management table by [@filipe-caetano-ovo](https://github.com/filipe-caetano-ovo) in https://github.com/datahub-project/datahub/pull/9974
* fix(ingestion/fivetran): Fix fivetran get connector jobs bug by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9975
* feat(ingest/dbt): generate CLL for all node types by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9964
* chore(search): bump OpenSearch image version to 2.11.0 by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9984
* feat(ingest): enable stateful_ingestion by default for DataHub rest sink by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9934
* feat(ingestion/cli): Adding check option to validate allow/deny and path_specs by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9983
* fix(ingest): only import PathSpec when necessary by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9989
* feat(config): add configuration to reprocess UI sourced events by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9988
* feat(pluginRegistry): add configuration to reduce runnable frequency by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9990
* build(react): Fix typescript errors in test files by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9982
* feat(docs): disable last update timestamps by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9987
* feat: add versioned content for 0.12.1 by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9944
* doc: add version 0.13.0 by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9991
* fix: fix mobile view and subtitles on slack/calendar page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9822
* fix(ingest/redshift): fix stl scan lineage for lineage v2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9986
* fix(ingest/delta-lake): support parsing nested types correctly by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/9862
* fix(test): nested domains by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9993
* fix(ci): refactor build-and-test command by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9999
* feat(ingest/snowflake): generate query nodes for snowflake by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9966
* fix(ingest/unity): creating group urn in case of group by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/9951
* fix(ui/left-side-bar): hide data products option in left side bar by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10001
* feat(ingest/redshift): make query generation configurable by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10000
* fix(opensearch): Rollover usage events at a file size rather than time-based manner by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10006
* chore(java): bump java dependency versions by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10009
* ci(react): Update package.json to enable lint check by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/10011
* fix(ui/ingest): trim leading and trailing whitespaces from the text f… by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10012
* fix(policy-backfull): fix policy backfill job by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10016
* feat(opensearch): support for updating ISM policy used for usage events by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10018
* refactor(react): Provide option to skip importing theme in CustomThemeProvider; rearrange toplevel components by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9940
* fix(openapi): fix openapi openlineage endpoint by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10019
* feat(ingest): update sqlglot fork by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10022
* feat(ingest/superset): map awsathena platform name to athena by [@LePuppy](https://github.com/LePuppy) in https://github.com/datahub-project/datahub/pull/10005
* fix(ingest/redshift): patch instead of replace redshift custom properties by [@ethan-cartwright](https://github.com/ethan-cartwright) in https://github.com/datahub-project/datahub/pull/9293
* fix(ingest/slack): tweak docs for slack source by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10007
* fix(ingest): use contextvar for cooperative timeout by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10021
* feat(ingest): improve custom package metadata by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9985
* feat(docs): build website using swc-loader instead of babel by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9977
* feat(ingest): add query formatting to sql aggregator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10025
* feat(ingest): add DataHubGraph.emit_all method by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10002
* feat(ingestion): Support for Server-less Redshift by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/9998
* fix(ingest/teradata): small teradata improvements by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9953
* feat(ingest): add classification for sql sources by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10013
* docs(monitoring): add health check endpoint by [@kopax-polyconseil](https://github.com/kopax-polyconseil) in https://github.com/datahub-project/datahub/pull/10033
* feat(ingest/dbt): capture both raw and compiled code by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10026
* fix(ingest/redshift): Temp table lineage fix by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10008
* feat(ingest): utilities for query logs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10036
* docs: add missing api sample docs by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9869
* feat(gms): add aspect name to siblings hook log by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10044
* feat(ingest): add classification to bigquery, redshift by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10031
* fix(ui/lineage): show data is too large error when limitation exceeds by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10038
* feat(ci): exempt more names from community by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10039
* docs: improve versiondropdown design & set docs main to /features by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9994
* fix(ingest/redshift): tweak lineage v2 queries by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10045
* chore(aws-msk-iam-auth): bump dependency version by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10063
* feat(lineage): add priority to via node by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10034
* docs(acryl-cloud): notes for 0.2.16 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10069
* fix(ingest/unity-catalog): generate sibling and lineage by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/9894
* fix(ingest): only auto-enable stateful ingestion if pipeline name is set by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10075
* feat(ingest/s3): set default spark version by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10057
* feat(ingest): better rest emitter error message by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10073
* docs(sdk): Update API guide with example for Acryl by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10072
* feat(ingest): check for private import path usages by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10059
* feat(ingest): add sql formatter utility by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10064
* feat(ingest): refactor LineageConfig class by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10074
* feat(ingest/dbt): point dbt assertions at dbt nodes by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10055
* feat(dbt): show source and compiled code in the UI by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10028
* feat(ui/ingest): ingestion form for Okta and AzureAD by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9829
* Update domains docs to include nested domains by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9890
* fix(ingestion): Handle Redshift string length limit in Serverless mode by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/10051
* build(deps): bump follow-redirects from 1.15.4 to 1.15.6 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/10060
* build(deps): bump es5-ext from 0.10.62 to 0.10.63 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9927
* fix(lineage): fix array out of bounds error by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10081
* Add owners, tags, glossary terms to dataset yaml loader by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9859
* Add rate limiting to slack source by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10082
* fix(metadata-ingestion)glue connector failure when Optional field Type of PartitionKey is absent for a Table by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/10052
* feat(redshift): adds flag to skip all external tables by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/10040
* feat(models) : Joins (Datasets) schema, resolvers and UI by [@poorvi767](https://github.com/poorvi767) in https://github.com/datahub-project/datahub/pull/8325
* feat(properties) Add upsertStructuredProperties graphql endpoint for assets by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9906
* Clean up logic for dataset.py yaml loader by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10089
* feat(ingest/dbt): add option to skip sources by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10077
* feat(ingest): support incremental column-level lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10090
* feat(ingest/powerbi): add chart subtypes by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10076
* fix(ingest/metabase): Use connect_uri instead of display_uri to query Metabase API by [@diegmonti](https://github.com/diegmonti) in https://github.com/datahub-project/datahub/pull/9996
* feat(tableau): ability to force extraction of table/column level linage from SQL queries by [@alexs-101](https://github.com/alexs-101) in https://github.com/datahub-project/datahub/pull/9838
* feat(ingest/datahub-gc): gc source to cleanup things by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10085
* docs(acryl-cloud): fix year in notes from 2023 to 2024 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10095
* feeat(openapi): add batch endpoint to v2 using requestbody by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10100
* fix(ingest/dbt): fix config validator for skip_sources_in_lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10098
* docs: add gtm tag  by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10083
* docs: add doc for assertions & data contracts by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10029
* test(ingest/mssql): use non-ephemeral mapping port by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10104
* fix(ingestion/unity-catalog): patch owners and properties by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10086
* fix(ingestion/transformer): added new transformer to cleanup suffix/prefix in owner URN by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10067
* fix(ui/user-group): add non existent entity page for user by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10004
* fix(resolver): Allow users to add/remove related terms for children glossary terms by [@pinakipb2](https://github.com/pinakipb2) in https://github.com/datahub-project/datahub/pull/9895
* Increase role member count in listRoles query to 20 from 10 by [@jayasimhankv](https://github.com/jayasimhankv) in https://github.com/datahub-project/datahub/pull/10020
* fix(frontend): exclude plugins/frontend/auth/user.props config does not exist warnings from log by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10043
* fix(ui): show dataset display name in browse paths v2 by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10054
* fix(metrics): get fieldName for GraphQL Mutation queries by [@trialiya](https://github.com/trialiya) in https://github.com/datahub-project/datahub/pull/9972
* feat(UI): disable access management ui when no roles are linked to entity by [@githendrik](https://github.com/githendrik) in https://github.com/datahub-project/datahub/pull/9610
* ci(filters): add graphql code to backend trigger by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10113
* test(urn): add test case by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10112
* fix(ui) Add min width to the usage stats component by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10056
* log(system-update): Update DataHubStartupStep.java by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9971
* fix(usage-stats): usage-stats error handling and filter by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10105
* fix(elasticsearch logging): log how long bulk execution took by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10116
* feat(auth): view authorization by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10066
* fix(searchContext): fix search flag immutability by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10117
* fix(ingest/looker): use `external_base_url` for explore url generation by [@k7ragav](https://github.com/k7ragav) in https://github.com/datahub-project/datahub/pull/10093
* feat(ingest/dagster): Dagster source by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10071
* fix(forms) Fix a couple of small inconsistencies with forms by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9928
* fix: exclude Elasticsearch ignore_throttled warnings from log by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10042
* Update build-and-test.yml by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10127
* fix(mae-consumer): fix aspect retriever injections mae-consumer by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10125
* fix(docs): fix docs build by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10129
* fix(search): respect the search flags term bucket size by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10130
* fix(ingestProposal): fix/handle no-op ingestion by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10126
* fix(ci): simplify python release process by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10133
* feat(lineage): add a parameter to allow limiting the per hop exploration of lineage search by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10062
* feat(ingest/bigquery): Respect dataset and table patterns when ingesting lineage via catalog api by [@ANich](https://github.com/ANich) in https://github.com/datahub-project/datahub/pull/10080
* feat(ingest): emit platform for query entities by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10103
* feat(ingest): loosen pyarrow dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10141
* fix(ingest/dbt): respect `convert_column_urns_to_lowercase` in mapping CLL by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10132
* chore(ingestion-base): update base requirements by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10142
* feat(ingest/dbt): dbt model performance by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9992
* fix(ingest/databricks): support hive metastore schemas with special char by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10049
* feat(ui): sort partition keys to the top of the table for better visibility by [@ngamanda](https://github.com/ngamanda) in https://github.com/datahub-project/datahub/pull/9959
* fix: OBS-729 | Filters: Fix alignment on nested dropdown by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/10140
* feat(ingest/dynamodb): add support for classification by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10138
* feat(incidents) incident resolution note more clearly displayed by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/10151
* fix(entity-client): fix entity client cache and test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10149
* chore(ingest): update doc & log detail by [@HuanjieGuo](https://github.com/HuanjieGuo) in https://github.com/datahub-project/datahub/pull/10139
* feat(ingest): loosen airflow plugin dependencies requirements by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10106
* feat(ingest): fix validators by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10115
* feat(ingest/bigquery): improve debug logs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10101
* fix(graphQL): Ignore soft-deleted assertions in UI calls by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/10148
* fix(openapi): fix system-metadata response by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10155
* docs: update markprompt project key by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10134
* add row type for athena types by [@rae89](https://github.com/rae89) in https://github.com/datahub-project/datahub/pull/10131
* fix(setup): fix postgres setup to create temp table with no data by [@trialiya](https://github.com/trialiya) in https://github.com/datahub-project/datahub/pull/10154
* feat(ingest/looker): update browse paths to align with looker UI by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10147
* feat(ingest/airflow): allow plugin to load on listener exception by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10152
* feat(ingestion/bigquery): BigQuery Owner Label to Datahub Ownership by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10047
* feat(ingest): bump sqlglot dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10144
* docs(website): tweak eyebrow copy by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10143
* docs: upgrade markprompt version by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10159
* fix(openapi): fix index out of bounds for sort order by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10168
* fix(search): fix field name in api by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10170
* build(docker): prefix pr on pr sha tags by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10171
* Revert docker helper changes by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10172
* feat(metadata-jobs): improve consumer logging by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10173
* test(graph): refactor graph test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10175
* fix(ingest/tableau) Fix Tableau lineage ingestion from Clickhouse by [@valeral](https://github.com/valeral) in https://github.com/datahub-project/datahub/pull/10167
* &lt;fix>[oracle ingestion]: get database name when using service by [@Nelvin73](https://github.com/Nelvin73) in https://github.com/datahub-project/datahub/pull/10158
* fix(docker): fix versioning for compose file post release by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10176
* fix(restoreIndices): batchSize vs limit by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10178
* feat(ui): show classification in test connection by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10156
* fix(ingest): add classification dep for dynamodb by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10162
* feat(ingest/dbt): enable model performance and compiled code by default by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10164
* refactor(docker): move to acryldata repo for all images by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9459
* fix(github): fix docker publish by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10186
* feat(lineage): mark nodes as explored by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10180
* feat(ingest/gc): add index truncation logic by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10099
* fix(entity-service): fix findFirst when already present by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10187
* fix(ingestion/salesforce): fixed the issue by escaping the markdown string by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10157

### New Contributors
* [@AvaniSiddhapuraAPT](https://github.com/AvaniSiddhapuraAPT) made their first contribution in https://github.com/datahub-project/datahub/pull/9757
* [@akarsh991](https://github.com/akarsh991) made their first contribution in https://github.com/datahub-project/datahub/pull/9882
* [@filipe-caetano-ovo](https://github.com/filipe-caetano-ovo) made their first contribution in https://github.com/datahub-project/datahub/pull/9974
* [@dushayntAW](https://github.com/dushayntAW) made their first contribution in https://github.com/datahub-project/datahub/pull/9862
* [@LePuppy](https://github.com/LePuppy) made their first contribution in https://github.com/datahub-project/datahub/pull/10005
* [@kopax-polyconseil](https://github.com/kopax-polyconseil) made their first contribution in https://github.com/datahub-project/datahub/pull/10033
* [@poorvi767](https://github.com/poorvi767) made their first contribution in https://github.com/datahub-project/datahub/pull/8325
* [@diegmonti](https://github.com/diegmonti) made their first contribution in https://github.com/datahub-project/datahub/pull/9996
* [@alexs-101](https://github.com/alexs-101) made their first contribution in https://github.com/datahub-project/datahub/pull/9838
* [@pinakipb2](https://github.com/pinakipb2) made their first contribution in https://github.com/datahub-project/datahub/pull/9895
* [@trialiya](https://github.com/trialiya) made their first contribution in https://github.com/datahub-project/datahub/pull/9972
* [@k7ragav](https://github.com/k7ragav) made their first contribution in https://github.com/datahub-project/datahub/pull/10093
* [@jayacryl](https://github.com/jayacryl) made their first contribution in https://github.com/datahub-project/datahub/pull/10151
* [@HuanjieGuo](https://github.com/HuanjieGuo) made their first contribution in https://github.com/datahub-project/datahub/pull/10139
* [@rae89](https://github.com/rae89) made their first contribution in https://github.com/datahub-project/datahub/pull/10131
* [@valeral](https://github.com/valeral) made their first contribution in https://github.com/datahub-project/datahub/pull/10167
* [@Nelvin73](https://github.com/Nelvin73) made their first contribution in https://github.com/datahub-project/datahub/pull/10158

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v0.13.0...v0.13.1

## [v0.13.0](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) {#v0-13-0}

Released on 2024-02-29 by [@RyanHolstien](https://github.com/RyanHolstien).

### DataHub v0.13.0 Release Notes Summary

#### User Experience
- **NEW - Asset Documentation Forms & UI-Editable Properties:** Define specific documentation requirements via a Form, and empower your asset owners to capture their valuable knowledge via UI-Editable Properties. _[Watch the demo here](https://www.youtube.com/live/JsftXZKEvU8?si=Odp6fzdIua1p6lNv&t=1272)!_
- **NEW - DataHub Incidents:** Create, communicate, and data quality and observability incidents when they inevitably arise. _[Watch the demo here!](https://youtu.be/m9NbsUS0z80?si=Ih1j9NZDaW9ZfGrM)_
UI Improvements: Editing secrets, handling forms, and rendering token pages and lineage diagrams have been improved for a smoother user interface experience.
- **UI Improvements**: Editing secrets, handling forms, and rendering token pages and lineage diagrams have been improved for a smoother user interface experience.

#### Developer Experience
- **Security Upgrades**: Core dependencies like shiro-core and FastAPI have been upgraded to fix vulnerabilities, ensuring a safer development environment.
- **GraphQL/OpenAPI Enhancements**: New GraphQL endpoints and better OpenAPI documentation provide more powerful tools for API interaction, making developers' jobs easier.
- **Performance Tuning**: Backend improvements for search operations and ingestion processes make the platform faster and more reliable.

#### Metadata Ingestion
- **Platform Integrations**: Enhanced support for dbt, Metabase, BigQuery, AWS Glue, Oracle, and Redshift allows for more comprehensive metadata capture, making integration with these platforms smoother.
- **Ingestion Framework**: The reliability of ingestion has been improved, with new capabilities like support for tags from Tableau datasources and compatibility with Airflow 2.5.0, facilitating a broader range of data synchronization tasks.
- **Connector Improvements**: Ingestion connectors for external data tools have been streamlined, ensuring easier integration and data synchronization.

#### Other Improvements and Fixes
- Enhanced internal testing frameworks with Cypress and pytest-random-order for ingestion tests.
- Simplified developer workflows with configurable Docker Compose project names in CLI.
- Addressed various ingestion-related bugs for platforms like Feast and Snowflake.
- Enhanced the UI codebase with TypeScript compilation linting and updated styles.
- Streamlined CI processes for pull requests and linting conditions.
- **Version Upgrades**: Upgraded pytest-docker, Pegasus, and SQLglot, among others, to improve stability and performance. Security vulnerabilities addressed by upgrading FastAPI, gitdb, and follow-redirects.

#### Notable Breaking Changes
- Updates to MySQL version for quickstarts and migration to Neo4j 5.x may impact existing setups.
- JDK17 build requirement and Docker Compose > 2.20 needed for building DataHub.
- Python 3.8+ requirement for the `acryl-datahub` CLI.
- Changes in Unity Catalog ingestion source configs and Redshift lineage generation.
- Deprecation of Spark 2.x and associated JDK8 build requirements.

For full details on breaking changes, please visit [DataHub's update guide](https://github.com/datahub-project/datahub/blob/master/docs/how/updating-datahub.md).

#### Acknowledgements
A huge thank you to all our contributors for making this release possible. Your hard work and dedication are greatly appreciated.

##### First-Time Contributors
[7onn](https://github.com/7onn), [Adityamalik123](https://github.com/Adityamalik123), [atjones0011](https://github.com/atjones0011), [BlueHorn07](https://github.com/BlueHorn07), [diegoreico](https://github.com/diegoreico), [dim-ops](https://github.com/dim-ops), [fer-marino](https://github.com/fer-marino), [Gerrit-K](https://github.com/Gerrit-K), [gp1105739](https://github.com/gp1105739), [ilpianista](https://github.com/ilpianista), [ingthorb](https://github.com/ingthorb), [KaYunKIM](https://github.com/KaYunKIM), [Kunal-kankriya](https://github.com/Kunal-kankriya), [muzzacode](https://github.com/muzzacode), [nnnkkk7](https://github.com/nnnkkk7), [pankajmahato-visa](https://github.com/pankajmahato-visa), [rubiojr](https://github.com/rubiojr), [ryaminal](https://github.com/ryaminal), [scalvanese452](https://github.com/scalvanese452), [sleeperdeep](https://github.com/sleeperdeep), [stevenayers](https://github.com/stevenayers).

##### Repeat Contributors
[allizex](https://github.com/allizex), [arunvasudevan](https://github.com/arunvasudevan), [cburroughs](https://github.com/cburroughs), [feldjay](https://github.com/feldjay), [gaurav2733](https://github.com/gaurav2733), [iprentic](https://github.com/iprentic), [KulykDmytro](https://github.com/KulykDmytro), [kushagra-apptware](https://github.com/kushagra-apptware), [mayurinehate](https://github.com/mayurinehate), [nmbryant](https://github.com/nmbryant), [noggi](https://github.com/noggi), [purnimagarg1](https://github.com/purnimagarg1), [rinzool](https://github.com/rinzool), [sgomezvillamor](https://github.com/sgomezvillamor), [shubhamjagtap639](https://github.com/shubhamjagtap639), [siddiquebagwan-gslab](https://github.com/siddiquebagwan-gslab), [siladitya2](https://github.com/siladitya2), [skrydal](https://github.com/skrydal), [sumitappt](https://github.com/sumitappt), [TonyOuyangGit](https://github.com/TonyOuyangGit), [wngus606](https://github.com/wngus606), [yangjiandan](https://github.com/yangjiandan), [Salman-Apptware](https://github.com/Salman-Apptware).

##### DataHub Maintainers
[anshbansal](https://github.com/anshbansal), [asikowitz](https://github.com/asikowitz), [chriscollins3456](https://github.com/chriscollins3456), [darnaut](https://github.com/darnaut), [david-leifker](https://github.com/david-leifker), [eboneil](https://github.com/eboneil), [ethan-cartwright](https://github.com/ethan-cartwright), [gabe-lyons](https://github.com/gabe-lyons), [hsheth2](https://github.com/hsheth2), [jjoyce0510](https://github.com/jjoyce0510), [maggiehays](https://github.com/maggiehays), [pedro93](https://github.com/pedro93), [RyanHolstien](https://github.com/RyanHolstien), [shirshanka](https://github.com/shirshanka), [sid-acryl](https://github.com/sid-acryl), [treff7es](https://github.com/treff7es), [yoonhyejin](https://github.com/yoonhyejin).

#### What's Changed
* fix(ingest/transformer): correct registration by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9418
* docs(ingest/sql-queries): Rearrange sections by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9426
* fix: Adjusting the view of the Column Stats by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9430
* feat(patch): support fine grained lineage patches by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9408
* fix(CVE-2023-6378): update logback classic by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9438
* feat: allow the sidebar size to be draggable by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9401
* fix(json-schema): do not send invalid URLs by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9417
* fix(ingest/profiling) Fixing profile eligibility check by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9446
* fix(ingest): avoid git dependency in dbt by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9447
* feat(ingest): add retries for tableau by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9437
* docs(updating-datahub): update docs for v0.12.1 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9441
* feat: Allow specifying Data Product URN via UI by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9386
* Add button to copy urn of an Ownership Type by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9452
* docs(ingest/tableau): add token to sink config in sample recipe by [@KaYunKIM](https://github.com/KaYunKIM) in https://github.com/datahub-project/datahub/pull/9411
* feat(glossary): add ability to clone glossary term(name and documentation) from term profile menu by [@allizex](https://github.com/allizex) in https://github.com/datahub-project/datahub/pull/9445
* feat(ingestion): Add typeUrn handling to ownership transformers by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/9370
* fix(ingest): reduce GraphQL Logs to warning for circuit breaker by [@arunvasudevan](https://github.com/arunvasudevan) in https://github.com/datahub-project/datahub/pull/9436
* fix: support Apollo caching for settings / Policies by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9442
* refactor | PRD-785 | datahub oss: migrate use of useGetAuthenticatedU… by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9456
* refactor(ui): Minor improvements & refactoring  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9420
* feat(ingest): add ingest `--no-progress` option by [@BlueHorn07](https://github.com/BlueHorn07) in https://github.com/datahub-project/datahub/pull/9300
* fix(powerbi): add access token refresh by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9405
* fix | PRD-463 | Stop trying to ping the track endpoint on login home … by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9462
* feat(ingest/unity): enable hive metastore ingestion by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9416
* feat(ingestion/transformer): create tag if not exist by [@siddiquebagwan-gslab](https://github.com/siddiquebagwan-gslab) in https://github.com/datahub-project/datahub/pull/9076
* fix(ingest): make user_urn and group_urn generation consider user and… by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9026
* feat(ingestion): Add test_connection methods for important sources by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9334
* docs: fix sample command for container logs by [@nnnkkk7](https://github.com/nnnkkk7) in https://github.com/datahub-project/datahub/pull/9427
* fix(ingest): bump source configs json schema version by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9424
* fix(ingest/profiling): Add option to enable external table profiling by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9463
* fix(operations): fix get index sizes integer wrap by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9450
* feat(build): gradle 8, jdk17, neo4j 5 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9458
* feat(ingest/redshift): drop repeated operations by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9440
* feat: Deprecation 'Note' changed to Markdown Renderable by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9396
* feat : markdown support for group description by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9455
* feat(ingest): enable CLL for dbt by default by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9466
* fix(ingest/snowflake) - Fixing snowflake url with default region by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9443
* Fix downstream CI issue by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/9479
* feat(ingest): pydantic v2 compatibility by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9434
* feat(gms): Add support for platform-based browse by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9376
* Searching for users on Users page shows incorrect roles: Issue resolved by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9474
* fix(ingest/redshift: Fixing operation query to not return duplicate operations by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9481
* Fade recipe section to transparent on Ingestion Run Details by [@purnimagarg1](https://github.com/purnimagarg1) in https://github.com/datahub-project/datahub/pull/9404
* Allow message_name field for protobuf ingestion by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9480
* feat(docker-compose): consolidate docker-compose profiles by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9478
* Adds urnBasedPagination option to datahub-upgrade RestoreIndices by [@nmbryant](https://github.com/nmbryant) in https://github.com/datahub-project/datahub/pull/9232
* fix(quickstart): force strings for mysql version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9485
* fix(docker): fix frontend dev docker path by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9488
* fix: Tab doesn't represent the page you are on for non-data asset pages by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9468
* Do not sync demo in downstream repos by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/9493
* fix(ingest): update ingest_stats event with transformer types by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9487
* feat | PRD-874 | Keep the same tab selected when browsing Glossary tr… by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9469
* style | PRD-893 | Tag overflow is missing padding by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9497
* feat(analytics): change MAU chart to be until last month by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9499
* fix(kafka): fix infinite deserialization logging by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9494
* fix(ingest/fivetran): only materialize upstream lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9490
* feat(ingest): handle multiline string coercion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9484
* fix(ingest/databricks): Pinning databricks sdk to not fail on mypy issues by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9500
* feat(ingest): remove librdkafka hacks by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9507
* feat(ingest): rename custom package path from models to metadata by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9502
* Prd 886 edit links by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9498
* feat(ingest): support CLL for redshift materialized views with auto refresh  by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9508
* feat: Input field added for the Custom cron, and issue on search sour… by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9510
* fix(ingest): update dbt type inference by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9512
* feat(ingest/redshift): merge CLL instead of overwriting by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9513
* Add debounce on search on ingestion listing page by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9516
* fix: correct the color of edit links by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9517
* fix(frontend): Add JSON list oidc group extraction logic by [@ethan-cartwright](https://github.com/ethan-cartwright) in https://github.com/datahub-project/datahub/pull/9495
* feat(frontend): align frontend sso code with refactors by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9506
* fix(ingest/glue): glue table partition (Athena v3) profiling parameters retrieval error by [@KulykDmytro](https://github.com/KulykDmytro) in https://github.com/datahub-project/datahub/pull/9521
* fix(ingest/fivetran): handle missing user_id for a connection by [@ryaminal](https://github.com/ryaminal) in https://github.com/datahub-project/datahub/pull/9460
* feat(ui): Allow copying assertion urn from the UI by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9523
* feat(ingest/openapi): support proxies and alternate auth schemes by [@fer-marino](https://github.com/fer-marino) in https://github.com/datahub-project/datahub/pull/9492
* build(ingest/feast): upgrade to latest feast version by [@cburroughs](https://github.com/cburroughs) in https://github.com/datahub-project/datahub/pull/9439
* build: enable gradle caching by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9525
* chore(build): update base-requirements + add script for regeneration by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9524
* add automatic reset password test by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9515
* feat(ingestion/bigquery): Use sqlglot_lineage for usage and add more perf timers by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9247
* fix(ingest/mongodb): support disabling schemaSamplingSize by [@diegoreico](https://github.com/diegoreico) in https://github.com/datahub-project/datahub/pull/9295
* fix(ingest): Fix mongodb ingestion when platform_instance is missing from recipe by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9486
* fix(ingest/snowflake): explicit set schema if public schema is absent by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9526
* fix | PRD-901 | Border is too thick for sidebar by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9528
* Humanise duration shown on ingestion page by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9530
* fix(cli): fix issue with upsert for data product external url by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9534
* fix posts are failing to be created as Admin user by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9533
* while creating secrets via UI validate validate character~ by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9548
* feat(ui): add databricks logo by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9473
* feat(databricks): add hive metastore analyze profiling by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9511
* Fix/PRD-906 make setting manage policy test by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9547
* search user functionality added by [@kushagra-apptware](https://github.com/kushagra-apptware) in https://github.com/datahub-project/datahub/pull/9532
* fix(ci): make test flexible to allow sha-based cli versions by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9551
* feat/PRD-895-Navigation-test by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9545
* docs(acryl cloud): release notes for 0.2.14.1 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9554
* ci(doc): tweak build rule to avoid docker build for docs by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9555
* fix(ingest): improve kafka-connect test stability by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9519
* fix(ingest/looker): add user stats to report by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9505
* perf(lineage): Rewrite lineage query for Elastic graph store by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9552
* feat(ingest): improve config loading helpers by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9477
* feat(patch): add dashboardInfo and chartInfo support for patch by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9536
* feat(docker): docker compose profiles updates by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9514
* feat(ui): switch to vite and vitest by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9451
* fix(graphql): BatchGetEntitiesResolver respects order by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9557
* ci(label): datahub-community-champion label based off usernames by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9558
* feat(quickstart): add actions to debug quickstart by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9559
* refactor: PRD-900 | Review glossary related cypress tests and extract… by [@sumitappt](https://github.com/sumitappt) in https://github.com/datahub-project/datahub/pull/9549
* fix(compose-profiles): hostname kafka-broker -> broker by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9563
* build(spark-smoke): dump container logs for spark smoke test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9565
* fix(ingest/looker): limit dashboard object lifetime to thread by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9564
* feat(ingest): track thread count in ingestion report by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9566
* build(deps): bump [@adobe](https://github.com/adobe)/css-tools from 4.3.1 to 4.3.2 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9561
* Lower count for CSV download query from 500 to 200 to alleviate timeouts by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9568
* fix(ci): ignore binaries from test results upload by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9560
* fix(ci): fix label logic by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9571
* bump(docker-compose): migrate to v2 docker compose cli by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9569
* feat(ingestion/transformer): Add dataset dataproduct transformer by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9491
* Fix - Removed AWS S3 Platform by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9581
* feat(entity-registry): entity registry plugins by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9538
* Fix/glossary test by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9584
* fix(owner): last modified on adding owner by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9553
* fix(frontend): restrict redirect uri domain by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9592
* docs(slack): add note about private Slack channels by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9589
* fix(ingest/snowflake): set platform instance for foreign keys by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9577
* fix(ingest/redshift): include table type in custom properties by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9576
* fix(graphql): fix npe in access mapper by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9593
* fix(ingest/bigquery): support google-cloud-bigquery 3.15.0 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9595
* Fix - updated verification steps by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9598
* fix(ingestion/starburst-trino): Fix validation errors in TrinoJoinedAccessEvent by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9580
* feat(ingest/snowflake): improve accuracy of computed sample-based pro… by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9600
* feat(ingestion/fivetran): Add fivetran bigquery destination support by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9531
* feat: Auto-focus on entity profile action modals by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9444
* fix(ingest): support `database_pattern` in clickhouse and clickhouse-usage by [@Gerrit-K](https://github.com/Gerrit-K) in https://github.com/datahub-project/datahub/pull/9482
* feat(ingest/tableau): include platform_instance in browse v1 path by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9607
* Fix/nested domain test by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9609
* feat(ingest/tableau): add retries on OSErrors by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9596
* feat(spring): update spring to version 6 and spring boot to version 3 by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9567
* feat(ingest): key-partitioning for rest emitter by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9613
* fix(ingest/nifi): make s3 dataset urn consistent with s3 source by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9599
* Fix - Changed popup text visibility and removed unnecessary code by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9611
* feat(ingest/looker): add retries to API calls by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9606
* fix(graphql): Add jsonProps to SchemaField type by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9622
* feat(ingest/looker): add backpressure-aware executor by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9615
* fix(ingest/mongodb): Fix downsampling the collection schema output undetermined by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9612
* Unskip "type" filter tests by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9630
* feat(ingest/dbt): speed up dbt CLL by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9617
* Added Homepage Post Steps by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9620
* feat(graphql): generate ToString method by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9634
* fix(internal schema): changes to make internal schema registry more compatible with other schema registries by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9636
* fix(autocomplete): Filter default entity types based on those present in types map  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9625
* feat: inital champions page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9429
* docs: add intro video to the docs main page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9597
* feat(search): add support for empty aggregations through searchable annotation by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9624
* docs: add events link by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9638
* feat(ingest/dbt-cloud): Add way to customize dbt cloud access endpoint by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9633
* build(ingest/feast): upgrade to latest feast version (0.35.x) by [@cburroughs](https://github.com/cburroughs) in https://github.com/datahub-project/datahub/pull/9627
* feat(classifier): Add support for excluding list of exact column names by [@ethan-cartwright](https://github.com/ethan-cartwright) in https://github.com/datahub-project/datahub/pull/9472
* feat(cli): add threads to sink report by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9642
* fix(extension) Fixes routing for the embed pages for chrome extension by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9648
* feat: add an endpoint to edit posts by [@muzzacode](https://github.com/muzzacode) in https://github.com/datahub-project/datahub/pull/9629
* feat(monitoring): add metrics for kafka consumers by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9643
* feat(web): update aws logos by [@rinzool](https://github.com/rinzool) in https://github.com/datahub-project/datahub/pull/9660
* fix(docs-website): update copy around the video on index by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9661
* fix(protobuf): fix reseved field error in fields in nested messages by [@wngus606](https://github.com/wngus606) in https://github.com/datahub-project/datahub/pull/9318
* feat(ingest/databricks): ingest hive metastore by default, more docs by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9601
* fix(docker):The datahub-frontend service failed to start when executing dev.sh [#7616](https://github.com/datahub-project/datahub/pull/7616) by [@yangjiandan](https://github.com/yangjiandan) in https://github.com/datahub-project/datahub/pull/7618
* feat(openapi): Implement getIndexSizes function from rest.li in openapi by [@iprentic](https://github.com/iprentic) in https://github.com/datahub-project/datahub/pull/8730
* feat(ingest/sql-parsing): Support file backed dict in SqlParsingBuilder for lineage by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9654
* feat(posts): add edit support for posts by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9666
* feat(roles): Add support for roles in groups in GMS by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9659
* fix(frontend): Add fallback for image load error on Avatar by [@ingthorb](https://github.com/ingthorb) in https://github.com/datahub-project/datahub/pull/9501
* fix(user-removal):  resolve user removal list update issue by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9671
* feat(ui) Add standardized GQL error handling function to FE by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9470
* feat(kafka): add health indicator for kafka by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9662
* perf(entity-service): batch exists calls by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9663
* feat(ingest/airflow): support airflow 2.8 dataset listeners by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9664
* fix(docs): Correct Kafka Connect sink documentation by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9672
* docs(observability): add databricks as supported source by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9619
* feat(build): conditional ci by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9673
* build(deps-dev): bump vite from 4.5.0 to 4.5.2 in /datahub-web-react by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9676
* feat(superset): add some custom properties for dashboards by [@rinzool](https://github.com/rinzool) in https://github.com/datahub-project/datahub/pull/9670
* fix(superset): handle comma in dataset table name by [@rinzool](https://github.com/rinzool) in https://github.com/datahub-project/datahub/pull/9656
* feat(openapi): allow swagger 3.x by [@dim-ops](https://github.com/dim-ops) in https://github.com/datahub-project/datahub/pull/9646
* feat(ingest/superset): add domains and platform_instance support by [@rinzool](https://github.com/rinzool) in https://github.com/datahub-project/datahub/pull/9647
* fix(workflow): workflow tweaks by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9678
* feat(ingest/databricks): view upstream lineage for hive metastore by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9657
* feat(ingest/dynamodb): add domain arg by [@dim-ops](https://github.com/dim-ops) in https://github.com/datahub-project/datahub/pull/9658
* feat(backend): structured properties and forms by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9626
* feat(ingest/lookml): support complex lookml manifests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9688
* docs: Add Case Studies and DataHub Basics to Resources tab by [@maggiehays](https://github.com/maggiehays) in https://github.com/datahub-project/datahub/pull/9687
* fix(ingestion/mssql): use platform_instance for mssql dataflow/datajob by [@sleeperdeep](https://github.com/sleeperdeep) in https://github.com/datahub-project/datahub/pull/9527
* Added to Verify  Edit Post Steps by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9683
* feat(ingest): improve sql tests + dbt reporting by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9649
* feat(ingest/sql-parser): test redshift temp tables by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9653
* feat(policies): Allow policies to be applied to resources based on tags by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9684
* feat(role-assignment): add role assignment dropdown in the UI for groups by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9689
* feat(ingest/looker): add browse paths for charts by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9639
* fix: Fix error message when attempting to delete home page posts with… by [@Salman-Apptware](https://github.com/Salman-Apptware) in https://github.com/datahub-project/datahub/pull/9667
* feat(ui) Support auto-render aspects on remaining entity types by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9696
* fix(consumer): wait for internal schema registry by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9699
* feat(build): support jdk8 spark lineage by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9697
* feat(ingest): add ODBC library and tools to base image by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9701
* feat (resolver): Add new endpoint for editing secrets by [@muzzacode](https://github.com/muzzacode) in https://github.com/datahub-project/datahub/pull/9665
* feat(ingest): handling for const in json schema by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9694
* refactor(ingest): simplify adding aspects to MCEs in transformers by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9686
* docs(openapi): improve description fields by [@dim-ops](https://github.com/dim-ops) in https://github.com/datahub-project/datahub/pull/9690
* feat(docs): Add documentation on Incident Change Event by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9709
* feat(ingest/dbt): support aws config without region by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9650
* fix(test): improve cypress tests by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9711
* feat(ingest/tableau): map trino_jdbc platform type by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9708
* fix(oidc settings): effective JWS algorithm setting by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9712
* feat(ingest/metabase): Use new sql parser; reduce error reporting levels by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9714
* fix(ingestion/bigquery): Table-view-snapshot Lineage Bug fix by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9579
* feat(ui) Add structured properties support in the UI by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9695
* docs(): Updating docs for assertions to correct databricks assertions support by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9713
* test(spark-lineage): minor tweaks by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9717
* feat(search): support filtering on count type searchable fields for equality by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9700
* feat(ui): Supporting rendering custom assertion descriptions by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9722
* infra(ui): Add a react context provider allowing sub-components to update theme conf by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9674
* fix(ingestion/metabase): Fetch Dashboards through Collections  by [@7onn](https://github.com/7onn) in https://github.com/datahub-project/datahub/pull/9631
* fix(ingest/glue): Profiling breaks for non-partitioned tables due to absent `Table.PartitionKeys` by [@KulykDmytro](https://github.com/KulykDmytro) in https://github.com/datahub-project/datahub/pull/9591
* fix(search): fix filters for hasX and numValues fields by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9729
* fix(ingest/airflow): fix plugin support for airflow 2.5.0 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9719
* fix(cli): fix example data contract yaml + update airflow codecov by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9707
* fix(ingest/metabase): add missing sql parser dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9725
* feat(glossary-term-dropdown): include parent term groups  in dropdown by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9715
* fix(ingest/s3): Not sorting schema fields to keep original order by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9349
* fix(ingest/test): Fixing breaking change in moto 5.0 library by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9736
* build(graphql): simplify gradle graphql codegen task by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9734
* feat(edit-secret): frontend support to edit secrets by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9737
* chore(cli): drop support for python 3.7 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9731
* docs: Add slack survey page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9590
* feat(platform): add support for via nodes by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/9733
* feat(ingestion/tableau) Ingest tags from datasource by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/9730
* feat(ingest/okta): option to only ingest users from filtered groups by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9738
* feat(cli): add sibling helper CLI command by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9744
* chore(gms): allow adjusting the log level for gms debug log file by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9743
* build(ingestion-smoke): fix smoke dockerfile by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9724
* feat(cli): option to init via username password, add lint for smoke-test by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9675
* feat(forms) Update form model to include searchable on actor assignment by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9747
* feat(ingestion/dbt): multiple node owner separated by comma by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/9740
* fix(mceConsumer): prevent health endpoint authentication failure by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9748
* fix(ingest/transformer): generate ownership aspect from handle_end_of_stream by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/9720
* fix(aspects): fix default aspect generation for non-restli locations by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9746
* chore(compose): mysql compose healthcheck by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9754
* chore(gradle): datahub-frontend docker dependency avoid yarnInstall by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9758
* fix(search): fix default entities for aggregation filters by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9761
* feat(ingestion/redshift): collapse lineage to permanent table by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/9704
* fix(ingest): upgrade pytest-docker by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9765
* fix(patch): patch builder import TagUrn by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9764
* feat(forms) Add support for metadata forms on entities in the UI by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9718
* chore(ingest/feast): drop redundant typeguard constraint by [@cburroughs](https://github.com/cburroughs) in https://github.com/datahub-project/datahub/pull/9770
* feat(ingestion/feast): loosen feast dependency by [@cburroughs](https://github.com/cburroughs) in https://github.com/datahub-project/datahub/pull/9769
* feat(ci): check for packages, change location of lint by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9759
* feat(tag-filter):  Add tag as filer in policy creation page by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9756
* feat(ingest/metabase): Allow to configure a different url for links by [@ilpianista](https://github.com/ilpianista) in https://github.com/datahub-project/datahub/pull/9727
* docs(elastricsearch): add description fiels by [@dim-ops](https://github.com/dim-ops) in https://github.com/datahub-project/datahub/pull/9693
* fix(ingest/snowflake): stop pinning transitive spacy dependency by [@cburroughs](https://github.com/cburroughs) in https://github.com/datahub-project/datahub/pull/9768
* feat(cli): Add support for custom ownership types to dataproduct CLI by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/9762
* docs: update champion bio by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9773
* fix(ingest/fivetran): Fixing issue when connector user is empty by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9774
* feat(ingest/glossary): support pydantic v2 in business-glossary source by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9763
* fix(datahub-flow-diagram): add missing image for onboarding tour by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9783
* Update aws.md by [@scalvanese452](https://github.com/scalvanese452) in https://github.com/datahub-project/datahub/pull/9726
* fix(gms/search):Fix missing mapping of DOUBLE searchable type by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/9651
* chore(lint): apply spotless by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9789
* docs(observe): add upsert assertion monitor graphql examples by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9766
* fix(docs): fix the subtitle on the slack page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9781
* feat(airflow) Override datajob external_url by [@gp1105739](https://github.com/gp1105739) in https://github.com/datahub-project/datahub/pull/9681
* fix(browsev2): align browse and aggregate queries by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9790
* misc: datahub-upgrade improvements, aspect key & default aspects fixes by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9796
* chore(pegasus): upgrade pegasus, remove gradle 8 hacks for pegasus plugin by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9798
* feat(graphql): get raw aspects for assertions, allow aspectNames filter by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/9792
* feat(ingest/slack): source to get user info from slack by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9776
* Added mutiple tests scenarios by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9750
* feat(token): helper to debug owner of raw token by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9793
* fix(forms) Update styles of submit/confirm button and fix num input bug by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9797
* feat(structured-props) Extend structured props support to other entity types by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9780
* feat(recommendations): Correct searchable entities for top platform by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9800
* feat(ingest/dbt): speed up test result only ingestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9791
* feat(access-token-list): admin being able to view all org access tokens by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9803
* feat(graphql): add configuration for limiting graphql query complexity by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9802
* feat(docs): embed luma calendar widget by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/9784
* docs: fix links to metadata modeling by [@rubiojr](https://github.com/rubiojr) in https://github.com/datahub-project/datahub/pull/9685
* feat(ingest): sql parsing aggregator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9786
* feat(ingest/glossary): handle ownership type in business glossary connector by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/9805
* test(ingest): use pytest-random-order for unit tests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9753
* feat(cli): make docker compose project name configurable by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9808
* feat(ingest/oracle): support changing data dictionary (ALL_ or DBA_) by [@sleeperdeep](https://github.com/sleeperdeep) in https://github.com/datahub-project/datahub/pull/8873
* feat(quickstart): remove `container_name` from compose files by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9809
* fix(cli): fix quickstart command with pydantic v2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9806
* docs: update docs referencing jdk8 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9807
* feat(openapi): allow Bearer token by [@dim-ops](https://github.com/dim-ops) in https://github.com/datahub-project/datahub/pull/9669
* Upgrade shiro-core to 1.13 by [@gp1105739](https://github.com/gp1105739) in https://github.com/datahub-project/datahub/pull/9818
* fix(mysql-setup): specify charset and collation when creating table by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/9817
* feat(build): upgrade fastapi and gitdb due to vulnerablities by [@gp1105739](https://github.com/gp1105739) in https://github.com/datahub-project/datahub/pull/9819
* fix(ingest/profiling): ignore limit/offset when counting table row count in profiling by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9635
* build(deps): bump follow-redirects from 1.15.2 to 1.15.4 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/9603
* fix(forms) Set form prompts default not required by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9820
* refactor(graphql): consolidate cache for stats by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9826
* feat(forms) Extend forms support to other entity types by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9801
* doc(policies): consistent descriptions for root user policies by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9823
* doc(acryl cloud): release notes for 0.2.15.1 by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9837
* fix(forms) Prevent schema field prompts from being required by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9831
* fix(ui/token): token page failing to render by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9827
* fix(ui/lineage): Do not crash on query entity by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9836
* feat(): Adding supports for data incidents for datasets, dashboards, charts, data jobs, data flows by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/9710
* feat(ingest): reporting logging tweaks by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9835
* feat(operations): add explain endpoint for search by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9832
* fix(search): fix inequality filters for count fields by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9858
* feat(ingest): clean up reporting methods by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9848
* feat(graphql): Miscellaneous query additions by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9855
* refactor(ui): Update eslint and rearrange imports by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9854
* feat(models,ui): Support query nodes in lineage by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9850
* feat(ui): Add and update platform logos by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9849
* feat(ingest/dynamoDB): flatten struct fields by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9852
* fix(ingest/looker): update for Looker query API breaking change by [@feldjay](https://github.com/feldjay) in https://github.com/datahub-project/datahub/pull/9865
* chore(graphql): bump graphql engine version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9864
* fix(ingest/redash): Limit size of RedashSourceReport by [@atjones0011](https://github.com/atjones0011) in https://github.com/datahub-project/datahub/pull/9873
* feat(forms) Add batchRemoveForm graphql endpoint by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/9840
* fix(lineage): logging reduction and fixes by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9878
* feat(ingest): add escape hatch methods to SqlParsingAggregator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9860
* fix(ingest): better logging line attribution by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9876
* fix(ingest): bump sqlglot + add some debug info to tests by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9867
* docs(ingest): document remote for ingest deploy by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/9897
* build(workflow): test enable workflow for docs change by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9901
* feat(ingest/mongodb): improve sorting when downsampling collection schema by [@TonyOuyangGit](https://github.com/TonyOuyangGit) in https://github.com/datahub-project/datahub/pull/9856
* feat(ingest/snowflake): speed up snowflake usage query by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9899
* feat(structured-properties): soft delete by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9812
* feat(ingest): add timeout to sqlglot parser by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9868
* feat(models): Add subtypes aspect to dataFlow by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9866
* fix(cli): add-sibling preserve existing siblings by [@stevenayers](https://github.com/stevenayers) in https://github.com/datahub-project/datahub/pull/9907
* feat(ingest/redshift): redshift lineage v2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9904
* build(frontend): Add tsc to lint by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/9911
* fix(posts): add padding to post link card by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9883
* feat(ingestion/trino): Add sibling support in ingestion by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9853
* PRD-1069 | Changed secret name by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9917
* feat(policies): Make policies searchable by privilege, type, status or editable fields by [@pedro93](https://github.com/pedro93) in https://github.com/datahub-project/datahub/pull/9877
* feat(ci): exempt more names from being marked as community by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9918
* feat(ingest/qlik): Qlik cloud connector integration by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/9682
* feat(ingest): use `uv` for python package installs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9885
* feat(ingest/tableau): add non-embedded custom sql to project container by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9875
* fix(ingest/patch): Adding proper json patch path quoting by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9872
* feat(token-status-filter): add filter for expired and all tokens by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/9930
* feat(ingest/slack): add option to ingest slack channels by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9884
* feat(ingest/csv-enricher): add support for ownership type urn by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9935
* feat(patch): refactor cll patch by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9922
* fix(pr): make prs only pull changes from pr branch instead of head merge by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9937
* feat(ingest): loosen sentry requirements by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9936
* fix(react): include flow diagram in docs build by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9785
* fix(ingest/mysql): Adding support for bit type by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/9950
* feat(ingest/patch): add helper for auto-quoting by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9938
* feat(ingest): Support for JSONL in s3 source with max_rows support by [@Adityamalik123](https://github.com/Adityamalik123) in https://github.com/datahub-project/datahub/pull/9921
* feat(ingest): fix bugs in SqlParsingAggregator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9926
* fix(ui/schema): error handling add by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9952
* PRD-1067 | added owner in gen_datahub_groups and condition for maximu… by [@Kunal-kankriya](https://github.com/Kunal-kankriya) in https://github.com/datahub-project/datahub/pull/9888
* feat(ci): skip smoke-test lint if there are no changes by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9945
* feat(search): search access controls by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9892
* feat(ingest/sql-parser): add alias for mariadb by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9956
* docs(ingest/lookml): update known discrepancy list by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/9941
* chore(vulnerability): Bumped up versions for vulnerability fix by [@pankajmahato-visa](https://github.com/pankajmahato-visa) in https://github.com/datahub-project/datahub/pull/9929
* Revert "chore(vulnerability): Bumped up versions for vulnerability fi… by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/9961

#### New Contributors
* [@KaYunKIM](https://github.com/KaYunKIM) made their first contribution in https://github.com/datahub-project/datahub/pull/9411
* [@BlueHorn07](https://github.com/BlueHorn07) made their first contribution in https://github.com/datahub-project/datahub/pull/9300
* [@nnnkkk7](https://github.com/nnnkkk7) made their first contribution in https://github.com/datahub-project/datahub/pull/9427
* [@ryaminal](https://github.com/ryaminal) made their first contribution in https://github.com/datahub-project/datahub/pull/9460
* [@fer-marino](https://github.com/fer-marino) made their first contribution in https://github.com/datahub-project/datahub/pull/9492
* [@diegoreico](https://github.com/diegoreico) made their first contribution in https://github.com/datahub-project/datahub/pull/9295
* [@Kunal-kankriya](https://github.com/Kunal-kankriya) made their first contribution in https://github.com/datahub-project/datahub/pull/9547
* [@Gerrit-K](https://github.com/Gerrit-K) made their first contribution in https://github.com/datahub-project/datahub/pull/9482
* [@muzzacode](https://github.com/muzzacode) made their first contribution in https://github.com/datahub-project/datahub/pull/9629
* [@ingthorb](https://github.com/ingthorb) made their first contribution in https://github.com/datahub-project/datahub/pull/9501
* [@dim-ops](https://github.com/dim-ops) made their first contribution in https://github.com/datahub-project/datahub/pull/9646
* [@sleeperdeep](https://github.com/sleeperdeep) made their first contribution in https://github.com/datahub-project/datahub/pull/9527
* [@7onn](https://github.com/7onn) made their first contribution in https://github.com/datahub-project/datahub/pull/9631
* [@sid-acryl](https://github.com/sid-acryl) made their first contribution in https://github.com/datahub-project/datahub/pull/9740
* [@ilpianista](https://github.com/ilpianista) made their first contribution in https://github.com/datahub-project/datahub/pull/9727
* [@scalvanese452](https://github.com/scalvanese452) made their first contribution in https://github.com/datahub-project/datahub/pull/9726
* [@gp1105739](https://github.com/gp1105739) made their first contribution in https://github.com/datahub-project/datahub/pull/9681
* [@rubiojr](https://github.com/rubiojr) made their first contribution in https://github.com/datahub-project/datahub/pull/9685
* [@atjones0011](https://github.com/atjones0011) made their first contribution in https://github.com/datahub-project/datahub/pull/9873
* [@stevenayers](https://github.com/stevenayers) made their first contribution in https://github.com/datahub-project/datahub/pull/9907
* [@Adityamalik123](https://github.com/Adityamalik123) made their first contribution in https://github.com/datahub-project/datahub/pull/9921
* [@pankajmahato-visa](https://github.com/pankajmahato-visa) made their first contribution in https://github.com/datahub-project/datahub/pull/9929

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v0.12.1...v0.13.0

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

