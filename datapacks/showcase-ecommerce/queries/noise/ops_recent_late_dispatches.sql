-- Dispatches >7 days from order, last 30d
SELECT COUNT(*) AS late_items
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
WHERE DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP) > 7
  AND o.order_date::TIMESTAMP >= DATEADD('day', -30, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders));
