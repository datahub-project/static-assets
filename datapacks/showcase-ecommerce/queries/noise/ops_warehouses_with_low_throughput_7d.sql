-- Warehouses with <5 orders in last 7 days
SELECT w.warehouse_name, COUNT(*) AS orders
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.warehouses w USING (warehouse_id)
WHERE o.order_date::TIMESTAMP >= DATEADD('day', -7, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP BY 1 HAVING COUNT(*) < 5;
