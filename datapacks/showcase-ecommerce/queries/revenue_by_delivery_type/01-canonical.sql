-- Revenue by delivery type
-- Author: PM / Karen

SELECT delivery_type,
       COUNT(*)            AS orders,
       SUM(order_total)    AS revenue,
       SUM(cost_of_delivery) AS shipping_cost
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
