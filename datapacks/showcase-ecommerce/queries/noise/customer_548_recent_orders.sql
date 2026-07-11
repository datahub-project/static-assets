-- Recent orders for customer 548. (Orly Bennion, Retail)
SELECT order_id, order_date, order_total, order_status, delivery_type
FROM order_entry_db.order_entry.orders
WHERE customer_id = 548
ORDER BY order_date::TIMESTAMP DESC LIMIT 20;
