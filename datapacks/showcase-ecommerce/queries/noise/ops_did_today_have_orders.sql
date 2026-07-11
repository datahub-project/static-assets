-- Orders on the latest available day
SELECT COUNT(*) AS orders_today
FROM order_entry_db.order_entry.orders
WHERE TO_DATE(order_date::TIMESTAMP) = (SELECT MAX(TO_DATE(order_date::TIMESTAMP)) FROM order_entry_db.order_entry.orders);
