-- Promotion budget vs realised discount value
-- Author: Sarah Chen — per Promo Attribution runbook, budget != actual discount

WITH actual AS (
    SELECT o.promotion_id,
           SUM((p.list_price - oi.unit_price) * oi.quantity) AS actual_discount
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.products    p  USING (product_id)
    JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
    WHERE  o.promotion_id IS NOT NULL
    GROUP  BY 1
)
SELECT pr.promotion_id, pr.promotion_name, pr.promotion_cost AS allocated_budget,
       a.actual_discount
FROM   order_entry_db.order_entry.promotions pr
LEFT   JOIN actual a USING (promotion_id)
ORDER  BY pr.promotion_cost DESC;
