-- Southport Storage Facility current load + stock
SELECT COUNT(DISTINCT o.order_id) AS orders_30d,
       COUNT(DISTINCT i.product_id) AS distinct_skus,
       SUM(GREATEST(i.quantity_on_hand, 0)) AS total_units_on_hand
FROM order_entry_db.order_entry.warehouses w
LEFT JOIN order_entry_db.order_entry.orders o ON o.warehouse_id = w.warehouse_id
  AND o.order_date::TIMESTAMP >= DATEADD('day', -30, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
LEFT JOIN order_entry_db.order_entry.inventories i ON i.warehouse_id = w.warehouse_id
WHERE w.warehouse_name = 'Southport Storage Facility';
