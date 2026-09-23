-- Top promotions by attributed revenue
-- Author: Sarah Chen (Senior Data Analyst)
--
-- Reference shape from the Promotion Attribution runbook. LEFT JOIN from orders
-- so the same scaffold can be reused for a baseline ("how much revenue is
-- *not* attributed to a promo") without rewriting the join. For this specific
-- question we just filter to promoted rows in the final WHERE.

SELECT p.promotion_id,
       p.promotion_name,
       COUNT(DISTINCT o.order_id)              AS orders_attributed,
       SUM(o.order_total)                      AS attributed_revenue,
       AVG(o.order_total)                      AS aov_on_promo,
       SUM(o.order_total) * 100.0
           / SUM(SUM(o.order_total)) OVER ()   AS pct_of_promoted_revenue
FROM   order_entry_db.order_entry.orders       o
LEFT   JOIN order_entry_db.order_entry.promotions p
       ON   o.promotion_id = p.promotion_id
WHERE  o.promotion_id IS NOT NULL                -- focus on promoted orders
  AND  o.order_status NOT IN (3, 4)              -- exclude held / cancelled
GROUP  BY 1, 2
ORDER  BY attributed_revenue DESC
LIMIT  20
;
