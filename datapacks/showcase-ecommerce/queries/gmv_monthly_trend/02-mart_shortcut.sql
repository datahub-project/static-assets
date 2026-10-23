-- Monthly GMV — last 12 months (mart version)
-- Author: James Wilson (BI Developer)
--
-- Hits the analytics.order_details denormalized view to avoid joining 5 tables.
-- order_details is line-item grain — need COUNT(DISTINCT order_id) for order counts
-- and SUM(DISTINCT order_total)... actually no — order_total repeats per line so
-- can't SUM(DISTINCT). Pull a deduped order header CTE instead.

with orders_dedup as (
    -- one row per order with its total + status
    select   order_id,
             any_value(order_date)    as order_date,
             any_value(order_total)   as order_total,
             any_value(order_status)  as order_status
    from     order_entry_db.analytics.order_details
    group by order_id
),
window_bounds as (
    select date_trunc('month', max(order_date::timestamp))                          as window_end,
           dateadd('month', -11, date_trunc('month', max(order_date::timestamp)))   as window_start
    from   orders_dedup
)
select   date_trunc('month', o.order_date::timestamp)::date as order_month,
         count(*)            as order_count,
         sum(o.order_total)  as gmv,
         avg(o.order_total)  as aov
from     orders_dedup o
join     window_bounds w
   on    o.order_date::timestamp >= w.window_start
  and    o.order_date::timestamp <  dateadd('month', 1, w.window_end)
where    o.order_status not in (3, 4)
group by 1
order by 1
;
