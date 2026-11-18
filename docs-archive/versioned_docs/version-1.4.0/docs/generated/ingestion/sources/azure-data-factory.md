---
sidebar_position: 4
title: Azure Data Factory
slug: /generated/ingestion/sources/azure-data-factory
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/azure-data-factory.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Azure Data Factory
# Azure Data Factory

For context on getting started with ingestion, check out our [metadata ingestion guide](../../../../metadata-ingestion/README.md).

## Setup

To install this plugin, run `pip install 'acryl-datahub[azure-data-factory]'`.

## Quickstart Recipe

```yaml
source:
  type: azure-data-factory
  config:
    # Required
    subscription_id: ${AZURE_SUBSCRIPTION_ID}

    # Authentication (service principal)
    credential:
      authentication_method: service_principal
      client_id: ${AZURE_CLIENT_ID}
      client_secret: ${AZURE_CLIENT_SECRET}
      tenant_id: ${AZURE_TENANT_ID}

    # Optional filters
    factory_pattern:
      allow: ["prod-.*"]

    # Features
    include_lineage: true
    include_execution_history: false

    env: PROD

sink:
  type: datahub-rest
  config:
    server: "http://localhost:8080"
```

## Authentication Methods

| Method            | Config Value        | Use Case          |
| ----------------- | ------------------- | ----------------- |
| Service Principal | `service_principal` | Production        |
| Managed Identity  | `managed_identity`  | Azure-hosted      |
| Azure CLI         | `cli`               | Local development |
| Auto-detect       | `default`           | Flexible          |

## Config Details

| Field                              | Required | Description                               |
| ---------------------------------- | -------- | ----------------------------------------- |
| `subscription_id`                  | ✅       | Azure subscription ID                     |
| `credential.authentication_method` |          | Auth method (default: `default`)          |
| `credential.client_id`             |          | App (client) ID for service principal     |
| `credential.client_secret`         |          | Client secret for service principal       |
| `credential.tenant_id`             |          | Tenant (directory) ID                     |
| `resource_group`                   |          | Filter to specific resource group         |
| `factory_pattern`                  |          | Regex allow/deny for factories            |
| `pipeline_pattern`                 |          | Regex allow/deny for pipelines            |
| `include_lineage`                  |          | Extract lineage (default: `true`)         |
| `include_execution_history`        |          | Extract pipeline runs (default: `false`)  |
| `execution_history_days`           |          | Days of history, 1-90 (default: `7`)      |
| `platform_instance_map`            |          | Map linked services to platform instances |
| `env`                              |          | Environment (default: `PROD`)             |

## Entity Mapping

| ADF Concept  | DataHub Entity      |
| ------------ | ------------------- |
| Data Factory | Container           |
| Pipeline     | DataFlow            |
| Activity     | DataJob             |
| Dataset      | Dataset             |
| Pipeline Run | DataProcessInstance |

## Questions

If you've got any questions on configuring this source, feel free to ping us on [our Slack](https://slack.datahubproject.io/).
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default. Supported for types - Data Factory. |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default via stateful ingestion. |
| [Platform Instance](../../../platform-instances.md) | ✅ | Enabled by default. |
| Table-Level Lineage | ✅ | Extracts lineage from Copy and Data Flow activities. Supported for types - Copy Activity, Data Flow Activity. |


:::note Not Azure Fabric
This connector is for **Azure Data Factory** (classic), not Azure Fabric's Data Factory. Azure Fabric support is planned for a future release.
:::

## Prerequisites

### Authentication

The connector supports multiple authentication methods:

| Method                     | Best For                                         | Configuration                                       |
| -------------------------- | ------------------------------------------------ | --------------------------------------------------- |
| **Service Principal**      | Production environments                          | `authentication_method: service_principal`          |
| **Managed Identity**       | Azure-hosted deployments (VMs, AKS, App Service) | `authentication_method: managed_identity`           |
| **Azure CLI**              | Local development                                | `authentication_method: cli` (run `az login` first) |
| **DefaultAzureCredential** | Flexible environments                            | `authentication_method: default`                    |

For service principal setup, see [Register an application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

### Required Permissions

The connector only performs **read operations**. Grant one of the following:

**Option 1: Built-in Reader Role** (recommended)

Assign the [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) role at subscription, resource group, or Data Factory level.

**Option 2: Custom Role with Minimal Permissions**

Download [`datahub-adf-reader-role.json`](https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahub-adf-reader-role.json), update the `{subscription-id}`, then:

```bash
# Create custom role
az role definition create --role-definition datahub-adf-reader-role.json

# Assign to service principal
az role assignment create \
  --assignee <service-principal-id> \
  --role "DataHub ADF Reader" \
  --scope /subscriptions/{subscription-id}
```

For detailed instructions, see [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles).

## Lineage Extraction

### Which Activities Produce Lineage?

The connector extracts **table-level lineage** from these ADF activity types:

| Activity Type       | Lineage Behavior                                           |
| ------------------- | ---------------------------------------------------------- |
| **Copy Activity**   | Creates lineage from input dataset(s) to output dataset    |
| **Data Flow**       | Extracts sources, sinks, and transformation script         |
| **Lookup Activity** | Creates input lineage from the lookup dataset              |
| **ExecutePipeline** | Creates pipeline-to-pipeline lineage to the child pipeline |

Lineage is enabled by default (`include_lineage: true`).

### How Lineage Resolution Works

For lineage to connect properly to datasets ingested from other sources (e.g., Snowflake, BigQuery), the connector needs to know which DataHub platform each ADF linked service corresponds to.

**Step 1: Automatic Platform Mapping**

The connector automatically maps ADF linked service types to DataHub platforms. For example, a `Snowflake` linked service maps to the `snowflake` platform.

<details>
<summary>View all supported linked service mappings</summary>

| ADF Linked Service Type  | DataHub Platform |
| ------------------------ | ---------------- |
| AzureBlobStorage         | `abs`            |
| AzureBlobFS              | `abs`            |
| AzureDataLakeStore       | `abs`            |
| AzureFileStorage         | `abs`            |
| AzureSqlDatabase         | `mssql`          |
| AzureSqlDW               | `mssql`          |
| AzureSynapseAnalytics    | `mssql`          |
| AzureSqlMI               | `mssql`          |
| SqlServer                | `mssql`          |
| AzureDatabricks          | `databricks`     |
| AzureDatabricksDeltaLake | `databricks`     |
| AmazonS3                 | `s3`             |
| AmazonS3Compatible       | `s3`             |
| AmazonRedshift           | `redshift`       |
| GoogleCloudStorage       | `gcs`            |
| GoogleBigQuery           | `bigquery`       |
| Snowflake                | `snowflake`      |
| PostgreSql               | `postgres`       |
| AzurePostgreSql          | `postgres`       |
| MySql                    | `mysql`          |
| AzureMySql               | `mysql`          |
| Oracle                   | `oracle`         |
| OracleServiceCloud       | `oracle`         |
| Db2                      | `db2`            |
| Teradata                 | `teradata`       |
| Vertica                  | `vertica`        |
| Hive                     | `hive`           |
| Spark                    | `spark`          |
| Hdfs                     | `hdfs`           |
| Salesforce               | `salesforce`     |
| SalesforceServiceCloud   | `salesforce`     |
| SalesforceMarketingCloud | `salesforce`     |

Unsupported linked service types log a warning and skip lineage for that dataset.

</details>

**Step 2: Platform Instance Mapping (for cross-recipe lineage)**

If you're ingesting the same data sources with other DataHub connectors (e.g., Snowflake, BigQuery), you need to ensure the `platform_instance` values match. Use `platform_instance_map` to map your ADF linked service names to the platform instance used in your other recipes:

```yaml
# ADF Recipe
source:
  type: azure-data-factory
  config:
    subscription_id: ${AZURE_SUBSCRIPTION_ID}
    platform_instance_map:
      # Key: Your ADF linked service name (exact match required)
      # Value: The platform_instance from your other source recipe
      "snowflake-prod-connection": "prod_warehouse"
      "bigquery-analytics": "analytics_project"
```

```yaml
# Corresponding Snowflake Recipe (platform_instance must match)
source:
  type: snowflake
  config:
    platform_instance: "prod_warehouse" # Must match the value in platform_instance_map
    # ... other config
```

Without matching `platform_instance` values, lineage will create separate dataset entities instead of connecting to your existing ingested datasets.

### Data Flow Transformation Scripts

For Data Flow activities, the connector extracts the transformation script and stores it in the `dataTransformLogic` aspect, visible in the DataHub UI under activity details.

## Execution History

Pipeline runs are extracted as `DataProcessInstance` entities by default:

```yaml
source:
  type: azure-data-factory
  config:
    include_execution_history: true # default
    execution_history_days: 7 # 1-90 days
```

This provides run status, duration, timestamps, trigger info, parameters, and activity-level details.

## Advanced: Multi-Environment Setup

### When to Use `platform_instance`

Use the ADF connector's `platform_instance` config to distinguish **separate ADF deployments** when ingesting from multiple subscriptions or tenants:

| Scenario               | Risk                           | Solution     |
| ---------------------- | ------------------------------ | ------------ |
| Single subscription    | None                           | Not needed   |
| Multiple subscriptions | Low                            | Recommended  |
| Multiple tenants       | **High** - name collision risk | **Required** |

```yaml
# Multi-tenant example
source:
  type: azure-data-factory
  config:
    subscription_id: "tenant-a-sub"
    platform_instance: "tenant-a" # Prevents URN collisions
```

:::warning
Factory names are unique within Azure, but different tenants could have identically-named factories. Use `platform_instance` to prevent entity overwrites.
:::

### URN Format

Pipeline URNs follow this format:

```
urn:li:dataFlow:(azure-data-factory,{factory_name}.{pipeline_name},{env})
```

With `platform_instance`:

```
urn:li:dataFlow:(azure-data-factory,{platform_instance}.{factory_name}.{pipeline_name},{env})
```

For Azure naming rules, see [Azure Data Factory naming rules](https://learn.microsoft.com/en-us/azure/data-factory/naming-rules).

### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
# Example recipe for Azure Data Factory source
# See README.md for full configuration options

source:
  type: azure-data-factory
  config:
    # Required: Azure subscription containing Data Factories
    subscription_id: ${AZURE_SUBSCRIPTION_ID}
    
    # Optional: Filter to specific resource group
    # resource_group: my-resource-group
    
    # Authentication (using service principal)
    credential:
      authentication_method: service_principal
      client_id: ${AZURE_CLIENT_ID}
      client_secret: ${AZURE_CLIENT_SECRET}
      tenant_id: ${AZURE_TENANT_ID}
    
    # Optional: Filter factories by name pattern
    factory_pattern:
      allow:
        - ".*"  # Allow all factories by default
      deny: []
    
    # Optional: Filter pipelines by name pattern
    pipeline_pattern:
      allow:
        - ".*"  # Allow all pipelines by default
      deny: []
    
    # Feature flags
    include_lineage: true
    include_column_lineage: false  # Advanced: requires Data Flow parsing
    include_execution_history: false  # Set to true for pipeline run history
    execution_history_days: 7  # Only used when include_execution_history is true
    
    # Optional: Map linked services to platform instances for accurate lineage
    # platform_instance_map:
    #   "my-snowflake-connection": "prod_snowflake"
    
    # Optional: Platform instance for this ADF connector
    # platform_instance: "main-adf"
    
    # Environment
    env: PROD
    
    # Optional: Stateful ingestion for stale entity removal
    # stateful_ingestion:
    #   enabled: true

sink:
  type: datahub-rest
  config:
    server: "http://localhost:8080"


```

### Code Coordinates
- Class Name: `datahub.ingestion.source.azure_data_factory.adf_source.AzureDataFactorySource`

<h2>Questions</h2>

If you've got any questions on configuring ingestion for Azure Data Factory, feel free to ping us on [our Slack](https://datahub.com/slack).
