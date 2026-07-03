---
sidebar_position: 19
title: Dataplex
slug: /generated/ingestion/sources/dataplex
custom_edit_url: null
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dataplex

## Overview

Dataplex is a DataHub utility or metadata-focused integration. Learn more in the [official Dataplex documentation](https://cloud.google.com/dataplex).

The DataHub integration for Dataplex covers metadata entities and operational objects relevant to this connector. Depending on module capabilities, it can also capture features such as lineage, usage, profiling, ownership, tags, and stateful deletion detection.

## Concept Mapping

| Dataplex Concept          | DataHub Concept                                                                     | Notes                                                                        |
| :------------------------ | :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| Entry (Universal Catalog) | [`Dataset`](/docs/generated/metamodel/entities/dataset)     | From Universal Catalog. Uses source platform URNs (e.g., `bigquery`, `gcs`). |
| BigQuery Project/Dataset  | [`Container`](/docs/generated/metamodel/entities/container) | Created as containers to align with native BigQuery connector.               |


## Module `dataplex`
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default. |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default via stateful ingestion. |
| Schema Metadata | ✅ | Enabled by default, can be disabled via configuration `include_schema`. |
| Table-Level Lineage | ✅ | Optionally enabled via configuration `include_lineage`. |
| Test Connection | ✅ | Enabled by default. |

### Overview

The `dataplex` module ingests metadata from Dataplex into DataHub. It is intended for production ingestion workflows and module-specific capabilities are documented below.

The Dataplex connector extracts metadata from Google Dataplex using the **Universal Catalog Entries API**. This API extracts entries from system-managed entry groups for Google Cloud services and is the recommended approach for discovering resources across your GCP organization.

#### Supported services

- **BigQuery**: datasets, tables, models, routines, connections, and linked datasets
- **Cloud SQL**: instances
- **AlloyDB**: instances, databases, schemas, tables, and views
- **Spanner**: instances, databases, and tables
- **Pub/Sub**: topics and subscriptions
- **Cloud Storage**: buckets
- **Bigtable**: instances, clusters, and tables
- **Vertex AI**: models, datasets, and feature stores
- **Dataform**: repositories and workflows
- **Dataproc Metastore**: services and databases

:::note
Only **BigQuery** and **Cloud Storage (GCS)** have been thoroughly tested with this connector. Other services may work but have not been validated.
:::

### Prerequisites

Refer to [Dataplex documentation](https://cloud.google.com/dataplex/docs) for Dataplex basics.

#### Authentication

Supports Application Default Credentials (ADC). See [GCP documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc) for ADC setup.

For service account authentication, follow these instructions:

#### Create a service account and assign roles

1. Create a service account following [GCP docs](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console) and assign the required roles

2. Download the service account JSON keyfile

   Example credential file:

   ```json
   {
     "type": "service_account",
     "project_id": "project-id-1234567",
     "private_key_id": "d0121d0000882411234e11166c6aaa23ed5d74e0",
     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIyourkey\n-----END PRIVATE KEY-----",
     "client_email": "test@suppproject-id-1234567.iam.gserviceaccount.com",
     "client_id": "113545814931671546333",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test%suppproject-id-1234567.iam.gserviceaccount.com"
   }
   ```

3. To provide credentials to the source, you can either:

   Set an environment variable:

   ```sh
   $ export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
   ```

   _or_

   Set credential config in your source based on the credential json file. For example:

   ```yml
   credential:
     project_id: "project-id-1234567"
     private_key_id: "d0121d0000882411234e11166c6aaa23ed5d74e0"
     private_key: "-----BEGIN PRIVATE KEY-----\nMIIyourkey\n-----END PRIVATE KEY-----\n"
     client_email: "test@suppproject-id-1234567.iam.gserviceaccount.com"
     client_id: "123456678890"
   ```

#### Permissions

Grant the following permissions to the service account on all target projects.

**Universal Catalog Entries API:**

**Default GCP Role:** [roles/dataplex.catalogViewer](https://cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)

| Permission                  | Description                           |
| --------------------------- | ------------------------------------- |
| `dataplex.entryGroups.get`  | Retrieve specific entry group details |
| `dataplex.entryGroups.list` | View all entry groups in a location   |
| `dataplex.entries.get`      | Access entry metadata and details     |
| `dataplex.entries.getData`  | View data aspects within entries      |
| `dataplex.entries.list`     | Enumerate entries within groups       |

**Lineage extraction** (optional, `include_lineage: true`):

**Default GCP Role:** [roles/datalineage.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer)

| Permission                 | Description                               |
| -------------------------- | ----------------------------------------- |
| `datalineage.links.get`    | Allows a user to view lineage links       |
| `datalineage.links.search` | Allows a user to search for lineage links |


### Install the Plugin
```shell
pip install 'acryl-datahub[dataplex]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: dataplex
  config:
    # Required: GCP project ID(s) where Dataplex resources are located
    project_ids:
      - "my-gcp-project"

    # Optional: GCP location for entries (Universal Catalog)
    # Use multi-region locations (us, eu, asia) to access system entry groups like @bigquery
    # Default: "us"
    entries_location: "us"

    # Optional: Environment (default: PROD)
    env: "PROD"

    # Optional: GCP credentials (if not using Application Default Credentials)
    # credential:
    #   project_id: "my-gcp-project"
    #   private_key_id: "d0121d0000882411234e11166c6aaa23ed5d74e0"
    #   private_key: "-----BEGIN PRIVATE KEY-----\nMIIyourkey\n-----END PRIVATE KEY-----\n"
    #   client_email: "test@suppproject-id-1234567.iam.gserviceaccount.com"
    #   client_id: "123456678890"

    # Optional: Metadata extraction
    # include_lineage: true   # Extract lineage (default: true)
    # include_schema: true    # Extract schema metadata (default: true)

    # Optional: Lineage retry settings
    # lineage_max_retries: 3                    # Max retry attempts (range: 1-10, default: 3)
    # lineage_retry_backoff_multiplier: 1.0     # Backoff delay multiplier (range: 0.1-10.0, default: 1.0)

    # Optional: Filtering patterns for entries
    # filter_config:
    #   entries:
    #     dataset_pattern:
    #       allow:
    #         - "bq_.*"      # Allow BigQuery entries
    #         - "pubsub_.*"  # Allow Pub/Sub entries
    #       deny:
    #         - ".*_test"    # Deny test entries
    #         - ".*_temp"    # Deny temporary entries

    # Optional: Performance tuning
    # batch_size: 1000 # Entries per batch for memory optimization (default: 1000)

sink:
  type: datahub-rest
  config:
    server: "http://localhost:8080"

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">batch_size</span></div> <div className="type-name-line"><span className="type-name">One of integer, null</span></div> | Batch size for metadata emission and lineage extraction. Entries are emitted in batches to prevent memory issues in large deployments. Lower values reduce memory usage but may increase processing time. Set to None to disable batching (process all entries at once). Recommended: 1000 for large deployments (>10k entries), None for small deployments (<1k entries). Default: 1000. <div className="default-line default-line-with-docs">Default: <span className="default-value">1000</span></div> |
| <div className="path-line"><span className="path-main">dataplex_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Base URL for Dataplex console (for generating external links). <div className="default-line default-line-with-docs">Default: <span className="default-value">https://console.cloud.google.com/dataplex</span></div> |
| <div className="path-line"><span className="path-main">enable_stateful_lineage_ingestion</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable stateful lineage ingestion. This will store lineage window timestamps after successful lineage ingestion. and will not run lineage ingestion for same timestamps in subsequent run. NOTE: This only works with use_queries_v2=False (legacy extraction path). For queries v2, use enable_stateful_time_window instead. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">entries_location</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | GCP location for Universal Catalog entries extraction. Must be a multi-region location (us, eu, asia) to access system-managed entry groups like @bigquery. Regional locations (us-central1, etc.) only contain placeholder entries and will miss BigQuery tables. Default: 'us' (recommended for most users). <div className="default-line default-line-with-docs">Default: <span className="default-value">us</span></div> |
| <div className="path-line"><span className="path-main">include_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract lineage information using Dataplex Lineage API. Extracts table-level lineage relationships between entries. Lineage API calls automatically retry transient errors (timeouts, rate limits) with exponential backoff. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">include_schema</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to extract and ingest schema metadata (columns, types, descriptions). Set to False to skip schema extraction for faster ingestion when only basic dataset metadata is needed. Disabling schema extraction can improve performance for large deployments. Default: True. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">lineage_max_retries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of retry attempts for lineage API calls when encountering transient errors (timeouts, rate limits, service unavailable). Each attempt uses exponential backoff. Higher values increase resilience but may slow down ingestion. Default: 3. <div className="default-line default-line-with-docs">Default: <span className="default-value">3</span></div> |
| <div className="path-line"><span className="path-main">lineage_retry_backoff_multiplier</span></div> <div className="type-name-line"><span className="type-name">number</span></div> | Multiplier for exponential backoff between lineage API retry attempts (in seconds). Wait time formula: multiplier * (2 ^ attempt_number), capped between 2-10 seconds. Higher values reduce API load but increase ingestion time. Default: 1.0. <div className="default-line default-line-with-docs">Default: <span className="default-value">1.0</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://docs.datahub.com/docs/platform-instances/ for more details. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">credential</span></div> <div className="type-name-line"><span className="type-name">One of GCPCredential, null</span></div> | GCP credential information. If not specified, uses Application Default Credentials. <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_email</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client email  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Client Id  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">private_key</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Private key in a form of '-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n'  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">private_key_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Private key id  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">auth_provider_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Auth provider x509 certificate url <div className="default-line default-line-with-docs">Default: <span className="default-value">https://www.googleapis.com/oauth2/v1/certs</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">auth_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://accounts.google.com/o/oauth2/auth</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">client_x509_cert_url</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | If not set it will be default to https://www.googleapis.com/robot/v1/metadata/x509/client_email <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">project_id</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> | Project id to set the credentials <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">token_uri</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Token uri <div className="default-line default-line-with-docs">Default: <span className="default-value">https://oauth2.googleapis.com/token</span></div> |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">type</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Authentication type <div className="default-line default-line-with-docs">Default: <span className="default-value">service&#95;account</span></div> |
| <div className="path-line"><span className="path-main">filter_config</span></div> <div className="type-name-line"><span className="type-name">DataplexFilterConfig</span></div> | Filter configuration for Dataplex ingestion.  |
| <div className="path-line"><span className="path-prefix">filter_config.</span><span className="path-main">entries</span></div> <div className="type-name-line"><span className="type-name">EntriesFilterConfig</span></div> | Filter configuration specific to Dataplex Entries API (Universal Catalog).  |
| <div className="path-line"><span className="path-prefix">filter_config.entries.</span><span className="path-main">dataset_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | A class to store allow deny regexes  |
| <div className="path-line"><span className="path-prefix">filter_config.entries.dataset_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">One of boolean, null</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">project_ids</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of Google Cloud Project IDs to ingest Dataplex resources from. If not specified, uses project_id or attempts to detect from credentials.  |
| <div className="path-line"><span className="path-prefix">project_ids.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">One of StatefulIngestionConfig, null</span></div> | Stateful Ingestion Config <div className="default-line default-line-with-docs">Default: <span className="default-value">None</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

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
    "DataplexFilterConfig": {
      "additionalProperties": false,
      "description": "Filter configuration for Dataplex ingestion.",
      "properties": {
        "entries": {
          "$ref": "#/$defs/EntriesFilterConfig",
          "description": "Filters specific to Dataplex Entries API (Universal Catalog)."
        }
      },
      "title": "DataplexFilterConfig",
      "type": "object"
    },
    "EntriesFilterConfig": {
      "additionalProperties": false,
      "description": "Filter configuration specific to Dataplex Entries API (Universal Catalog).",
      "properties": {
        "dataset_pattern": {
          "$ref": "#/$defs/AllowDenyPattern",
          "default": {
            "allow": [
              ".*"
            ],
            "deny": [],
            "ignoreCase": true
          },
          "description": "Regex patterns for entry IDs to filter in ingestion."
        }
      },
      "title": "EntriesFilterConfig",
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
    "StatefulIngestionConfig": {
      "additionalProperties": false,
      "description": "Basic Stateful Ingestion Specific Configuration for any source.",
      "properties": {
        "enabled": {
          "default": false,
          "description": "Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False",
          "title": "Enabled",
          "type": "boolean"
        }
      },
      "title": "StatefulIngestionConfig",
      "type": "object"
    }
  },
  "additionalProperties": false,
  "description": "Configuration for Google Dataplex source.",
  "properties": {
    "enable_stateful_lineage_ingestion": {
      "default": true,
      "description": "Enable stateful lineage ingestion. This will store lineage window timestamps after successful lineage ingestion. and will not run lineage ingestion for same timestamps in subsequent run. NOTE: This only works with use_queries_v2=False (legacy extraction path). For queries v2, use enable_stateful_time_window instead.",
      "title": "Enable Stateful Lineage Ingestion",
      "type": "boolean"
    },
    "stateful_ingestion": {
      "anyOf": [
        {
          "$ref": "#/$defs/StatefulIngestionConfig"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Stateful Ingestion Config"
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
    "env": {
      "default": "PROD",
      "description": "The environment that all assets produced by this connector belong to",
      "title": "Env",
      "type": "string"
    },
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
      "description": "GCP credential information. If not specified, uses Application Default Credentials."
    },
    "project_ids": {
      "description": "List of Google Cloud Project IDs to ingest Dataplex resources from. If not specified, uses project_id or attempts to detect from credentials.",
      "items": {
        "type": "string"
      },
      "title": "Project Ids",
      "type": "array"
    },
    "entries_location": {
      "default": "us",
      "description": "GCP location for Universal Catalog entries extraction. Must be a multi-region location (us, eu, asia) to access system-managed entry groups like @bigquery. Regional locations (us-central1, etc.) only contain placeholder entries and will miss BigQuery tables. Default: 'us' (recommended for most users).",
      "title": "Entries Location",
      "type": "string"
    },
    "filter_config": {
      "$ref": "#/$defs/DataplexFilterConfig",
      "description": "Filters to control which Dataplex resources are ingested."
    },
    "include_schema": {
      "default": true,
      "description": "Whether to extract and ingest schema metadata (columns, types, descriptions). Set to False to skip schema extraction for faster ingestion when only basic dataset metadata is needed. Disabling schema extraction can improve performance for large deployments. Default: True.",
      "title": "Include Schema",
      "type": "boolean"
    },
    "include_lineage": {
      "default": true,
      "description": "Whether to extract lineage information using Dataplex Lineage API. Extracts table-level lineage relationships between entries. Lineage API calls automatically retry transient errors (timeouts, rate limits) with exponential backoff.",
      "title": "Include Lineage",
      "type": "boolean"
    },
    "lineage_max_retries": {
      "default": 3,
      "description": "Maximum number of retry attempts for lineage API calls when encountering transient errors (timeouts, rate limits, service unavailable). Each attempt uses exponential backoff. Higher values increase resilience but may slow down ingestion. Default: 3.",
      "maximum": 10,
      "minimum": 1,
      "title": "Lineage Max Retries",
      "type": "integer"
    },
    "lineage_retry_backoff_multiplier": {
      "default": 1.0,
      "description": "Multiplier for exponential backoff between lineage API retry attempts (in seconds). Wait time formula: multiplier * (2 ^ attempt_number), capped between 2-10 seconds. Higher values reduce API load but increase ingestion time. Default: 1.0.",
      "maximum": 10.0,
      "minimum": 0.1,
      "title": "Lineage Retry Backoff Multiplier",
      "type": "number"
    },
    "batch_size": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 1000,
      "description": "Batch size for metadata emission and lineage extraction. Entries are emitted in batches to prevent memory issues in large deployments. Lower values reduce memory usage but may increase processing time. Set to None to disable batching (process all entries at once). Recommended: 1000 for large deployments (>10k entries), None for small deployments (<1k entries). Default: 1000.",
      "title": "Batch Size"
    },
    "dataplex_url": {
      "default": "https://console.cloud.google.com/dataplex",
      "description": "Base URL for Dataplex console (for generating external links).",
      "title": "Dataplex Url",
      "type": "string"
    }
  },
  "title": "DataplexConfig",
  "type": "object"
}
```


</TabItem>
</Tabs>

### Capabilities

Use the **Important Capabilities** table above as the source of truth for supported features and whether additional configuration is required.

:::caution
The Dataplex connector will overwrite metadata from other Google Cloud source connectors (BigQuery, GCS, etc.) if they extract the same entities. If you're running multiple Google Cloud connectors, be aware that the last connector to run will determine the final metadata state for overlapping entities.
:::

#### Platform Alignment

Datasets discovered by Dataplex use the same URNs as native connectors (e.g., `bigquery`, `gcs`). This means:

- **No Duplication**: Dataplex and native BigQuery/GCS connectors can run together - entities discovered by both will merge
- **Native Containers**: BigQuery tables appear in their native dataset containers
- **Unified View**: Users see a single view of all datasets regardless of discovery method

#### Custom Properties

The connector adds the following custom properties to datasets:

- `dataplex_entry_id`: The entry identifier in Dataplex
- `dataplex_entry_group`: The entry group containing this entry
- `dataplex_fully_qualified_name`: The fully qualified name of the entry
- `dataplex_ingested`: Marker indicating the dataset was ingested via Dataplex

:::note
To access system-managed entry groups like `@bigquery`, use multi-region locations (`us`, `eu`, `asia`) via the `entries_location` config parameter. Regional locations (`us-central1`, etc.) only contain placeholder entries.
:::

#### Filtering Configuration

Filter which datasets to ingest using regex patterns with allow/deny lists:

**Example:**

```yaml
source:
  type: dataplex
  config:
    project_ids:
      - "my-gcp-project"

    filter_config:
      entries:
        dataset_pattern:
          allow:
            - "production_.*" # Only production datasets
          deny:
            - ".*_test" # Exclude test datasets
            - ".*_temp" # Exclude temporary datasets
```

#### Lineage

When `include_lineage` is enabled and proper permissions are granted, the connector extracts **table-level lineage** using the Dataplex Lineage API. Dataplex automatically tracks lineage from these Google Cloud systems:

**Supported Systems:**

- **BigQuery**: DDL (CREATE TABLE, CREATE TABLE AS SELECT, views, materialized views) and DML (SELECT, INSERT, MERGE, UPDATE, DELETE) operations
- **Cloud Data Fusion**: Pipeline executions
- **Cloud Composer**: Workflow orchestration
- **Dataflow**: Streaming and batch jobs
- **Dataproc**: Apache Spark and Apache Hive jobs (including Dataproc Serverless)
- **Vertex AI**: Models, datasets, feature store views, and feature groups

:::note
Only **BigQuery** lineage has been thoroughly tested with this connector. Lineage from other systems may work but has not been validated.
:::

**Not Supported:**

- **Column-level lineage**: The connector extracts only table-level lineage (column-level lineage is available in Dataplex but not exposed through this connector)
- **Custom sources**: Only Google Cloud systems with automatic lineage tracking are supported
- **BigQuery Data Transfer Service**: Recurring loads are not automatically tracked

**Lineage Limitations:**

- Lineage data is retained for 30 days in Dataplex
- Lineage may take up to 24 hours to appear after job completion
- Cross-region lineage is not supported by Dataplex
- Lineage is only available for entries with active lineage tracking enabled

For more details, see [Dataplex Lineage Documentation](https://docs.cloud.google.com/dataplex/docs/about-data-lineage).

#### Configuration Options

**Metadata Extraction:**

- **`include_schema`** (default: `true`): Extract column metadata and types
- **`include_lineage`** (default: `true`): Extract table-level lineage (automatically retries transient errors)

**Performance Tuning:**

- **`batch_size`** (default: `1000`): Entries per batch for memory optimization. Set to `None` to disable batching (small deployments only)

**Lineage Retry Settings** (optional):

- **`lineage_max_retries`** (default: `3`, range: `1-10`): Retry attempts for transient errors
- **`lineage_retry_backoff_multiplier`** (default: `1.0`, range: `0.1-10.0`): Backoff delay multiplier

**Example Configuration:**

```yaml
source:
  type: dataplex
  config:
    project_ids:
      - "my-gcp-project"

    # Location for entries (Universal Catalog) - defaults to "us"
    # Must be multi-region (us, eu, asia) for system entry groups like @bigquery
    entries_location: "us"

    # Metadata extraction settings
    include_schema: true # Enable schema metadata extraction (default: true)
    include_lineage: true # Enable lineage extraction with automatic retries

    # Lineage retry settings (optional, defaults shown)
    lineage_max_retries: 3 # Max retry attempts (range: 1-10)
    lineage_retry_backoff_multiplier: 1.0 # Exponential backoff multiplier (range: 0.1-10.0)
```

**Configuration for Large Deployments:**

For deployments with thousands of entries, memory optimization is important. The connector uses batched emission to keep memory bounded:

```yaml
source:
  type: dataplex
  config:
    project_ids:
      - "my-gcp-project"
    entries_location: "us"

    # Performance tuning
    batch_size: 1000 # Process and emit 1000 entries at a time to optimize memory usage
```

### Limitations

Module behavior is constrained by source APIs, permissions, and metadata exposed by the platform. Refer to capability notes for unsupported or conditional features.

### Troubleshooting

#### Lineage Extraction Issues

**Automatic Retry Behavior:**

The connector automatically retries transient errors when extracting lineage:

- **Retried errors** (with exponential backoff): Timeouts (DeadlineExceeded), rate limiting (HTTP 429), service issues (HTTP 503, 500)
- **Non-retried errors** (logs warning and continues): Permission denied (HTTP 403), not found (HTTP 404), invalid argument (HTTP 400)

After exhausting retries, the connector logs a warning and continues processing other entries. You'll still get metadata even if lineage extraction fails for some entries.

**Common Issues:**

1. **Regional restrictions**: Lineage API requires multi-region location (`us`, `eu`, `asia`) rather than specific regions (`us-central1`). The connector automatically uses the `entries_location` config.
2. **Missing permissions**: Ensure service account has `roles/datalineage.viewer` role on all projects.
3. **No lineage data**: Some entries may not have lineage if they weren't created through supported systems (BigQuery DDL/DML, Cloud Data Fusion, etc.).
4. **Rate limiting**: If you encounter persistent rate limiting, increase `lineage_retry_backoff_multiplier` to add more delay between retries, or decrease `lineage_max_retries` if you prefer faster failure.

#### Others

If ingestion fails, validate credentials, permissions, connectivity, and scope filters first. Then review ingestion logs for source-specific errors and adjust configuration accordingly.


### Code Coordinates
- Class Name: `datahub.ingestion.source.dataplex.dataplex.DataplexSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/dataplex/dataplex.py)


:::tip Questions?

If you've got any questions on configuring ingestion for Dataplex, feel free to ping us on [our Slack](https://datahub.com/slack).
:::



:::note 💡 **Contributing to this documentation**
This page is auto-generated from the underlying source code. To make changes, please edit the relevant source files in the [metadata-ingestion](https://github.com/datahub-project/datahub/tree/master/metadata-ingestion) directory. 

**Tip:** For quick typo fixes or documentation updates, you can click the ✏️ **Edit** icon directly in the GitHub UI to open a Pull Request. For larger changes and PR naming conventions, please refer to our [Contributing Guide](/docs/contributing).
:::
