-- Order → dispatch lead time distribution
-- Author: David Kim — looking at tail risk for the SLA review

WITH lead AS (
    SELECT DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP) AS days_to_dispatch
    FROM   order_entry_db.order_entry.orders      o
    JOIN   order_entry_db.order_entry.order_items oi USING (order_id)
    WHERE  oi.dispatch_date IS NOT NULL
)
SELECT
    AVG(days_to_dispatch)                                       AS mean_days,
    MEDIAN(days_to_dispatch)                                    AS p50_days,
    PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY days_to_dispatch) AS p90_days,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days_to_dispatch) AS p95_days,
    MAX(days_to_dispatch)                                        AS max_days,
    COUNT(*)                                                     AS line_items
FROM lead
;
