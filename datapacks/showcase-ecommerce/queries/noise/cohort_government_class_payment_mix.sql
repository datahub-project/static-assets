-- How does Government customer class pay?
SELECT payment_method_code, COUNT(*) AS orders, AVG(order_total) AS aov
FROM order_entry_db.analytics.order_details
WHERE customer_class = 'Government'
GROUP BY 1 ORDER BY orders DESC;
