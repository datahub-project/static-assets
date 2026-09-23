-- Overdue items grouped by warehouse — for the daily ops stand-up
-- Author: Ben Porter

SELECT w.warehouse_name,
       COUNT(*)                                          AS overdue_items,
       AVG(DATEDIFF('day', oi.estimated_delivery::TIMESTAMP,
                    (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
       )                                                  AS avg_days_overdue
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.warehouses  w  USING (warehouse_id)
WHERE  oi.estimated_delivery::TIMESTAMP <
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)
  AND  oi.dispatch_date IS NULL
GROUP  BY 1
ORDER  BY overdue_items DESC
;
