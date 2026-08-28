-- Top products in "Tools" category
SELECT p.product_name, COUNT(*) AS orders, SUM(oi.unit_price * oi.quantity) AS revenue
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.products p USING (product_id)
JOIN order_entry_db.order_entry.product_categories c USING (category_id)
WHERE c.category_name = 'Tools'
GROUP BY 1 ORDER BY revenue DESC LIMIT 10;
