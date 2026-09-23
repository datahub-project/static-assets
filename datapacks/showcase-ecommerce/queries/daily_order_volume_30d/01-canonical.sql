-- Daily orders, last 30 days
-- Author: Sarah Chen
-- Standard ops health-check that backs the morning dashboard tile.

WITH window_end AS (
    SELECT MAX(order_date::TIMESTAMP) AS as_of FROM order_entry_db.order_entry.orders
)
SELECT TO_DATE(o.order_date::TIMESTAMP) AS order_day,
       COUNT(*)                         AS order_count,
       SUM(o.order_total)               AS revenue
FROM   order_entry_db.order_entry.orders o, window_end w
WHERE  o.order_date::TIMESTAMP >= DATEADD('day', -30, w.as_of)
GROUP  BY 1
ORDER  BY 1
;
