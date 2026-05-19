-- Breakdown of zero/negative orders by status
select order_status,
       count(*) as orders,
       sum(case when order_total = 0 then 1 else 0 end) as zero_totals,
       sum(case when order_total < 0 then 1 else 0 end) as negative_totals,
       min(order_total) as worst_total
from order_entry_db.order_entry.orders
where order_total <= 0
group by 1 order by 1;
