-- Reorder candidates with suggested reorder quantity
-- Author: Ben Porter — for the planner

SELECT p.product_name,
       w.warehouse_name,
       i.quantity_on_hand,
       i.restock_level,
       i.reorder_quantity,
       i.max_stock_level,
       LEAST(i.reorder_quantity, i.max_stock_level - i.quantity_on_hand) AS suggested_po_qty
FROM   order_entry_db.order_entry.inventories i
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
WHERE  i.quantity_on_hand < i.restock_level
ORDER  BY suggested_po_qty DESC
;
