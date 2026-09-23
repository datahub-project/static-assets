-- Top products by returns, with category context
-- Author: Sarah Chen

SELECT p.product_id, p.product_name, c.category_name,
       COUNT(*)                                AS returns,
       SUM(oi.unit_price * oi.quantity)        AS returned_revenue
FROM   order_entry_db.order_entry.order_items        oi
JOIN   order_entry_db.order_entry.products           p  USING (product_id)
JOIN   order_entry_db.order_entry.product_categories c  USING (category_id)
WHERE  oi.return_date IS NOT NULL
GROUP  BY 1, 2, 3
ORDER  BY returns DESC
LIMIT  25
;
