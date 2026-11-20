-- Stock value ranking
-- Author: Sarah Chen

WITH wh_value AS (
    SELECT w.warehouse_id,
           w.warehouse_name,
           SUM(GREATEST(i.quantity_on_hand, 0) * p.list_price) AS stock_value
    FROM   order_entry_db.order_entry.inventories i
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
    GROUP  BY 1, 2
)
SELECT warehouse_id,
       warehouse_name,
       stock_value,
       RANK() OVER (ORDER BY stock_value DESC)         AS rank_by_value,
       stock_value * 100.0 / SUM(stock_value) OVER ()  AS pct_of_network
FROM   wh_value
ORDER  BY rank_by_value
;
