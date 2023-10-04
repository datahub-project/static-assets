---
sidebar_position: 48
title: SQL Queries
slug: /generated/ingestion/sources/sql-queries
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/sql-queries.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SQL Queries
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)



### CLI based Ingestion

#### Install the Plugin
```shell
pip install 'acryl-datahub[sql-queries]'
```

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">platform</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | The platform for which to generate data, e.g. snowflake  |
| <div className="path-line"><span className="path-main">query_file</span>&nbsp;<abbr title="Required">✅</abbr></div> <div className="type-name-line"><span className="type-name">string</span></div> | Path to file to ingest  |
| <div className="path-line"><span className="path-main">default_db</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The default database to use for unqualified table names  |
| <div className="path-line"><span className="path-main">default_schema</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The default schema to use for unqualified table names  |
| <div className="path-line"><span className="path-main">platform_instance</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The instance of the platform that all assets produced by this recipe belong to  |
| <div className="path-line"><span className="path-main">env</span></div> <div className="type-name-line"><span className="type-name">string</span></div> | The environment that all assets produced by this connector belong to <div className="default-line default-line-with-docs">Default: <span className="default-value">PROD</span></div> |
| <div className="path-line"><span className="path-main">usage</span></div> <div className="type-name-line"><span className="type-name">BaseUsageConfig</span></div> | The usage config to use when generating usage statistics <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;bucket&#95;duration&#x27;: &#x27;DAY&#x27;, &#x27;end&#95;time&#x27;: &#x27;2023-09-08...</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">bucket_duration</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Size of the time window to aggregate usage stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">DAY</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">end_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Latest date of lineage/usage to consider. Default: Current time in UTC  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">format_sql_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to format sql queries <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to display operational stats. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_read_operational_stats</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to report read operational stats. Experimental. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">include_top_n_queries</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ingest the top_n_queries. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">start_time</span></div> <div className="type-name-line"><span className="type-name">string(date-time)</span></div> | Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.  |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">top_n_queries</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of top queries to save to each table. <div className="default-line default-line-with-docs">Default: <span className="default-value">10</span></div> |
| <div className="path-line"><span className="path-prefix">usage.</span><span className="path-main">user_email_pattern</span></div> <div className="type-name-line"><span className="type-name">AllowDenyPattern</span></div> | regex patterns for user emails to filter in usage. <div className="default-line default-line-with-docs">Default: <span className="default-value">&#123;&#x27;allow&#x27;: &#91;&#x27;.&#42;&#x27;&#93;, &#x27;deny&#x27;: &#91;&#93;, &#x27;ignoreCase&#x27;: True&#125;</span></div> |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">allow</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">deny</span></div> <div className="type-name-line"><span className="type-name">array(string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">usage.user_email_pattern.</span><span className="path-main">ignoreCase</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to ignore case sensitivity during pattern matching. <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |

</div>
</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "SqlQueriesSourceConfig",
  "description": "Any source that connects to a platform should inherit this class",
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
    "query_file": {
      "title": "Query File",
      "description": "Path to file to ingest",
      "type": "string"
    },
    "platform": {
      "title": "Platform",
      "description": "The platform for which to generate data, e.g. snowflake",
      "type": "string"
    },
    "usage": {
      "title": "Usage",
      "description": "The usage config to use when generating usage statistics",
      "default": {
        "bucket_duration": "DAY",
        "end_time": "2023-09-08T18:00:35.098174+00:00",
        "start_time": "2023-09-07T00:00:00+00:00",
        "queries_character_limit": 24000,
        "top_n_queries": 10,
        "user_email_pattern": {
          "allow": [
            ".*"
          ],
          "deny": [],
          "ignoreCase": true
        },
        "include_operational_stats": true,
        "include_read_operational_stats": false,
        "format_sql_queries": false,
        "include_top_n_queries": true
      },
      "allOf": [
        {
          "$ref": "#/definitions/BaseUsageConfig"
        }
      ]
    },
    "default_db": {
      "title": "Default Db",
      "description": "The default database to use for unqualified table names",
      "type": "string"
    },
    "default_schema": {
      "title": "Default Schema",
      "description": "The default schema to use for unqualified table names",
      "type": "string"
    }
  },
  "required": [
    "query_file",
    "platform"
  ],
  "additionalProperties": false,
  "definitions": {
    "BucketDuration": {
      "title": "BucketDuration",
      "description": "An enumeration.",
      "enum": [
        "DAY",
        "HOUR"
      ],
      "type": "string"
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
    "BaseUsageConfig": {
      "title": "BaseUsageConfig",
      "type": "object",
      "properties": {
        "bucket_duration": {
          "description": "Size of the time window to aggregate usage stats.",
          "default": "DAY",
          "allOf": [
            {
              "$ref": "#/definitions/BucketDuration"
            }
          ]
        },
        "end_time": {
          "title": "End Time",
          "description": "Latest date of lineage/usage to consider. Default: Current time in UTC",
          "type": "string",
          "format": "date-time"
        },
        "start_time": {
          "title": "Start Time",
          "description": "Earliest date of lineage/usage to consider. Default: Last full day in UTC (or hour, depending on `bucket_duration`). You can also specify relative time with respect to end_time such as '-7 days' Or '-7d'.",
          "type": "string",
          "format": "date-time"
        },
        "top_n_queries": {
          "title": "Top N Queries",
          "description": "Number of top queries to save to each table.",
          "default": 10,
          "exclusiveMinimum": 0,
          "type": "integer"
        },
        "user_email_pattern": {
          "title": "User Email Pattern",
          "description": "regex patterns for user emails to filter in usage.",
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
        "include_operational_stats": {
          "title": "Include Operational Stats",
          "description": "Whether to display operational stats.",
          "default": true,
          "type": "boolean"
        },
        "include_read_operational_stats": {
          "title": "Include Read Operational Stats",
          "description": "Whether to report read operational stats. Experimental.",
          "default": false,
          "type": "boolean"
        },
        "format_sql_queries": {
          "title": "Format Sql Queries",
          "description": "Whether to format sql queries",
          "default": false,
          "type": "boolean"
        },
        "include_top_n_queries": {
          "title": "Include Top N Queries",
          "description": "Whether to ingest the top_n_queries.",
          "default": true,
          "type": "boolean"
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
- Class Name: `datahub.ingestion.source.sql_queries.SqlQueriesSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/sql_queries.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for SQL Queries, feel free to ping us on [our Slack](https://slack.datahubproject.io).
