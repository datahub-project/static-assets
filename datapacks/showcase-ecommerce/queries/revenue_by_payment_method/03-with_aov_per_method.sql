-- Payment method + AOV
-- Author: Sarah Chen

SELECT payment_method_code,
       COUNT(*)         AS orders,
       SUM(order_total) AS revenue,
       AVG(order_total) AS aov
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY aov DESC
;
