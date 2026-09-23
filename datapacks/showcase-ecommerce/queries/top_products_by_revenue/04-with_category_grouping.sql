-- Top revenue products grouped by category for the merch review
-- Author: Sarah Chen — rolls up by category, ranks within

WITH revenue AS (
    SELECT p.product_id,
           p.product_name,
           p.category_id,
           SUM(oi.unit_price * oi.quantity) AS rev
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    JOIN   order_entry_db.order_entry.orders      o USING (order_id)
    WHERE  o.order_date::TIMESTAMP >= DATEADD('quarter', -1,
               (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
      AND  o.order_status NOT IN (3, 4)
    GROUP  BY 1, 2, 3
)
SELECT c.category_name,
       r.product_id,
       r.product_name,
       r.rev,
       RANK() OVER (PARTITION BY c.category_name ORDER BY r.rev DESC) AS rank_in_cat
FROM   revenue r
JOIN   order_entry_db.order_entry.product_categories c USING (category_id)
QUALIFY rank_in_cat <= 3            -- top 3 per category
ORDER  BY c.category_name, rank_in_cat
;
