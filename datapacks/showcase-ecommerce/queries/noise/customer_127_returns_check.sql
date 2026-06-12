-- Return history for customer 127
SELECT oi.line_item_id, p.product_name, oi.dispatch_date, oi.return_date,
       DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.return_date::TIMESTAMP) AS days_to_return
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.order_items oi USING (order_id)
JOIN order_entry_db.order_entry.products p USING (product_id)
WHERE o.customer_id = 127 AND oi.return_date IS NOT NULL
ORDER BY oi.return_date DESC;
