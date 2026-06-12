# Showcase E-Commerce — Query Corpus

This directory holds the source SQL files that produce `04-queries.json` in the parent datapack. Each `urn:li:query` MCP in `04-queries.json` corresponds to exactly one `.sql` file here.

## Layout

```
queries/
├── README.md                ← this file
├── intent-matrix.yaml       ← top-level index of all 50 intents
├── <intent_id>/             ← one dir per intent (50 dirs)
│   ├── 00-intent.yaml       ← intent metadata: question, canonical def, variant names
│   └── 0N-<variant>.sql     ← 2–5 SQL variants per intent
└── noise/                   ← 152 ad-hoc / one-off queries (long-tail)
    └── *.sql
```

## What's "cluster" vs. "noise"?

- **Cluster** (`<intent_id>/*.sql`, 160 files): variants of 50 distinct intents. Each cluster should collapse to a single anchor in the text-to-SQL pipeline. Variants vary on join path (raw vs `analytics.order_details` mart), filter idiom, CTE-vs-subquery, persona writing style, and occasionally an intentional "wrong-but-equivalent" shape.
- **Noise** (`noise/*.sql`, 152 files): one-off analyst queries — customer/order/product/promotion drill-downs against specific IDs, date-window investigations, DQ checks, schema exploration, abandoned half-finished queries. These should *not* cluster cleanly.

## Author personas

Comments use these shorthand author labels; the build script maps them to real corpuser URNs in the datapack:

| Persona | corpuser URN suffix |
|---|---|
| Sarah Chen (Senior Data Analyst) | `sam@example.com` |
| Andrea Garcia (Analytics Engineer) | `alex@example.com` |
| David Kim (Data Scientist) | `brock1@example.com` |
| Ben Porter (Data Engineer) | `bryan@example.com` |
| Julia Novak (Data Quality Engineer) | `jonny1@example.com` |
| James Wilson (BI Developer) | `jonny2@example.com` |
| Karen Okonkwo (Product Manager) | `kirk@example.com` |
| Ian Chen (Director of Data) | `EMP006` |

## Data realities to be aware of (gotchas baked into the SQL)

The `ORDER_ENTRY_DB` schema diverges from the original docs in several ways. Queries here use the actual values:

- `orders.order_status` is **NUMBER 0..4** (not strings like `Cancelled`/`On Hold`). Best-guess exclusion: `NOT IN (3, 4)`.
- `customers.mailshot` / `partner_mailshot` are **0/1 NUMBER**, not `'Y'`/`'N'` strings.
- `customers.country_id` has values 21..9991 — **not a valid FK** to the 25-row `countries` table. Resolve country via `addresses.country_id` instead.
- Enum values for `order_mode`, `delivery_type`, `payment_method_code`, `customer_class`, `condition`, `product_status` all differ from the original spec — see any cluster query for the actual values.
- All date columns are **TEXT**, not DATE/TIMESTAMP. Queries cast with `::TIMESTAMP`.
- Data window: **2024-05-14 to 2025-05-14** (1 year). Time-relative queries anchor on `MAX(order_date)` rather than `CURRENT_DATE` so they keep returning data as the datapack ages.
- 100% of dispatched items have a `return_date` populated, so global return-rate = 100%. Return-rate intents use **time-windowed** variants (e.g., "returned within 30 days of dispatch") to surface real variance.
- All customers have an `account_mgr_id` — any "B2C only" filter returns 0 rows.
- 0 products are OOS across all warehouses; 50% of `(product, warehouse)` pairs are below `restock_level`.

## Notable demo-grade findings the corpus surfaces

- **Negative discount rates** — `discount_rate_by_promo` returns -73% for Travel Hair Straightener and -131% for Vanilla Bean Ice Cream because `unit_price > list_price` in the data.
- **Promotion misattribution** — `orders_outside_promo_window` finds 4028 / 5027 promoted orders fall outside their promo's date window; all 50 promotions affected.
- **Pickup invariant violation** — `pickup_orders_missing_delivery_addr` finds 1250 violations (In-Store Pickup orders with a `delivery_address_id`).
- **Negative dispatch lead time** — three warehouses show negative avg days from order to dispatch (dispatch_date predates order_date).
- **Order header ≠ line sum** — order 9866 has `order_total = $210` but its line items sum to $1000 (a $790 gap).

## How to add a new intent

1. Create a directory `queries/<intent_id>/`.
2. Add `00-intent.yaml` with the fields below.
3. Write 2–5 `.sql` files, each with an author comment header and a meaningful name like `01-canonical.sql`, `02-mart_version.sql`, `03-anti_join_pattern.sql`.
4. Add an entry to `queries/intent-matrix.yaml`.
5. Rebuild `04-queries.json` (the build script reads this directory).

### `00-intent.yaml` schema

```yaml
id: my_new_intent
data_product: Order Entry Analytics
question: "Plain-English question this intent answers"
metric: GMV                           # optional — one of the canonical KPIs
primary_tables:
  - order_entry_db.order_entry.orders
variants:
  - canonical
  - mart_version
  - with_yoy_compare
notes: |
  Any caveats about the data, intentional anti-shapes, etc.
```

## Build

Producing `04-queries.json` from this tree is a one-shot script (kept alongside the datapack-build tooling) that:
1. Walks each intent dir + `noise/`
2. Reads each `.sql` file
3. Detects author from the `-- Author:` comment line
4. Scans for `order_entry_db.<schema>.<table>` references to populate `querySubjects`
5. Assigns a random `created` timestamp inside the data window (2024-06 → 2025-05) so the corpus looks like a real activity history
6. Emits one `urn:li:query` entity per file with `queryProperties` + `querySubjects` + `dataPlatformInstance` + `subTypes` aspects
