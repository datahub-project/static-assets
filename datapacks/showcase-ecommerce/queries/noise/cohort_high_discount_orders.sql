-- Who gets the >30% discounts?
SELECT customer_class, COUNT(DISTINCT order_id) AS orders, AVG(discount_percent) AS avg_discount
FROM order_entry_db.analytics.order_details
WHERE discount_percent > 30
GROUP BY 1 ORDER BY orders DESC;
