-- "New customer" defined by first ORDER, not by signup
-- Author: Sarah Chen — marketing uses signup-cohort; finance uses first-order-cohort.

WITH first_order AS (
    SELECT customer_id,
           MIN(order_date::TIMESTAMP) AS first_order_at
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT DATE_TRUNC('month', first_order_at)::DATE AS first_order_month,
       COUNT(*) AS new_customers_by_first_order
FROM   first_order
GROUP  BY 1
ORDER  BY 1
;
