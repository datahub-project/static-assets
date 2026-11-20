-- Orphan check: orders pointing at non-existent customers
SELECT COUNT(*) AS orders_without_customer
FROM order_entry_db.order_entry.orders o
LEFT JOIN order_entry_db.order_entry.customers c USING (customer_id)
WHERE c.customer_id IS NULL;
