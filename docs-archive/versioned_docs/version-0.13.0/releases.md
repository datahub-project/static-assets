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
| **v0.13.0** | 2024-02-29 |[Release Notes](#v0-13-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) |
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


## [v0.13.0](https://github.com/datahub-project/datahub/releases/tag/v0.13.0) {#v0-13-0}

Released on 2024-02-29 by [@RyanHolstien](https://github.com/RyanHolstien).

### Breaking Changes

- Updating MySQL version for quickstarts to 8.2, may cause quickstart issues for existing instances.
- Neo4j 5.x, may require migration from 4.x
- Build requires JDK17 (Runtime Java 11)
- Build requires Docker Compose > 2.20
- [#9731](https://github.com/datahub-project/datahub/pull/9731) - The `acryl-datahub` CLI now requires Python 3.8+
- [#9601](https://github.com/datahub-project/datahub/pull/9601) - The Unity Catalog(UC) ingestion source config `include_metastore` is now disabled by default. This change will affect the urns of all entities in the workspace.&lt;br/>
  Entity Hierarchy with `include_metastore: true` (Old)

  ```
  - UC Metastore
    - Catalog
      - Schema
        - Table
  ```

  Entity Hierarchy with `include_metastore: false` (New)

  ```
  - Catalog
    - Schema
      - Table
  ```

  We recommend using `platform_instance` for differentiating across metastores.

  If stateful ingestion is enabled, running ingestion with latest cli version will perform all required cleanup. Otherwise, we recommend soft deleting all databricks data via the DataHub CLI:
  `datahub delete --platform databricks --soft` and then reingesting with latest cli version.

- [#9601](https://github.com/datahub-project/datahub/pull/9601) - The Unity Catalog(UC) ingestion source config `include_hive_metastore` is now enabled by default. This requires config `warehouse_id` to be set. You can disable `include_hive_metastore` by setting it to `False` to avoid ingesting legacy hive metastore catalog in Databricks.
- [#9904](https://github.com/datahub-project/datahub/pull/9904) - The default Redshift `table_lineage_mode` is now MIXED, instead of `STL_SCAN_BASED`. Improved lineage generation is also available by enabling `use_lineaege_v2`. This v2 implementation will become the default in a future release.

### Deprecations
Spark 2.x (including previous JDK8 build requirements)

### What's Changed
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

### New Contributors
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

