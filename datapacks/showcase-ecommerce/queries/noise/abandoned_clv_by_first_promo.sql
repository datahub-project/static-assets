-- Wanted to see whether customers whose first order used a promo end up with
-- different CLV than customers whose first order was full-price. Got partway
-- and realised I need to also account for the "first promo used" cohort across
-- multiple orders, not just whether they had ANY promo. Leaving it for now.
-- TODO: come back when I have time / talk to David about the right framing.

WITH first_order AS (
    SELECT customer_id,
           MIN(order_date::TIMESTAMP) AS first_order_at
           --, ???  how do I tie this back to whether the FIRST order had a promo?
    FROM   order_entry_db.order_entry.orders
    GROUP  BY 1
)
-- SELECT first_promo_flag, AVG(lifetime_revenue) ...
-- but lifetime_revenue is per-customer not per-cohort
-- so probably need another CTE

SELECT customer_id, first_order_at
FROM   first_order
ORDER  BY first_order_at
LIMIT  20
;

-- leftover scratch:
-- select count(distinct customer_id) from order_entry_db.order_entry.orders
-- where promotion_id is not null  -- 4831 customers used a promo at least once
