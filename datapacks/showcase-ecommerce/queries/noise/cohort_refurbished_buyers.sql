-- Who buys refurbished?
SELECT c.customer_class, COUNT(DISTINCT o.order_id) AS orders, COUNT(*) AS refurb_lines
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
JOIN order_entry_db.order_entry.customers c USING (customer_id)
WHERE oi.condition = 'Refurbished'
GROUP BY 1 ORDER BY refurb_lines DESC;
