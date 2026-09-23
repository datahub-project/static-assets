-- CLV distribution
-- Author: David Kim

WITH clv AS (
    SELECT customer_id, SUM(order_total) AS lifetime_revenue
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT
    COUNT(*)                                                       AS customers,
    AVG(lifetime_revenue)                                          AS mean_clv,
    MEDIAN(lifetime_revenue)                                       AS p50,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY lifetime_revenue) AS p75,
    PERCENTILE_CONT(0.9)  WITHIN GROUP (ORDER BY lifetime_revenue) AS p90,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY lifetime_revenue) AS p95,
    PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY lifetime_revenue) AS p99,
    MAX(lifetime_revenue)                                          AS max_clv
FROM   clv
;
