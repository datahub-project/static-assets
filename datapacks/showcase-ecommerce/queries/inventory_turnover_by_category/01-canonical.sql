-- Inventory turnover by category — units sold ÷ total on-hand
-- Author: Sarah Chen — over the full data window

WITH sold AS (
    SELECT p.category_id, SUM(oi.quantity) AS units_sold
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    GROUP  BY 1
),
stock AS (
    SELECT p.category_id,
           SUM(GREATEST(i.quantity_on_hand, 0)) AS total_stock
    FROM   order_entry_db.order_entry.inventories i
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    GROUP  BY 1
)
SELECT c.category_name,
       s.units_sold, st.total_stock,
       s.units_sold * 1.0 / NULLIF(st.total_stock, 0) AS turnover_ratio
FROM   order_entry_db.order_entry.product_categories c
JOIN   sold  s  USING (category_id)
JOIN   stock st USING (category_id)
ORDER  BY turnover_ratio DESC;
