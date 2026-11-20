-- Enterprise vs Small Business revenue
select customer_class, count(distinct order_id) as orders, sum(order_total) as revenue
from order_entry_db.analytics.order_details
where customer_class IN ('Enterprise', 'Small Business')
group by 1;
