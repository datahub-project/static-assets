-- AOV by month from raw orders
-- Author: Sarah Chen

SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
       SUM(order_total) / COUNT(DISTINCT order_id)      AS aov,
       COUNT(DISTINCT order_id)                         AS order_count,
       SUM(order_total)                                 AS gmv
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY 1
;
