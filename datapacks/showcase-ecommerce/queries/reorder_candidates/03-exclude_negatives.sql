-- Reorder candidates, excluding suspected CDC anomalies (qty < 0)
-- Author: Andrea Garcia
-- Per the Inventory Staleness runbook, negative on_hand is a known CDC race condition.
-- Excluding from reorder triggers so we don't double-order.

SELECT p.product_id,
       p.product_name,
       w.warehouse_name,
       i.quantity_on_hand,
       i.restock_level,
       i.restock_level - i.quantity_on_hand AS shortfall
FROM   order_entry_db.order_entry.inventories i
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
WHERE  i.quantity_on_hand >= 0
  AND  i.quantity_on_hand < i.restock_level
ORDER  BY shortfall DESC
;
