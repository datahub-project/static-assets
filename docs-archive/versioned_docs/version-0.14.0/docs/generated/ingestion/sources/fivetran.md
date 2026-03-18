---
sidebar_position: 20
title: Fivetran
slug: /generated/ingestion/sources/fivetran
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/fivetran.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fivetran
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Column-level Lineage | ✅ | Enabled by default, can be disabled via configuration `include_column_lineage` |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default |


This plugin extracts fivetran users, connectors, destinations and sync history.
This plugin is in beta and has only been tested on Snowflake connector.

## Integration Details

This source extracts the following:

- Connectors in fivetran as Data Pipelines and Data Jobs to represent data lineage information between source and destination.
- Connector sources - DataJob input Datasets.
- Connector destination - DataJob output Datasets.
- Connector runs - DataProcessInstances as DataJob runs.

## Configuration Notes

1. Fivetran supports the fivetran platform connector to dump the log events and connectors, destinations, users and roles metadata in your destination.
2. You need to setup and start the initial sync of the fivetran platform connector before using this source. Refer [link](https://fivetran.com/docs/logs/fivetran-platform/setup-guide).
3. Once initial sync up of your fivetran platform connector is done, you need to provide the fivetran platform connector's destination platform and its configuration in the recipe.

## Concept mapping 

| Fivetran		   | Datahub												    |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| `Connector`              | [DataJob](/docs/generated/metamodel/entities/datajob/)       	            |
| `Source`                 | [Dataset](/docs/generated/metamodel/entities/dataset/)                        |
| `Destination`            | [Dataset](/docs/generated/metamodel/entities/dataset/)                        |
| `Connector Run`          | [DataProcessInstance](/docs/generated/metamodel/entities/dataprocessinstance) |

Source and destination are mapped to Dataset as an Input and Output of Connector.

## Current limitations

Works only for

- Snowflake destination
- Bigquery destination

## Snowflake destination Configuration Guide
1. If your fivetran platform connector destination is snowflake, you need to provide user details and its role with correct privileges in order to fetch metadata.
2. Snowflake system admin can follow this guide to create a fivetran_datahub role, assign it the required privileges, and assign it to a user by executing the following Snowflake commands from a user with the ACCOUNTADMIN role or MANAGE GRANTS privilege.

```sql
create or replace role fivetran_datahub;

// Grant access to a warehouse to run queries to view metadata
grant operate, usage on warehouse "<your-warehouse>" to role fivetran_datahub;

// Grant access to view database and schema in which your log and metadata tables exist
grant usage on DATABASE "<fivetran-log-database>" to role fivetran_datahub;
grant usage on SCHEMA "<fivetran-log-database>"."<fivetran-log-schema>" to role fivetran_datahub;

// Grant access to execute select query on schema in which your log and metadata tables exist
grant select on all tables in SCHEMA "<fivetran-log-database>"."<fivetran-log-schema>" to role fivetran_datahub;

// Grant the fivetran_datahub to the snowflake user.
grant role fivetran_datahub to user snowflake_user;
```

## Bigquery destination Configuration Guide
1. If your fivetran platform connector destination is bigquery, you need to setup a ServiceAccount as per [BigQuery docs](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console) and select BigQuery Data Viewer and BigQuery Job User IAM roles. 
2. Create and Download a service account JSON keyfile and provide bigquery connection credential in bigquery destination config.

## Advanced Configurations

### Working with Platform Instances
If you've multiple instances of source/destination systems that are referred in your `fivetran` setup, you'd need to configure platform instance for these systems in `fivetran` recipe to generate correct lineage edges. Refer the document [Working with Platform Instances](/docs/platform-instances) to understand more about this.

While configuration of platform instance for source system you need to provide connector id as key and for destination system provide destination id as key.

#### Example - Multiple Postgres Source Connectors each reading from different postgres instance
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

#### Example - Multiple Snowflake Destinations each writing to different snowflake instance
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




### CLI based Ingestion

#### Install the Plugin
The `fivetran` source works out of the box with `acryl-datahub`.

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

    # Optional - filter for certain connector names instead of ingesting everything.
    # connector_patterns:
    #   allow:
    #     - connector_name

    # Optional -- A mapping of the connector's all sources to its database.
    # sources_to_database:
    #   connector_id: source_db
    
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
| <div className="path-line"><span className="path-main">fivetran_log_config</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">FivetranLogConfig</span></div> | Fivetran log connector destination server configurations.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">destination_platform</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | One of: "snowflake", "bigquery" <div className="default-line default-line-with-docs">Default: <span className="default-value">snowflake</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">bigquery_destination_config</span></div> <div className="type-name-line"><span className="type-name">BigQueryDestinationConfig</span></div> | If destination platform is 'bigquery', provide bigquery configuration.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">dataset</span>&nbsp;<abbr title="Required if bigquery_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log dataset.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">extra_client_options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Additional options to pass to google.cloud.logging_v2.client.Client. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">project_on_behalf</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | [Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.</span><span className="path-main">credential</span></div> <div className="type-name-line"><span className="type-name">BigQueryCredential</span></div> | BigQuery credential informations  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_email</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client email  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client Id  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">private_key</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n'  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">private_key_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key id  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">project_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Project id to set the credentials  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">auth_provider_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Auth provider x509 certificate url <div className="default-line default-line-with-docs">Default: <span className="default-value">https://www.googleapis.com/oauth2/v1/certs</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">auth_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://accounts.google.com/o/oauth2/auth</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">client_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">token_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Token uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://oauth2.googleapis.com/token</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.bigquery_destination_config.credential.</span><span className="path-main">type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication type <div className="default-line default-line-with-docs">Default: <span className="default-value">service&#95;account</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.</span><span className="path-main">snowflake_destination_config</span></div> <div className="type-name-line"><span className="type-name">SnowflakeDestinationConfig</span></div> | If destination platform is 'snowflake', provide snowflake configuration.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">account_id</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake account identifier. e.g. xy12345,  xy12345.us-east-2.aws, xy12345.us-central1.gcp, xy12345.central-us.azure, xy12345.us-west-2.privatelink. Refer [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region) for more details.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">database</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log database.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">log_schema</span>&nbsp;<abbr title="Required if snowflake_destination_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The fivetran connector log schema.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">authentication_type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The type of authenticator to use when connecting to Snowflake. Supports "DEFAULT_AUTHENTICATOR", "OAUTH_AUTHENTICATOR", "EXTERNAL_BROWSER_AUTHENTICATOR" and "KEY_PAIR_AUTHENTICATOR". <div className="default-line default-line-with-docs">Default: <span className="default-value">DEFAULT&#95;AUTHENTICATOR</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">connect_args</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Connect args to pass to Snowflake SqlAlchemy driver  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">options</span></div> <div className="type-name-line"><span className="type-name">object</span></div> | Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Snowflake password.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n' if using key pair authentication. Encrypted version of private key will be in a form of '-----BEGIN ENCRYPTED PRIVATE KEY-----\nencrypted-private-key\n-----END ENCRYPTED PRIVATE KEY-----\n' See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key_password</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Password for your private key. Required if using key pair authentication with encrypted private key.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">private_key_path</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The path to the private key if using key pair authentication. Ignored if `private_key` is set. See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">role</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake role.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">scheme</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value">snowflake</span></div> |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">username</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake username.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">warehouse</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Snowflake warehouse.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.</span><span className="path-main">oauth_config</span></div> <div className="type-name-line"><span className="type-name">OAuthConfiguration</span></div> | oauth configuration - https://docs.snowflake.com/en/user-guide/python-connector-example.html#connecting-with-oauth  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">authority_url</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authority url of your identity provider  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | client id of your registered application  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">provider</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Identity provider for oauth.Supported providers are microsoft and okta.  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">scopes</span>&nbsp;<abbr title="Required if oauth_config is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">array</span></div> | scopes required to connect to snowflake  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.scopes.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">client_secret</span></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | client secret of the application if use_certificate = false  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">encoded_oauth_private_key</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | base64 encoded private key content if use_certificate = true  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">encoded_oauth_public_key</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | base64 encoded certificate content if use_certificate = true  |
| <div className="path-line"><span className="path-prefix">fivetran_log_config.snowflake_destination_config.oauth_config.</span><span className="path-main">use_certificate</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Do you want to use certificate and private key to authenticate using oauth <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">history_sync_lookback_period</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | The number of days to look back when extracting connectors' sync history. <div className="default-line default-line-with-docs">Default: <span className="default-value">7</span></div> |
| <div className="path-line"><span className="path-main">include_column_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Populates table->table column lineage. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">sources_to_database</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">connector_patterns</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | Regex patterns for connectors to filter in ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to include in ingestion <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;.&#42;&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.allow.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">connector_patterns.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of regex patterns to exclude from ingestion. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">connector_patterns.deny.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">destination_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> |   |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-prefix">destination_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by DataHub platform ingestion source belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">sources_to_platform_instance</span></div> <div className="type-name-line"><span className="type-name">map(str,PlatformDetail)</span></div> |   |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-prefix">sources_to_platform_instance.`key`.</span><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by DataHub platform ingestion source belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Airbyte Stateful Ingestion Config.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "FivetranSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to",
      "type": "string"
    },
    "stateful_ingestion": {
      "title": "Stateful Ingestion",
      "description": "Airbyte Stateful Ingestion Config.",
      "allOf": [
        {
          "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
        }
      ]
    },
    "fivetran_log_config": {
      "title": "Fivetran Log Config",
      "description": "Fivetran log connector destination server configurations.",
      "allOf": [
        {
          "$ref": "#/definitions/FivetranLogConfig"
        }
      ]
    },
    "connector_patterns": {
      "title": "Connector Patterns",
      "description": "Regex patterns for connectors to filter in ingestion.",
      "default": {
        "allow": [
          ".*"
        ],
        "deny": [],
        "ignoreCase": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/AllowDenyPattern"
        }
      ]
    },
    "include_column_lineage": {
      "title": "Include Column Lineage",
      "description": "Populates table->table column lineage.",
      "default": true,
      "type": "boolean"
    },
    "sources_to_database": {
      "title": "Sources To Database",
      "description": "A mapping of the connector's all sources to its database. Use connector id as key.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "sources_to_platform_instance": {
      "title": "Sources To Platform Instance",
      "description": "A mapping of the connector's all sources dataset to platform instance. Use connector id as key.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/PlatformDetail"
      }
    },
    "destination_to_platform_instance": {
      "title": "Destination To Platform Instance",
      "description": "A mapping of destination dataset to platform instance. Use destination id as key.",
      "default": {},
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/PlatformDetail"
      }
    },
    "history_sync_lookback_period": {
      "title": "History Sync Lookback Period",
      "description": "The number of days to look back when extracting connectors' sync history.",
      "default": 7,
      "type": "integer"
    }
  },
  "required": [
    "fivetran_log_config"
  ],
  "additionalProperties": false,
  "definitions": {
    "DynamicTypedStateProviderConfig": {
      "title": "DynamicTypedStateProviderConfig",
      "type": "object",
      "properties": {
        "type": {
          "title": "Type",
          "description": "The type of the state provider to use. For DataHub use `datahub`",
          "type": "string"
        },
        "config": {
          "title": "Config",
          "description": "The configuration required for initializing the state provider. Default: The datahub_api config if set at pipeline level. Otherwise, the default DatahubClientConfig. See the defaults (https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/graph/client.py#L19).",
          "default": {},
          "type": "object"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "StatefulStaleMetadataRemovalConfig": {
      "title": "StatefulStaleMetadataRemovalConfig",
      "description": "Base specialized config for Stateful Ingestion with stale metadata removal capability.",
      "type": "object",
      "properties": {
        "enabled": {
          "title": "Enabled",
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "default": false,
          "type": "boolean"
        },
        "remove_stale_metadata": {
          "title": "Remove Stale Metadata",
          "description": "Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled.",
          "default": true,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "OAuthIdentityProvider": {
      "title": "OAuthIdentityProvider",
      "description": "An enumeration.",
      "enum": [
        "microsoft",
        "okta"
      ]
    },
    "OAuthConfiguration": {
      "title": "OAuthConfiguration",
      "type": "object",
      "properties": {
        "provider": {
          "description": "Identity provider for oauth.Supported providers are microsoft and okta.",
          "allOf": [
            {
              "$ref": "#/definitions/OAuthIdentityProvider"
            }
          ]
        },
        "authority_url": {
          "title": "Authority Url",
          "description": "Authority url of your identity provider",
          "type": "string"
        },
        "client_id": {
          "title": "Client Id",
          "description": "client id of your registered application",
          "type": "string"
        },
        "scopes": {
          "title": "Scopes",
          "description": "scopes required to connect to snowflake",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "use_certificate": {
          "title": "Use Certificate",
          "description": "Do you want to use certificate and private key to authenticate using oauth",
          "default": false,
          "type": "boolean"
        },
        "client_secret": {
          "title": "Client Secret",
          "description": "client secret of the application if use_certificate = false",
          "type": "string",
          "writeOnly": true,
          "format": "password"
        },
        "encoded_oauth_public_key": {
          "title": "Encoded Oauth Public Key",
          "description": "base64 encoded certificate content if use_certificate = true",
          "type": "string"
        },
        "encoded_oauth_private_key": {
          "title": "Encoded Oauth Private Key",
          "description": "base64 encoded private key content if use_certificate = true",
          "type": "string"
        }
      },
      "required": [
        "provider",
        "authority_url",
        "client_id",
        "scopes"
      ],
      "additionalProperties": false
    },
    "SnowflakeDestinationConfig": {
      "title": "SnowflakeDestinationConfig",
      "type": "object",
      "properties": {
        "options": {
          "title": "Options",
          "description": "Any options specified here will be passed to [SQLAlchemy.create_engine](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine) as kwargs.",
          "type": "object"
        },
        "scheme": {
          "title": "Scheme",
          "default": "snowflake",
          "type": "string"
        },
        "username": {
          "title": "Username",
          "description": "Snowflake username.",
          "type": "string"
        },
        "password": {
          "title": "Password",
          "description": "Snowflake password.",
          "type": "string",
          "writeOnly": true,
          "format": "password"
        },
        "private_key": {
          "title": "Private Key",
          "description": "Private key in a form of '-----BEGIN PRIVATE KEY-----\\nprivate-key\\n-----END PRIVATE KEY-----\\n' if using key pair authentication. Encrypted version of private key will be in a form of '-----BEGIN ENCRYPTED PRIVATE KEY-----\\nencrypted-private-key\\n-----END ENCRYPTED PRIVATE KEY-----\\n' See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html",
          "type": "string"
        },
        "private_key_path": {
          "title": "Private Key Path",
          "description": "The path to the private key if using key pair authentication. Ignored if `private_key` is set. See: https://docs.snowflake.com/en/user-guide/key-pair-auth.html",
          "type": "string"
        },
        "private_key_password": {
          "title": "Private Key Password",
          "description": "Password for your private key. Required if using key pair authentication with encrypted private key.",
          "type": "string",
          "writeOnly": true,
          "format": "password"
        },
        "oauth_config": {
          "title": "Oauth Config",
          "description": "oauth configuration - https://docs.snowflake.com/en/user-guide/python-connector-example.html#connecting-with-oauth",
          "allOf": [
            {
              "$ref": "#/definitions/OAuthConfiguration"
            }
          ]
        },
        "authentication_type": {
          "title": "Authentication Type",
          "description": "The type of authenticator to use when connecting to Snowflake. Supports \"DEFAULT_AUTHENTICATOR\", \"OAUTH_AUTHENTICATOR\", \"EXTERNAL_BROWSER_AUTHENTICATOR\" and \"KEY_PAIR_AUTHENTICATOR\".",
          "default": "DEFAULT_AUTHENTICATOR",
          "type": "string"
        },
        "account_id": {
          "title": "Account Id",
          "description": "Snowflake account identifier. e.g. xy12345,  xy12345.us-east-2.aws, xy12345.us-central1.gcp, xy12345.central-us.azure, xy12345.us-west-2.privatelink. Refer [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#format-2-legacy-account-locator-in-a-region) for more details.",
          "type": "string"
        },
        "warehouse": {
          "title": "Warehouse",
          "description": "Snowflake warehouse.",
          "type": "string"
        },
        "role": {
          "title": "Role",
          "description": "Snowflake role.",
          "type": "string"
        },
        "connect_args": {
          "title": "Connect Args",
          "description": "Connect args to pass to Snowflake SqlAlchemy driver",
          "type": "object"
        },
        "database": {
          "title": "Database",
          "description": "The fivetran connector log database.",
          "type": "string"
        },
        "log_schema": {
          "title": "Log Schema",
          "description": "The fivetran connector log schema.",
          "type": "string"
        }
      },
      "required": [
        "account_id",
        "database",
        "log_schema"
      ],
      "additionalProperties": false
    },
    "BigQueryCredential": {
      "title": "BigQueryCredential",
      "type": "object",
      "properties": {
        "project_id": {
          "title": "Project Id",
          "description": "Project id to set the credentials",
          "type": "string"
        },
        "private_key_id": {
          "title": "Private Key Id",
          "description": "Private key id",
          "type": "string"
        },
        "private_key": {
          "title": "Private Key",
          "description": "Private key in a form of '-----BEGIN PRIVATE KEY-----\\nprivate-key\\n-----END PRIVATE KEY-----\\n'",
          "type": "string"
        },
        "client_email": {
          "title": "Client Email",
          "description": "Client email",
          "type": "string"
        },
        "client_id": {
          "title": "Client Id",
          "description": "Client Id",
          "type": "string"
        },
        "auth_uri": {
          "title": "Auth Uri",
          "description": "Authentication uri",
          "default": "https://accounts.google.com/o/oauth2/auth",
          "type": "string"
        },
        "token_uri": {
          "title": "Token Uri",
          "description": "Token uri",
          "default": "https://oauth2.googleapis.com/token",
          "type": "string"
        },
        "auth_provider_x509_cert_url": {
          "title": "Auth Provider X509 Cert Url",
          "description": "Auth provider x509 certificate url",
          "default": "https://www.googleapis.com/oauth2/v1/certs",
          "type": "string"
        },
        "type": {
          "title": "Type",
          "description": "Authentication type",
          "default": "service_account",
          "type": "string"
        },
        "client_x509_cert_url": {
          "title": "Client X509 Cert Url",
          "description": "If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email",
          "type": "string"
        }
      },
      "required": [
        "project_id",
        "private_key_id",
        "private_key",
        "client_email",
        "client_id"
      ],
      "additionalProperties": false
    },
    "BigQueryDestinationConfig": {
      "title": "BigQueryDestinationConfig",
      "type": "object",
      "properties": {
        "credential": {
          "title": "Credential",
          "description": "BigQuery credential informations",
          "allOf": [
            {
              "$ref": "#/definitions/BigQueryCredential"
            }
          ]
        },
        "extra_client_options": {
          "title": "Extra Client Options",
          "description": "Additional options to pass to google.cloud.logging_v2.client.Client.",
          "default": {},
          "type": "object"
        },
        "project_on_behalf": {
          "title": "Project On Behalf",
          "description": "[Advanced] The BigQuery project in which queries are executed. Will be passed when creating a job. If not passed, falls back to the project associated with the service account.",
          "type": "string"
        },
        "dataset": {
          "title": "Dataset",
          "description": "The fivetran connector log dataset.",
          "type": "string"
        }
      },
      "required": [
        "dataset"
      ],
      "additionalProperties": false
    },
    "FivetranLogConfig": {
      "title": "FivetranLogConfig",
      "type": "object",
      "properties": {
        "destination_platform": {
          "title": "Destination Platform",
          "description": "The destination platform where fivetran connector log tables are dumped.",
          "default": "snowflake",
          "enum": [
            "snowflake",
            "bigquery"
          ],
          "type": "string"
        },
        "snowflake_destination_config": {
          "title": "Snowflake Destination Config",
          "description": "If destination platform is 'snowflake', provide snowflake configuration.",
          "allOf": [
            {
              "$ref": "#/definitions/SnowflakeDestinationConfig"
            }
          ]
        },
        "bigquery_destination_config": {
          "title": "Bigquery Destination Config",
          "description": "If destination platform is 'bigquery', provide bigquery configuration.",
          "allOf": [
            {
              "$ref": "#/definitions/BigQueryDestinationConfig"
            }
          ]
        }
      },
      "additionalProperties": false
    },
    "AllowDenyPattern": {
      "title": "AllowDenyPattern",
      "description": "A class to store allow deny regexes",
      "type": "object",
      "properties": {
        "allow": {
          "title": "Allow",
          "description": "List of regex patterns to include in ingestion",
          "default": [
            ".*"
          ],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "deny": {
          "title": "Deny",
          "description": "List of regex patterns to exclude from ingestion.",
          "default": [],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "ignoreCase": {
          "title": "Ignorecase",
          "description": "Whether to ignore case sensitivity during pattern matching.",
          "default": true,
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "PlatformDetail": {
      "title": "PlatformDetail",
      "type": "object",
      "properties": {
        "platform_instance": {
          "title": "Platform Instance",
          "description": "The instance of the platform that all assets produced by this recipe belong to",
          "type": "string"
        },
        "env": {
          "title": "Env",
          "description": "The environment that all assets produced by DataHub platform ingestion source belong to",
          "default": "PROD",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.fivetran.fivetran.FivetranSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/fivetran/fivetran.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Fivetran, feel free to ping us on [our Slack](https://slack.datahubproject.io).
