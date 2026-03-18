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
| **v0.13.3** | 2024-05-23 |[Release Notes](#v0-13-3), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.13.3) |
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
| **v0.8.41** | 2022-07-15 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.41) |
| **v0.8.40** | 2022-06-30 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.40) |
| **v0.8.39** | 2022-06-24 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.39) |
| **v0.8.38** | 2022-06-09 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.8.38) |


## [v0.13.3](https://github.com/datahub-project/datahub/releases/tag/v0.13.3) {#v0-13-3}

Released on 2024-05-23 by [@david-leifker](https://github.com/david-leifker).

### DataHub Release Notes

#### User Experience
- **NEW: Business Attributes**: Business Attributes are used to standardize and manage data elements across multiple domains, projects, and applications. By linking dataset attributes to Business Attributes, organizations ensure uniformity and ease of updates, as changes made to a Business Attribute are automatically propagated across all linked datasets. [#9863](https://github.com/datahub-project/datahub/pull/9863)
- **Improved UI for Dataset Properties**: Added collapse functionality for long dataset properties, making it easier to navigate and view relevant information. [[#10203](https://github.com/datahub-project/datahub/pull/10203)](https://github.com/datahub-project/datahub/pull/10203)
- **Pagination for Ingestion Tasks Listing**: Added pagination to the tasks listing page, making it easier to manage and navigate through tasks. [[#10293](https://github.com/datahub-project/datahub/pull/10293)](https://github.com/datahub-project/datahub/pull/10293)
- **Rich Text Support for Form Descriptions**: Added support for rich text in form descriptions, enhancing the user experience. [[#104](https://github.com/datahub-project/datahub/pull/104)](https://github.com/datahub-project/datahub/pull/10425)[2](https://suno.com/song/15dc3d51-4ed6-4489-a447-39897ee8174a)[5](https://github.com/datahub-project/datahub/pull/10425)
- **New Analytics Charts**: Added charts in the Analytics tab to identify Top Users and New Users. [#10344](https://github.com/datahub-project/datahub/pull/10344) 
- Enhanced search functionality with customizable autocomplete configuration. [[#10426](https://github.com/datahub-project/datahub/pull/10426)](https://github.com/datahub-project/datahub/pull/10426)

#### Developer Experience
- **Unified CI Workflow Updates**: Improved CI build with unified workflow updates and disk space cleanup, making the build process more efficient. [[#10353](https://github.com/datahub-project/datahub/pull/10353)](https://github.com/datahub-project/datahub/pull/10353)
- **Improved Logging for GraphQL Requests**: Enhanced logging for GraphQL requests, providing better insights and debugging capabilities. [[#10404](https://github.com/datahub-project/datahub/pull/10404)](https://github.com/datahub-project/datahub/pull/10404)
- **Enhanced Documentation for Lineage Feature Guide**: Updated documentation for the lineage feature guide, making it easier to understand and implement. [[#10401](https://github.com/datahub-project/datahub/pull/10401)](https://github.com/datahub-project/datahub/pull/10401)
- **Improved Documentation for SchemaField.label**: Updated documentation for SchemaField.label, providing clearer guidance for developers. [[#10251](https://github.com/datahub-project/datahub/pull/10251)](https://github.com/datahub-project/datahub/pull/10251)
- **Enhanced CI with Docker Image Publishing**: Added Docker image publishing capabilities to the CI workflow, streamlining the deployment process. [[#10193](https://github.com/datahub-project/datahub/pull/10193)](https://github.com/datahub-project/datahub/pull/10193)
- **Redesigned Docs Site Feedback Button**: Improved the design of the feedback button in the documentation, making it more user-friendly. [[#10182](https://github.com/datahub-project/datahub/pull/10182)](https://github.com/datahub-project/datahub/pull/10182)

#### Metadata Ingestion

- Improved Data Profiling by early filtering of tables, correctly computing sample row counts, and combining unique count queries per table. [#10378](https://github.com/datahub-project/datahub/pull/10378), [#10319](https://github.com/datahub-project/datahub/pull/10319), [#10322](https://github.com/datahub-project/datahub/pull/10322)
- **Airflow**: Introduced support for `BigQueryInsertJobOperator`. [#10452](https://github.com/datahub-project/datahub/pull/10452)
- **BigQuery**: Added support for Table Clones and incremental column-level lineage.
- **Snowflake**: Improved reporting for usage aggregation and handled lineage errors; Improved ingestion performance with system sampling on very large tables. [#10279](https://github.com/datahub-project/datahub/pull/10279), [#10430](https://github.com/datahub-project/datahub/pull/10430)
- **Glue**: Introduced support for delta schemas. [[#10299](https://github.com/datahub-project/datahub/pull/10299)](https://github.com/datahub-project/datahub/pull/10299)
- **Redshift**: Improved usage extraction by filtering out system queries. [#10247](https://github.com/datahub-project/datahub/pull/10247) 
- **Mode**: Enhanced ingestion for Mode by adding dashboards into containers, improving data visualization and management. [[#10563](https://github.com/datahub-project/datahub/pull/10563)](https://github.com/datahub-project/datahub/pull/10563)
- **PowerBI**: Added support to automatically extract table lineage between PowerBI and Databricks. [[#10416](https://github.com/datahub-project/datahub/pull/10416)](https://github.com/datahub-project/datahub/pull/10416)
- **dbt**: Improved dbt ingestion by handling complex SQL and enhancing documentation, providing better data management and insights. [[#10323](https://github.com/datahub-project/datahub/pull/10323)](https://github.com/datahub-project/datahub/pull/10323)
- **NiFi**: Enhanced ingestion for NiFi with process group as browse path and incremental lineage, improving data organization and tracking. [[#10202](https://github.com/datahub-project/datahub/pull/10202)](https://github.com/datahub-project/datahub/pull/10202)
- Incubating **Sigma** and **CockroachDB** sources. [#10037](https://github.com/datahub-project/datahub/pull/10037), [#10226](https://github.com/datahub-project/datahub/pull/10226) 

#### Breaking Changes
- **DynamoDB Connector**: `aws_region` is now a required configuration. The connector will no longer loop through all AWS regions; instead, it will only use the region passed into the recipe configuration. [[#10419](https://github.com/datahub-project/datahub/pull/10419)](https://github.com/datahub-project/datahub/pull/10419)
- **Custom Validators and Mutators**: Dropped a previously required constructor. [[#10389](https://github.com/datahub-project/datahub/pull/10389)](https://github.com/datahub-project/datahub/pull/10389)
- **FabricType RVW**: Added as a new FabricType. No rollbacks allowed once metadata with this fabric type is added without manual cleanups in databases. [[#10472](https://github.com/datahub-project/datahub/pull/10472)](https://github.com/datahub-project/datahub/pull/10472)

For full details on breaking changes, please refer to the [updating DataHub documentation](https://github.com/datahub-project/datahub/blob/master/docs/how/updating-datahub.md).

#### Contributors
A big thank you to all our contributors for this release!

##### First-Time Contributors
[@bouaouda-achraf](https://github.com/bouaouda-achraf), [@camilogutierrez](https://github.com/camilogutierrez), [@dotan-mor](https://github.com/dotan-mor), [@egemenberk](https://github.com/egemenberk), [@erikkvale](https://github.com/erikkvale), [@guyr-ziprecruiter](https://github.com/guyr-ziprecruiter), [@ishtartec](https://github.com/ishtartec), [@jonasHanhan](https://github.com/jonasHanhan), [@mrjefflewis](https://github.com/mrjefflewis), [@noggi](https://github.com/noggi), [@olgapenedo](https://github.com/olgapenedo), [@paguos](https://github.com/paguos), [@richenc](https://github.com/richenc), [@Rosmirose](https://github.com/Rosmirose), [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware), [@timothyjin](https://github.com/timothyjin)

##### Repeat Contributors
[@ajoymajumdar](https://github.com/ajoymajumdar), [@deepgarg-visa](https://github.com/deepgarg-visa), [@dushayntAW](https://github.com/dushayntAW), [@filipe-caetano-ovo](https://github.com/filipe-caetano-ovo), [@gaurav2733](https://github.com/gaurav2733), [@kevin1chun](https://github.com/kevin1chun), [@ksrinath](https://github.com/ksrinath), [@Masterchen09](https://github.com/Masterchen09), [@mayurinehate](https://github.com/mayurinehate), [@ms32035](https://github.com/ms32035), [@Nelvin73](https://github.com/Nelvin73), [@rtekal](https://github.com/rtekal), [@sgomezvillamor](https://github.com/sgomezvillamor), [@shubhamjagtap639](https://github.com/shubhamjagtap639), [@siladitya2](https://github.com/siladitya2), [@skrydal](https://github.com/skrydal)

##### DataHub Maintainers
[@anshbansal](https://github.com/anshbansal), [@asikowitz](https://github.com/asikowitz), [@chriscollins3456](https://github.com/chriscollins3456), [@darnaut](https://github.com/darnaut), [@david-leifker](https://github.com/david-leifker), [@eboneil](https://github.com/eboneil), [@gabe-lyons](https://github.com/gabe-lyons), [@hsheth2](https://github.com/hsheth2), [@jayacryl](https://github.com/jayacryl), [@jjoyce0510](https://github.com/jjoyce0510), [@RyanHolstien](https://github.com/RyanHolstien), [@shirshanka](https://github.com/shirshanka) , [@sid-acryl](https://github.com/sid-acryl), [@treff7es](https://github.com/treff7es), [@yoonhyejin](https://github.com/yoonhyejin)

Thank you all for your hard work and contributions!

#### What's Changed
* fix(ingest/bigquery): Supporting lineage extraction in case the select query result's target table is set on job by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10191
* fix(retention): fix time-based retention by [@trialiya](https://github.com/trialiya) in https://github.com/datahub-project/datahub/pull/10118
* feat(lineage): give via and paths in entity lineage response by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10192
* fix(ingestion/datahub): implemented the filter to ignore/include URN for ingestion by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10174
* fix(ingestion/glue): fix to ingest the comment for partition key as description by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10189
* feat(ingest/looker): cleanup usage generation code by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10153
* fix(dev): fix env file overrides for profiles by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10194
* fix(ingestion/hive): ignore sampling for tagged column/table by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10096
* fix(ui/property): add collapse for long dataset properties by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10203
* saas release v0.3.1 release notes by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10205
* fix(ingest/databricks): pin pandas for databricks ingestion by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10204
* Fixed issue where the custom defined aspects were missing from the API specification. by [@ajoymajumdar](https://github.com/ajoymajumdar) in https://github.com/datahub-project/datahub/pull/10208
* feat(ingestion/transformer): Handle overlapping while mapping in extract ownership from tags transformer by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10201
* fix(build): avoid nested gradle commands by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10198
* feat(ingest/great_expectations): support in-memory (Pandas) data assets by [@bouaouda-achraf](https://github.com/bouaouda-achraf) in https://github.com/datahub-project/datahub/pull/9811
* ci(workflow): publish docker from pr with label by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10193
* bump(version): bump classgraph version, add early package filter by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10207
* fix(ingestion/mongodb): MongoDB source unable to parse datetimes with years > 9999   by [@jonasHanhan](https://github.com/jonasHanhan) in https://github.com/datahub-project/datahub/pull/10110
* fix(graphql-core): DomainEntitiesResolver does not support values FacetFilterInput parameter by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/10188
* fix(graphql-core):Auto completion/suggestion of Domains are not working  by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/10150
* chore(usage-stats): measure time for getting buckets and aggregations by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10220
* test(search): introduce retry for search test by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10206
* feat(ingest/bigquery): fix support for incremental column lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10222
* fix(ingest/dbt): better dbt timestamp parsing by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10223
* feat(ingest/sql): normalize bigquery partitioned tables when parsing by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10224
* docs: fix feedback button design by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10182
* docs: add discourse to community tab by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10181
* docs: edit the text and destination for sign up link by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10183
* fix(ingestion/datahub): moved urn_pattern config to source config by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10215
* fix(ingestion/airflow-plugin): ingesting the tags along with the data by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10216
* fix(ingest): suppress all column-level parsing errors by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10211
* fix(ci): unified workflow login logic by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10235
* fix(lineage): fix lighting cache dataJob platform by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10233
* feat(vianode): v3 of cll via datajob update by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10221
* chore(build): bump actions versions by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10240
* fix(ingest): avoid requiring sqlalchemy for dynamodb classification by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10213
* docs(cli/init): make datahub init docs more clear by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10245
* feat(ingest/redshift): filter out system queries from usage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10247
* feat(gql): support operationName by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10210
* fix(frontend): fix frontend script used in release checklist by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10243
* docs(init): Update entrypoints.py to be more clear about acryl init by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10248
* fix(airflow): disable OL regardless of plugin status by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10250
* fix(ingestion/salesforce): added additional check for description by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10239
* feat(api): Add description parameter to editable dataset change entity event by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10237
* fix(ingest/bigquery): fix lineage if multiple sql expression passed in and destination table set by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10212
* feat(ingest/nifi): ingest process group as browse path v2, incremental lineage by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10202
* fix publish-datahub-jars workflow by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10244
* fix(ingest/unity): Fix bug around unity notebook ingestion by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/10253
* feat(ingest/cockroachdb): add cockroachdb ingestion by [@dotan-mor](https://github.com/dotan-mor) in https://github.com/datahub-project/datahub/pull/10226
* feat(ingestion/bigquery): support patterns for label -> tag capture by [@olgapenedo](https://github.com/olgapenedo) in https://github.com/datahub-project/datahub/pull/10146
* feat(ingest/fivetran): use emails in owner user urns by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10229
* feat(cli): Make yaml loaders compatible with pydantic v2 by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10257
* fix(ingest): support pydantic v2 with properties subcommand by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10256
* feat(ingestion): Add `-e` flag to `uv` command in ingestion Dockerfiles by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/10114
* fix(quickstart): remove unneeded init.sql by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10266
* fix(ingestion/airflow-plugin): replace deprecated calls by [@ms32035](https://github.com/ms32035) in https://github.com/datahub-project/datahub/pull/10238
* build(deps): bump webpack-dev-middleware from 5.3.3 to 5.3.4 in /docs-website by [@dependabot](https://github.com/dependabot) in https://github.com/datahub-project/datahub/pull/10109
* fix(metadata-io):Recently viewed, Recently Edited and Recently Searched section is missing in datahub home page by [@siladitya2](https://github.com/siladitya2) in https://github.com/datahub-project/datahub/pull/10234
* Update datahub-executor docs by [@noggi](https://github.com/noggi) in https://github.com/datahub-project/datahub/pull/10263
* feat(access): Improve external role retrieval by [@filipe-caetano-ovo](https://github.com/filipe-caetano-ovo) in https://github.com/datahub-project/datahub/pull/10160
* fix(openapi): fix structured properties mapping by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10260
* fix(authorization): fix restricted entity privmitives by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10265
* fix(ingest/mongodb): schema_metadata referenced before assignment by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10169
* feat(ui/folder-structure-sort): sort folder structure alphabetically by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10268
* feat(ui/ingestion): add pagination on ingestion executions by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10269
* feat(access): Experimental policy debugger by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/9833
* feat(docs) Update updating-datahub.md for GA4 analytics change by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10196
* fix(docs): update docs for SchemaField.label by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10251
* feat(ingest): show custom model info by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10259
* fix(ingest/bigquery): Adding way to change api's batch size on schema init by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10255
* feat(ingest/mode): Mode improvements: by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10273
* fix(ingestion/powerbi): patch column lineage for powerbi report by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10270
* fix(ingestion/lite): An index with the name aspect_idxalready exists … by [@jonasHanhan](https://github.com/jonasHanhan) in https://github.com/datahub-project/datahub/pull/10267
* feat(ingest/looker): browse path followups by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10217
* fix: revert signup page by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10282
* feat: add posts to quickstart sample data by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10276
* fix(ingestion/transformer): tranformer to replace the externalUrl in dataset properties by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10281
* fix(ingestion/csv): add to support multiple ownership type for the sa… by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10287
* docs: update welcome acryl doc by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10280
* feat(ui/backend/openapi/docs) : Add support for Business Attributes by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/9863
* feat(ingest/sigma): Sigma connector integration by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10037
* feat(graph-retriever): implement graph retriever by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10241
* fix(ingestion/scheduler): add extraArgs support for Ingestion Scheduler (e.g. for extra pip packages) by [@Nelvin73](https://github.com/Nelvin73) in https://github.com/datahub-project/datahub/pull/10195
* fix(spring): refactor spring configuration by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10290
* fix(ingest): improve performance of get_allowed_list in AllowDenyPattern when dealing with large lists by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10219
* fix(oidc settings): use correct path for preferredJwsAlgorithm by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10302
* chore(ingest/presto-on-hive): Renaming presto-on-hive to hive-metastore source by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10278
* fix(ingest): disallow src.* imports, fix powerbi/sigma by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10292
* Cc  fix broken cll impact analysis by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10303
* docs: add content describing diff between datahub and acryl datahub by [@shirshanka](https://github.com/shirshanka) in https://github.com/datahub-project/datahub/pull/10301
* docs: versions bump for 0.13.1 by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10285
* doc(gms/scim): SCIM API user guide by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10311
* chore(docker): bump kafka docker base image by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10313
* fix(ui) Show edited field descriptions in schema table by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10314
* chore(pyiceburg): set minimum version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10318
* fix(ingest/tableau): handle very large filter queries by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10295
* fix(ingest/databricks): handle and report config parse failure, updat… by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10261
* feat(ingest/airflow): support disabling iolet materialization by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10305
* feat(ingest/sigma): fix stateful ingestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10321
* fix(ingest/profiling): compute sample row count correctly by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10319
* fix(ingest/transformers): Use set to store tags in AddDatasetTags by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/10317
* feat(views): apply views to homepage entity counts & recommendations by [@ksrinath](https://github.com/ksrinath) in https://github.com/datahub-project/datahub/pull/10283
* fix(ingest): make gms url configuration resilient in rest emitter by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10316
* feat(ingest/profiling): allow unique count queries to be combined by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10322
* fix(ingest/kafka): clarify meta-mapping docs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10320
* feat(ingest): materialize terms produced by ingestion by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10249
* openapi-v3 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/9550
* chore(kafka-setup): bump kafka version by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10329
* fix: make next as default version & create redirection by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10309
* feat(ui/tasks): add pagination on tasks listing page by [@gaurav2733](https://github.com/gaurav2733) in https://github.com/datahub-project/datahub/pull/10293
* feat(ingest): mark acryl cloud package first-party for logging by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10334
* feat(ingest/classify): add pip dependency by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10335
* feat(ingest/metabase): add ability to exclude other users collections by [@paguos](https://github.com/paguos) in https://github.com/datahub-project/datahub/pull/10330
* chore(metadata) Addressing vulnerabilities by [@rtekal](https://github.com/rtekal) in https://github.com/datahub-project/datahub/pull/10296
* fix(ingest/bigquery): set default `max_overflow` to -1 by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10342
* fix(auth-impl): handle empty entities in field resolver providers by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10341
* feat(ingest): bump acryl-sqlglot dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10343
* fix(ingestion/transformer): updated transformer to avoid duplicating … by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10348
* feat(schema-registry): exclude schema reg onboot check from schema re… by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10349
* fix(ingest/starburst): parse create_time datetime format by [@ishtartec](https://github.com/ishtartec) in https://github.com/datahub-project/datahub/pull/10345
* test(ingestion/sigma): Add integration test cases by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10356
* fix(ingestion/salesforce): escape markdown char for multiline description by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10351
* fix(mae): fix mae standalone platform consumer by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10352
* fix(ingestion/qlik): Unable to ingest more than ten spaces by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10228
* docker(ingestion-base): set certificate location for python by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10364
* build(ci): unified workflow update 1 by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10353
* feat(ui): Adding new analytics charts for new users, top users past month by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/10344
* feat(ingestion/bigquery): support for table clones by [@camilogutierrez](https://github.com/camilogutierrez) in https://github.com/datahub-project/datahub/pull/10274
* build(ingest): update base requirements file by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10368
* feat(ingest/mssql): improve docs on using odbc by [@mrjefflewis](https://github.com/mrjefflewis) in https://github.com/datahub-project/datahub/pull/10370
* feat(ingest/dbt): handle complex dbt sql + improve docs by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10323
* feat:(entity-registry): add ability to search for float and double by [@Rosmirose](https://github.com/Rosmirose) in https://github.com/datahub-project/datahub/pull/10324
* fix(hazelcast): fix cache value classloading by [@RyanHolstien](https://github.com/RyanHolstien) in https://github.com/datahub-project/datahub/pull/10373
* docs(business-attribute):add info businessAttributeEntityEnable flag by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/10379
* fix(ingest/bigquery): map date types correctly by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10383
* feat(ingest/dbt): use columns from manifest as a fallback by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10374
* fix(ingest/profiling): Filter tables early based on profile pattern filter by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10378
* feat(ingest/dbt): support a `datahub` section in meta mappings by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10371
* docs(observe): update docs for remote executor, databricks by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10393
* fix(graphql) Fix entity type filter clash with legacy filters by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10362
* fix(backend): do not lower-case dataset key parts i.e. data platform … by [@ksrinath](https://github.com/ksrinath) in https://github.com/datahub-project/datahub/pull/10385
* docs(search): document default search operator by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10397
* fix: add redirection for the past versions by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10395
* feat: add keywords for SEO by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10358
* docs: add slack utm component in docs by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10214
* perf(ingestion/fivetran): Connector performance optimization by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10346
* feat(graphql): Improve logging of GraphQL requests by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10404
* fix(ingest): map bigquery nested types properly by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10409
* fix(ingestion/looker): fix lineage for dimension group column by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10382
* feat(metabase): add stateful ingestion by [@paguos](https://github.com/paguos) in https://github.com/datahub-project/datahub/pull/10360
* docs(apis): Update datahub-apis.md to add link to search example by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10412
* feat(graphql): log query name if operation name is not provided by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10420
* DynamoDB IAM auth by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10419
* fix(ingest/bigquery): Fixing double sanitization of urns by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10386
* fix(ingestion/transformer): new transformer to clean user URN for DatasetUsageStatistics aspect by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10398
* fix(ingestion/airflow-plugin): emit the operation aspect by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10402
* feat(search): allow overriding case-sensitivity to zero by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10422
* fix(ci): add labeled to list of pr types for ci by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10363
* docs(ingest): update datahub sink doc to include an acryl example by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10411
* feat(ui) Support rich text for form descriptions by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10425
* feat(auth): improve authentication flow logging by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10428
* feat(upgrade): common base for mcl upgrades by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10429
* feat(search): autocomplete custom configuration by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10426
* fix(upgrade): fix upgrade npe by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10436
* fix(docker): use distinct empty env files by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10438
* feat(ingest/snowflake): use system sampling on very large tables by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10430
* fix(ingest/bigquery): remove last modified timestamp fallback by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10431
* feat(cli): cache sql parsing intermediates by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10399
* docs: fix blog link by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10441
* fix(ingestion/tableau): Fix tableau custom sql lineage gap by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10359
* fix(changeEvents): add description-parameter to the change-event of a schemaField-description by [@ksrinath](https://github.com/ksrinath) in https://github.com/datahub-project/datahub/pull/10414
* feat(ci): add linting for cypress tests by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10424
* feat(spark/openlineage): Openlineage 1.13.1 upgrade by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10433
* feat(ingestion): Copy urns from previous checkpoint state on ingestion failure by [@shubhamjagtap639](https://github.com/shubhamjagtap639) in https://github.com/datahub-project/datahub/pull/10347
* fix(ingest/snowflake): add more reporting for usage aggregation, handle lineage errors by [@mayurinehate](https://github.com/mayurinehate) in https://github.com/datahub-project/datahub/pull/10279
* feat(docker): Enable and expose Jetty statistics by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10448
* fix(ingest/mode): Improve query lineage by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10284
* feat(ingest): add actorUrn for ingestion through UI by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10447
* fix(ingestion/airflow-plugin): warning log for non-materialized iolets by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10421
* fix(ingestion/salesforce): handle the label with none value scenario by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10446
* fix(ingestion): Explicitly set requirement on snowflake-connector-python to be newer or equal to 3.4.0 by [@skrydal](https://github.com/skrydal) in https://github.com/datahub-project/datahub/pull/10445
* perf(ingest): speed up urn encode happy path by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10451
* feat(ingest/tableau): Fetch Upstreams From Columns by [@egemenberk](https://github.com/egemenberk) in https://github.com/datahub-project/datahub/pull/9874
* docs(ingest): fix typos and clarify ingestion recipe docs by [@guyr-ziprecruiter](https://github.com/guyr-ziprecruiter) in https://github.com/datahub-project/datahub/pull/10405
* fix(patch): update json patch library by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10449
* fix(metadata-service): add PE processor to component scan by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10462
* fix(ingestion/airflow-plugin): bumping up the openlineage-airflow version by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10457
* fix(ingest/tableau): catch exception during sign out by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/10459
* fix(ingest/dbt): failures due to API change by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10467
* fix(ingestion/kafka-connect): fixed the issue with ingestion requiring multiple substitutes by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10443
* feat(ingest/cli): add some URNs per aspect for easier debugging by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10468
* fix(ingest/dbt): Adding fix if dbt data type is null by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10471
* fix(docs): adjust new requirements for DynamoDB ingestion by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10470
* feat(ingest/redshift): add timers for lineage v2 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10460
* feat(fabricType): add fabric type RVW by [@eboneil](https://github.com/eboneil) in https://github.com/datahub-project/datahub/pull/10472
* feat(structured-properties): immutable flag by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10461
* fix(docker): mount newly added jetty-jmx.xml by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10475
* feat(plugins): spring custom plugins by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10389
* docs(impact analysis): Add column level impact analysis graphql example by [@gabe-lyons](https://github.com/gabe-lyons) in https://github.com/datahub-project/datahub/pull/10427
* fix(entity-registry): fix plugin load error by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10476
* fix(openapi): fix lookupAspectSpec by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10478
* fix(openapi-v3): comprehensive aspect name casing fix by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10484
* feat(ingest/slack): Support profile ingestion using users:info by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/10410
* docs: fix docs utms & slack footer by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10481
* feat(docs): Updating assertion docs + adding schema assertion doc  by [@jjoyce0510](https://github.com/jjoyce0510) in https://github.com/datahub-project/datahub/pull/10473
* fix(misc): misc fixes for OSS release by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10493
* docs: sort feature section alphabetically by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10400
* docs(developers): add section regarding symbolic links on Windows 10/11 to developer's guide by [@Masterchen09](https://github.com/Masterchen09) in https://github.com/datahub-project/datahub/pull/10487
* fix(ingestion/transformer): Add dataset domains based on tags using transformer by [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) in https://github.com/datahub-project/datahub/pull/10458
* chore(ingest/presto-on-hive) Set enable_properties_merge to True by default by [@dushayntAW](https://github.com/dushayntAW) in https://github.com/datahub-project/datahub/pull/10469
* fix(ci): documentation build fix by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10507
* docs: 0.3.2 Acryl by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10377
* feat(ingest/tableau): support platform instance mapping based off database server hostname by [@richenc](https://github.com/richenc) in https://github.com/datahub-project/datahub/pull/10254
* fix(ingestion/looker): deduplicate the view field by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10482
* fix(graphql): Support querying Posts and Queries by [@asikowitz](https://github.com/asikowitz) in https://github.com/datahub-project/datahub/pull/10502
* fix(ebean): fix auto-closeable ebean dao streams by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10506
* feat(ingest/airflow): support BigQueryInsertJobOperator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10452
* fix(ingest): avoid using `_inner_dict` in urn iterator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10492
* fix(ingest/snowflake): use block sampling more conservatively by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10494
* feat(sdk): add DataHubGraph.get_timeseries_values() method by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10501
* fix(mcp): fix mcp key aspect by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10503
* fix(ingest): fix bug in incremental lineage by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10515
* chore(ingest): run pyupgrade for python 3.8 by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10513
* docs: update cli recommendation by [@anshbansal](https://github.com/anshbansal) in https://github.com/datahub-project/datahub/pull/10518
* Wrap non-required $ref properties in an object to mark as nullable by [@timothyjin](https://github.com/timothyjin) in https://github.com/datahub-project/datahub/pull/10514
* Fix formatting for [#10514](https://github.com/datahub-project/datahub/pull/10514) by [@timothyjin](https://github.com/timothyjin) in https://github.com/datahub-project/datahub/pull/10525
* feat(ingestion/glue): delta schemas by [@sgomezvillamor](https://github.com/sgomezvillamor) in https://github.com/datahub-project/datahub/pull/10299
* fix(ingestion/snowflake): fix dataclass defaults for SnowflakeReport by [@ms32035](https://github.com/ms32035) in https://github.com/datahub-project/datahub/pull/10529
* Security/CWE 200 graphql introspection toggle by [@erikkvale](https://github.com/erikkvale) in https://github.com/datahub-project/datahub/pull/10531
* feat(neo4j): neo4j pagination as per v2 scrollApi for related entities by [@deepgarg-visa](https://github.com/deepgarg-visa) in https://github.com/datahub-project/datahub/pull/10537
* docs: add api templates by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10521
* fix(ingestion/powerbi): handle special character #(tab) in native query parsing by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10520
* OpenAPI v3 Spec bug fixes: by [@kevin1chun](https://github.com/kevin1chun) in https://github.com/datahub-project/datahub/pull/10548
* fix(assertions) aligned graphql AssertionType definition with the AssertionType defined in metadata-models by [@jayacryl](https://github.com/jayacryl) in https://github.com/datahub-project/datahub/pull/10534
* fix(smoke-test): pin requests to 2.31.0 by [@darnaut](https://github.com/darnaut) in https://github.com/datahub-project/datahub/pull/10549
* fix(ingest/dbt): improve handling for CLL via ephemeral nodes by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10535
* feat(connections) Add Connection entity type and graphql endpoints by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10550
* doc(gms/scim-api): fix title and add overview by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10388
* docs: add guides on forms & structured properties by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10340
* fix(graphl): fix introspection setting by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10560
* feat(ingest): bump acryl-sqlglot dep by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10554
* feat(ingest): auto-fix duplicate schema fieldPaths by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10526
* refactor(ingest): defer ctx.graph initialization by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10504
* consider all values of FabricType enum in DatasetUrn util by [@kevin1chun](https://github.com/kevin1chun) in https://github.com/datahub-project/datahub/pull/10564
* fix(ingest/airflow): fix support for bigquery insert job operator by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10567
* fix(ingest/mode): Adding Dashboards into containers by [@treff7es](https://github.com/treff7es) in https://github.com/datahub-project/datahub/pull/10563
* feat: update lineage feature guide by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10401
* docs: improve lineage docs by [@yoonhyejin](https://github.com/yoonhyejin) in https://github.com/datahub-project/datahub/pull/10396
* fix(ingestion/powerbi): Databricks support for table lineage by [@sid-acryl](https://github.com/sid-acryl) in https://github.com/datahub-project/datahub/pull/10416
* fix(ingest/dbt): resolve more dbt ephemeral node lineage gaps by [@hsheth2](https://github.com/hsheth2) in https://github.com/datahub-project/datahub/pull/10553
* fix(ui) Fix preventing users from deleting personal views by [@chriscollins3456](https://github.com/chriscollins3456) in https://github.com/datahub-project/datahub/pull/10510
* fix(lint): fix linting by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10572
* build(jar): enable custom plugin lib by [@david-leifker](https://github.com/david-leifker) in https://github.com/datahub-project/datahub/pull/10552

#### New Contributors
* [@bouaouda-achraf](https://github.com/bouaouda-achraf) made their first contribution in https://github.com/datahub-project/datahub/pull/9811
* [@jonasHanhan](https://github.com/jonasHanhan) made their first contribution in https://github.com/datahub-project/datahub/pull/10110
* [@dotan-mor](https://github.com/dotan-mor) made their first contribution in https://github.com/datahub-project/datahub/pull/10226
* [@olgapenedo](https://github.com/olgapenedo) made their first contribution in https://github.com/datahub-project/datahub/pull/10146
* [@paguos](https://github.com/paguos) made their first contribution in https://github.com/datahub-project/datahub/pull/10330
* [@ishtartec](https://github.com/ishtartec) made their first contribution in https://github.com/datahub-project/datahub/pull/10345
* [@camilogutierrez](https://github.com/camilogutierrez) made their first contribution in https://github.com/datahub-project/datahub/pull/10274
* [@mrjefflewis](https://github.com/mrjefflewis) made their first contribution in https://github.com/datahub-project/datahub/pull/10370
* [@Rosmirose](https://github.com/Rosmirose) made their first contribution in https://github.com/datahub-project/datahub/pull/10324
* [@guyr-ziprecruiter](https://github.com/guyr-ziprecruiter) made their first contribution in https://github.com/datahub-project/datahub/pull/10405
* [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) made their first contribution in https://github.com/datahub-project/datahub/pull/10458
* [@timothyjin](https://github.com/timothyjin) made their first contribution in https://github.com/datahub-project/datahub/pull/10514
* [@erikkvale](https://github.com/erikkvale) made their first contribution in https://github.com/datahub-project/datahub/pull/10531

**Full Changelog**: https://github.com/datahub-project/datahub/compare/v0.13.1...v0.13.3

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

