-- AOV by month with prior-year side-by-side
-- Author: Ian Chen — exec deck

WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
           SUM(order_total) / COUNT(DISTINCT order_id)      AS aov,
           COUNT(DISTINCT order_id)                          AS order_count
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT cur.order_month,
       cur.aov                                       AS aov_current,
       prv.aov                                       AS aov_prior_year,
       cur.aov - prv.aov                             AS yoy_delta,
       (cur.aov - prv.aov) / NULLIF(prv.aov, 0) * 100 AS yoy_pct
FROM   monthly cur
LEFT   JOIN monthly prv
       ON   prv.order_month = DATEADD('year', -1, cur.order_month)
ORDER  BY cur.order_month
;
