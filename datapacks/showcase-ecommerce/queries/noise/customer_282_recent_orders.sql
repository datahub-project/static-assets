-- Recent orders for customer 282.
SELECT order_id, order_date, order_total, order_status, delivery_type
FROM order_entry_db.order_entry.orders
WHERE customer_id = 282
ORDER BY order_date::TIMESTAMP DESC LIMIT 20;
