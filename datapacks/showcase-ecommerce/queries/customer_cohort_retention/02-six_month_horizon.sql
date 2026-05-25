-- Just months 0..6 of the retention grid — for the slide
-- Author: David Kim

with first_order as (
    select customer_id, min(order_date::timestamp) as first_order_at
    from order_entry_db.order_entry.orders where order_status not in (3, 4)
    group by 1
),
labelled as (
    select fo.customer_id,
           date_trunc('month', fo.first_order_at) as cohort_month,
           months_between(date_trunc('month', o.order_date::timestamp), date_trunc('month', fo.first_order_at)) as month_offset
    from first_order fo
    join order_entry_db.order_entry.orders o on o.customer_id = fo.customer_id and o.order_status not in (3, 4)
)
select cohort_month::date as cohort_month,
       count(distinct case when month_offset = 0 then customer_id end) as m0,
       count(distinct case when month_offset = 1 then customer_id end) as m1,
       count(distinct case when month_offset = 2 then customer_id end) as m2,
       count(distinct case when month_offset = 3 then customer_id end) as m3,
       count(distinct case when month_offset = 4 then customer_id end) as m4,
       count(distinct case when month_offset = 5 then customer_id end) as m5,
       count(distinct case when month_offset = 6 then customer_id end) as m6
from labelled
group by 1
order by 1;
