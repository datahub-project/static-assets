-- Audit via order_details (dedup order_id since mart is line-item grain)
select to_date(order_date::timestamp) as day, count(distinct order_id) as orders
from order_entry_db.analytics.order_details
where order_date::timestamp >= dateadd('day', -14, (select max(order_date::timestamp) from order_entry_db.analytics.order_details))
group by 1 order by 1 desc;
