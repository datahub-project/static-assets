-- Warehouse throughput + revenue/order
-- Author: Sarah Chen — comparing the fulfillment mix

SELECT w.warehouse_name,
       COUNT(*)                          AS orders,
       SUM(o.order_total)                AS revenue,
       AVG(o.order_total)                AS aov,
       SUM(o.cost_of_delivery)           AS shipping_costs,
       SUM(o.cost_of_delivery) / COUNT(*) AS avg_shipping_per_order
FROM   order_entry_db.order_entry.orders     o
JOIN   order_entry_db.order_entry.warehouses w USING (warehouse_id)
WHERE  o.order_date::TIMESTAMP >= DATEADD('day', -90,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
  AND  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
