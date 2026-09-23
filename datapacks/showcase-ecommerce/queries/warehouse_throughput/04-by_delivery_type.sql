-- Throughput pivoted by delivery type
-- Author: Sarah Chen — for the ops scorecard

SELECT w.warehouse_name,
       o.delivery_type,
       COUNT(*)        AS orders,
       SUM(o.order_total) AS revenue
FROM   order_entry_db.order_entry.orders     o
JOIN   order_entry_db.order_entry.warehouses w USING (warehouse_id)
WHERE  o.order_date::TIMESTAMP >= DATEADD('day', -90,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP  BY 1, 2
ORDER  BY w.warehouse_name, orders DESC
;
