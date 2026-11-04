-- Return rate last 90 days only — actionable window
-- Author: Sarah Chen

SELECT c.category_name,
       COUNT(*)                                                AS items_dispatched,
       COUNT(oi.return_date)                                   AS items_returned,
       COUNT(oi.return_date) * 100.0 / NULLIF(COUNT(*), 0)     AS return_rate_pct
FROM   order_entry_db.order_entry.order_items        oi
JOIN   order_entry_db.order_entry.products           p  USING (product_id)
JOIN   order_entry_db.order_entry.product_categories c  USING (category_id)
WHERE  oi.dispatch_date::TIMESTAMP >= DATEADD('day', -90,
           (SELECT MAX(dispatch_date::TIMESTAMP) FROM order_entry_db.order_entry.order_items))
GROUP  BY 1
ORDER  BY return_rate_pct DESC
;
