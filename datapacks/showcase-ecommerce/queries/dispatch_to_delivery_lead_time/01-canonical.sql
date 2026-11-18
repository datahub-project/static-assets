-- Avg days from dispatch to estimated delivery
-- Author: Sarah Chen

SELECT AVG(DATEDIFF('day', dispatch_date::TIMESTAMP, estimated_delivery::TIMESTAMP)) AS avg_days_in_transit,
       COUNT(*) AS line_items
FROM   order_entry_db.order_entry.order_items
WHERE  dispatch_date IS NOT NULL AND estimated_delivery IS NOT NULL
;
