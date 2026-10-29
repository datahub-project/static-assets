-- Customers by class
SELECT customer_class, COUNT(*) AS customers
FROM   order_entry_db.order_entry.customers
GROUP  BY 1
ORDER  BY customers DESC;
