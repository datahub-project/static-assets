-- Return rate via mart
select category_name,
       count(*) as items_dispatched,
       count(return_date) as items_returned,
       count(return_date) * 100.0 / nullif(count(*), 0) as return_rate_pct
from order_entry_db.analytics.order_details
where dispatch_date is not null
group by 1 order by return_rate_pct desc;
