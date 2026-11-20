-- Revenue by product category — full history
-- Author: Sarah Chen

SELECT c.category_id,
       c.category_name,
       SUM(oi.unit_price * oi.quantity) AS revenue,
       COUNT(DISTINCT o.order_id)        AS orders,
       SUM(oi.quantity)                  AS units_sold
FROM   order_entry_db.order_entry.order_items        oi
JOIN   order_entry_db.order_entry.orders             o  USING (order_id)
JOIN   order_entry_db.order_entry.products           p  USING (product_id)
JOIN   order_entry_db.order_entry.product_categories c  USING (category_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1, 2
ORDER  BY revenue DESC
;
