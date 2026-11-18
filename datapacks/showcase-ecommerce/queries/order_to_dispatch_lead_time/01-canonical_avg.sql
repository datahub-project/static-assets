-- Avg lead time from order to dispatch (per line item)
-- Author: Sarah Chen

SELECT AVG(DATEDIFF('day', o.order_date::TIMESTAMP, oi.dispatch_date::TIMESTAMP)) AS avg_days_to_dispatch,
       COUNT(*) AS line_items
FROM   order_entry_db.order_entry.orders      o
JOIN   order_entry_db.order_entry.order_items oi USING (order_id)
WHERE  oi.dispatch_date IS NOT NULL
;
