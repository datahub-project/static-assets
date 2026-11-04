-- Monthly sales of Water Bottle with Built-in Fruit Infuser (product 555, status Active)
SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS month,
       COUNT(*) AS line_items, SUM(oi.quantity) AS units, SUM(oi.unit_price * oi.quantity) AS revenue
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
WHERE oi.product_id = 555
GROUP BY 1 ORDER BY 1;
