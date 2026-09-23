-- What values appear in orders.payment_method_code?
SELECT payment_method_code AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.orders
GROUP BY 1 ORDER BY cnt DESC;
