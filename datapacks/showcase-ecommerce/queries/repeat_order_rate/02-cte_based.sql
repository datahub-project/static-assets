-- Repeat-order rate using a CTE (easier to extend later)
-- Author: Sarah Chen

WITH customer_orders AS (
    SELECT customer_id,
           COUNT(DISTINCT order_id) AS order_ct
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
),
totals AS (
    SELECT
        COUNT(*)                                                AS total_customers,
        COUNT(CASE WHEN order_ct > 1 THEN 1 END)                AS repeat_customers,
        COUNT(CASE WHEN order_ct >= 3 THEN 1 END)               AS three_plus_customers
    FROM   customer_orders
)
SELECT total_customers,
       repeat_customers,
       three_plus_customers,
       repeat_customers      * 100.0 / NULLIF(total_customers, 0) AS repeat_rate_pct,
       three_plus_customers  * 100.0 / NULLIF(total_customers, 0) AS three_plus_rate_pct
FROM   totals
;
