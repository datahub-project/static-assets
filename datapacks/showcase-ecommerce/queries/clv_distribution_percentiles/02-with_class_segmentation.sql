-- CLV percentiles within each customer class
-- Author: David Kim

WITH clv AS (
    SELECT c.customer_id, c.customer_class, SUM(o.order_total) AS lifetime_revenue
    FROM   order_entry_db.order_entry.orders    o
    JOIN   order_entry_db.order_entry.customers c USING (customer_id)
    WHERE  o.order_status NOT IN (3, 4)
    GROUP  BY 1, 2
)
SELECT customer_class,
       COUNT(*) AS customers,
       MEDIAN(lifetime_revenue) AS p50,
       PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY lifetime_revenue) AS p90,
       MAX(lifetime_revenue) AS max_clv
FROM   clv
GROUP  BY 1
ORDER  BY p90 DESC
;
