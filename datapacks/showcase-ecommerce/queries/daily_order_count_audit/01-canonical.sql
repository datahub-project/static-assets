-- Daily order count audit, last 14 days (per Order Count Discrepancy runbook)
-- Author: Ben Porter
SELECT TO_DATE(order_date::TIMESTAMP) AS day, COUNT(*) AS orders
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP >= DATEADD('day', -14,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP  BY 1
ORDER  BY 1 DESC;
