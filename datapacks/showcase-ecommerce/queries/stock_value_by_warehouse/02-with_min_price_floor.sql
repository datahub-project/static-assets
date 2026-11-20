-- Stock value using min_price (conservative floor)
-- Author: Andrea Garcia — finance prefers a conservative floor over list price.

select w.warehouse_name,
       count(distinct i.product_id)                                 as sku_count,
       sum(greatest(i.quantity_on_hand, 0))                         as total_units,
       sum(greatest(i.quantity_on_hand, 0) * p.min_price)           as conservative_value,
       sum(greatest(i.quantity_on_hand, 0) * p.list_price)          as list_value
from   order_entry_db.order_entry.inventories i
join   order_entry_db.order_entry.products    p using (product_id)
join   order_entry_db.order_entry.warehouses  w using (warehouse_id)
group by 1
order by conservative_value desc
;
