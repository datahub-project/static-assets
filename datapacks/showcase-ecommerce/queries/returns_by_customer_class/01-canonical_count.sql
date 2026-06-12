-- Return counts by customer class
-- Author: Karen Okonkwo

SELECT c.customer_class,
       COUNT(*) AS returns
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.customers   c  USING (customer_id)
WHERE  oi.return_date IS NOT NULL
GROUP  BY 1
ORDER  BY returns DESC
;
