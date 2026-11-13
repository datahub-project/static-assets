-- In-transit time by delivery type
-- Author: Sarah Chen — confirming "Overnight" actually beats "Express"

SELECT o.delivery_type,
       COUNT(*)                                                              AS items,
       AVG(DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.estimated_delivery::TIMESTAMP)) AS avg_days,
       MEDIAN(DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.estimated_delivery::TIMESTAMP)) AS median_days
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o USING (order_id)
WHERE  oi.dispatch_date IS NOT NULL AND oi.estimated_delivery IS NOT NULL
GROUP  BY 1
ORDER  BY avg_days
;
