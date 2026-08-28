-- Monthly GMV — last 12 months
-- Author: Sarah Chen (Senior Data Analyst)
-- Source: orders (raw). For the same number off the mart, see 02-mart_shortcut.sql.
--
-- GMV = SUM(order_total) on completed orders. Per Key Metrics Reference doc,
-- this is "gross" — does NOT subtract returns. See net_revenue_monthly intent
-- for the net version.
--
-- order_status note: shows up as NUMBER(0..4) in raw, mapping not in the docs.
-- 3 and 4 are the two least-frequent in shipped reports, treating those as
-- {On Hold, Cancelled} for the exclusion until finance confirms.

WITH window_bounds AS (
    -- Anchor the 12-month window on the latest order we have.
    -- Avoids burning the query when the daily feed is late.
    SELECT DATE_TRUNC('month', MAX(order_date::TIMESTAMP))                                AS window_end,
           DATEADD('month', -11, DATE_TRUNC('month', MAX(order_date::TIMESTAMP)))         AS window_start
    FROM   order_entry_db.order_entry.orders
)
SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS order_month,
       COUNT(DISTINCT o.order_id)                         AS order_count,
       SUM(o.order_total)                                 AS gmv,
       SUM(o.order_total) / COUNT(DISTINCT o.order_id)    AS aov
FROM   order_entry_db.order_entry.orders o,
       window_bounds w
WHERE  o.order_date::TIMESTAMP >= w.window_start
  AND  o.order_date::TIMESTAMP <  DATEADD('month', 1, w.window_end)
  AND  o.order_status NOT IN (3, 4)   -- TODO: confirm numeric→status mapping w/ finance
GROUP  BY 1
ORDER  BY 1
;
