---
sidebar_position: 15
title: DataHubMockData
slug: /generated/ingestion/sources/datahubmockdata
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahubmockdata.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubMockData
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


This source is for generating mock data for testing purposes.
Expect breaking changes as we iterate on the mock data source.


### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">enabled</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether this source is enabled <div className="default-line default-line-with-docs">Default: <span className="default-value">True</span></div> |
| <div className="path-line"><span className="path-main">gen_1</span></div> <div className="type-name-line"><span className="type-name">LineageConfigGen1</span></div> | Configuration for lineage data generation  |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">emit_lineage</span></div> <div className="type-name-line"><span className="type-name">boolean</span></div> | Whether to emit lineage data for testing purposes. When False, no lineage data is generated regardless of other settings. <div className="default-line default-line-with-docs">Default: <span className="default-value">False</span></div> |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">level_subtypes</span></div> <div className="type-name-line"><span className="type-name">map(str,string)</span></div> |   |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">lineage_fan_out</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of downstream tables that each upstream table connects to. This controls the 'width' of the lineage graph. Higher values create more parallel downstream tables per level. <div className="default-line default-line-with-docs">Default: <span className="default-value">3</span></div> |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">lineage_fan_out_after_first_hop</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Optional limit on fanout for hops after the first hop. When set, prevents exponential growth by limiting the number of downstream tables per upstream table at levels 2 and beyond. When None, uses the standard exponential growth (lineage_fan_out^level).  |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">lineage_hops</span></div> <div className="type-name-line"><span className="type-name">integer</span></div> | Number of hops (levels) in the lineage graph. This controls the 'depth' of the lineage graph. Level 0 is the root table, and each subsequent level contains downstream tables. Higher values create deeper lineage chains. <div className="default-line default-line-with-docs">Default: <span className="default-value">2</span></div> |
| <div className="path-line"><span className="path-prefix">gen_1.</span><span className="path-main">subtype_pattern</span></div> <div className="type-name-line"><span className="type-name">Enum</span></div> | Pattern for determining SubTypes. Options: 'alternating', 'all_table', 'all_view', 'level_based' <div className="default-line default-line-with-docs">Default: <span className="default-value">alternating</span></div> |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataHubMockDataConfig",
  "type": "object",
  "properties": {
    "enabled": {
      "title": "Enabled",
      "description": "Whether this source is enabled",
      "default": true,
      "type": "boolean"
    },
    "gen_1": {
      "title": "Gen 1",
      "description": "Configuration for lineage data generation",
      "allOf": [
        {
          "$ref": "#/definitions/LineageConfigGen1"
        }
      ]
    }
  },
  "additionalProperties": false,
  "definitions": {
    "SubTypePattern": {
      "title": "SubTypePattern",
      "description": "An enumeration.",
      "enum": [
        "alternating",
        "all_table",
        "all_view",
        "level_based"
      ],
      "type": "string"
    },
    "LineageConfigGen1": {
      "title": "LineageConfigGen1",
      "description": "Configuration for generating mock lineage data for testing purposes.\n\nThis configuration controls how the mock data source generates a hierarchical\nlineage graph with multiple levels of upstream/downstream relationships.\n\nThe lineage graph is structured as follows:\n- Level 0: 1 table (root)\n- Level 1: lineage_fan_out tables (each connected to the root)\n- Level 2+: If lineage_fan_out_after_first_hop is set, uses that value;\n            otherwise uses lineage_fan_out^level tables (each connected to a level 1 table)\n- ... and so on for lineage_hops levels\n\nExamples:\n    - With lineage_fan_out=2, lineage_hops=1: Creates 3 tables total\n      (1 root + 2 downstream) with 2 lineage relationships\n    - With lineage_fan_out=3, lineage_hops=2: Creates 13 tables total\n      (1 + 3 + 9) with 12 lineage relationships\n    - With lineage_fan_out=4, lineage_hops=1: Creates 5 tables total\n      (1 + 4) with 4 lineage relationships\n    - With lineage_fan_out=3, lineage_hops=3, lineage_fan_out_after_first_hop=2:\n      Creates 1 + 3 + 6 + 12 = 22 tables total (prevents exponential growth)\n\nTable naming convention: \"hops_{lineage_hops}_f_{lineage_fan_out}_h{level}_t{table_index}\"",
      "type": "object",
      "properties": {
        "emit_lineage": {
          "title": "Emit Lineage",
          "description": "Whether to emit lineage data for testing purposes. When False, no lineage data is generated regardless of other settings.",
          "default": false,
          "type": "boolean"
        },
        "lineage_fan_out": {
          "title": "Lineage Fan Out",
          "description": "Number of downstream tables that each upstream table connects to. This controls the 'width' of the lineage graph. Higher values create more parallel downstream tables per level.",
          "default": 3,
          "type": "integer"
        },
        "lineage_hops": {
          "title": "Lineage Hops",
          "description": "Number of hops (levels) in the lineage graph. This controls the 'depth' of the lineage graph. Level 0 is the root table, and each subsequent level contains downstream tables. Higher values create deeper lineage chains.",
          "default": 2,
          "type": "integer"
        },
        "lineage_fan_out_after_first_hop": {
          "title": "Lineage Fan Out After First Hop",
          "description": "Optional limit on fanout for hops after the first hop. When set, prevents exponential growth by limiting the number of downstream tables per upstream table at levels 2 and beyond. When None, uses the standard exponential growth (lineage_fan_out^level).",
          "type": "integer"
        },
        "subtype_pattern": {
          "description": "Pattern for determining SubTypes. Options: 'alternating', 'all_table', 'all_view', 'level_based'",
          "default": "alternating",
          "allOf": [
            {
              "$ref": "#/definitions/SubTypePattern"
            }
          ]
        },
        "level_subtypes": {
          "title": "Level Subtypes",
          "description": "Mapping of level to subtype for level_based pattern",
          "default": {
            "0": "Table",
            "1": "View",
            "2": "Table"
          },
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
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
- Class Name: `datahub.ingestion.source.mock_data.datahub_mock_data.DataHubMockDataSource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/mock_data/datahub_mock_data.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHubMockData, feel free to ping us on [our Slack](https://datahub.com/slack).
