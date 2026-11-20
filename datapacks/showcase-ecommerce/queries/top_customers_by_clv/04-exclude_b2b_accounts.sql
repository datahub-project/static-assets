-- Top B2C customers by CLV (excludes accounts assigned to a sales rep)
-- Author: Karen Okonkwo — for the consumer marketing campaign list

SELECT c.customer_id,
       c.cust_first_name || ' ' || c.cust_last_name AS customer_name,
       c.customer_class,
       SUM(o.order_total)         AS lifetime_revenue,
       COUNT(DISTINCT o.order_id) AS lifetime_orders
FROM   order_entry_db.order_entry.orders    o
JOIN   order_entry_db.order_entry.customers c USING (customer_id)
WHERE  o.order_status NOT IN (3, 4)
  AND  c.account_mgr_id IS NULL     -- B2C only — no assigned sales rep
GROUP  BY 1, 2, 3
ORDER  BY lifetime_revenue DESC
LIMIT  10
;
