-- New customers (first-order based) in last 30 days
WITH first_order AS (
    SELECT customer_id, MIN(order_date::TIMESTAMP) AS first_at
    FROM order_entry_db.order_entry.orders GROUP BY 1
)
SELECT COUNT(*) AS first_time_in_last_30d
FROM first_order
WHERE first_at >= DATEADD('day', -30, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders));
