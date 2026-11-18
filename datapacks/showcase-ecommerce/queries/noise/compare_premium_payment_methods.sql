-- Which payment methods do high-tier customer classes prefer?
SELECT payment_method_code, COUNT(*) AS orders, AVG(order_total) AS aov
FROM order_entry_db.analytics.order_details
WHERE customer_class IN ('Enterprise', 'Healthcare', 'Government')
GROUP BY 1 ORDER BY aov DESC;
