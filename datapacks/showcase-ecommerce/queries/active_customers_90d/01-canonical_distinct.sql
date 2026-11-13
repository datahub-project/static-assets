-- Active customers — ordered in the last 90 days
-- Author: Sarah Chen — per the Active Customer metric definition

SELECT COUNT(DISTINCT customer_id) AS active_customers_90d
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP >= DATEADD('day', -90,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
  AND  order_status NOT IN (3, 4)
;
