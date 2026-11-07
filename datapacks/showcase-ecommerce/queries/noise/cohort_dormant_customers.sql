-- Dormant customers (no orders >180 days)
SELECT c.customer_id, c.cust_first_name, c.cust_last_name,
       MAX(o.order_date) AS last_order,
       DATEDIFF('day', MAX(o.order_date::TIMESTAMP),
                (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)) AS days_since_last
FROM order_entry_db.order_entry.customers c
LEFT JOIN order_entry_db.order_entry.orders o USING (customer_id)
GROUP BY 1, 2, 3
HAVING DATEDIFF('day', MAX(o.order_date::TIMESTAMP),
                (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)) > 180
ORDER BY days_since_last DESC LIMIT 30;
