-- Customer distribution via order_details (shipping_country pre-resolved)
-- order_details is line-item grain; dedupe to one row per order before summing order_total
with hdr as (
    select order_id, any_value(shipping_country) as shipping_country, any_value(customer_id) as customer_id,
           any_value(order_total) as order_total, any_value(order_status) as order_status
    from   order_entry_db.analytics.order_details
    group by order_id
)
select shipping_country, count(distinct customer_id) as customers, count(*) as orders, sum(order_total) as revenue
from   hdr
where  order_status not in (3, 4)
group by 1 order by revenue desc;
