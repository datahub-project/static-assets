-- Revenue rolled up to top-level category via the parent_category_id tree
-- Author: David Kim — needed this for the category P&L review.
-- product_categories is self-referential. Recursive CTE to find root for each leaf,
-- then sum revenue under each root.

WITH RECURSIVE cat_tree AS (
    SELECT category_id,
           category_name,
           parent_category_id,
           category_id   AS root_id,
           category_name AS root_name,
           1 AS depth
    FROM   order_entry_db.order_entry.product_categories
    WHERE  parent_category_id IS NULL
    UNION ALL
    SELECT c.category_id,
           c.category_name,
           c.parent_category_id,
           t.root_id,
           t.root_name,
           t.depth + 1
    FROM   order_entry_db.order_entry.product_categories c
    JOIN   cat_tree t ON c.parent_category_id = t.category_id
),
product_revenue AS (
    SELECT p.product_id,
           p.category_id,
           SUM(oi.unit_price * oi.quantity) AS rev
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    JOIN   order_entry_db.order_entry.orders      o USING (order_id)
    WHERE  o.order_status NOT IN (3, 4)
    GROUP  BY 1, 2
)
SELECT t.root_name           AS top_level_category,
       SUM(pr.rev)            AS revenue,
       COUNT(DISTINCT pr.product_id) AS products,
       MAX(t.depth)           AS deepest_subcategory
FROM   product_revenue pr
JOIN   cat_tree t USING (category_id)
GROUP  BY 1
ORDER  BY revenue DESC
;
