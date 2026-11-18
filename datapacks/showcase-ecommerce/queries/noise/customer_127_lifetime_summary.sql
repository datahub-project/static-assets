-- Lifetime summary for 127
SELECT COUNT(DISTINCT order_id) AS lifetime_orders,
       SUM(order_total) AS lifetime_revenue,
       AVG(order_total) AS aov,
       MIN(order_date) AS first_order,
       MAX(order_date) AS most_recent_order
FROM order_entry_db.order_entry.orders
WHERE customer_id = 127 AND order_status NOT IN (3, 4);
