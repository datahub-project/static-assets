---
sidebar_position: 56
title: Slack
slug: /generated/ingestion/sources/slack
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/slack.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Slack
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)



### CLI based Ingestion

#### Install the Plugin
The `slack` source works out of the box with `acryl-datahub`.

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">bot_token</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string(password)</span></div> | Bot token for the Slack workspace. Needs `users:read`, `users:read.email` and `users.profile:read` scopes.  |
| <div className="path-line"><span className="path-main">api_requests_per_min</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of API requests per minute. Low-level config. Do not tweak unless you are facing any issues. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-main">channel_min_members</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Ingest channels with at least this many members. <div className="default-line default-line-with-docs">Default: <span className="default-value">2</span></div> |
| <div className="path-line"><span className="path-main">channels_iteration_limit</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Limit the number of channels to be ingested in a iteration. Low-level config. Do not tweak unless you are facing any issues. <div className="default-line default-line-with-docs">Default: <span className="default-value">200</span></div> |
| <div className="path-line"><span className="path-main">enrich_user_metadata</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to enrich user metadata. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">ingest_public_channels</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest public channels. If set to true needs `channels:read` scope. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-main">should_ingest_archived_channels</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest archived channels. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "SlackSourceConfig",
  "type": "object",
  "properties": {
    "bot_token": {
      "title": "Bot Token",
      "description": "Bot token for the Slack workspace. Needs `users:read`, `users:read.email` and `users.profile:read` scopes.",
      "type": "string",
      "writeOnly": true,
      "format": "password"
    },
    "enrich_user_metadata": {
      "title": "Enrich User Metadata",
      "description": "Whether to enrich user metadata.",
      "default": true,
      "type": "boolean"
    },
    "api_requests_per_min": {
      "title": "Api Requests Per Min",
      "description": "Number of API requests per minute. Low-level config. Do not tweak unless you are facing any issues.",
      "default": 10,
      "type": "integer"
    },
    "ingest_public_channels": {
      "title": "Ingest Public Channels",
      "description": "Whether to ingest public channels. If set to true needs `channels:read` scope.",
      "default": false,
      "type": "boolean"
    },
    "channels_iteration_limit": {
      "title": "Channels Iteration Limit",
      "description": "Limit the number of channels to be ingested in a iteration. Low-level config. Do not tweak unless you are facing any issues.",
      "default": 200,
      "type": "integer"
    },
    "channel_min_members": {
      "title": "Channel Min Members",
      "description": "Ingest channels with at least this many members.",
      "default": 2,
      "type": "integer"
    },
    "should_ingest_archived_channels": {
      "title": "Should Ingest Archived Channels",
      "description": "Whether to ingest archived channels.",
      "default": false,
      "type": "boolean"
    }
  },
  "required": [
    "bot_token"
  ],
  "additionalProperties": false
}
```


</TabItem>
</Tabs>


### Code Coordinates
- Class Name: `datahub.ingestion.source.slack.slack.SlackSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/slack/slack.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for Slack, feel free to ping us on [our Slack](https://slack.datahubproject.io).
