---
sidebar_position: 11
title: DataHubGc
slug: /generated/ingestion/sources/datahubgc
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahubgc.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubGc
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)



### CLI based Ingestion

#### Install the Plugin
The `datahub-gc` source works out of the box with `acryl-datahub`.

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">cleanup_expired_tokens</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to clean up expired tokens or not <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">truncate_index_older_than_days</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Indices older than this number of days will be truncated <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-main">truncate_indices</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to truncate elasticsearch indices or not which can be safely truncated <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">truncation_sleep_between_seconds</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Sleep between truncation monitoring. <div className="default-line default-line-with-docs">Default: <span className="default-value">30</span></div> |
| <div className="path-line"><span className="path-main">truncation_watch_until</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Wait for truncation of indices until this number of documents are left <div className="default-line default-line-with-docs">Default: <span className="default-value">10000</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataHubGcSourceConfig",
  "type": "object",
  "properties": {
    "cleanup_expired_tokens": {
      "title": "Cleanup Expired Tokens",
      "description": "Whether to clean up expired tokens or not",
      "default": true,
      "type": "boolean"
    },
    "truncate_indices": {
      "title": "Truncate Indices",
      "description": "Whether to truncate elasticsearch indices or not which can be safely truncated",
      "default": true,
      "type": "boolean"
    },
    "truncate_index_older_than_days": {
      "title": "Truncate Index Older Than Days",
      "description": "Indices older than this number of days will be truncated",
      "default": 30,
      "type": "integer"
    },
    "truncation_watch_until": {
      "title": "Truncation Watch Until",
      "description": "Wait for truncation of indices until this number of documents are left",
      "default": 10000,
      "type": "integer"
    },
    "truncation_sleep_between_seconds": {
      "title": "Truncation Sleep Between Seconds",
      "description": "Sleep between truncation monitoring.",
      "default": 30,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.gc.datahub_gc.DataHubGcSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/gc/datahub_gc.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHubGc, feel free to ping us on [our Slack](https://slack.datahubproject.io).
