-- Stock for Bike Repair Tool Kit across warehouses
SELECT w.warehouse_name, i.quantity_on_hand, i.restock_level, i.max_stock_level
FROM order_entry_db.order_entry.inventories i
JOIN order_entry_db.order_entry.warehouses w USING (warehouse_id)
WHERE i.product_id = 508
ORDER BY i.quantity_on_hand DESC;
