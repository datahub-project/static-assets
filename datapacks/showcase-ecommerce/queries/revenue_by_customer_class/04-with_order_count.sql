-- Order count by customer class — same shape, no revenue dollars
-- Author: Sarah Chen — sometimes finance wants pure counts only.

SELECT c.customer_class,
       COUNT(DISTINCT o.order_id)    AS orders,
       COUNT(DISTINCT o.customer_id) AS distinct_buyers,
       COUNT(DISTINCT o.order_id) * 1.0 / COUNT(DISTINCT o.customer_id) AS orders_per_buyer
FROM   order_entry_db.order_entry.orders    o
JOIN   order_entry_db.order_entry.customers c USING (customer_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY orders DESC
;
