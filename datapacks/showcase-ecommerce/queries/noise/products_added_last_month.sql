-- New SKUs in the last 30 days — need to confirm they're tagged correctly.
SELECT product_id, product_name, category_id, list_price, date_added, product_status
FROM   order_entry_db.order_entry.products
WHERE  date_added::TIMESTAMP >= DATEADD('day', -30, CURRENT_TIMESTAMP)
ORDER  BY date_added::TIMESTAMP DESC;
