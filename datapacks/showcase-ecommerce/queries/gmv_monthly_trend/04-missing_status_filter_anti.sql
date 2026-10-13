-- Monthly revenue trend
-- Author: Karen Okonkwo (Product Manager) — quick check before the prod review
--
-- Note from Sarah: this one drops the order_status exclusion that finance uses
-- for the official GMV. So this number will be higher than the dashboard for
-- months with more cancellations / holds. Still useful as a "top of funnel" view.

SELECT TO_CHAR(order_date::TIMESTAMP, 'YYYY-MM') AS month,
       SUM(order_total)                          AS revenue,
       COUNT(*)                                  AS orders
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP >= DATEADD('month', -12,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP  BY 1
ORDER  BY 1
;
