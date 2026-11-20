-- Online vs in-store AOV comparison
SELECT order_mode, COUNT(*) AS orders, AVG(order_total) AS aov, MEDIAN(order_total) AS p50
FROM order_entry_db.order_entry.orders
WHERE order_mode IN ('ONLINE', 'INSTORE') AND order_status NOT IN (3, 4)
GROUP BY 1;
