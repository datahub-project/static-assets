-- Freshness check — latest order_date on snowflake
SELECT MAX(order_date::TIMESTAMP) AS latest_order, COUNT(*) AS total_orders
FROM   order_entry_db.order_entry.orders;
