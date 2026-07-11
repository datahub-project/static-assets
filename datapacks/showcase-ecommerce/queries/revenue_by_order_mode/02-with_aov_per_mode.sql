-- Channel comparison with AOV
-- Author: Sarah Chen — looking at whether in-store has higher basket size

SELECT order_mode,
       COUNT(*)         AS orders,
       SUM(order_total) AS revenue,
       AVG(order_total) AS aov,
       MEDIAN(order_total) AS median_order
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY aov DESC
;
