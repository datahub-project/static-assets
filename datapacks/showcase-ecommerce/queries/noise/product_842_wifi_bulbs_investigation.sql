-- Why is product 842 (Smart Wi-Fi Light Bulbs) showing "Out of Stock" status
-- in the catalogue but inventories still has positive stock? Sales rep flagged
-- it after a customer was told it was unavailable but our system showed 4500+
-- units across warehouses. Want to confirm before pinging merchandising.
-- Author: Andrea Garcia

SELECT
    p.product_id,
    p.product_name,
    p.product_status,
    p.list_price,
    p.date_added,
    i.warehouse_id,
    w.warehouse_name,
    i.quantity_on_hand,
    i.restock_level
FROM order_entry_db.order_entry.products    p
JOIN order_entry_db.order_entry.inventories i USING (product_id)
JOIN order_entry_db.order_entry.warehouses  w USING (warehouse_id)
WHERE p.product_id = 842
ORDER BY i.quantity_on_hand DESC;
