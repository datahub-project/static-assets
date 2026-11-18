-- Avg days-to-return by category
-- Author: Sarah Chen

SELECT c.category_name,
       COUNT(*) AS returns,
       AVG(DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.return_date::TIMESTAMP)) AS avg_days_to_return,
       MEDIAN(DATEDIFF('day', oi.dispatch_date::TIMESTAMP, oi.return_date::TIMESTAMP)) AS median_days
FROM   order_entry_db.order_entry.order_items        oi
JOIN   order_entry_db.order_entry.products           p  USING (product_id)
JOIN   order_entry_db.order_entry.product_categories c  USING (category_id)
WHERE  oi.return_date IS NOT NULL AND oi.dispatch_date IS NOT NULL
GROUP  BY 1
ORDER  BY avg_days_to_return DESC
;
