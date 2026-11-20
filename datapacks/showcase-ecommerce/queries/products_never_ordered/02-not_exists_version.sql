-- Same set via NOT EXISTS — preferred when product table is large
SELECT p.product_id, p.product_name, p.product_status, p.date_added
FROM   order_entry_db.order_entry.products p
WHERE  NOT EXISTS (
           SELECT 1 FROM order_entry_db.order_entry.order_items oi
           WHERE oi.product_id = p.product_id
       )
ORDER  BY p.date_added DESC;
