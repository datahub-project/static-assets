---
sidebar_position: 23
title: Feast
slug: /generated/ingestion/sources/feast
custom_edit_url: >-
  https://github.com/datahub-project/datahub/blob/master/docs/generated/ingestion/sources/feast.md
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Feast
![Certified](https://img.shields.io/badge/support%20status-certified-brightgreen)


### Important Capabilities
| Capability | Status | Notes |
| ---------- | ------ | ----- |
| Descriptions | ✅ | Enabled by default. |
| [Detect Deleted Entities](../../../../metadata-ingestion/docs/dev_guides/stateful.md#stale-entity-removal) | ✅ | Enabled by default via stateful ingestion. |
| Schema Metadata | ✅ | Enabled by default. |
| Table-Level Lineage | ✅ | Enabled by default. |



### CLI based Ingestion

### Starter Recipe
Check out the following recipe to get started with ingestion! See [below](#config-details) for full configuration options.


For general pointers on writing and running a recipe, see our [main recipe guide](../../../../metadata-ingestion/README.md#recipes).
```yaml
source:
  type: feast
  config:
    # Coordinates
    path: "/path/to/repository/"
    # Options
    environment: "PROD"

sink:
  # sink configs

```

### Code Coordinates
- Class Name: `datahub.ingestion.source.feast.FeastRepositorySource`

<h2>Questions</h2>

If you've got any questions on configuring ingestion for Feast, feel free to ping us on [our Slack](https://datahub.com/slack).
