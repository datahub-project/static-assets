-- Channel revenue via the mart
-- Author: James Wilson

with hdr as (
    select order_id, any_value(order_mode) as order_mode, any_value(order_total) as order_total, any_value(order_status) as order_status
    from order_entry_db.analytics.order_details
    group by order_id
)
select order_mode, count(*) as orders, sum(order_total) as revenue, avg(order_total) as aov
from hdr where order_status not in (3, 4)
group by 1 order by revenue desc;
