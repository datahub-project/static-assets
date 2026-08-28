-- Delivery type revenue via mart
-- Author: James Wilson

with hdr as (
    select order_id, any_value(delivery_type) as dt, any_value(order_total) as total,
           any_value(cost_of_delivery) as ship, any_value(order_status) as status
    from order_entry_db.analytics.order_details group by order_id
)
select dt as delivery_type, count(*) as orders, sum(total) as revenue, sum(ship) as shipping_cost
from hdr where status not in (3, 4)
group by 1 order by revenue desc;
