-- Credit utilization ratio (spend / credit_limit) — risk/marketing list
-- Author: Sarah Chen

with cust_spend as (
    select c.customer_id, c.credit_limit, sum(o.order_total) as spend
    from order_entry_db.order_entry.customers c
    join order_entry_db.order_entry.orders o using (customer_id)
    where o.order_status not in (3, 4)
    group by 1, 2
)
select customer_id, credit_limit, spend,
       spend / nullif(credit_limit, 0) as utilization_ratio,
       case when spend > credit_limit then 'over_limit'
            when spend > credit_limit * 0.8 then 'high_utilization'
            when spend > credit_limit * 0.5 then 'medium'
            else 'low' end as utilization_band
from cust_spend
order by utilization_ratio desc nulls last
limit 25;
