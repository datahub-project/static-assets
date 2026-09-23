-- Daily detail for window: february_2025
SELECT TO_DATE(order_date::TIMESTAMP) AS day,
       COUNT(*) AS orders, SUM(order_total) AS revenue, AVG(order_total) AS aov
FROM order_entry_db.order_entry.orders
WHERE order_date::TIMESTAMP BETWEEN '2025-02-01' AND '2025-02-28 23:59:59'
GROUP BY 1 ORDER BY 1;
