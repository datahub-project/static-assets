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
| **v1.0.0** | 2025-03-14 |[Release Notes](#v1-0-0), [View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v1.0.0) |
| **v0.15.0.1** | 2025-01-21 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.15.0.1) |
| **v0.15.0** | 2025-01-15 |[View on GitHub](https://github.com/datahub-project/datahub/releases/tag/v0.15.0) |
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


## [v1.0.0](https://github.com/datahub-project/datahub/releases/tag/v1.0.0) {#v1-0-0}

Released on 2025-03-14 by [@pedro93](https://github.com/pedro93).

### DataHub v1.0.0

#### Release Highlights 
DataHub v1.0.0 is packed with exciting updates, including:

* A completely redesigned user experience focused on simplified navigation and a visually stunning interface.
* Unified support for Data & AI, including AI Model Group Versions, AI Model Lineage, Model Stats, and Experiment/Run ingestion.
* DataHub Iceberg Catalog, allowing users to manage Iceberg tables directly from DataHub.

_Read the blog post [here!](https://medium.com/datahub-project/datahub-1-0-is-here-94805883135f)_

#### Changelog

##### New User Interface: Putting Usability First

With a completely re-designed user interface, DataHub v1.0 represents a fundamental rethinking of how users interact with their metadata and data assets. The new experience includes:

* **Intuitive Platform-Based Navigation** - Hierarchically browse data by database and schema in Snowflake, BigQuery, Redshift, Databricks, and more. Combine hierarchical navigation with filtering by data owners, domain, tags, and glossary terms to find the right data fast.
* **Seamless Lineage Exploration** - Our reimagined lineage view features multi-level expansion, name-based search, and column-level visibility, making it easier than ever to understand data relationships and impact.
* **Integrated Data Quality** - Make confident decisions with deeply integrated quality signals throughout the platform, helping you quickly identify and trust reliable data assets.

DataHub Admins can enable the new UI for all users by setting the `THEME_V2_DEFAULT` environment variable to `true`; until then, Users can opt into the new experience by navigating to **Settings > Appearance > Try New User Experience**.

##### Comprehensive AI Asset Support: Unifying Data and AI

DataHub v1.0 treats AI assets as first-class citizens within the data ecosystem, allowing users to track their entire data-to-AI pipeline in one place. 

* **Unified Search and Discovery**: Seamlessly search across models, model groups, and traditional data assets in one unified interface.
* **Advanced Versioning System**: Track multiple versions of datasets and ML models with detailed performance metrics and clear linkages between versions.
* **Rich Model Statistics**: Monitor key metrics across versions, understand performance trends, and make data-driven decisions about model deployment.
* **End-to-End Lineage**: Trace data flows from raw inputs through models to final outputs, with complete versioning support.

##### DataHub Iceberg REST Catalog Beta: Simplifying Data Lake Management

This release introduces an integration with Apace Iceberg, allowing users to manage Iceberg tables directly through DataHub, including:
* Create and manage Iceberg tables through DataHub
* Maintain consistent metadata across DataHub and Iceberg
* Facilitate data discovery by exposing Iceberg table metadata in DataHub
* Enable secure access to Iceberg tables through DataHub's permissions model

_Read the docs [here](https://datahubproject.io/docs/iceberg-catalog/)!_

##### DataHub CLI
This release introduces the following improvements to our CLI:

* Added `container` command to apply tags, terms, and owners on all assets within the container. [ [[#1241](https://github.com/datahub-project/datahub/pull/1241)](https://github.com/datahub-project/datahub/pull/12418)[8](https://suno.com/song/62230885-8b8c-45c2-bdf6-eeb0d7fcc101?sh=hJ6DQioE7oCuCiYg), [#12436](https://github.com/datahub-project/datahub/pull/12436)] 
* Improved `delete` command to optionally reference a file with a list of URNS to be deleted. [[#12247](https://github.com/datahub-project/datahub/pull/12247)]
* Expanded `ingest` command to support ingesting MCPs from S3. [[#12649](https://github.com/datahub-project/datahub/pull/12649)]

##### Metadata Ingestion
We’re continuously improving our integrations to add new capabilities and squash bugs.

* **dbt**: Added the parameter `include_database_name` to support including the database name in URN generation. [[#12411](https://github.com/datahub-project/datahub/pull/12411)] 
* **Iceberg**: Alongside our new Iceberg Catalog API, we’ve made various improvements to our Iceberg integration. [[#12744](https://github.com/datahub-project/datahub/pull/12744)] 
* **MLFlow**: Significantly revamped our MLFlow connector, adding support for tracking Model Group Versions and Model Stats; tracking Model lineage to underlying datasets; and capturing Experiments and Runs.
* **MSSQL**: Improved support for extracting stored procedures from MS SQL. [ [#12244](https://github.com/datahub-project/datahub/pull/12244), [#12563](https://github.com/datahub-project/datahub/pull/12563)] 
* **Oracle**: Improved the accuracy of column-level lineage resolution.
* **PowerBI**: Improved lineage mapping so PowerBI Reports can now contain PowerBI Dashboards. [[#12451](https://github.com/datahub-project/datahub/pull/12451)]
* **Redshift**: Added support for data shares and external schemas, including automatic lineage resolution across Redshift namespaces.
* **S3**: Added functionality to the S3 ingestion process to ignore paths that do not match the specified depth, resolving warning messages triggered by mismatched paths. [[#12326](https://github.com/datahub-project/datahub/pull/12326)]
* **Snowflake**: Added support for Snowflake Streams and Hybrid Tables, and fixed a bug with lineage resolution across table renames. [[#12318](https://github.com/datahub-project/datahub/pull/12318)]
* **Superset**: (community contribution!): Added support for Superset virtual datasets and lineage. [[#12679](https://github.com/datahub-project/datahub/pull/12679)]

Additionally, we’re working on a new integration with **Vertex AI**. Please reach out if you’re interested in joining the beta.

Of course, this only scratches the surface of changes. This release contains 100+ improvements across 25 different integrations.

#### Thank You to our Contributors!

##### First-Time Contributors
[@Bhadhri03](https://github.com/Bhadhri03) [@brock-acryl](https://github.com/brock-acryl) [@cccs-cat001](https://github.com/cccs-cat001) [@davidebriscese](https://github.com/davidebriscese) [@Deepalijain13](https://github.com/Deepalijain13) [@dougbot01](https://github.com/dougbot01) [@Haebuk](https://github.com/Haebuk) [@haon85](https://github.com/haon85) [@josges](https://github.com/josges) [@mihai103](https://github.com/mihai103) [@rajatgl17](https://github.com/rajatgl17) [@Rasnar](https://github.com/Rasnar) [@rharisi](https://github.com/rharisi) [@samanthafigueredo5](https://github.com/samanthafigueredo5) [@ttekampe](https://github.com/ttekampe)

##### Repeat Contributors
[@bda618](https://github.com/bda618) [@deepgarg-visa](https://github.com/deepgarg-visa) [@eagle-25](https://github.com/eagle-25) [@jayasimhankv](https://github.com/jayasimhankv) [@ksrinath](https://github.com/ksrinath) [@llance](https://github.com/llance) [@Masterchen09](https://github.com/Masterchen09) [@mayurinehate](https://github.com/mayurinehate) [@mkamalas](https://github.com/mkamalas) [@PeteMango](https://github.com/PeteMango) [@pinakipb2](https://github.com/pinakipb2) [@remisalmon](https://github.com/remisalmon) [@sagar-salvi-apptware](https://github.com/sagar-salvi-apptware) [@svdimchenko](https://github.com/svdimchenko) [@v-tarasevich-blitz-brain](https://github.com/v-tarasevich-blitz-brain)

##### Project Maintainers
[@anshbansal](https://github.com/anshbansal) [@asikowitz](https://github.com/asikowitz) [@chakru-r](https://github.com/chakru-r) [@chriscollins3456](https://github.com/chriscollins3456) [@david-leifker](https://github.com/david-leifker) [@gabe-lyons](https://github.com/gabe-lyons) [@hsheth2](https://github.com/hsheth2) [@jayacryl](https://github.com/jayacryl) [@jjoyce0510](https://github.com/jjoyce0510) [@kevinkarchacryl](https://github.com/kevinkarchacryl) [@pedro93](https://github.com/pedro93) [@RyanHolstien](https://github.com/RyanHolstien) [@ryota-cloud](https://github.com/ryota-cloud) [@sakethvarma397](https://github.com/sakethvarma397) [@sgomezvillamor](https://github.com/sgomezvillamor) [@shirshanka](https://github.com/shirshanka) [@skrydal](https://github.com/skrydal) [@treff7es](https://github.com/treff7es) [@yoonhyejin](https://github.com/yoonhyejin)


**View the full changelog**: https://github.com/datahub-project/datahub/compare/v0.15.0.1...v1.0.0

## [v0.15.0.1](https://github.com/datahub-project/datahub/releases/tag/v0.15.0.1) {#v0-15-0-1}

Released on 2025-01-21 by [@pedro93](https://github.com/pedro93).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.15.0.1) for v0.15.0.1 on GitHub.

## [V0.15.0](https://github.com/datahub-project/datahub/releases/tag/v0.15.0) {#v0-15-0}

Released on 2025-01-15 by [@pedro93](https://github.com/pedro93).

View the [release notes](https://github.com/datahub-project/datahub/releases/tag/v0.15.0) for V0.15.0 on GitHub.

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

