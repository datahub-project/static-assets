-- Which products have only ever sold in non-new condition?
-- Trying to identify the marketplace-only catalogue.

SELECT p.product_id,
       p.product_name,
       COUNT(*) AS line_items,
       LISTAGG(DISTINCT oi.condition, ', ') WITHIN GROUP (ORDER BY oi.condition) AS conditions_seen
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.products    p USING (product_id)
GROUP  BY 1, 2
HAVING SUM(CASE WHEN oi.condition = 'New' THEN 1 ELSE 0 END) = 0
ORDER  BY line_items DESC
LIMIT  20
;
