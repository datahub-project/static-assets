with hdr as (
    select order_id, any_value(order_date) as order_date, any_value(promotion_id) as promo, any_value(order_status) as status
    from order_entry_db.analytics.order_details group by order_id
)
select date_trunc('month', order_date::timestamp)::date as order_month,
       count(*) as orders, count(promo) as promoted,
       count(promo) * 100.0 / nullif(count(*), 0) as attachment_rate_pct
from hdr where status not in (3, 4)
group by 1 order by 1;
