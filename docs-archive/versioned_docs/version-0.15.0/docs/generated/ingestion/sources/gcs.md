---
sidebar_position: 24
title: Google Cloud Storage
slug: /generated/ingestion/sources/gcs
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/gcs.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Google Cloud Storage
This connector ingests Google Cloud Storage datasets into DataHub. It allows mapping an individual file or a folder of files to a dataset in DataHub. 
To specify the group of files that form a dataset, use `path_specs` configuration in ingestion recipe. This source leverages [Interoperability of GCS with S3](https://cloud.google.com/storage/docs/interoperability)
and uses DataHub S3 Data Lake integration source under the hood. Refer section [Path Specs](/docs/generated/ingestion/sources/s3/#path-specs) from S3 connector for more details.



### Concept Mapping

This ingestion source maps the following Source System Concepts to DataHub Concepts:

| Source Concept                             | DataHub Concept                                                                            | Notes                |
| ------------------------------------------ |--------------------------------------------------------------------------------------------| -------------------- |
| `"Google Cloud Storage"`                   | [Data Platform](/docs/generated/metamodel/entities/dataplatform/) |                      |
| GCS object / Folder containing GCS objects | [Dataset](/docs/generated/metamodel/entities/dataset/)            |                      |
| GCS bucket                                 | [Container](/docs/generated/metamodel/entities/container/)        | Subtype `GCS bucket` |
| GCS folder                                 | [Container](/docs/generated/metamodel/entities/container/)        | Subtype `Folder`     |


### Supported file types
Supported file types are as follows:

- CSV
- TSV
- JSONL
- JSON
- Parquet
- Apache Avro

Schemas for Parquet and Avro files are extracted as provided.

Schemas for schemaless formats (CSV, TSV, JSONL, JSON) are inferred. For CSV, TSV and JSONL files, we consider the first 100 rows by default, which can be controlled via the `max_rows` recipe parameter (see [below](#config-details))
JSON file schemas are inferred on the basis of the entire file (given the difficulty in extracting only the first few objects of the file), which may impact performance.
We are working on using iterator-based JSON parsers to avoid reading in the entire JSON object.


### Prerequisites
1. Create a service account with "Storage Object Viewer" Role - https://cloud.google.com/iam/docs/service-accounts-create
2. Make sure you meet following requirements to generate HMAC key - https://cloud.google.com/storage/docs/authentication/managing-hmackeys#before-you-begin
3. Create an HMAC key for service account created above - https://cloud.google.com/storage/docs/authentication/managing-hmackeys#create .
![Incubating](https://img.shields.io/badge/support%20status-incubating-blue)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Asset Containers | ✅ | Enabled by default |
| [Data Profiling](../../../../metadata-ingestion/docs/dev_guides/sql_profiles.md) | ❌ | Not supported |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |
| Schema Metadata | ✅ | Enabled by default |



### CLI based Ingestion

#### Install the Plugin
The `gcs` source works out of the box with `acryl-datahub`.

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: gcs
  config:
    path_specs: 
       - include: gs://gcs-ingestion-bucket/parquet_example/{table}/year={partition[0]}/*.parquet
    credential:
      hmac_access_id: <hmac access id>
      hmac_access_secret: <hmac access secret>

```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">credential</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">HMACKey</span></div> | Google cloud storage [HMAC keys](https://cloud.google.com/storage/docs/authentication/hmackeys)  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">hmac_access_id</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Access ID  |
| <div className="path-line"><span className="path-prefix">credential.</span><span className="path-main">hmac_access_secret</span>&nbsp;<abbr title="Required if credential is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Secret  |
| <div className="path-line"><span className="path-main">path_specs</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of PathSpec. See [below](#path-spec) the details about PathSpec  |
| <div className="path-line"><span className="path-prefix">path_specs.</span><span className="path-main">PathSpec</span></div> <div className="type-name-line"><span className="type-name">PathSpec</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">include</span>&nbsp;<abbr title="Required if PathSpec is set">❓</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to table. Name variable `{table}` is used to mark the folder with dataset. In absence of `{table}`, file level dataset will be created. Check below examples for more details.  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">allow_double_stars</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Allow double stars in the include path. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">autodetect_partitions</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Autodetect partition(s) from the path. If set to true, it will autodetect partition key/value if the folder format is {partition_key}={partition_value} for example `year=2024` <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">default_extension</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | For files without extension it will assume the specified file type. If it is not set the files without extensions will be skipped.  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">enable_compression</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Enable or disable processing compressed files. Currently .gz and .bz files are supported. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">include_hidden_folders</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Include hidden folders in the traversal (folders starting with . or _ <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">sample_files</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Not listing all the files but only taking a handful amount of sample file to infer the schema. File count and file size calculation will be disabled. This can affect performance significantly if enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">table_name</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Display name of the dataset.Combination of named variables from include path and strings  |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">traversal_method</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Method to traverse the folder. ALL: Traverse all the folders, MIN_MAX: Traverse the folders by finding min and max value, MAX: Traverse the folder with max value <div className="default-line default-line-with-docs">Default: <span className="default-value">MAX</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">exclude</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | list of paths in glob pattern which will be excluded while scanning for the datasets <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.exclude.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.</span><span className="path-main">file_types</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | Files with extenstions specified here (subset of default value) only will be scanned to create dataset. Other files will be omitted. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#91;&#x27;csv&#x27;, &#x27;tsv&#x27;, &#x27;json&#x27;, &#x27;parquet&#x27;, &#x27;avro&#x27;&#93;</span></div> |
| <div className="path-line"><span className="path-prefix">path_specs.PathSpec.file_types.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">max_rows</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Maximum number of rows to use when inferring schemas for TSV and CSV files. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-main">number_of_files_to_sample</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of files to list to sample for schema inference. This will be ignored if sample_files is set to False in the pathspec. <div className="default-line default-line-with-docs">Default: <span className="default-value">100</span></div> |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "GCSSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "path_specs": {
      "title": "Path Specs",
      "description": "List of PathSpec. See [below](#path-spec) the details about PathSpec",
      "type": "array",
      "items": {
        "$ref": "#/definitions/PathSpec"
      }
    },
    "env": {
      "title": "Env",
      "description": "The environment that all assets produced by this connector belong to",
      "default": "PROD",
      "type": "string"
    },
    "platform_instance": {
      "title": "Platform Instance",
      "description": "The instance of the platform that all assets produced by this recipe belong to. This should be unique within the platform. See https://datahubproject.io/docs/platform-instances/ for more details.",
      "type": "string"
    },
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "credential": {
      "title": "Credential",
      "description": "Google cloud storage [HMAC keys](https://cloud.google.com/storage/docs/authentication/hmackeys)",
      "allOf": [
        {
          "$ref": "#/definitions/HMACKey"
        }
      ]
    },
    "max_rows": {
      "title": "Max Rows",
      "description": "Maximum number of rows to use when inferring schemas for TSV and CSV files.",
      "default": 100,
      "type": "integer"
    },
    "number_of_files_to_sample": {
      "title": "Number Of Files To Sample",
      "description": "Number of files to list to sample for schema inference. This will be ignored if sample_files is set to False in the pathspec.",
      "default": 100,
      "type": "integer"
    }
  },
  "required": [
    "path_specs",
    "credential"
  ],
  "additionalProperties": false,
  "definitions": {
    "SortKeyType": {
      "title": "SortKeyType",
      "description": "An enumeration.",
      "enum": [
        "STRING",
        "INTEGER",
        "FLOAT",
        "DATETIME",
        "DATE"
      ]
    },
    "SortKey": {
      "title": "SortKey",
      "type": "object",
      "properties": {
        "key": {
          "title": "Key",
          "description": "The key to sort on. This can be a compound key based on the path_spec variables.",
          "type": "string"
        },
        "type": {
          "description": "The date format to use when sorting. This is used to parse the date from the key. The format should follow the java [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) format.",
          "default": "STRING",
          "allOf": [
            {
              "$ref": "#/definitions/SortKeyType"
            }
          ]
        },
        "date_format": {
          "title": "Date Format",
          "description": "The date format to use when sorting. This is used to parse the date from the key. The format should follow the java [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) format.",
          "type": "string"
        }
      },
      "required": [
        "key"
      ],
      "additionalProperties": false
    },
    "FolderTraversalMethod": {
      "title": "FolderTraversalMethod",
      "description": "An enumeration.",
      "enum": [
        "ALL",
        "MIN_MAX",
        "MAX"
      ]
    },
    "PathSpec": {
      "title": "PathSpec",
      "type": "object",
      "properties": {
        "include": {
          "title": "Include",
          "description": "Path to table. Name variable `{table}` is used to mark the folder with dataset. In absence of `{table}`, file level dataset will be created. Check below examples for more details.",
          "type": "string"
        },
        "exclude": {
          "title": "Exclude",
          "description": "list of paths in glob pattern which will be excluded while scanning for the datasets",
          "default": [],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "file_types": {
          "title": "File Types",
          "description": "Files with extenstions specified here (subset of default value) only will be scanned to create dataset. Other files will be omitted.",
          "default": [
            "csv",
            "tsv",
            "json",
            "parquet",
            "avro"
          ],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "default_extension": {
          "title": "Default Extension",
          "description": "For files without extension it will assume the specified file type. If it is not set the files without extensions will be skipped.",
          "type": "string"
        },
        "table_name": {
          "title": "Table Name",
          "description": "Display name of the dataset.Combination of named variables from include path and strings",
          "type": "string"
        },
        "enable_compression": {
          "title": "Enable Compression",
          "description": "Enable or disable processing compressed files. Currently .gz and .bz files are supported.",
          "default": true,
          "type": "boolean"
        },
        "sample_files": {
          "title": "Sample Files",
          "description": "Not listing all the files but only taking a handful amount of sample file to infer the schema. File count and file size calculation will be disabled. This can affect performance significantly if enabled",
          "default": true,
          "type": "boolean"
        },
        "allow_double_stars": {
          "title": "Allow Double Stars",
          "description": "Allow double stars in the include path. This can affect performance significantly if enabled",
          "default": false,
          "type": "boolean"
        },
        "autodetect_partitions": {
          "title": "Autodetect Partitions",
          "description": "Autodetect partition(s) from the path. If set to true, it will autodetect partition key/value if the folder format is {partition_key}={partition_value} for example `year=2024`",
          "default": true,
          "type": "boolean"
        },
        "traversal_method": {
          "description": "Method to traverse the folder. ALL: Traverse all the folders, MIN_MAX: Traverse the folders by finding min and max value, MAX: Traverse the folder with max value",
          "default": "MAX",
          "allOf": [
            {
              "$ref": "#/definitions/FolderTraversalMethod"
            }
          ]
        },
        "include_hidden_folders": {
          "title": "Include Hidden Folders",
          "description": "Include hidden folders in the traversal (folders starting with . or _",
          "default": false,
          "type": "boolean"
        }
      },
      "required": [
        "include"
      ],
      "additionalProperties": false
    },
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
    "HMACKey": {
      "title": "HMACKey",
      "type": "object",
      "properties": {
        "hmac_access_id": {
          "title": "Hmac Access Id",
          "description": "Access ID",
          "type": "string"
        },
        "hmac_access_secret": {
          "title": "Hmac Access Secret",
          "description": "Secret",
          "type": "string",
          "writeOnly": true,
          "format": "password"
        }
      },
      "required": [
        "hmac_access_id",
        "hmac_access_secret"
      ],
      "additionalProperties": false
    }
  }
}
```


</TabItem>
</Tabs>


### Path Specs

**Example - Dataset per file**

Bucket structure:

```
test-gs-bucket
├── employees.csv
└── food_items.csv
```

Path specs config
```
path_specs:
    - include: gs://test-gs-bucket/*.csv

```

**Example - Datasets with partitions**

Bucket structure:
```
test-gs-bucket
├── orders
│   └── year=2022
│       └── month=2
│           ├── 1.parquet
│           └── 2.parquet
└── returns
    └── year=2021
        └── month=2
            └── 1.parquet

```

Path specs config:
```
path_specs:
    - include: gs://test-gs-bucket/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
```

**Example - Datasets with partition and exclude**

Bucket structure:
```
test-gs-bucket
├── orders
│   └── year=2022
│       └── month=2
│           ├── 1.parquet
│           └── 2.parquet
└── tmp_orders
    └── year=2021
        └── month=2
            └── 1.parquet


```

Path specs config:
```
path_specs:
    - include: gs://test-gs-bucket/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
      exclude: 
        - **/tmp_orders/**
```
**Example - Datasets of mixed nature**

Bucket structure:
```
test-gs-bucket
├── customers
│   ├── part1.json
│   ├── part2.json
│   ├── part3.json
│   └── part4.json
├── employees.csv
├── food_items.csv
├── tmp_10101000.csv
└──  orders
    └── year=2022
        └── month=2
            ├── 1.parquet
            ├── 2.parquet
            └── 3.parquet

```

Path specs config:
```
path_specs:
    - include: gs://test-gs-bucket/*.csv
      exclude:
        - **/tmp_10101000.csv
    - include: gs://test-gs-bucket/{table}/*.json
    - include: gs://test-gs-bucket/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.parquet
```

**Valid path_specs.include**

```python
gs://my-bucket/foo/tests/bar.avro # single file table   
gs://my-bucket/foo/tests/*.* # mulitple file level tables
gs://my-bucket/foo/tests/{table}/*.avro #table without partition
gs://my-bucket/foo/tests/{table}/*/*.avro #table where partitions are not specified
gs://my-bucket/foo/tests/{table}/*.* # table where no partitions as well as data type specified
gs://my-bucket/{dept}/tests/{table}/*.avro # specifying keywords to be used in display name
gs://my-bucket/{dept}/tests/{table}/{partition_key[0]}={partition[0]}/{partition_key[1]}={partition[1]}/*.avro # specify partition key and value format
gs://my-bucket/{dept}/tests/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.avro # specify partition value only format
gs://my-bucket/{dept}/tests/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # for all extensions
gs://my-bucket/*/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # table is present at 2 levels down in bucket
gs://my-bucket/*/*/{table}/{partition[0]}/{partition[1]}/{partition[2]}/*.* # table is present at 3 levels down in bucket
```

**Valid path_specs.exclude**
- \**/tests/**
- gs://my-bucket/hr/**
- **/tests/*.csv
- gs://my-bucket/foo/*/my_table/**

**Notes**

- {table} represents folder for which dataset will be created.
- include path must end with (*.* or *.[ext]) to represent leaf level.
- if *.[ext] is provided then only files with specified type will be scanned.
- /*/ represents single folder.
- {partition[i]} represents value of partition.
- {partition_key[i]} represents name of the partition.
- While extracting, “i” will be used to match partition_key to partition.
- all folder levels need to be specified in include. Only exclude path can have ** like matching.
- exclude path cannot have named variables ( {} ).
- Folder names should not contain {, }, *, / in their names.
- {folder} is reserved for internal working. please do not use in named variables.



If you would like to write a more complicated function for resolving file names, then a {transformer} would be a good fit.

:::caution

Specify as long fixed prefix ( with out /*/ ) as possible in `path_specs.include`. This will reduce the scanning time and cost, specifically on Google Cloud Storage.

:::


:::caution

If you are ingesting datasets from Google Cloud Storage, we recommend running the ingestion on a server in the same region to avoid high egress costs.

:::

### Code Coordinates
- Class Name: `datahub.ingestion.source.gcs.gcs_source.GCSSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/gcs/gcs_source.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Google Cloud Storage, feel free to ping us on [our Slack](https://slack.datahubproject.io).
