# Fiction Retail E-Commerce Dataset

A synthetic e-commerce dataset simulating a mid-sized global retail operation. It covers the full order lifecycle — from customer acquisition through purchasing, fulfillment, shipment, and returns — across 10 interconnected tables.

All data is entirely fictional and generated for analytical and educational use.

**Source:** [Kaggle — Fiction Retail E-Commerce Dataset](https://www.kaggle.com/datasets/nasalakshay/fiction-retail-e-commerce-dataset)  
**License:** [CC0 1.0 Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) — no attribution required, free for any use

---

## What's Included

| File | Description |
|---|---|
| `fiction-retail.db` | Single SQLite database containing all 10 tables below (~95 MB) |
| `ingest.yaml` | DataHub ingestion recipe — loads all 10 tables into DataHub |
| `add_lineage.py` | Emits FK-based lineage between tables after ingestion |
| `add_metadata.py` | Adds tags, glossary terms, and ownership after ingestion |

### Quick Start

```bash
# Prerequisites
pip install 'acryl-datahub[sqlalchemy,datahub-rest]'
# DataHub must be running locally

datahub ingest -c ingest.yaml
python add_lineage.py
python add_metadata.py
```

---

## Schema

### `customers` — 50,000 rows

| Column | Type | Description |
|---|---|---|
| `customer_id` | TEXT | Unique customer identifier |
| `name` | TEXT | Full name |
| `email` | TEXT | Email address |
| `phone` | TEXT | Phone number |
| `signup_date` | TEXT | Date the customer registered |
| `country` | TEXT | Country of residence |
| `state` | TEXT | State / province |
| `city` | TEXT | City |
| `customer_segment` | TEXT | Segment label (e.g. Wholesale, Retail) |

---

### `orders` — 150,000 rows

| Column | Type | Description |
|---|---|---|
| `order_id` | TEXT | Unique order identifier |
| `customer_id` | TEXT | FK → `customers.customer_id` |
| `order_date` | TEXT | Date the order was placed |
| `order_status` | TEXT | Status (e.g. Delivered, Cancelled, Returned) |
| `total_amount` | REAL | Total order value in USD |
| `payment_method` | TEXT | Payment method used |
| `shipping_country` | TEXT | Destination country |
| `promo_id` | TEXT | FK → `promotions.promo_id` (nullable) |

---

### `order_items` — 346,202 rows

| Column | Type | Description |
|---|---|---|
| `order_item_id` | TEXT | Unique line-item identifier |
| `order_id` | TEXT | FK → `orders.order_id` |
| `product_id` | TEXT | FK → `products.product_id` |
| `quantity` | INTEGER | Units ordered |
| `unit_price` | REAL | Price per unit at time of order |
| `discount_pct` | REAL | Discount percentage applied |

---

### `products` — 5,000 rows

| Column | Type | Description |
|---|---|---|
| `product_id` | TEXT | Unique product identifier |
| `name` | TEXT | Product name |
| `category` | TEXT | Product category |
| `brand` | TEXT | Brand name |
| `price` | REAL | List price in USD |
| `weight_kg` | REAL | Weight in kilograms |
| `supplier_id` | TEXT | FK → `suppliers.supplier_id` |

---

### `suppliers` — 500 rows

| Column | Type | Description |
|---|---|---|
| `supplier_id` | TEXT | Unique supplier identifier |
| `name` | TEXT | Supplier name |
| `country` | TEXT | Country of operation |
| `contract_start_date` | TEXT | Date the supplier contract began |
| `status` | TEXT | Active / Inactive |

---

### `inventory` — 11,476 rows

| Column | Type | Description |
|---|---|---|
| `inventory_id` | TEXT | Unique inventory record identifier |
| `product_id` | TEXT | FK → `products.product_id` |
| `warehouse_id` | TEXT | FK → `warehouses.warehouse_id` |
| `quantity_on_hand` | INTEGER | Current stock count |
| `reserved_quantity` | INTEGER | Units reserved for open orders |
| `reorder_threshold` | INTEGER | Stock level that triggers a reorder |
| `last_restocked_date` | TEXT | Date of most recent restock |

---

### `warehouses` — 15 rows

| Column | Type | Description |
|---|---|---|
| `warehouse_id` | TEXT | Unique warehouse identifier |
| `name` | TEXT | Warehouse name |
| `city` | TEXT | City |
| `state` | TEXT | State / province |
| `country` | TEXT | Country |
| `capacity_units` | INTEGER | Maximum storage capacity in units |
| `opened_date` | TEXT | Date the warehouse opened |

---

### `shipments` — 119,936 rows

| Column | Type | Description |
|---|---|---|
| `shipment_id` | TEXT | Unique shipment identifier |
| `order_id` | TEXT | FK → `orders.order_id` |
| `warehouse_id` | TEXT | FK → `warehouses.warehouse_id` |
| `carrier` | TEXT | Carrier name |
| `tracking_number` | TEXT | Carrier tracking number |
| `shipped_date` | TEXT | Date shipped |
| `delivered_date` | TEXT | Date delivered (nullable if in transit) |
| `shipment_state` | TEXT | State of shipment (e.g. Delivered, In Transit) |

---

### `returns` — 11,934 rows

| Column | Type | Description |
|---|---|---|
| `return_id` | TEXT | Unique return identifier |
| `order_id` | TEXT | FK → `orders.order_id` |
| `product_id` | TEXT | FK → `products.product_id` |
| `return_date` | TEXT | Date the return was initiated |
| `refund_amount` | REAL | Refund value in USD |
| `return_reason_code` | TEXT | Reason code (e.g. Defective, Wrong Item) |
| `processed_by` | TEXT | Agent or system that processed the return |

---

### `promotions` — 200 rows

| Column | Type | Description |
|---|---|---|
| `promo_id` | TEXT | Unique promotion identifier |
| `promo_code` | TEXT | Alphanumeric promo code |
| `description` | TEXT | Human-readable description |
| `discount_pct` | REAL | Discount percentage |
| `valid_from` | TEXT | Promotion start date |
| `valid_until` | TEXT | Promotion end date |
| `applies_to_category` | TEXT | Product category the promo applies to (nullable = all) |
| `max_uses` | INTEGER | Maximum redemption count |
| `status` | TEXT | Active / Expired |

---

## Key Relationships

```
customers ──< orders ──< order_items >── products >── suppliers
                │                             │
                │                         inventory >── warehouses
                │
           shipments >── warehouses
                │
            returns
                │
          promotions (via orders.promo_id)
```

All foreign keys are present in the data but not enforced at the SQLite level (no `FOREIGN KEY` constraints), consistent with a typical analytical dataset.
