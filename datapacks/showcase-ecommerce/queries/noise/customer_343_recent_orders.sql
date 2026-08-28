-- Recent orders for customer 343. (Almira Dominici, Nonprofit)
SELECT order_id, order_date, order_total, order_status, delivery_type
FROM order_entry_db.order_entry.orders
WHERE customer_id = 343
ORDER BY order_date::TIMESTAMP DESC LIMIT 20;
