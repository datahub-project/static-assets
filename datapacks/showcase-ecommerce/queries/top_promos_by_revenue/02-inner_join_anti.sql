-- Top promos by revenue (promotion-driven join)
-- Author: James Wilson (BI Developer)
--
-- Drives the join from the promotions table, INNER joining orders.
-- Works for this question because we *want* only promoted orders, but the
-- runbook flags this shape as a footgun: if someone reuses it for a baseline
-- ("revenue with vs without promotion") the null-promo orders get dropped.

SELECT   p.promotion_id,
         p.promotion_name,
         COUNT(o.order_id)        AS orders_attributed,
         SUM(o.order_total)       AS attributed_revenue
FROM     order_entry_db.order_entry.promotions p
INNER JOIN order_entry_db.order_entry.orders   o
        ON p.promotion_id = o.promotion_id
WHERE    o.order_status NOT IN (3, 4)
GROUP BY 1, 2
ORDER BY attributed_revenue DESC
LIMIT    20
;
