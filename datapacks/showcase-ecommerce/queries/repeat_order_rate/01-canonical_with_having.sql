-- Repeat-order rate — share of customers with > 1 order
-- Author: PM / Karen

SELECT
    COUNT(DISTINCT CASE WHEN order_ct > 1 THEN customer_id END) * 100.0
        / NULLIF(COUNT(DISTINCT customer_id), 0) AS repeat_order_rate_pct,
    COUNT(DISTINCT customer_id)                   AS total_customers,
    COUNT(DISTINCT CASE WHEN order_ct > 1 THEN customer_id END) AS repeat_customers
FROM (
    SELECT customer_id, COUNT(DISTINCT order_id) AS order_ct
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
;
