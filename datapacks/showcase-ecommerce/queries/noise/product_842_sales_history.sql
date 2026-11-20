-- Monthly sales of Smart Wi-Fi Light Bulbs (product 842, status Out of Stock)
SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS month,
       COUNT(*) AS line_items, SUM(oi.quantity) AS units, SUM(oi.unit_price * oi.quantity) AS revenue
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
WHERE oi.product_id = 842
GROUP BY 1 ORDER BY 1;
