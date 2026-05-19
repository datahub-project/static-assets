-- Overstocked records (qty > max_stock_level)
SELECT product_id, warehouse_id, quantity_on_hand, max_stock_level
FROM order_entry_db.order_entry.inventories
WHERE quantity_on_hand > max_stock_level
LIMIT 50;
