-- Who buys gift-wrapped items?
SELECT c.customer_class, COUNT(DISTINCT o.order_id) AS gift_wrap_orders, AVG(o.order_total) AS aov
FROM order_entry_db.order_entry.order_items oi
JOIN order_entry_db.order_entry.orders o USING (order_id)
JOIN order_entry_db.order_entry.customers c USING (customer_id)
WHERE oi.gift_wrap = 'Y'
GROUP BY 1 ORDER BY gift_wrap_orders DESC;
