-- Return rate by channel, with deviation from overall baseline
-- Author: Sarah Chen — for the spotting outliers

with stats as (
    select o.order_mode, count(*) as dispatched, count(oi.return_date) as returned
    from order_entry_db.order_entry.order_items oi
    join order_entry_db.order_entry.orders o using (order_id)
    where oi.dispatch_date is not null
    group by 1
)
select order_mode, dispatched, returned,
       returned * 100.0 / nullif(dispatched, 0) as rate_pct,
       (returned * 100.0 / nullif(dispatched, 0))
         - (sum(returned) over () * 100.0 / nullif(sum(dispatched) over (), 0)) as vs_baseline_pp
from stats
order by rate_pct desc;
