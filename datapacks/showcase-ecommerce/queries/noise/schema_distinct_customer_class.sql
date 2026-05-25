-- What values appear in customers.customer_class?
SELECT customer_class AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.customers
GROUP BY 1 ORDER BY cnt DESC;
