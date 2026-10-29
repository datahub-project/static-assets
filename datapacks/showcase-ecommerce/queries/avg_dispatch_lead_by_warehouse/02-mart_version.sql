-- Same metric via order_details
-- Author: James Wilson

select warehouse_name,
       count(*) as line_items,
       avg(datediff('day', order_date::timestamp, dispatch_date::timestamp)) as avg_days
from   order_entry_db.analytics.order_details
where  dispatch_date is not null
group by 1
order by avg_days
;
