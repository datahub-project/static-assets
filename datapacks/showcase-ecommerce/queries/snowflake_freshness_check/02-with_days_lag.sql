-- Freshness lag in days vs now
SELECT MAX(order_date::TIMESTAMP) AS latest_order,
       DATEDIFF('day', MAX(order_date::TIMESTAMP), CURRENT_TIMESTAMP) AS days_behind_today,
       CASE WHEN DATEDIFF('day', MAX(order_date::TIMESTAMP), CURRENT_TIMESTAMP) > 1 THEN 'stale' ELSE 'fresh' END AS health
FROM   order_entry_db.order_entry.orders;
