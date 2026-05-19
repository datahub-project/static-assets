-- Looking at the Video Camera (product 385) — it's marked Discontinued in catalog
-- but we keep seeing it on dashboards. Want to see the order history so I can
-- explain to merchandising whether to actually pull it from BI.

SELECT TO_DATE(o.order_date::TIMESTAMP) AS order_day,
       COUNT(*)                         AS orders,
       SUM(oi.quantity)                 AS units,
       SUM(oi.unit_price * oi.quantity) AS revenue
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
WHERE  oi.product_id = 385
GROUP  BY 1
ORDER  BY 1 DESC
LIMIT  30
;
