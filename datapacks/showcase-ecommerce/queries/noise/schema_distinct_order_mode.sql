-- What values appear in orders.order_mode?
SELECT order_mode AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.orders
GROUP BY 1 ORDER BY cnt DESC;
