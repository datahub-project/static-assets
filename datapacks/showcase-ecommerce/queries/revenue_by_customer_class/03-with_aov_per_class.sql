-- Revenue + AOV per class
-- Author: PM / Karen
-- Wanted to know if AOV varies materially by class (it should, intuitively).

select   customer_class,
         count(distinct order_id)                           as orders,
         sum(order_total)                                   as revenue,
         sum(order_total) / count(distinct order_id)        as aov,
         count(distinct customer_id)                        as customers,
         sum(order_total) / count(distinct customer_id)     as avg_revenue_per_customer
from     order_entry_db.analytics.order_details
group by 1
order by aov desc
;
