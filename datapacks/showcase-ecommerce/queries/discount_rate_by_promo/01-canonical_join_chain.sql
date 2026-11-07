-- Discount rate by promotion = avg((list - unit) / list) on promoted lines
-- Author: Sarah Chen
SELECT pr.promotion_id,
       pr.promotion_name,
       AVG((p.list_price - oi.unit_price) / NULLIF(p.list_price, 0) * 100) AS avg_discount_pct,
       SUM((p.list_price - oi.unit_price) * oi.quantity)                   AS total_discount_value
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.products    p  USING (product_id)
JOIN   order_entry_db.order_entry.promotions  pr USING (promotion_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1, 2
ORDER  BY avg_discount_pct DESC;
