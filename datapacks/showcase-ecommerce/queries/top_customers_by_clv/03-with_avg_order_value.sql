-- CLV leaderboard + per-customer AOV
-- Author: Sarah Chen — Karen asked whether the top CLV are also high-AOV

select   c.customer_id,
         c.cust_first_name,
         c.cust_last_name,
         c.customer_class,
         sum(o.order_total)                   as clv,
         count(distinct o.order_id)           as orders,
         sum(o.order_total)
           / count(distinct o.order_id)       as aov_per_customer
from     order_entry_db.order_entry.orders    o
join     order_entry_db.order_entry.customers c using (customer_id)
where    o.order_status not in (3, 4)
group by 1, 2, 3, 4
order by clv desc
limit    10
;
