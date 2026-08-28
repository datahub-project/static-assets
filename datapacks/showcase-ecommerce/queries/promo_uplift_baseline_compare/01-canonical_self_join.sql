-- Promotional uplift: revenue during window vs equivalent prior window
-- Author: David Kim
-- Promotion windows that have NULL end_date treated as "still running" — skipping those for the comparison.

WITH active_promos AS (
    SELECT promotion_id, promotion_name,
           promotion_start_date::TIMESTAMP AS promo_start,
           promotion_end_date::TIMESTAMP   AS promo_end,
           DATEDIFF('day', promotion_start_date::TIMESTAMP, promotion_end_date::TIMESTAMP) AS promo_len_days
    FROM   order_entry_db.order_entry.promotions
    WHERE  promotion_end_date IS NOT NULL
),
during AS (
    SELECT p.promotion_id, SUM(o.order_total) AS revenue_during
    FROM   active_promos p
    JOIN   order_entry_db.order_entry.orders o ON o.order_date::TIMESTAMP BETWEEN p.promo_start AND p.promo_end
    GROUP  BY 1
),
before AS (
    SELECT p.promotion_id, SUM(o.order_total) AS revenue_before
    FROM   active_promos p
    JOIN   order_entry_db.order_entry.orders o ON o.order_date::TIMESTAMP BETWEEN
               DATEADD('day', -p.promo_len_days, p.promo_start) AND p.promo_start
    GROUP  BY 1
)
SELECT p.promotion_id, p.promotion_name,
       b.revenue_before, d.revenue_during,
       d.revenue_during - b.revenue_before                 AS uplift,
       (d.revenue_during - b.revenue_before) * 100.0
           / NULLIF(b.revenue_before, 0)                   AS uplift_pct
FROM   active_promos p
LEFT   JOIN during d USING (promotion_id)
LEFT   JOIN before b USING (promotion_id)
ORDER  BY uplift DESC;
