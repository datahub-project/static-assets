-- Monthly AOV via the mart
-- Author: James Wilson — straight off order_details for the PowerBI feed.
-- Grain is line-item, so dedupe via the order header.

with hdr as (
    select   order_id,
             any_value(order_date)   as order_date,
             any_value(order_total)  as order_total,
             any_value(order_status) as order_status
    from     order_entry_db.analytics.order_details
    group by order_id
)
select   date_trunc('month', order_date::timestamp)::date as order_month,
         avg(order_total)                                 as aov,
         count(*)                                         as order_count
from     hdr
where    order_status not in (3, 4)
group by 1
order by 1
;
