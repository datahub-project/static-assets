-- Highest-value orders in the last 2 weeks
SELECT order_id, order_date, order_total, customer_id, delivery_type
FROM order_entry_db.order_entry.orders
WHERE order_total > 290
  AND order_date::TIMESTAMP >= DATEADD('day', -14, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
ORDER BY order_total DESC LIMIT 20;
