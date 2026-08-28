-- What values appear in orders.delivery_type?
SELECT delivery_type AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.orders
GROUP BY 1 ORDER BY cnt DESC;
