-- WoW via self-join — older style but easier to read for some folks
-- Author: Andrea Garcia

WITH weekly AS (
    SELECT DATE_TRUNC('week', order_date::TIMESTAMP)::DATE AS week_start,
           SUM(order_total)                                AS revenue
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT cur.week_start,
       cur.revenue                            AS current_revenue,
       prv.revenue                            AS prior_week_revenue,
       cur.revenue - prv.revenue              AS wow_delta,
       (cur.revenue - prv.revenue) / NULLIF(prv.revenue, 0) * 100 AS wow_pct
FROM   weekly cur
LEFT   JOIN weekly prv
       ON   prv.week_start = DATEADD('week', -1, cur.week_start)
ORDER  BY cur.week_start
;
