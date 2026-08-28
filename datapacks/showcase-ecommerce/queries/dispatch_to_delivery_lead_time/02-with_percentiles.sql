-- In-transit time distribution
-- Author: David Kim

with t as (
    select datediff('day', dispatch_date::timestamp, estimated_delivery::timestamp) as transit_days
    from   order_entry_db.order_entry.order_items
    where  dispatch_date is not null and estimated_delivery is not null
)
select avg(transit_days)                                              as mean_days,
       median(transit_days)                                           as p50_days,
       percentile_cont(0.9) within group (order by transit_days)      as p90_days,
       percentile_cont(0.95) within group (order by transit_days)     as p95_days,
       max(transit_days)                                              as max_days
from   t
;
