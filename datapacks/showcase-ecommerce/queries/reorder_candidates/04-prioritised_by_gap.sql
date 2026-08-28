-- Reorder candidates prioritised by shortfall ratio
-- Author: Sarah Chen — ranking which to do first by % below restock

select   p.product_name,
         w.warehouse_name,
         i.quantity_on_hand,
         i.restock_level,
         i.restock_level - i.quantity_on_hand                 as units_short,
         (i.restock_level - i.quantity_on_hand) * 1.0
             / nullif(i.restock_level, 0) * 100               as pct_below_restock,
         i.reorder_quantity
from     order_entry_db.order_entry.inventories i
join     order_entry_db.order_entry.products    p using (product_id)
join     order_entry_db.order_entry.warehouses  w using (warehouse_id)
where    i.quantity_on_hand < i.restock_level
  and    i.quantity_on_hand >= 0
order by pct_below_restock desc
limit    50
;
