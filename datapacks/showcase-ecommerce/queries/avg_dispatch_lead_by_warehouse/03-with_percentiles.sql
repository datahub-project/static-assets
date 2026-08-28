-- Dispatch lead percentiles by warehouse
-- Author: David Kim — the avg is misleading without the tail

WITH lead AS (
    SELECT w.warehouse_name,
           DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP) AS days_to_dispatch
    FROM   order_entry_db.order_entry.orders      o
    JOIN   order_entry_db.order_entry.order_items oi USING (order_id)
    JOIN   order_entry_db.order_entry.warehouses  w  USING (warehouse_id)
    WHERE  oi.dispatch_date IS NOT NULL
)
SELECT warehouse_name,
       COUNT(*)                                                            AS line_items,
       AVG(days_to_dispatch)                                                AS mean_days,
       MEDIAN(days_to_dispatch)                                             AS p50_days,
       PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY days_to_dispatch)        AS p90_days,
       PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days_to_dispatch)       AS p95_days
FROM   lead
GROUP  BY 1
ORDER  BY p90_days
;
