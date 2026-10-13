-- Order count by status
-- Author: Ben Porter — operational tile

SELECT order_status,
       COUNT(*)         AS order_count,
       SUM(order_total) AS revenue_in_status
FROM   order_entry_db.order_entry.orders
GROUP  BY 1
ORDER  BY 1
;
