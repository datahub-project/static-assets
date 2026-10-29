-- Time-to-return distribution
-- Author: David Kim — looking for the "fast return" cliff

with t as (
    select datediff('day', dispatch_date::timestamp, return_date::timestamp) as days_to_return
    from order_entry_db.order_entry.order_items
    where return_date is not null and dispatch_date is not null
)
select count(*) as returns,
       avg(days_to_return)                                       as mean_days,
       median(days_to_return)                                    as p50,
       percentile_cont(0.25) within group (order by days_to_return) as p25,
       percentile_cont(0.75) within group (order by days_to_return) as p75,
       percentile_cont(0.95) within group (order by days_to_return) as p95,
       max(days_to_return)                                       as max_days,
       count(case when days_to_return <= 7 then 1 end)           as returns_within_7d,
       count(case when days_to_return <= 30 then 1 end)          as returns_within_30d
from t;
