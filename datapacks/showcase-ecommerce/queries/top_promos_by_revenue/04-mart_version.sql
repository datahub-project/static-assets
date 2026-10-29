-- Top promos by revenue — mart shortcut
-- Author: James Wilson (BI Developer)
--
-- analytics.order_details has promotion_name pre-resolved + the discount columns.
-- Grain is line-item; dedupe via the order header before summing.

with order_header as (
    select   order_id,
             any_value(promotion_id)    as promotion_id,
             any_value(promotion_name)  as promotion_name,
             any_value(order_total)     as order_total,
             any_value(order_status)    as order_status
    from     order_entry_db.analytics.order_details
    group by order_id
)
select   promotion_id,
         promotion_name,
         count(*)                       as orders_attributed,
         sum(order_total)               as attributed_revenue,
         avg(order_total)               as aov_on_promo
from     order_header
where    promotion_id is not null
  and    order_status not in (3, 4)
group by 1, 2
order by attributed_revenue desc
limit    20
;
