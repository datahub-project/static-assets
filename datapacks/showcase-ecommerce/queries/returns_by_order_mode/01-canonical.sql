-- Return rate by channel
-- Author: Karen / PM

SELECT o.order_mode,
       COUNT(*) AS items_dispatched,
       COUNT(oi.return_date) AS items_returned,
       COUNT(oi.return_date) * 100.0 / NULLIF(COUNT(*), 0) AS return_rate_pct
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
WHERE  oi.dispatch_date IS NOT NULL
GROUP  BY 1
ORDER  BY return_rate_pct DESC
;
