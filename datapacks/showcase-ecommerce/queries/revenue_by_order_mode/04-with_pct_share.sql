-- Channel mix %
-- Author: Ian Chen — exec slide

SELECT order_mode,
       COUNT(*)                                          AS orders,
       SUM(order_total)                                  AS revenue,
       SUM(order_total) * 100.0 / SUM(SUM(order_total)) OVER () AS pct_of_revenue,
       COUNT(*)         * 100.0 / SUM(COUNT(*))         OVER () AS pct_of_orders
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
