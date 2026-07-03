---
sidebar_position: 16
title: DataHubDebug
slug: /generated/ingestion/sources/datahubdebug
custom_edit_url: null
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubDebug

## Overview

DataHub Debug is a DataHub utility or metadata-focused integration. Learn more in the [official DataHub Debug documentation](https://datahub.com/docs/).

The DataHub integration for DataHub Debug covers metadata entities and operational objects relevant to this connector. Depending on module capabilities, it can also capture features such as lineage, usage, profiling, ownership, tags, and stateful deletion detection.

## Concept Mapping

| Source Concept    | DataHub Concept                  | Notes                                                            |
| ----------------- | -------------------------------- | ---------------------------------------------------------------- |
| Debug query/input | DataHub entity/aspect inspection | Reads metadata for diagnostics.                                  |
| Diagnostic output | Operational debugging signal     | Used for troubleshooting and validation, not catalog enrichment. |


## Module `datahub-debug`
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


### Important Capabilities
Capability metadata is not explicitly declared for this module. Refer to module documentation and configuration sections below.

### Overview

The `datahub-debug` module provides targeted debugging and inspection capabilities for DataHub metadata operations.

### Prerequisites

- Access to the DataHub instance being inspected.
- Authentication with sufficient read permissions on entities/aspects involved in debugging.


### Install the Plugin
```shell
pip install 'acryl-datahub[datahub-debug]'
```

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: datahub-debug
  config: {}

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
| <div className="path-line"><span className="path-main">dns_probe_url</span></div> <div className="type-name-line"><span className="type-name">One of string, null</span></div> |  <div className="default-line ">Default: <span className="default-value">None</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "additionalProperties": false,
  "properties": {
    "dns_probe_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Dns Probe Url"
    }
  },
  "title": "DataHubDebugSourceConfig",
  "type": "object"
}
```


</TabItem>
</Tabs>

### Capabilities

Use the **Important Capabilities** table above as the source of truth. This module is intended for diagnostics and validation workflows.

### Limitations

- This module is not a general external-source ingestion connector.
- Output is intended for debugging workflows and may require interpretation by platform operators.

### Troubleshooting

- Confirm authentication and API connectivity to the target DataHub environment.
- Scope debug requests narrowly first, then expand once the expected output is validated.
- Use ingestion logs to identify permission or query errors.


### Code Coordinates
- Class Name: `datahub.ingestion.source.debug.datahub_debug.DataHubDebugSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/debug/datahub_debug.py)


:::tip Questions?

If you've got any questions on configuring ingestion for DataHubDebug, feel free to ping us on [our Slack](https://datahub.com/slack).
:::



:::note 💡 **Contributing to this documentation**
This page is auto-generated from the underlying source code. To make changes, please edit the relevant source files in the [metadata-ingestion](https://github.com/datahub-project/datahub/tree/master/metadata-ingestion) directory. 

**Tip:** For quick typo fixes or documentation updates, you can click the ✏️ **Edit** icon directly in the GitHub UI to open a Pull Request. For larger changes and PR naming conventions, please refer to our [Contributing Guide](/docs/contributing).
:::
