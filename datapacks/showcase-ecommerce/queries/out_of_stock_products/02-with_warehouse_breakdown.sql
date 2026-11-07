-- Out-of-stock products with per-warehouse detail
-- Author: Andrea Garcia (Analytics Engineer)
--
-- Same OOS set as the canonical, but expands per-warehouse so ops can see
-- which sites carry the SKU at all. Useful when buyer asks "did warehouse X
-- ever stock this?" — a NULL on the inventories side means never carried.

WITH oos_products AS (
    SELECT i.product_id
    FROM   order_entry_db.order_entry.inventories i
    GROUP  BY i.product_id
    HAVING SUM(GREATEST(i.quantity_on_hand, 0)) = 0
)
SELECT p.product_id,
       p.product_name,
       w.warehouse_name,
       COALESCE(i.quantity_on_hand, 0)  AS qty_on_hand,
       i.restock_level,
       CASE WHEN i.product_id IS NULL THEN 'never carried'
            WHEN i.quantity_on_hand < 0 THEN 'data anomaly'
            ELSE 'zero stock'
       END                              AS oos_reason
FROM   oos_products                          oos
JOIN   order_entry_db.order_entry.products   p  USING (product_id)
CROSS  JOIN order_entry_db.order_entry.warehouses w
LEFT   JOIN order_entry_db.order_entry.inventories i
       ON   i.product_id = p.product_id
       AND  i.warehouse_id = w.warehouse_id
ORDER  BY p.product_name, w.warehouse_name
;
