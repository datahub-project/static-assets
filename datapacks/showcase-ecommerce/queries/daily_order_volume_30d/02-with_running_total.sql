-- Daily orders w/ running 30-day total
-- Author: James Wilson — for the Looker dashboard tooltip

WITH daily AS (
    SELECT TO_DATE(order_date::TIMESTAMP) AS order_day,
           COUNT(*)                       AS order_count,
           SUM(order_total)               AS revenue
    FROM   order_entry_db.order_entry.orders
    WHERE  order_date::TIMESTAMP >= DATEADD('day', -30,
                                            (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
    GROUP  BY 1
)
SELECT order_day,
       order_count,
       revenue,
       SUM(order_count) OVER (ORDER BY order_day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_orders,
       SUM(revenue)     OVER (ORDER BY order_day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_revenue
FROM   daily
ORDER  BY order_day
;
