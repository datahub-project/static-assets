-- Category revenue with % share of total
-- Author: BID

SELECT category_name,
       SUM(line_total)                                AS revenue,
       SUM(line_total) * 100.0 / SUM(SUM(line_total)) OVER () AS pct_of_total,
       COUNT(DISTINCT order_id)                       AS orders
FROM   order_entry_db.analytics.order_details
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
