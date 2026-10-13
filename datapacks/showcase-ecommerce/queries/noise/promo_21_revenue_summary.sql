-- Summary stats for "Spicy Hummus"
SELECT COUNT(DISTINCT o.order_id) AS orders,
       SUM(o.order_total) AS attributed_revenue,
       AVG(o.order_total) AS aov,
       MIN(o.order_date) AS first_order,
       MAX(o.order_date) AS last_order
FROM order_entry_db.order_entry.orders o
WHERE o.promotion_id = 21;
