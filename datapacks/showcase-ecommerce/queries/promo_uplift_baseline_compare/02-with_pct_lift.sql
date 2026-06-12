-- Same uplift but only the % column for the slide
-- Author: David Kim

with promos as (
    select promotion_id, promotion_name,
           promotion_start_date::timestamp as ps, promotion_end_date::timestamp as pe,
           datediff('day', promotion_start_date::timestamp, promotion_end_date::timestamp) as length_days
    from order_entry_db.order_entry.promotions
    where promotion_end_date is not null
)
select p.promotion_name,
       (
           select sum(order_total) from order_entry_db.order_entry.orders
           where order_date::timestamp between p.ps and p.pe
       )
       / nullif((
           select sum(order_total) from order_entry_db.order_entry.orders
           where order_date::timestamp between dateadd('day', -p.length_days, p.ps) and p.ps
       ), 0) - 1 as uplift_multiplier
from   promos p
order by uplift_multiplier desc nulls last;
