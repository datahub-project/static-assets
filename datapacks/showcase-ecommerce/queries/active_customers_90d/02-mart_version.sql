-- Active customers via mart
select count(distinct customer_id) as active_customers_90d
from   order_entry_db.analytics.order_details
where  order_date::timestamp >= dateadd('day', -90, (select max(order_date::timestamp) from order_entry_db.analytics.order_details))
  and  order_status not in (3, 4);
