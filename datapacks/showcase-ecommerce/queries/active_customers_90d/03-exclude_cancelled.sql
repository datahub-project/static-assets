-- Active customers — only exclude cancelled, not held (different definition variant)
-- Author: Karen — wanted to see if loosening the filter changed the number

SELECT COUNT(DISTINCT customer_id) AS active_customers_loose_definition
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP >= DATEADD('day', -90,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
  AND  order_status != 4  -- only exclude what we believe is 'Cancelled'
;
