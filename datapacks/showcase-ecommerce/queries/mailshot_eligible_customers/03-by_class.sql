-- Mailshot consent by customer class — which segments are most reachable?
-- Author: Sarah Chen

-- mailshot is stored as 0/1 (NUMBER), not 'Y'/'N' as the original docs claimed.
select   customer_class,
         count(*)                                           as customers,
         sum(case when mailshot = 1 then 1 else 0 end)      as mailshot_yes,
         sum(case when mailshot = 1 then 1 else 0 end) * 100.0 / count(*) as pct_opt_in
from     order_entry_db.order_entry.customers
group by 1
order by pct_opt_in desc
;
