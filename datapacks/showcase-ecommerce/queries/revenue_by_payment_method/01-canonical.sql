-- Revenue by payment method
-- Author: BID

SELECT payment_method_code,
       COUNT(*)         AS orders,
       SUM(order_total) AS revenue
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
