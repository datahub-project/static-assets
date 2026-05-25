-- Top promos by revenue, attributed only within active promo window
-- Author: David Kim (Data Scientist)
--
-- Per the Promo Attribution runbook step 2: enforce that the order_date falls
-- inside [promotion_start_date, promotion_end_date]. Catches data quality
-- issues where promotion_id is set on orders that pre-date or post-date the
-- campaign. Treats NULL end_date as "still active" so we don't drop ongoing
-- campaign attributions.

WITH promo_attribution AS (
    SELECT  o.order_id,
            o.order_total,
            o.order_date::TIMESTAMP                     AS order_ts,
            p.promotion_id,
            p.promotion_name,
            p.promotion_start_date::TIMESTAMP           AS promo_start,
            COALESCE(p.promotion_end_date::TIMESTAMP,
                     '9999-12-31'::TIMESTAMP)           AS promo_end
    FROM    order_entry_db.order_entry.orders     o
    JOIN    order_entry_db.order_entry.promotions p ON o.promotion_id = p.promotion_id
    WHERE   o.order_status NOT IN (3, 4)
)
SELECT promotion_id,
       promotion_name,
       COUNT(DISTINCT order_id)  AS orders_in_window,
       SUM(order_total)          AS revenue_in_window,
       SUM(CASE WHEN order_ts NOT BETWEEN promo_start AND promo_end
                THEN 1 ELSE 0 END) AS orders_outside_window      -- data-quality canary
FROM   promo_attribution
WHERE  order_ts BETWEEN promo_start AND promo_end
GROUP  BY 1, 2
ORDER  BY revenue_in_window DESC
LIMIT  20
;
