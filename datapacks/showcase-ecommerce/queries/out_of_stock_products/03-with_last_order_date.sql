-- OOS products + when they were last ordered
-- Author: Sarah Chen (Senior Data Analyst)
--
-- Merchandising asks for OOS items they can prioritise restocking. Pull the
-- last order date so they can rank by recency of demand: high-demand OOS items
-- restock first.

WITH oos AS (
    SELECT product_id
    FROM   order_entry_db.order_entry.inventories
    GROUP  BY product_id
    HAVING SUM(GREATEST(quantity_on_hand, 0)) = 0
),
last_order AS (
    -- one row per product with the most recent order date it appeared on
    SELECT oi.product_id,
           MAX(o.order_date::TIMESTAMP) AS last_ordered_at,
           COUNT(*)                     AS line_items_lifetime
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
    GROUP  BY oi.product_id
)
SELECT p.product_id,
       p.product_name,
       p.product_status,
       p.list_price,
       lo.last_ordered_at,
       DATEDIFF('day', lo.last_ordered_at,
                (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders)
       )                                       AS days_since_last_sale,
       lo.line_items_lifetime
FROM   oos                                      oos
JOIN   order_entry_db.order_entry.products      p  USING (product_id)
LEFT   JOIN last_order                          lo USING (product_id)
ORDER  BY lo.last_ordered_at DESC NULLS LAST
;
