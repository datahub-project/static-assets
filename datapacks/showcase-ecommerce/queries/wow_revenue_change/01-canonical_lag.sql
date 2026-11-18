-- WoW revenue change using LAG
-- Author: Sarah Chen — weekly trend tile

WITH weekly AS (
    SELECT DATE_TRUNC('week', order_date::TIMESTAMP)::DATE AS week_start,
           SUM(order_total)                                AS revenue,
           COUNT(*)                                        AS orders
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT week_start,
       revenue,
       orders,
       LAG(revenue, 1) OVER (ORDER BY week_start)               AS prior_week_revenue,
       revenue - LAG(revenue, 1) OVER (ORDER BY week_start)     AS wow_delta,
       (revenue - LAG(revenue, 1) OVER (ORDER BY week_start))
           / NULLIF(LAG(revenue, 1) OVER (ORDER BY week_start), 0) * 100 AS wow_pct
FROM   weekly
ORDER  BY week_start
;
