---
sidebar_position: 37
title: Metadata File
slug: /generated/ingestion/sources/metadata-file
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/metadata-file.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Metadata File
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Optionally enabled via `stateful_ingestion.remove_stale_metadata` |


This plugin pulls metadata from a previously generated file.
The [metadata file sink](../../../../metadata-ingestion/sink_docs/metadata-file.md) can produce such files, and a number of
samples are included in the [examples/mce_files](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/mce_files) directory.


### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: file
  config:
    # Coordinates
    filename: ./path/to/mce/file.json

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
| <div className="path-line"><span className="path-main">path</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | File path to folder or file to ingest, or URL to a remote file. If pointed to a folder, all files with extension {file_extension} (default json) within that folder will be processed.  |
| <div className="path-line"><span className="path-main">aspect</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | Set to an aspect to only read this aspect for ingestion.  |
| <div className="path-line"><span className="path-main">count_all_before_starting</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | When enabled, counts total number of records in the file before starting. Used for accurate estimation of completion time. Turn it off if startup time is too high. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">file_extension</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | When providing a folder to use to read files, set this field to control file extensions that you want the source to process. * is a special value that means process every file regardless of extension <div className="default-line default-line-with-docs">Default: <span className="default-value">.json</span></div> |
| <div className="path-line"><span className="path-main">read_mode</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> |  <div className="default-line ">Default: <span className="default-value">AUTO</span></div> |
| <div className="path-line"><span className="path-main">stateful_ingestion</span></div> <div className="type-name-line"><span className="type-name">StatefulStaleMetadataRemovalConfig</span></div> | Base specialized config for Stateful Ingestion with stale metadata removal capability.  |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether or not to enable stateful ingest. Default: True if a pipeline_name is set and either a datahub-rest sink or `datahub_api` is specified, otherwise False <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">stateful_ingestion.</span><span className="path-main">remove_stale_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Soft-deletes the entities present in the last successful run but missing in the current run with stateful_ingestion enabled. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "FileSourceConfig",
  "description": "Base configuration class for stateful ingestion for source configs to inherit from.",
  "type": "object",
  "properties": {
    "stateful_ingestion": {
      "$ref": "#/definitions/StatefulStaleMetadataRemovalConfig"
    },
    "path": {
      "title": "Path",
      "description": "File path to folder or file to ingest, or URL to a remote file. If pointed to a folder, all files with extension {file_extension} (default json) within that folder will be processed.",
      "type": "string"
    },
    "file_extension": {
      "title": "File Extension",
      "description": "When providing a folder to use to read files, set this field to control file extensions that you want the source to process. * is a special value that means process every file regardless of extension",
      "default": ".json",
      "type": "string"
    },
    "read_mode": {
      "default": "AUTO",
      "allOf": [
        {
          "$ref": "#/definitions/FileReadMode"
        }
      ]
    },
    "aspect": {
      "title": "Aspect",
      "description": "Set to an aspect to only read this aspect for ingestion.",
      "type": "string"
    },
    "count_all_before_starting": {
      "title": "Count All Before Starting",
      "description": "When enabled, counts total number of records in the file before starting. Used for accurate estimation of completion time. Turn it off if startup time is too high.",
      "default": true,
      "type": "boolean"
    }
  },
  "required": [
    "path"
  ],
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
    "FileReadMode": {
      "title": "FileReadMode",
      "description": "An enumeration.",
      "enum": [
        "STREAM",
        "BATCH",
        "AUTO"
      ]
    }
  }
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.file.GenericFileSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/file.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Metadata File, feel free to ping us on [our Slack](https://slack.datahubproject.io).
