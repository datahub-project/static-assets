-- Top products by revenue — quick version
-- Author: Karen Okonkwo
-- !! finance flagged this one: list_price ignores discounts so this OVERSTATES
-- revenue on promoted lines. Should be order_items.unit_price. Leaving on the
-- wiki as "do not use" example for now.

SELECT p.product_id,
       p.product_name,
       SUM(p.list_price * oi.quantity) AS revenue_overstated
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.orders      o USING (order_id)
WHERE  o.order_date::TIMESTAMP >= DATEADD('quarter', -1,
             (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP  BY 1, 2
ORDER  BY revenue_overstated DESC
LIMIT  20
;
