-- Top products by absolute return count
SELECT p.product_id,
       p.product_name,
       COUNT(*) AS returns
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.products    p USING (product_id)
WHERE  oi.return_date IS NOT NULL
GROUP  BY 1, 2
ORDER  BY returns DESC
LIMIT  25;
