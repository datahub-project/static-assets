-- Customer distribution via order_details (shipping_country pre-resolved)
select shipping_country, count(distinct customer_id) as customers, count(distinct order_id) as orders, sum(order_total) as revenue
from   order_entry_db.analytics.order_details
where  order_status not in (3, 4)
group by 1 order by revenue desc;
