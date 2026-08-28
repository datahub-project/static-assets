-- Payment method revenue via mart
-- Author: James Wilson

with hdr as (
    select order_id, any_value(payment_method_code) as pm, any_value(order_total) as total, any_value(order_status) as status
    from order_entry_db.analytics.order_details
    group by order_id
)
select pm as payment_method_code, count(*) as orders, sum(total) as revenue
from hdr where status not in (3, 4)
group by 1 order by revenue desc;
