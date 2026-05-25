-- Products that have never appeared on an order_items row (LEFT JOIN ... IS NULL pattern)
-- Author: Sarah Chen

SELECT p.product_id, p.product_name, p.product_status, p.date_added
FROM   order_entry_db.order_entry.products p
LEFT   JOIN order_entry_db.order_entry.order_items oi USING (product_id)
WHERE  oi.product_id IS NULL
ORDER  BY p.date_added DESC;
