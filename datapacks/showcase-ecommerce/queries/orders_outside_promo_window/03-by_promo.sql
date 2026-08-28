-- Misattribution counts grouped by promotion
select p.promotion_name,
       count(*) as misattributed_orders,
       avg(case when o.order_date::timestamp < p.promotion_start_date::timestamp
                then datediff('day', o.order_date::timestamp, p.promotion_start_date::timestamp)
                else datediff('day', coalesce(p.promotion_end_date::timestamp, '9999-12-31'::timestamp), o.order_date::timestamp)
           end) as avg_days_off
from order_entry_db.order_entry.orders o
join order_entry_db.order_entry.promotions p using (promotion_id)
where o.order_date::timestamp not between p.promotion_start_date::timestamp
                                       and coalesce(p.promotion_end_date::timestamp, '9999-12-31'::timestamp)
group by 1 order by misattributed_orders desc;
