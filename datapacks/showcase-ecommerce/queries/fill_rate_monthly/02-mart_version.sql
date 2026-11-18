-- Fill rate via the mart
-- Author: James Wilson

select date_trunc('month', order_date::timestamp)::date as order_month,
       count(*)                                          as items_ordered,
       count(dispatch_date)                              as items_dispatched,
       count(dispatch_date) * 100.0 / nullif(count(*), 0) as fill_rate_pct
from   order_entry_db.analytics.order_details
where  order_status not in (3, 4)
group by 1 order by 1
;
