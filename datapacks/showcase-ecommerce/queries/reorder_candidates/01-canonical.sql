-- Reorder candidates (per (product, warehouse))
-- Author: Ben Porter — feeds the purchase order draft job

SELECT p.product_id,
       p.product_name,
       w.warehouse_name,
       i.quantity_on_hand,
       i.restock_level,
       i.restock_level - i.quantity_on_hand AS shortfall
FROM   order_entry_db.order_entry.inventories i
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
WHERE  i.quantity_on_hand < i.restock_level
ORDER  BY shortfall DESC
;
