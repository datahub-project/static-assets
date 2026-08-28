-- Top 20 products by revenue, last quarter — via the mart
-- order_details has line_total pre-computed.

with q as (
    select date_trunc('quarter', max(order_date::timestamp))                          as this_q_start,
           dateadd('quarter', -1, date_trunc('quarter', max(order_date::timestamp)))  as last_q_start
    from   order_entry_db.analytics.order_details
)
select   product_id,
         product_name,
         sum(line_total)             as revenue,
         count(distinct order_id)    as orders,
         sum(quantity)               as units_sold
from     order_entry_db.analytics.order_details od, q
where    order_date::timestamp >= q.last_q_start
  and    order_date::timestamp <  q.this_q_start
  and    order_status not in (3, 4)
group by 1, 2
order by revenue desc
limit    20
;
