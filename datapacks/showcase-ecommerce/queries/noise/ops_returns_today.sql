-- Returns on the latest available day
SELECT COUNT(*) AS returns_today
FROM order_entry_db.order_entry.order_items
WHERE TO_DATE(return_date::TIMESTAMP) = (SELECT MAX(TO_DATE(return_date::TIMESTAMP)) FROM order_entry_db.order_entry.order_items);
