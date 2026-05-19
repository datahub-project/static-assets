-- Credit limit vs realized spend (top quintile credit limit only)
-- Author: Sarah Chen

WITH cust AS (
    SELECT c.customer_id, c.cust_first_name, c.cust_last_name, c.credit_limit,
           SUM(o.order_total) AS spend
    FROM   order_entry_db.order_entry.customers c
    LEFT   JOIN order_entry_db.order_entry.orders o
           ON o.customer_id = c.customer_id AND o.order_status NOT IN (3, 4)
    GROUP  BY 1, 2, 3, 4
)
SELECT customer_id, cust_first_name, cust_last_name, credit_limit, COALESCE(spend, 0) AS spend
FROM   cust
WHERE  credit_limit >= (SELECT PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY credit_limit)
                        FROM order_entry_db.order_entry.customers)
ORDER  BY spend DESC
LIMIT  25
;
