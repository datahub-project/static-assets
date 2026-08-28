-- Warehouse throughput via mart
-- Author: James Wilson

with hdr as (
    select order_id, any_value(warehouse_name) as wh, any_value(order_total) as total, any_value(order_date) as dt
    from order_entry_db.analytics.order_details group by order_id
)
select wh as warehouse_name, count(*) as orders, sum(total) as revenue
from hdr
where dt::timestamp >= dateadd('day', -90, (select max(dt::timestamp) from hdr))
group by 1 order by orders desc;
