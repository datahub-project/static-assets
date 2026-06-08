-- Categories ranked by return rate, plus baseline rate for comparison
-- Author: David Kim

WITH stats AS (
    SELECT c.category_name,
           COUNT(*)                AS items_dispatched,
           COUNT(oi.return_date)   AS items_returned
    FROM   order_entry_db.order_entry.order_items        oi
    JOIN   order_entry_db.order_entry.products           p  USING (product_id)
    JOIN   order_entry_db.order_entry.product_categories c  USING (category_id)
    WHERE  oi.dispatch_date IS NOT NULL
    GROUP  BY 1
),
overall AS (
    SELECT SUM(items_returned) * 100.0 / NULLIF(SUM(items_dispatched), 0) AS baseline_rate
    FROM   stats
)
SELECT s.category_name,
       s.items_dispatched,
       s.items_returned,
       s.items_returned * 100.0 / NULLIF(s.items_dispatched, 0) AS category_rate,
       o.baseline_rate,
       (s.items_returned * 100.0 / NULLIF(s.items_dispatched, 0)) - o.baseline_rate AS rate_vs_baseline,
       RANK() OVER (ORDER BY s.items_returned * 100.0 / NULLIF(s.items_dispatched, 0) DESC) AS rank_by_rate
FROM   stats s, overall o
ORDER  BY rank_by_rate
;
