-- Zero-quantity line items
SELECT COUNT(*) FROM order_entry_db.order_entry.order_items WHERE quantity = 0 OR quantity IS NULL;
