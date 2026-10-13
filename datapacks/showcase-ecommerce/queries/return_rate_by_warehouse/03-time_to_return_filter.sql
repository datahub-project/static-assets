-- Return rate within 30 days of dispatch — strict "fast return" window
-- Author: David Kim
-- "Returns within window" is more actionable than lifetime returns because
-- it filters out long-tail returns that may be unrelated to the warehouse.

SELECT w.warehouse_name,
       COUNT(*) AS items_dispatched,
       COUNT(CASE WHEN oi.return_date IS NOT NULL
                   AND DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.return_date::TIMESTAMP) <= 30
                  THEN 1 END) AS fast_returns,
       COUNT(CASE WHEN oi.return_date IS NOT NULL
                   AND DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.return_date::TIMESTAMP) <= 30
                  THEN 1 END) * 100.0 / NULLIF(COUNT(*), 0) AS fast_return_rate_pct
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.warehouses  w  USING (warehouse_id)
WHERE  oi.dispatch_date IS NOT NULL
GROUP  BY 1
ORDER  BY fast_return_rate_pct DESC
;
