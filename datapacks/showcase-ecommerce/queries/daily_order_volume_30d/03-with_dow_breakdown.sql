-- Day-of-week pattern for orders, last 30 days
-- Karen asked which days are quietest for ops planning.
-- Author: Andrea Garcia

select   dayname(order_date::timestamp)     as day_of_week,
         dayofweek(order_date::timestamp)   as dow_num,
         count(*)                           as order_count,
         avg(order_total)                   as aov,
         sum(order_total)                   as revenue
from     order_entry_db.order_entry.orders
where    order_date::timestamp >= dateadd('day', -30,
             (select max(order_date::timestamp) from order_entry_db.order_entry.orders))
group by 1, 2
order by dow_num
;
