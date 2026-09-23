-- What does customer 6 buy?
SELECT c.category_name, COUNT(*) AS items, SUM(oi.unit_price * oi.quantity) AS spend
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.order_items oi USING (order_id)
JOIN order_entry_db.order_entry.products p USING (product_id)
JOIN order_entry_db.order_entry.product_categories c USING (category_id)
WHERE o.customer_id = 6
GROUP BY 1 ORDER BY spend DESC;
