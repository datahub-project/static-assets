-- Customers paying with Bitcoin
SELECT customer_id, COUNT(*) AS bitcoin_orders, SUM(order_total) AS spend
FROM order_entry_db.order_entry.orders
WHERE payment_method_code = 'BITCOIN'
GROUP BY 1 ORDER BY bitcoin_orders DESC LIMIT 30;
