-- Revenue by customer class — matches the glossary term definition
-- Author: BID
-- order_details is line-item grain and repeats order_total on every line,
-- so collapse to one row per order before summing.

WITH order_header AS (
    SELECT order_id,
           ANY_VALUE(customer_class) AS customer_class,
           ANY_VALUE(order_total)    AS order_total,
           ANY_VALUE(order_status)   AS order_status
    FROM   order_entry_db.analytics.order_details
    GROUP  BY order_id
)
SELECT customer_class,
       SUM(order_total) AS total_revenue,
       COUNT(*)         AS order_count,
       AVG(order_total) AS avg_order_value
FROM   order_header
WHERE  order_status NOT IN (3, 4)
GROUP  BY customer_class
ORDER  BY total_revenue DESC
;
