-- Revenue by order channel
-- Author: PM / Karen

SELECT order_mode,
       COUNT(*)          AS orders,
       SUM(order_total)  AS revenue
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
