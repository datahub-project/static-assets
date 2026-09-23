-- Items overdue (past estimated delivery, never dispatched)
-- Author: Ben Porter

SELECT line_item_id,
       order_id,
       product_id,
       estimated_delivery,
       DATEDIFF('day', estimated_delivery::TIMESTAMP,
                (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)
       ) AS days_overdue
FROM   order_entry_db.order_entry.order_items
WHERE  estimated_delivery::TIMESTAMP <
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)
  AND  dispatch_date IS NULL
ORDER  BY days_overdue DESC
LIMIT  100
;
