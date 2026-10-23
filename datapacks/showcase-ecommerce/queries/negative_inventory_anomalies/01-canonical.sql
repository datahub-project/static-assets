-- Negative inventory check (per Inventory Staleness runbook)
-- Author: Julia (DQE)
SELECT p.product_id, p.product_name, w.warehouse_name, i.quantity_on_hand
FROM   order_entry_db.order_entry.inventories i
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
WHERE  i.quantity_on_hand < 0
ORDER  BY i.quantity_on_hand;
