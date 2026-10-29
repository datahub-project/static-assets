-- What share of revenue do the top-decile (top 10%) customers contribute?
-- Author: David Kim — for the 80/20 deck

WITH clv AS (
    SELECT customer_id,
           SUM(order_total) AS lifetime_revenue,
           NTILE(10) OVER (ORDER BY SUM(order_total) DESC) AS decile
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT decile,
       COUNT(*)                AS customers,
       SUM(lifetime_revenue)   AS revenue_in_decile,
       SUM(lifetime_revenue) * 100.0 / SUM(SUM(lifetime_revenue)) OVER () AS pct_of_total_revenue
FROM   clv
GROUP  BY 1
ORDER  BY 1
;
