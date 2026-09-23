-- Category revenue via order_details (category_name already resolved)
-- Author: James Wilson

SELECT   category_name,
         SUM(line_total)         AS revenue,
         COUNT(DISTINCT order_id) AS orders
FROM     order_entry_db.analytics.order_details
WHERE    order_status NOT IN (3, 4)
GROUP BY 1
ORDER BY revenue DESC
;
