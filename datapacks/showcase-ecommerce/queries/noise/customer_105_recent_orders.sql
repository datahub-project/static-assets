-- Recent orders for customer 105.
SELECT order_id, order_date, order_total, order_status, delivery_type
FROM order_entry_db.order_entry.orders
WHERE customer_id = 105
ORDER BY order_date::TIMESTAMP DESC LIMIT 20;
