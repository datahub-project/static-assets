-- WoW revenue via order_details
-- Author: James Wilson

with hdr as (
    select order_id, any_value(order_date) as order_date, any_value(order_total) as order_total, any_value(order_status) as order_status
    from order_entry_db.analytics.order_details group by order_id
),
weekly as (
    select date_trunc('week', order_date::timestamp)::date as week_start, sum(order_total) as revenue
    from hdr where order_status not in (3, 4)
    group by 1
)
select week_start, revenue,
       lag(revenue) over (order by week_start) as prior_revenue,
       revenue - lag(revenue) over (order by week_start) as wow_delta
from weekly order by week_start;
