-- Same metric, raw-tables version
-- Author: Sarah Chen — keeping for the integrity check vs mart

SELECT c.customer_class,
       SUM(o.order_total)         AS total_revenue,
       COUNT(DISTINCT o.order_id) AS order_count
FROM   order_entry_db.order_entry.orders    o
JOIN   order_entry_db.order_entry.customers c USING (customer_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY total_revenue DESC
;
