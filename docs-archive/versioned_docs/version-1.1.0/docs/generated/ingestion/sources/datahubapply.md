---
sidebar_position: 12
title: DataHubApply
slug: /generated/ingestion/sources/datahubapply
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/datahubapply.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DataHubApply
![Testing](https://img.shields.io/badge/support%20status-testing-lightgrey)


This source is a helper over CLI
so people can use the helper to apply various metadata changes to DataHub
via Managed Ingestion


### CLI based Ingestion

### Config Details
<Tabs>
                <TabItem value="options" label="Options" default>

Note that a `.` is used to denote nested fields in the YAML recipe.


<div className='config-table'>

| Field | Description |
|:--- |:--- |
| <div className="path-line"><span className="path-main">domain_apply</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List to apply domains to assets  |
| <div className="path-line"><span className="path-prefix">domain_apply.</span><span className="path-main">DomainApplyConfig</span></div> <div className="type-name-line"><span className="type-name">DomainApplyConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">domain_apply.DomainApplyConfig.</span><span className="path-main">domain_urn</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-prefix">domain_apply.DomainApplyConfig.</span><span className="path-main">assets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of assets to apply domain hierarchichaly. Currently only containers and datasets are supported  |
| <div className="path-line"><span className="path-prefix">domain_apply.DomainApplyConfig.assets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">owner_apply</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List to apply owners to assets  |
| <div className="path-line"><span className="path-prefix">owner_apply.</span><span className="path-main">OwnerApplyConfig</span></div> <div className="type-name-line"><span className="type-name">OwnerApplyConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">owner_apply.OwnerApplyConfig.</span><span className="path-main">owner_urn</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-prefix">owner_apply.OwnerApplyConfig.</span><span className="path-main">assets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of assets to apply owner hierarchichaly. Currently only containers and datasets are supported  |
| <div className="path-line"><span className="path-prefix">owner_apply.OwnerApplyConfig.assets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">tag_apply</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List to apply tags to assets  |
| <div className="path-line"><span className="path-prefix">tag_apply.</span><span className="path-main">TagApplyConfig</span></div> <div className="type-name-line"><span className="type-name">TagApplyConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">tag_apply.TagApplyConfig.</span><span className="path-main">tag_urn</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-prefix">tag_apply.TagApplyConfig.</span><span className="path-main">assets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of assets to apply tag hierarchichaly. Currently only containers and datasets are supported  |
| <div className="path-line"><span className="path-prefix">tag_apply.TagApplyConfig.assets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |
| <div className="path-line"><span className="path-main">term_apply</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List to apply terms to assets  |
| <div className="path-line"><span className="path-prefix">term_apply.</span><span className="path-main">TermApplyConfig</span></div> <div className="type-name-line"><span className="type-name">TermApplyConfig</span></div> |   |
| <div className="path-line"><span className="path-prefix">term_apply.TermApplyConfig.</span><span className="path-main">term_urn</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |  <div className="default-line ">Default: <span className="default-value"></span></div> |
| <div className="path-line"><span className="path-prefix">term_apply.TermApplyConfig.</span><span className="path-main">assets</span></div> <div className="type-name-line"><span className="type-name">array</span></div> | List of assets to apply term hierarchichaly. Currently only containers and datasets are supported  |
| <div className="path-line"><span className="path-prefix">term_apply.TermApplyConfig.assets.</span><span className="path-main">string</span></div> <div className="type-name-line"><span className="type-name">string</span></div> |   |

</div>


</TabItem>
<TabItem value="schema" label="Schema">

The [JSONSchema](https://json-schema.org/) for this configuration is inlined below.


```javascript
{
  "title": "DataHubApplyConfig",
  "type": "object",
  "properties": {
    "domain_apply": {
      "title": "Domain Apply",
      "description": "List to apply domains to assets",
      "type": "array",
      "items": {
        "$ref": "#/definitions/DomainApplyConfig"
      }
    },
    "tag_apply": {
      "title": "Tag Apply",
      "description": "List to apply tags to assets",
      "type": "array",
      "items": {
        "$ref": "#/definitions/TagApplyConfig"
      }
    },
    "term_apply": {
      "title": "Term Apply",
      "description": "List to apply terms to assets",
      "type": "array",
      "items": {
        "$ref": "#/definitions/TermApplyConfig"
      }
    },
    "owner_apply": {
      "title": "Owner Apply",
      "description": "List to apply owners to assets",
      "type": "array",
      "items": {
        "$ref": "#/definitions/OwnerApplyConfig"
      }
    }
  },
  "additionalProperties": false,
  "definitions": {
    "DomainApplyConfig": {
      "title": "DomainApplyConfig",
      "type": "object",
      "properties": {
        "assets": {
          "title": "Assets",
          "description": "List of assets to apply domain hierarchichaly. Currently only containers and datasets are supported",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "domain_urn": {
          "title": "Domain Urn",
          "default": "",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "TagApplyConfig": {
      "title": "TagApplyConfig",
      "type": "object",
      "properties": {
        "assets": {
          "title": "Assets",
          "description": "List of assets to apply tag hierarchichaly. Currently only containers and datasets are supported",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tag_urn": {
          "title": "Tag Urn",
          "default": "",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "TermApplyConfig": {
      "title": "TermApplyConfig",
      "type": "object",
      "properties": {
        "assets": {
          "title": "Assets",
          "description": "List of assets to apply term hierarchichaly. Currently only containers and datasets are supported",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "term_urn": {
          "title": "Term Urn",
          "default": "",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "OwnerApplyConfig": {
      "title": "OwnerApplyConfig",
      "type": "object",
      "properties": {
        "assets": {
          "title": "Assets",
          "description": "List of assets to apply owner hierarchichaly. Currently only containers and datasets are supported",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "owner_urn": {
          "title": "Owner Urn",
          "default": "",
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
- Class Name: `datahub.ingestion.source.apply.datahub_apply.DataHubApplySource`
- Browse on [GitHub](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/src/datahub/ingestion/source/apply/datahub_apply.py)


<h2>Questions</h2>

If you've got any questions on configuring ingestion for DataHubApply, feel free to ping us on [our Slack](https://datahub.com/slack).
