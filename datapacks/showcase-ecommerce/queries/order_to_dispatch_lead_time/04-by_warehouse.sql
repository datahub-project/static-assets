-- Lead time broken out by warehouse
-- Author: Sarah Chen — for the warehouse ops review

SELECT w.warehouse_name,
       COUNT(*)                                                                  AS line_items,
       AVG(DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP)) AS avg_days,
       MEDIAN(DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP)) AS median_days
FROM   order_entry_db.order_entry.orders      o
JOIN   order_entry_db.order_entry.order_items oi USING (order_id)
JOIN   order_entry_db.order_entry.warehouses  w  USING (warehouse_id)
WHERE  oi.dispatch_date IS NOT NULL
GROUP  BY 1
ORDER  BY avg_days DESC
;
