-- Q4 2024 vs Q1 2025 revenue
SELECT
    SUM(CASE WHEN order_date::TIMESTAMP BETWEEN '2024-10-01' AND '2024-12-31 23:59:59' THEN order_total END) AS q4_2024,
    SUM(CASE WHEN order_date::TIMESTAMP BETWEEN '2025-01-01' AND '2025-03-31 23:59:59' THEN order_total END) AS q1_2025
FROM order_entry_db.order_entry.orders;
