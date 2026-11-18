-- Orders attributed to "Sweet Potato and Chickpea Bowl" promotion (id 24)
SELECT o.order_id, o.order_date, o.order_total, c.cust_first_name, c.cust_last_name
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.customers c USING (customer_id)
WHERE o.promotion_id = 24
ORDER BY o.order_date DESC LIMIT 50;
