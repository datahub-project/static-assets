-- Class counts via mart (line-item grain — dedupe with DISTINCT customer_id)
select customer_class, count(distinct customer_id) as customers
from   order_entry_db.analytics.order_details
group by 1 order by customers desc;
