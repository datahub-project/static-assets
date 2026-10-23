-- Quick — do weekend orders skew differently in mode mix? (Curious from ops chat)
select   case when dayofweek(order_date::timestamp) in (0, 6) then 'weekend' else 'weekday' end as period,
         order_mode,
         count(*) as orders,
         avg(order_total) as aov
from     order_entry_db.order_entry.orders
group by 1, 2
order by 1, orders desc
;
