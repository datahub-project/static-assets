-- Suspiciously high or negative credit limits
SELECT customer_id, credit_limit
FROM order_entry_db.order_entry.customers
WHERE credit_limit > 100000 OR credit_limit < 0
ORDER BY credit_limit DESC LIMIT 20;
