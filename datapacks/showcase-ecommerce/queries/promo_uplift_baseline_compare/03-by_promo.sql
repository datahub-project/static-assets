-- Uplift only for orders attributed to that promo (more conservative)
-- Author: Sarah Chen — strictly attributed revenue, not all revenue in window

WITH p AS (
    SELECT promotion_id, promotion_name,
           promotion_start_date::TIMESTAMP AS ps, promotion_end_date::TIMESTAMP AS pe,
           DATEDIFF('day', promotion_start_date::TIMESTAMP, promotion_end_date::TIMESTAMP) AS length_days
    FROM   order_entry_db.order_entry.promotions
    WHERE  promotion_end_date IS NOT NULL
)
SELECT p.promotion_name,
       SUM(CASE WHEN o.promotion_id = p.promotion_id
                  AND o.order_date::TIMESTAMP BETWEEN p.ps AND p.pe
                THEN o.order_total ELSE 0 END) AS attributed_revenue_during,
       SUM(CASE WHEN o.order_date::TIMESTAMP BETWEEN DATEADD('day', -p.length_days, p.ps) AND p.ps
                THEN o.order_total ELSE 0 END) AS baseline_revenue_before
FROM   p
CROSS  JOIN order_entry_db.order_entry.orders o
GROUP  BY p.promotion_name
ORDER  BY attributed_revenue_during DESC;
