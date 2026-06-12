-- Order status distribution with %
-- Author: Sarah Chen

SELECT order_status,
       COUNT(*)                                       AS order_count,
       COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()       AS pct_of_orders,
       SUM(order_total)                               AS revenue_in_status
FROM   order_entry_db.order_entry.orders
GROUP  BY 1
ORDER  BY order_count DESC
;
