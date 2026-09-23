-- Orphan check: orders with non-existent billing_address_id
SELECT COUNT(*) AS orders_with_bad_billing_addr
FROM order_entry_db.order_entry.orders o
LEFT JOIN order_entry_db.order_entry.addresses a ON o.billing_address_id = a.address_id
WHERE a.address_id IS NULL AND o.billing_address_id IS NOT NULL;
