-- Top sales reps (B2B / direct channel)
SELECT sales_rep_id, COUNT(*) AS orders, SUM(order_total) AS revenue
FROM order_entry_db.order_entry.orders
WHERE order_mode != 'ONLINE' AND sales_rep_id IS NOT NULL
GROUP BY 1 ORDER BY revenue DESC LIMIT 10;
