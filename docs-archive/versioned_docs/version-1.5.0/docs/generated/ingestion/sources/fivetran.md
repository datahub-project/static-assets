---
sidebar_position: 31
title: Fivetran
slug: /generated/ingestion/sources/fivetran
custom_edit_url: null
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fivetran

## Overview

Fivetran is a streaming or integration platform. Learn more in the [official Fivetran documentation](https://www.fivetran.com/).

The DataHub integration for Fivetran covers streaming/integration entities such as topics, connectors, pipelines, or jobs. Depending on module capabilities, it can also capture features such as lineage, usage, profiling, ownership, tags, and stateful deletion detection.

## Concept Mapping

| Fivetran        | Datahub                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| `Connector`     | [DataJob](/docs/generated/metamodel/entities/datajob/)                        |
| `Source`        | [Dataset](/docs/generated/metamodel/entities/dataset/)                        |
| `Destination`   | [Dataset](/docs/generated/metamodel/entities/dataset/)                        |
| `Connector Run` | [DataProcessInstance](/docs/generated/metamodel/entities/dataprocessinstance) |

Source and destination are mapped to Dataset as an Input and Output of Connector.


## Module `fivetran`
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Column-level Lineage | ✅ | Enabled by default, can be disabled via configuration `include_column_lineage`. |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default via stateful ingestion. |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default. |

### Overview

The `fivetran` module ingests metadata from Fivetran into DataHub. It is intended for production ingestion workflows and module-specific capabilities are documented below.

#### Integration Details

This source extracts the following:

- Connectors in fivetran as Data Pipelines and Data Jobs to represent data lineage information between source and destination.
- Connector sources - DataJob input Datasets.
- Connector destination - DataJob output Datasets.
- Connector runs - DataProcessInstances as DataJob runs.

#### Configuration Notes

**Prerequisites:**

1. Set up and complete initial sync of the [Fivetran Platform Connector](https://fivetran.com/docs/logs/fivetran-platform/setup-guide)
2. Enable automatic schema updates (default) to avoid sync inconsistencies
3. Configure the destination platform (Snowflake, BigQuery, or Databricks) in your recipe

### Prerequisites

Before running ingestion, ensure network connectivity to the source, valid authentication credentials, and read permissions for metadata APIs required by this module.

To use the Fivetran REST API integration, you need:

**Required API Permissions**:

- **Read access** to connection details (`GET /v1/connections/{connection_id}`)
- The API key must be associated with a user or service account that has access to the connectors you want to ingest
- The API key inherits permissions from the user or service account it's associated with

#### Fivetran REST API Configuration

The Fivetran REST API configuration is **required** for Google Sheets connectors and optional for other use cases. It provides access to connection details that aren't available in the Platform Connector logs.

##### Setup

To obtain API credentials:

1. Log in to your Fivetran account
2. Go to **Settings** → **API Config**
3. Create or use an existing API key and secret

```yaml
api_config:
  api_key: "your_api_key"
  api_secret: "your_api_secret"
  base_url: "https://api.fivetran.com" # Optional, defaults to this
  request_timeout_sec: 30 # Optional, defaults to 30 seconds
```

#### Google Sheets Connector Support

Google Sheets connectors require special handling because Google Sheets is not yet natively supported as a DataHub source. As a workaround, the Fivetran source creates Dataset entities for Google Sheets and includes them in the lineage.

##### Requirements

- **Fivetran REST API configuration** (`api_config`) is required for Google Sheets connectors
- The API is used to fetch connection details that aren't available in Platform Connector logs

##### What Gets Created

For each Google Sheets connector, two Dataset entities are created:

1. **Google Sheet Dataset**: Represents the entire Google Sheet

   - Platform: `google_sheets`
   - Subtype: `GOOGLE_SHEETS`
   - Contains the sheet ID extracted from the Google Sheets URL

2. **Named Range Dataset**: Represents the specific named range being synced
   - Platform: `google_sheets`
   - Subtype: `GOOGLE_SHEETS_NAMED_RANGE`
   - Contains the named range identifier
   - Has upstream lineage to the Google Sheet Dataset

##### Limitations

- **Column lineage is disabled** for Google Sheets connectors due to stale metadata issues in the Fivetran Platform Connector (as of October 2025)
- This is a workaround that will be removed once DataHub natively supports Google Sheets as a source
- If the Fivetran API is unavailable or the connector details can't be fetched, the connector will be skipped with a warning

##### Example Configuration

```yaml
source:
  type: fivetran
  config:
    # Required for Google Sheets connectors
    api_config:
      api_key: "your_api_key"
      api_secret: "your_api_secret"

    # ... other configuration ...
```


### Install the Plugin
```shell
pip install 'acryl-datahub[fivetran]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: fivetran
  config:
    # Fivetran log connector destination server configurations
    fivetran_log_config:
      destination_platform: snowflake
      # Optional - If destination platform is 'snowflake', provide snowflake configuration.
      snowflake_destination_config:
        # Coordinates
        account_id: "abc48144"
        warehouse: "COMPUTE_WH"
        database: "MY_SNOWFLAKE_DB"
        log_schema: "FIVETRAN_LOG"

        # Credentials
        username: "${SNOWFLAKE_USER}"
        password: "${SNOWFLAKE_PASS}"
        role: "snowflake_role"
      # Optional - If destination platform is 'bigquery', provide bigquery configuration.
      bigquery_destination_config:
        # Credentials
        credential:
          private_key_id: "project_key_id"
          project_id: "project_id"
          client_email: "client_email"
          client_id: "client_id"
          private_key: "private_key"
        dataset: "fivetran_log_dataset"
      # Optional - If destination platform is 'databricks', provide databricks configuration.
      databricks_destination_config:
        # Credentials
        credential:
          token: "token"
          workspace_url: "workspace_url"
          warehouse_id: "warehouse_id"

           # Coordinates
          catalog: "fivetran_catalog"
          log_schema: "fivetran_log"
     
    # Optional - filter for certain connector names instead of ingesting everything.
    # connector_patterns:
    #   allow:
    #     - connector_name

    # Optional -- A mapping of the connector's all sources to its database.
    # sources_to_database:
    #   connector_id: source_db

    # Optional - Fivetran REST API configuration (required for Google Sheets connectors)
    # api_config:
    #   api_key: "your_api_key"
    #   api_secret: "your_api_secret"
    #   base_url: "https://api.fivetran.com"  # Optional
    #   request_timeout_sec: 30  # Optional
    # Optional -- This mapping is optional and only required to configure platform-instance for source
    # A mapping of Fivetran connector id to data platform instance
    # sources_to_platform_instance:
    #   connector_id:
    #     platform_instance: cloud_instance
    #     env: DEV

    # Optional -- This mapping is optional and only required to configure platform-instance for destination.
    # A mapping of Fivetran destination id to data platform instance
    # destination_to_platform_instance:
    #   destination_id:
    #     platform_instance: cloud_instance
    #     env: DEV

sink:
  # sink configs

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">fivetran_log_config</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">FivetranLogConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">destination_platform</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "snowflake", "bigquery", "databricks" <div className="default-line default-line-with-docs">Default: <span className="default-value">snowflake</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">max_column_lineage_per_connector</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of column lineage entries to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. When this limit is exceeded, only the most recent entries are ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">max_jobs_per_connector</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of sync jobs to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. Increase cautiously if you need to see more historical sync runs. <div className="default-line default-line-with-docs">Default: <span className="default-value">500</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">max_table_lineage_per_connector</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of table lineage entries to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. When this limit is exceeded, only the most recent entries are ingested. <div className="default-line default-line-with-docs">Default: <span className="default-value">120</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">bigquery_destination_config</span></div> <div className="type-name-line"><span className="type-name">One of BigQueryDestinationConfig, null</span></div> | If destination platform is 'bigquery', provide bigquery configuration. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">dataset</span>&nbsp;<abbr title="Required if bigquery_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log dataset.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">extra_client_options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Additional options to pass to google.cloud.logging_v2.client.Client. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">project_on_behalf</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | [Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">credential</span></div> <div className="type-name-line"><span className="type-name">One of GCPCredential, null</span></div> | BigQuery credential informations <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_email</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client email  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client Id  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">private_key</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n'  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">private_key_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key id  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">auth_provider_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Auth provider x509 certificate url <div className="default-line default-line-with-docs">Default: <span className="default-value">https://www.googleapis.com/oauth2/v1/certs</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">auth_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://accounts.google.com/o/oauth2/auth</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">project_id</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Project id to set the credentials <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">token_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Token uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://oauth2.googleapis.com/token</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication type <div className="default-line default-line-with-docs">Default: <span className="default-value">service&#95;account</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">databricks_destination_config</span></div> <div className="type-name-line"><span className="type-name">One of DatabricksDestinationConfig, null</span></div> | If destination platform is 'databricks', provide databricks configuration. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">catalog</span>&nbsp;<abbr title="Required if databricks_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log catalog.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">log_schema</span>&nbsp;<abbr title="Required if databricks_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log schema.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">workspace_url</span>&nbsp;<abbr title="Required if databricks_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Databricks workspace url. e.g. https://my-workspace.cloud.databricks.com  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">client_id</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Databricks service principal client ID <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">client_secret</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | Databricks service principal client secret <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">extra_client_options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Additional options to pass to Databricks SQLAlchemy client. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">databricks</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">token</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | Databricks personal access token <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">warehouse_id</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | SQL Warehouse id, for running queries. Must be explicitly provided to enable SQL-based features. Required for the following features that need SQL access: 1) Tag extraction (include_tags=True) - queries system.information_schema.tags 2) Hive Metastore catalog (include_hive_metastore=True) - queries legacy hive_metastore catalog 3) System table lineage (lineage_data_source=SYSTEM_TABLES) - queries system.access.table_lineage/column_lineage 4) Data profiling (profiling.enabled=True) - runs SELECT/ANALYZE queries on tables. When warehouse_id is missing, these features will be automatically disabled (with warnings) to allow ingestion to continue. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.</span><span className="path-main">azure_auth</span></div> <div className="type-name-line"><span className="type-name">One of AzureAuthConfig, null</span></div> | Azure configuration <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.azure_auth.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if azure_auth is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure application (client) ID. This is the unique identifier for the registered Azure AD application.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.azure_auth.</span><span className="path-main">client_secret</span>&nbsp;<abbr title="Required if azure_auth is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Azure application client secret used for authentication. This is a confidential credential that should be kept secure.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.databricks_destination_config.azure_auth.</span><span className="path-main">tenant_id</span>&nbsp;<abbr title="Required if azure_auth is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Azure tenant (directory) ID. This identifies the Azure AD tenant where the application is registered.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">snowflake_destination_config</span></div> <div className="type-name-line"><span className="type-name">One of SnowflakeDestinationConfig, null</span></div> | If destination platform is 'snowflake', provide snowflake configuration. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">account_id</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake account identifier. e.g. xy12345,  xy12345.us-east-2.aws, xy12345.us-central1.gcp, xy12345.central-us.azure, xy12345.us-west-2.privatelink. Refer [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region) for more details.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">database</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log database.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">log_schema</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log schema.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">authentication_type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The type of authenticator to use when connecting to Snowflake. Supports "DEFAULT_AUTHENTICATOR", "OAUTH_AUTHENTICATOR", "EXTERNAL_BROWSER_AUTHENTICATOR" and "KEY_PAIR_AUTHENTICATOR". <div className="default-line default-line-with-docs">Default: <span className="default-value">DEFAULT&#95;AUTHENTICATOR</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">connect_args</span></div> <div className="type-name-line"><span className="type-name">One of object, null</span></div> | Connect args to pass to Snowflake SqlAlchemy driver <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | Snowflake password. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n' if using key pair authentication. Encrypted version of private key will be in a form of '-----BEGIN ENCRYPTED PRIVATE KEY-----\nencrypted-private-key\n-----END ENCRYPTED PRIVATE KEY-----\n' See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key_password</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | Password for your private key. Required if using key pair authentication with encrypted private key. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key_path</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The path to the private key if using key pair authentication. Ignored if `private_key` is set. See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">role</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Snowflake role. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">snowflake_domain</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake domain. Use 'snowflakecomputing.com' for most regions or 'snowflakecomputing.cn' for China (cn-northwest-1) region. <div className="default-line default-line-with-docs">Default: <span className="default-value">snowflakecomputing.com</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">token</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | OAuth token from external identity provider. Not recommended for most use cases because it will not be able to refresh once expired. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Snowflake username. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">warehouse</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Snowflake warehouse. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">oauth_config</span></div> <div className="type-name-line"><span className="type-name">One of OAuthConfiguration, null</span></div> | oauth configuration - https://docs.snowflake.com/en/user-guide/python-connector-example.html#connecting-with-oauth <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">authority_url</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authority url of your identity provider  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | client id of your registered application  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">provider</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "microsoft", "okta"  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">scopes</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">array</span></div> | scopes required to connect to snowflake  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.scopes.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">client_secret</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | client secret of the application if use_certificate = false <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">encoded_oauth_private_key</span></div> <div className="type-name-line"><span className="type-name">One of string(password), null</span></div> | base64 encoded private key content if use_certificate = true <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">encoded_oauth_public_key</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | base64 encoded certificate content if use_certificate = true <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">use_certificate</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Do you want to use certificate and private key to authenticate using oauth <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">history_sync_lookback_period</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of days to look back when extracting connectors' sync history. <div className="default-line default-line-with-docs">Default: <span className="default-value">7</span></div> |
| <div className="path-line"><span className="path-main">include_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates table->table column lineage. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">api_config</span></div> <div className="type-name-line"><span className="type-name">One of FivetranAPIConfig, null</span></div> | Fivetran REST API configuration, used to provide wider support for connections. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">api_config.</span><span className="path-main">api_key</span>&nbsp;<abbr title="Required if api_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Fivetran API key  |
| <div className="path-line"><span className="path-prefix">api_config.</span><span className="path-main">api_secret</span>&nbsp;<abbr title="Required if api_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Fivetran API secret  |
| <div className="path-line"><span className="path-prefix">api_config.</span><span className="path-main">base_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Fivetran API base URL <div className="default-line default-line-with-docs">Default: <span className="default-value">https://api.fivetran.com</span></div> |
| <div className="path-line"><span className="path-prefix">api_config.</span><span className="path-main">request_timeout_sec</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Request timeout in seconds <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-main">connector_patterns</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">One of boolean, null</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">destination_patterns</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">destination_patterns.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">One of boolean, null</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">destination_patterns.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">destination_patterns.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">destination_patterns.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">destination_patterns.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">destination_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> |   |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">platform</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Override the platform type detection. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">database</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The database that all assets produced by this connector belong to. For destinations, this defaults to the fivetran log config's database. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">include_schema_in_urn</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include schema in the dataset URN. In some cases, the schema is not relevant to the dataset URN and Fivetran sets it to the source and destination table names in the connector. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The instance of the platform that all assets produced by this recipe belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by DataHub platform ingestion source belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">sources_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> |   |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">platform</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Override the platform type detection. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">database</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The database that all assets produced by this connector belong to. For destinations, this defaults to the fivetran log config's database. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">include_schema_in_urn</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include schema in the dataset URN. In some cases, the schema is not relevant to the dataset URN and Fivetran sets it to the source and destination table names in the connector. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The instance of the platform that all assets produced by this recipe belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by DataHub platform ingestion source belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">One of StatefulStaleMetadataRemovalConfig, null</span></div> | Fivetran Stateful Ingestion Config. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">fail_safe_threshold</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'. <div className="default-line default-line-with-docs">Default: <span className="default-value">75.0</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "$defs": {
    "AllowDenyPattern": {
      "additionalProperties": false,
      "description": "A class to store allow deny regexes",
      "properties": {
        "allow": {
          "default": [
            ".*"
          ],
          "description": "List of regex patterns to include in ingestion",
          "items": {
            "type": "string"
          },
          "title": "Allow",
          "type": "array"
        },
        "deny": {
          "default": [],
          "description": "List of regex patterns to exclude from ingestion.",
          "items": {
            "type": "string"
          },
          "title": "Deny",
          "type": "array"
        },
        "ignoreCase": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "default": true,
          "description": "Whether to ignore case sensitivity during pattern matching.",
          "title": "Ignorecase"
        }
      },
      "title": "AllowDenyPattern",
      "type": "object"
    },
    "AzureAuthConfig": {
      "additionalProperties": false,
      "properties": {
        "client_secret": {
          "description": "Azure application client secret used for authentication. This is a confidential credential that should be kept secure.",
          "format": "password",
          "title": "Client Secret",
          "type": "string",
          "writeOnly": true
        },
        "client_id": {
          "description": "Azure application (client) ID. This is the unique identifier for the registered Azure AD application.",
          "title": "Client Id",
          "type": "string"
        },
        "tenant_id": {
          "description": "Azure tenant (directory) ID. This identifies the Azure AD tenant where the application is registered.",
          "title": "Tenant Id",
          "type": "string"
        }
      },
      "required": [
        "client_secret",
        "client_id",
        "tenant_id"
      ],
      "title": "AzureAuthConfig",
      "type": "object"
    },
    "BigQueryDestinationConfig": {
      "additionalProperties": false,
      "properties": {
        "credential": {
          "anyOf": [
            {
              "$ref": "#/$defs/GCPCredential"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "BigQuery credential informations"
        },
        "extra_client_options": {
          "additionalProperties": true,
          "default": {},
          "description": "Additional options to pass to google.cloud.logging_v2.client.Client.",
          "title": "Extra Client Options",
          "type": "object"
        },
        "project_on_behalf": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "[Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account.",
          "title": "Project On Behalf"
        },
        "dataset": {
          "description": "The fivetran connector log dataset.",
          "title": "Dataset",
          "type": "string"
        }
      },
      "required": [
        "dataset"
      ],
      "title": "BigQueryDestinationConfig",
      "type": "object"
    },
    "DatabricksDestinationConfig": {
      "additionalProperties": false,
      "properties": {
        "scheme": {
          "default": "databricks",
          "title": "Scheme",
          "type": "string"
        },
        "token": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Databricks personal access token",
          "title": "Token"
        },
        "azure_auth": {
          "anyOf": [
            {
              "$ref": "#/$defs/AzureAuthConfig"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Azure configuration"
        },
        "client_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Databricks service principal client ID",
          "title": "Client Id"
        },
        "client_secret": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Databricks service principal client secret",
          "title": "Client Secret"
        },
        "workspace_url": {
          "description": "Databricks workspace url. e.g. https://my-workspace.cloud.databricks.com",
          "title": "Workspace Url",
          "type": "string"
        },
        "warehouse_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "SQL Warehouse id, for running queries. Must be explicitly provided to enable SQL-based features. Required for the following features that need SQL access: 1) Tag extraction (include_tags=True) - queries system.information_schema.tags 2) Hive Metastore catalog (include_hive_metastore=True) - queries legacy hive_metastore catalog 3) System table lineage (lineage_data_source=SYSTEM_TABLES) - queries system.access.table_lineage/column_lineage 4) Data profiling (profiling.enabled=True) - runs SELECT/ANALYZE queries on tables. When warehouse_id is missing, these features will be automatically disabled (with warnings) to allow ingestion to continue.",
          "title": "Warehouse Id"
        },
        "extra_client_options": {
          "additionalProperties": true,
          "default": {},
          "description": "Additional options to pass to Databricks SQLAlchemy client.",
          "title": "Extra Client Options",
          "type": "object"
        },
        "catalog": {
          "description": "The fivetran connector log catalog.",
          "title": "Catalog",
          "type": "string"
        },
        "log_schema": {
          "description": "The fivetran connector log schema.",
          "title": "Log Schema",
          "type": "string"
        }
      },
      "required": [
        "workspace_url",
        "catalog",
        "log_schema"
      ],
      "title": "DatabricksDestinationConfig",
      "type": "object"
    },
    "FivetranAPIConfig": {
      "additionalProperties": false,
      "properties": {
        "api_key": {
          "description": "Fivetran API key",
          "format": "password",
          "title": "Api Key",
          "type": "string",
          "writeOnly": true
        },
        "api_secret": {
          "description": "Fivetran API secret",
          "format": "password",
          "title": "Api Secret",
          "type": "string",
          "writeOnly": true
        },
        "base_url": {
          "default": "https://api.fivetran.com",
          "description": "Fivetran API base URL",
          "title": "Base Url",
          "type": "string"
        },
        "request_timeout_sec": {
          "default": 30,
          "description": "Request timeout in seconds",
          "title": "Request Timeout Sec",
          "type": "integer"
        }
      },
      "required": [
        "api_key",
        "api_secret"
      ],
      "title": "FivetranAPIConfig",
      "type": "object"
    },
    "FivetranLogConfig": {
      "additionalProperties": false,
      "properties": {
        "destination_platform": {
          "default": "snowflake",
          "description": "The destination platform where fivetran connector log tables are dumped.",
          "enum": [
            "snowflake",
            "bigquery",
            "databricks"
          ],
          "title": "Destination Platform",
          "type": "string"
        },
        "snowflake_destination_config": {
          "anyOf": [
            {
              "$ref": "#/$defs/SnowflakeDestinationConfig"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "If destination platform is 'snowflake', provide snowflake configuration."
        },
        "bigquery_destination_config": {
          "anyOf": [
            {
              "$ref": "#/$defs/BigQueryDestinationConfig"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "If destination platform is 'bigquery', provide bigquery configuration."
        },
        "databricks_destination_config": {
          "anyOf": [
            {
              "$ref": "#/$defs/DatabricksDestinationConfig"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "If destination platform is 'databricks', provide databricks configuration."
        },
        "max_jobs_per_connector": {
          "default": 500,
          "description": "Maximum number of sync jobs to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. Increase cautiously if you need to see more historical sync runs.",
          "exclusiveMinimum": 0,
          "title": "Max Jobs Per Connector",
          "type": "integer"
        },
        "max_table_lineage_per_connector": {
          "default": 120,
          "description": "Maximum number of table lineage entries to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. When this limit is exceeded, only the most recent entries are ingested.",
          "exclusiveMinimum": 0,
          "title": "Max Table Lineage Per Connector",
          "type": "integer"
        },
        "max_column_lineage_per_connector": {
          "default": 1000,
          "description": "Maximum number of column lineage entries to retrieve per connector. This acts as a safety net to prevent excessive data ingestion. When this limit is exceeded, only the most recent entries are ingested.",
          "exclusiveMinimum": 0,
          "title": "Max Column Lineage Per Connector",
          "type": "integer"
        }
      },
      "title": "FivetranLogConfig",
      "type": "object"
    },
    "GCPCredential": {
      "additionalProperties": false,
      "properties": {
        "project_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Project id to set the credentials",
          "title": "Project Id"
        },
        "private_key_id": {
          "description": "Private key id",
          "title": "Private Key Id",
          "type": "string"
        },
        "private_key": {
          "description": "Private key in a form of '-----BEGIN PRIVATE KEY-----\\nprivate-key\\n-----END PRIVATE KEY-----\\n'",
          "format": "password",
          "title": "Private Key",
          "type": "string",
          "writeOnly": true
        },
        "client_email": {
          "description": "Client email",
          "title": "Client Email",
          "type": "string"
        },
        "client_id": {
          "description": "Client Id",
          "title": "Client Id",
          "type": "string"
        },
        "auth_uri": {
          "default": "https://accounts.google.com/o/oauth2/auth",
          "description": "Authentication uri",
          "title": "Auth Uri",
          "type": "string"
        },
        "token_uri": {
          "default": "https://oauth2.googleapis.com/token",
          "description": "Token uri",
          "title": "Token Uri",
          "type": "string"
        },
        "auth_provider_x509_cert_url": {
          "default": "https://www.googleapis.com/oauth2/v1/certs",
          "description": "Auth provider x509 certificate url",
          "title": "Auth Provider X509 Cert Url",
          "type": "string"
        },
        "type": {
          "default": "service_account",
          "description": "Authentication type",
          "title": "Type",
          "type": "string"
        },
        "client_x509_cert_url": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email",
          "title": "Client X509 Cert Url"
        }
      },
      "required": [
        "private_key_id",
        "private_key",
        "client_email",
        "client_id"
      ],
      "title": "GCPCredential",
      "type": "object"
    },
    "OAuthConfiguration": {
      "additionalProperties": false,
      "properties": {
        "provider": {
          "$ref": "#/$defs/OAuthIdentityProvider",
          "description": "Identity provider for oauth.Supported providers are microsoft and okta."
        },
        "authority_url": {
          "description": "Authority url of your identity provider",
          "title": "Authority Url",
          "type": "string"
        },
        "client_id": {
          "description": "client id of your registered application",
          "title": "Client Id",
          "type": "string"
        },
        "scopes": {
          "description": "scopes required to connect to snowflake",
          "items": {
            "type": "string"
          },
          "title": "Scopes",
          "type": "array"
        },
        "use_certificate": {
          "default": false,
          "description": "Do you want to use certificate and private key to authenticate using oauth",
          "title": "Use Certificate",
          "type": "boolean"
        },
        "client_secret": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "client secret of the application if use_certificate = false",
          "title": "Client Secret"
        },
        "encoded_oauth_public_key": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "base64 encoded certificate content if use_certificate = true",
          "title": "Encoded Oauth Public Key"
        },
        "encoded_oauth_private_key": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "base64 encoded private key content if use_certificate = true",
          "title": "Encoded Oauth Private Key"
        }
      },
      "required": [
        "provider",
        "authority_url",
        "client_id",
        "scopes"
      ],
      "title": "OAuthConfiguration",
      "type": "object"
    },
    "OAuthIdentityProvider": {
      "enum": [
        "microsoft",
        "okta"
      ],
      "title": "OAuthIdentityProvider",
      "type": "string"
    },
    "PlatformDetail": {
      "additionalProperties": false,
      "properties": {
        "platform": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Override the platform type detection.",
          "title": "Platform"
        },
        "platform_instance": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "The instance of the platform that all assets produced by this recipe belong to",
          "title": "Platform Instance"
        },
        "env": {
          "default": "PROD",
          "description": "The environment that all assets produced by DataHub platform ingestion source belong to",
          "title": "Env",
          "type": "string"
        },
        "database": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "The database that all assets produced by this connector belong to. For destinations, this defaults to the fivetran log config's database.",
          "title": "Database"
        },
        "include_schema_in_urn": {
          "default": true,
          "description": "Include schema in the dataset URN. In some cases, the schema is not relevant to the dataset URN and Fivetran sets it to the source and destination table names in the connector.",
          "title": "Include Schema In Urn",
          "type": "boolean"
        }
      },
      "title": "PlatformDetail",
      "type": "object"
    },
    "SnowflakeDestinationConfig": {
      "additionalProperties": false,
      "properties": {
        "options": {
          "additionalProperties": true,
          "description": "Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.",
          "title": "Options",
          "type": "object"
        },
        "username": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Snowflake username.",
          "title": "Username"
        },
        "password": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Snowflake password.",
          "title": "Password"
        },
        "private_key": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Private key in a form of '-----BEGIN PRIVATE KEY-----\\nprivate-key\\n-----END PRIVATE KEY-----\\n' if using key pair authentication. Encrypted version of private key will be in a form of '-----BEGIN ENCRYPTED PRIVATE KEY-----\\nencrypted-private-key\\n-----END ENCRYPTED PRIVATE KEY-----\\n' See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html",
          "title": "Private Key"
        },
        "private_key_path": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "The path to the private key if using key pair authentication. Ignored if `private_key` is set. See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html",
          "title": "Private Key Path"
        },
        "private_key_password": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Password for your private key. Required if using key pair authentication with encrypted private key.",
          "title": "Private Key Password"
        },
        "oauth_config": {
          "anyOf": [
            {
              "$ref": "#/$defs/OAuthConfiguration"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "oauth configuration - https://docs.snowflake.com/en/user-guide/python-connector-example.html#connecting-with-oauth"
        },
        "authentication_type": {
          "default": "DEFAULT_AUTHENTICATOR",
          "description": "The type of authenticator to use when connecting to Snowflake. Supports \"DEFAULT_AUTHENTICATOR\", \"OAUTH_AUTHENTICATOR\", \"EXTERNAL_BROWSER_AUTHENTICATOR\" and \"KEY_PAIR_AUTHENTICATOR\".",
          "title": "Authentication Type",
          "type": "string"
        },
        "account_id": {
          "description": "Snowflake account identifier. e.g. xy12345,  xy12345.us-east-2.aws, xy12345.us-central1.gcp, xy12345.central-us.azure, xy12345.us-west-2.privatelink. Refer [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region) for more details.",
          "title": "Account Id",
          "type": "string"
        },
        "warehouse": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Snowflake warehouse.",
          "title": "Warehouse"
        },
        "role": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Snowflake role.",
          "title": "Role"
        },
        "connect_args": {
          "anyOf": [
            {
              "additionalProperties": true,
              "type": "object"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Connect args to pass to Snowflake SqlAlchemy driver",
          "title": "Connect Args"
        },
        "token": {
          "anyOf": [
            {
              "format": "password",
              "type": "string",
              "writeOnly": true
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "OAuth token from external identity provider. Not recommended for most use cases because it will not be able to refresh once expired.",
          "title": "Token"
        },
        "snowflake_domain": {
          "default": "snowflakecomputing.com",
          "description": "Snowflake domain. Use 'snowflakecomputing.com' for most regions or 'snowflakecomputing.cn' for China (cn-northwest-1) region.",
          "title": "Snowflake Domain",
          "type": "string"
        },
        "database": {
          "description": "The fivetran connector log database.",
          "title": "Database",
          "type": "string"
        },
        "log_schema": {
          "description": "The fivetran connector log schema.",
          "title": "Log Schema",
          "type": "string"
        }
      },
      "required": [
        "account_id",
        "database",
        "log_schema"
      ],
      "title": "SnowflakeDestinationConfig",
      "type": "object"
    },
    "StatefulStaleMetadataRemovalConfig": {
      "additionalProperties": false,
      "description": "Base specialized config for Stateful Ingestion with stale metadata removal capability.",
      "properties": {
        "enabled": {
          "default": false,
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "title": "Enabled",
          "type": "boolean"
        },
        "remove_stale_metadata": {
          "default": true,
          "description": "Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled.",
          "title": "Remove Stale Metadata",
          "type": "boolean"
        },
        "fail_safe_threshold": {
          "default": 75.0,
          "description": "Prevents large amount of soft deletes & the state from committing from accidental changes to the source configuration if the relative change percent in entities compared to the previous state is above the 'fail_safe_threshold'.",
          "maximum": 100.0,
          "minimum": 0.0,
          "title": "Fail Safe Threshold",
          "type": "number"
        }
      },
      "title": "StatefulStaleMetadataRemovalConfig",
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "env": {
      "default": "PROD",
      "description": "The environment that all assets produced by this connector belong to",
      "title": "Env",
      "type": "string"
    },
    "platform_instance": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details.",
      "title": "Platform Instance"
    },
    "stateful_ingestion": {
      "anyOf": [
        {
          "$ref": "#/$defs/StatefulStaleMetadataRemovalConfig"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Fivetran Stateful Ingestion Config."
    },
    "fivetran_log_config": {
      "$ref": "#/$defs/FivetranLogConfig",
      "description": "Fivetran log connector destination server configurations."
    },
    "connector_patterns": {
      "$ref": "#/$defs/AllowDenyPattern",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "description": "Filtering regex patterns for connector names."
    },
    "destination_patterns": {
      "$ref": "#/$defs/AllowDenyPattern",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "description": "Regex patterns for destination ids to filter in ingestion. Fivetran destination IDs are usually two word identifiers e.g. canyon_tolerable, and are not the same as the destination database name. They're visible in the Fivetran UI under Destinations -> Overview -> Destination Group ID."
    },
    "include_column_lineage": {
      "default": true,
      "description": "Populates table->table column lineage.",
      "title": "Include Column Lineage",
      "type": "boolean"
    },
    "sources_to_platform_instance": {
      "additionalProperties": {
        "$ref": "#/$defs/PlatformDetail"
      },
      "default": {},
      "description": "A mapping from connector id to its platform/instance/env/database details.",
      "title": "Sources To Platform Instance",
      "type": "object"
    },
    "destination_to_platform_instance": {
      "additionalProperties": {
        "$ref": "#/$defs/PlatformDetail"
      },
      "default": {},
      "description": "A mapping of destination id to its platform/instance/env details.",
      "title": "Destination To Platform Instance",
      "type": "object"
    },
    "api_config": {
      "anyOf": [
        {
          "$ref": "#/$defs/FivetranAPIConfig"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Fivetran REST API configuration, used to provide wider support for connections."
    },
    "history_sync_lookback_period": {
      "default": 7,
      "description": "The number of days to look back when extracting connectors' sync history.",
      "title": "History Sync Lookback Period",
      "type": "integer"
    }
  },
  "required": [
    "fivetran_log_config"
  ],
  "title": "FivetranSourceConfig",
  "type": "object"
}
```


</TabItem>
</Tabs>

### Capabilities

Use the **Important Capabilities** table above as the source of truth for supported features and whether additional configuration is required.

#### Database and Schema Name Handling

The Fivetran source uses **quoted identifiers** for database and schema names to properly handle special characters and case-sensitive names. This follows Snowflake's quoted identifier convention, which is then transpiled to the target database dialect (Snowflake, BigQuery, or Databricks).

**Important Notes:**

- **Database names** are automatically wrapped in double quotes (e.g., `use database "my-database"`)
- **Schema names** are automatically wrapped in double quotes (e.g., `"my-schema".table_name`)
- This ensures proper handling of database and schema names containing:
  - Hyphens (e.g., `my-database`)
  - Spaces (e.g., `my database`)
  - Special characters (e.g., `my.database`)
  - Case-sensitive names (e.g., `MyDatabase`)

**Migration Impact:**

- If you have database or schema names with special characters, they will now be properly quoted in SQL queries
- This change ensures consistent behavior across all supported destination platforms
- No configuration changes are required - the quoting is handled automatically

**Case Sensitivity Considerations:**

- **Important**: In Snowflake, unquoted identifiers are automatically converted to uppercase when stored and resolved (e.g., `mydatabase` becomes `MYDATABASE`), while double-quoted identifiers preserve the exact case as entered (e.g., `"mydatabase"` stays as `mydatabase`). See [Snowflake's identifier documentation](https://docs.snowflake.com/en/sql-reference/identifiers-syntax#double-quoted-identifiers) for details.
- **Backward Compatibility**: The system automatically handles backward compatibility for valid unquoted identifiers (identifiers containing only letters, numbers, and underscores). These identifiers are automatically uppercased before quoting to match Snowflake's behavior for unquoted identifiers. This means:
  - If your database/schema name is a valid unquoted identifier (e.g., `fivetran_logs`, `MY_SCHEMA`), it will be automatically uppercased to match existing Snowflake objects created without quotes
  - No configuration changes are required for standard identifiers (letters, numbers, underscores only)
- **Recommended**: For best practices and to ensure consistency, maintain the exact case of your database and schema names in your configuration to match what's stored in Snowflake

#### Snowflake destination Configuration Guide

1. If your fivetran platform connector destination is snowflake, you need to provide user details and its role with correct privileges in order to fetch metadata.
2. Snowflake system admin can follow this guide to create a fivetran_datahub role, assign it the required privileges, and assign it to a user by executing the following Snowflake commands from a user with the ACCOUNTADMIN role or MANAGE GRANTS privilege.

```sql
create or replace role fivetran_datahub;

// Grant access to a warehouse to run queries to view metadata
grant operate, usage on warehouse "<your-warehouse>" to role fivetran_datahub;

// Grant access to view database and schema in which your log and metadata tables exist
// Note: Database and schema names are automatically quoted, so use quoted identifiers if your names contain special characters
grant usage on DATABASE "<fivetran-log-database>" to role fivetran_datahub;
grant usage on SCHEMA "<fivetran-log-database>"."<fivetran-log-schema>" to role fivetran_datahub;

// Grant access to execute select query on schema in which your log and metadata tables exist
grant select on all tables in SCHEMA "<fivetran-log-database>"."<fivetran-log-schema>" to role fivetran_datahub;

// Grant the fivetran_datahub to the snowflake user.
grant role fivetran_datahub to user snowflake_user;
```

#### Bigquery destination Configuration Guide

1. If your fivetran platform connector destination is bigquery, you need to setup a ServiceAccount as per [BigQuery docs](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console) and select BigQuery Data Viewer and BigQuery Job User IAM roles.
2. Create and Download a service account JSON keyfile and provide bigquery connection credential in bigquery destination config.

#### Databricks destination Configuration Guide

1. Get your Databricks instance's [workspace url](https://docs.databricks.com/workspace/workspace-details.html#workspace-instance-names-urls-and-ids)
2. Create a [Databricks Service Principal](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#what-is-a-service-principal)
   1. You can skip this step and use your own account to get things running quickly, but we strongly recommend creating a dedicated service principal for production use.
3. Generate a Databricks Personal Access token following the following guides:
   1. [Service Principals](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#personal-access-tokens)
   2. [Personal Access Tokens](https://docs.databricks.com/dev-tools/auth.html#databricks-personal-access-tokens)
4. Provision your service account, to ingest your workspace's metadata and lineage, your service principal must have all of the following:
   1. One of: metastore admin role, ownership of, or `USE CATALOG` privilege on any catalogs you want to ingest
   2. One of: metastore admin role, ownership of, or `USE SCHEMA` privilege on any schemas you want to ingest
   3. Ownership of or `SELECT` privilege on any tables and views you want to ingest
   4. [Ownership documentation](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/ownership.html)
   5. [Privileges documentation](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/privileges.html)
5. Check the starter recipe below and replace `workspace_url` and `token` with your information from the previous steps.

#### Working with Platform Instances

If you have multiple instances of source/destination systems that are referred in your `fivetran` setup, you'd need to configure platform instance for these systems in `fivetran` recipe to generate correct lineage edges. Refer the document [Working with Platform Instances](/docs/platform-instances) to understand more about this.

While configuring the platform instance for source system you need to provide connector id as key and for destination system provide destination id as key.
When creating the connection details in the fivetran UI make a note of the destination Group ID of the service account, as that will need to be used in the `destination_to_platform_instance` configuration.
I.e:

<p align="center">
  <img width="70%"  src="https://github.com/datahub-project/static-assets/raw/main/imgs/integrations/bigquery/bq-connection-id.png"/>
</p>

In this case the configuration would be something like:

```yaml
destination_to_platform_instance:
  greyish_positive: <--- this comes from bigquery destination - see screenshot
    database: <big query project ID>
    env: PROD
```

##### Example - Multiple Postgres Source Connectors each reading from different postgres instance

```yml
# Map of connector source to platform instance
sources_to_platform_instance:
  postgres_connector_id1:
    platform_instance: cloud_postgres_instance
    env: PROD

  postgres_connector_id2:
    platform_instance: local_postgres_instance
    env: DEV
```

##### Example - Multiple Snowflake Destinations each writing to different snowflake instance

```yml
# Map of destination to platform instance
destination_to_platform_instance:
  snowflake_destination_id1:
    platform_instance: prod_snowflake_instance
    env: PROD

  snowflake_destination_id2:
    platform_instance: dev_snowflake_instance
    env: PROD
```

### Limitations

Module behavior is constrained by source APIs, permissions, and metadata exposed by the platform. Refer to capability notes for unsupported or conditional features.

#### Supported Destinations

Works only for:

- Snowflake destination
- Bigquery destination
- Databricks destination

#### Ingestion Limits

To prevent excessive data ingestion, the following configurable limits apply per connector:

- **Sync History**: Maximum of 500 sync runs per connector (default: 500, configurable via `fivetran_log_config.max_jobs_per_connector`)
- **Table Lineage**: Maximum of 120 table lineage entries per connector (default: 120, configurable via `fivetran_log_config.max_table_lineage_per_connector`)
- **Column Lineage**: Maximum of 1000 column lineage entries per connector (default: 1000, configurable via `fivetran_log_config.max_column_lineage_per_connector`)

When these limits are exceeded, only the most recent entries are ingested. Warnings will be logged during ingestion to notify you when truncation occurs.

These limits act as safety nets to prevent excessive data ingestion. You can increase them cautiously if you need to ingest more historical data or have connectors with many tables/columns. Example configuration:

```yaml
source:
  type: fivetran
  config:
    fivetran_log_config:
      # ... other config ...
      max_jobs_per_connector: 1000 # Increase sync history limit
      max_table_lineage_per_connector: 500 # Increase table lineage limit
      max_column_lineage_per_connector: 5000 # Increase column lineage limit
```

### Troubleshooting

If ingestion fails, validate credentials, permissions, connectivity, and scope filters first. Then review ingestion logs for source-specific errors and adjust configuration accordingly.


### Code Coordinates
- Class Name: `datahub.ingestion.source.fivetran.fivetran.FivetranSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/fivetran/fivetran.py)


:::tip Questions?

If you've got any questions on configuring ingestion for Fivetran, feel free to ping us on [our Slack](https://datahub.com/slack).
:::



:::note 💡 **Contributing to this documentation**
This page is auto-generated from the underlying source code. To make changes, please edit the relevant source files in the [metadata-ingestion](https://github.com/datahub-project/datahub/tree/master/metadata-ingestion) directory. 

**Tip:** For quick typo fixes or documentation updates, you can click the ✏️ **Edit** icon directly in the GitHub UI to open a Pull Request. For larger changes and PR naming conventions, please refer to our [Contributing Guide](/docs/contributing).
:::
