-- Top products during march_2025
SELECT p.product_name, COUNT(*) AS line_items, SUM(oi.unit_price * oi.quantity) AS revenue
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
JOIN order_entry_db.order_entry.products p USING (product_id)
WHERE o.order_date::TIMESTAMP BETWEEN '2025-03-01' AND '2025-03-31 23:59:59'
GROUP BY 1 ORDER BY revenue DESC LIMIT 15;
