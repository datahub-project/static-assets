-- Revenue + AOV per class
-- Author: PM / Karen
-- Wanted to know if AOV varies materially by class (it should, intuitively).
-- Sarah: order_details is one row per line item, dedupe to the order header first.

with order_header as (
    select   order_id,
             any_value(customer_class) as customer_class,
             any_value(customer_id)    as customer_id,
             any_value(order_total)    as order_total,
             any_value(order_status)   as order_status
    from     order_entry_db.analytics.order_details
    group by order_id
)
select   customer_class,
         count(*)                                       as orders,
         sum(order_total)                               as revenue,
         sum(order_total) / count(*)                    as aov,
         count(distinct customer_id)                    as customers,
         sum(order_total) / count(distinct customer_id) as avg_revenue_per_customer
from     order_header
where    order_status not in (3, 4)
group by 1
order by aov desc
;
