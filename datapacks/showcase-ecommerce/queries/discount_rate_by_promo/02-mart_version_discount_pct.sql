-- Discount rate via mart — uses pre-computed discount_percent
select promotion_id, promotion_name,
       avg(discount_percent) as avg_discount_pct,
       sum(discount_amount) as total_discount_value
from order_entry_db.analytics.order_details
where promotion_id is not null and order_status not in (3, 4)
group by 1, 2 order by avg_discount_pct desc;
