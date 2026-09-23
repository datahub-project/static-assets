-- Discount rate sanity-check vs min_price floor — flag any below min_price
-- Author: DQE / Julia
SELECT pr.promotion_id, pr.promotion_name,
       AVG((p.list_price - oi.unit_price) / NULLIF(p.list_price, 0) * 100) AS avg_discount_pct,
       COUNT(CASE WHEN oi.unit_price < p.min_price THEN 1 END) AS lines_below_min_price
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.products    p  USING (product_id)
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.promotions  pr USING (promotion_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1, 2
ORDER  BY lines_below_min_price DESC, avg_discount_pct DESC;
