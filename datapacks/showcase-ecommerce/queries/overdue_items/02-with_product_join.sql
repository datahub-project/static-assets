-- Overdue items with product name (for the ops slack channel)
-- Author: Andrea Garcia

with as_of as (select max(order_date::timestamp) as now_ts from order_entry_db.order_entry.orders)
select   oi.line_item_id,
         oi.order_id,
         p.product_name,
         oi.estimated_delivery,
         datediff('day', oi.estimated_delivery::timestamp, a.now_ts) as days_overdue
from     order_entry_db.order_entry.order_items oi
join     order_entry_db.order_entry.products    p using (product_id)
cross join as_of a
where    oi.estimated_delivery::timestamp < a.now_ts
  and    oi.dispatch_date is null
order by days_overdue desc
limit    100
;
