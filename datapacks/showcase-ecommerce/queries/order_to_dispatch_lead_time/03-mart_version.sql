-- Same metric via order_details
-- Author: James Wilson

select avg(datediff('day', order_date::timestamp, dispatch_date::timestamp)) as avg_days_to_dispatch,
       count(*) as line_items
from   order_entry_db.analytics.order_details
where  dispatch_date is not null
;
