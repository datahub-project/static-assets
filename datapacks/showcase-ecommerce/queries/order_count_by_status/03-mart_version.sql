-- Order count by status — mart
-- Author: James Wilson
-- order_details grain is line-item; dedupe.

with hdr as (
    select order_id, any_value(order_status) as order_status, any_value(order_total) as order_total
    from order_entry_db.analytics.order_details
    group by order_id
)
select order_status, count(*) as order_count, sum(order_total) as revenue
from hdr
group by 1
order by 1
;
