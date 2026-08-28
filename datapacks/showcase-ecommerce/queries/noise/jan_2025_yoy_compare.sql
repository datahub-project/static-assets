-- Jan 2025 vs Jan 2024 quick comparison for the LinkedIn post
-- (just need the totals, not a fancy chart)

SELECT
    SUM(CASE WHEN order_date::TIMESTAMP >= '2025-01-01' AND order_date::TIMESTAMP < '2025-02-01' THEN order_total END) AS jan_2025_revenue,
    SUM(CASE WHEN order_date::TIMESTAMP >= '2024-05-14' AND order_date::TIMESTAMP < '2024-06-01' THEN order_total END) AS partial_may_2024_baseline,
    COUNT(CASE WHEN order_date::TIMESTAMP >= '2025-01-01' AND order_date::TIMESTAMP < '2025-02-01' THEN 1 END) AS jan_2025_orders
FROM order_entry_db.order_entry.orders
;
