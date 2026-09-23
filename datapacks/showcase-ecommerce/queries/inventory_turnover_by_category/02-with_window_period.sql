-- Turnover for last 90 days only, normalised to 90-day-equivalent
-- Author: Sarah Chen

with sold_90 as (
    select p.category_id, sum(oi.quantity) as units_sold
    from order_entry_db.order_entry.order_items oi
    join order_entry_db.order_entry.products p using (product_id)
    join order_entry_db.order_entry.orders o using (order_id)
    where o.order_date::timestamp >= dateadd('day', -90, (select max(order_date::timestamp) from order_entry_db.order_entry.orders))
    group by 1
),
stock as (
    select p.category_id, sum(greatest(i.quantity_on_hand, 0)) as total_stock
    from order_entry_db.order_entry.inventories i
    join order_entry_db.order_entry.products p using (product_id)
    group by 1
)
select c.category_name, s.units_sold, st.total_stock,
       s.units_sold * 1.0 / nullif(st.total_stock, 0) as turnover_90d
from order_entry_db.order_entry.product_categories c
join sold_90 s using (category_id)
join stock st using (category_id)
order by turnover_90d desc;
