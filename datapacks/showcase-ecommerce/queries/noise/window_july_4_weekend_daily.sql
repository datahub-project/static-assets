-- Daily detail for window: july_4_weekend
SELECT TO_DATE(order_date::TIMESTAMP) AS day,
       COUNT(*) AS orders, SUM(order_total) AS revenue, AVG(order_total) AS aov
FROM order_entry_db.order_entry.orders
WHERE order_date::TIMESTAMP BETWEEN '2024-07-04' AND '2024-07-08 23:59:59'
GROUP BY 1 ORDER BY 1;
