-- Total stock value by warehouse — using list_price
-- Author: Ben Porter — for the quarterly inventory carry review

SELECT w.warehouse_name,
       COUNT(DISTINCT i.product_id)                  AS sku_count,
       SUM(GREATEST(i.quantity_on_hand, 0))          AS total_units,
       SUM(GREATEST(i.quantity_on_hand, 0) * p.list_price) AS stock_value_list
FROM   order_entry_db.order_entry.inventories i
JOIN   order_entry_db.order_entry.products    p USING (product_id)
JOIN   order_entry_db.order_entry.warehouses  w USING (warehouse_id)
GROUP  BY 1
ORDER  BY stock_value_list DESC
;
