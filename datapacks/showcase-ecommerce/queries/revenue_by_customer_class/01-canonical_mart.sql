-- Revenue by customer class — matches the glossary term definition
-- Author: BID

SELECT customer_class,
       SUM(order_total)         AS total_revenue,
       COUNT(DISTINCT order_id) AS order_count,
       AVG(order_total)         AS avg_order_value
FROM   order_entry_db.analytics.order_details
GROUP  BY customer_class
ORDER  BY total_revenue DESC
;
