-- Return before dispatch? Should be impossible
SELECT COUNT(*) AS items_returned_before_dispatch
FROM order_entry_db.order_entry.order_items
WHERE return_date::TIMESTAMP < dispatch_date::TIMESTAMP;
