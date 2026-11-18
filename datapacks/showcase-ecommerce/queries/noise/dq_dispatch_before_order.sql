-- How often does dispatch_date precede order_date? (suspected data bug)
SELECT COUNT(*) AS items
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.order_items oi USING (order_id)
WHERE oi.dispatch_date::TIMESTAMP < o.order_date::TIMESTAMP;
