-- Top 20 products by revenue — last full quarter
-- Author: Sarah Chen
-- Revenue uses order_items.unit_price (post-discount), NOT products.list_price.

WITH q_bounds AS (
    SELECT DATE_TRUNC('quarter', MAX(order_date::TIMESTAMP))                   AS this_q_start,
           DATEADD('quarter', -1, DATE_TRUNC('quarter', MAX(order_date::TIMESTAMP))) AS last_q_start
    FROM   order_entry_db.order_entry.orders
)
SELECT p.product_id,
       p.product_name,
       SUM(oi.unit_price * oi.quantity) AS revenue,
       COUNT(DISTINCT oi.order_id)      AS orders,
       SUM(oi.quantity)                 AS units_sold
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.products    p  USING (product_id)
CROSS  JOIN q_bounds q
WHERE  o.order_date::TIMESTAMP >= q.last_q_start
  AND  o.order_date::TIMESTAMP <  q.this_q_start
  AND  o.order_status NOT IN (3, 4)
GROUP  BY 1, 2
ORDER  BY revenue DESC
LIMIT  20
;
