-- Marketing pulled in for ABM planning: which categories do Enterprise customers spend on?
-- One-off, won't need this again.

SELECT category_name,
       COUNT(DISTINCT order_id) AS orders,
       SUM(line_total)          AS revenue
FROM   order_entry_db.analytics.order_details
WHERE  customer_class = 'Enterprise'
GROUP  BY 1
ORDER  BY revenue DESC
LIMIT  10
;
