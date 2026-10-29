-- Budget vs actual with variance pct (over- vs under-budget)
WITH actual AS (
    SELECT o.promotion_id, SUM((p.list_price - oi.unit_price) * oi.quantity) AS actual_discount
    FROM order_entry_db.order_entry.order_items oi
    JOIN order_entry_db.order_entry.products p USING (product_id)
    JOIN order_entry_db.order_entry.orders o USING (order_id)
    WHERE o.promotion_id IS NOT NULL
    GROUP BY 1
)
SELECT pr.promotion_name, pr.promotion_cost AS budget, COALESCE(a.actual_discount, 0) AS actual,
       COALESCE(a.actual_discount, 0) - pr.promotion_cost AS variance,
       (COALESCE(a.actual_discount, 0) - pr.promotion_cost) * 100.0 / NULLIF(pr.promotion_cost, 0) AS variance_pct,
       CASE WHEN a.actual_discount > pr.promotion_cost * 1.1 THEN 'over_budget'
            WHEN a.actual_discount < pr.promotion_cost * 0.5 THEN 'under_used'
            ELSE 'on_budget' END AS status
FROM order_entry_db.order_entry.promotions pr
LEFT JOIN actual a USING (promotion_id)
ORDER BY ABS(COALESCE(a.actual_discount, 0) - pr.promotion_cost) DESC;
