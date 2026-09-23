-- Same daily volume but via the analytics mart
-- Author: James Wilson
-- Grain on order_details is line-item; dedup before counting.

SELECT TO_DATE(order_date::TIMESTAMP)  AS order_day,
       COUNT(DISTINCT order_id)        AS order_count,
       SUM(DISTINCT order_total)       AS revenue_approx   -- approx since DISTINCT drops equal totals
FROM   order_entry_db.analytics.order_details
WHERE  order_date::TIMESTAMP >= DATEADD('day', -30,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.analytics.order_details))
GROUP  BY 1
ORDER  BY 1
;
