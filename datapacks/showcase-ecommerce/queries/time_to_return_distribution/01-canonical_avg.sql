-- Time-to-return mean
-- Author: David Kim

SELECT AVG(DATEDIFF('day', dispatch_date::TIMESTAMP, return_date::TIMESTAMP)) AS avg_days_to_return,
       COUNT(*) AS returned_items
FROM   order_entry_db.order_entry.order_items
WHERE  return_date IS NOT NULL AND dispatch_date IS NOT NULL
;
