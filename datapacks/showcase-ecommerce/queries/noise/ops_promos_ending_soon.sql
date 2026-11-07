-- Promotions ending in the next 30 days
SELECT promotion_name, promotion_end_date,
       DATEDIFF('day', (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders), promotion_end_date::TIMESTAMP) AS days_left
FROM order_entry_db.order_entry.promotions
WHERE promotion_end_date IS NOT NULL
  AND promotion_end_date::TIMESTAMP > (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)
  AND promotion_end_date::TIMESTAMP < DATEADD('day', 30, (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
ORDER BY days_left;
