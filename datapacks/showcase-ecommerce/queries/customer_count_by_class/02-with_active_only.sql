-- Class counts, active customers only (ordered in last 90d)
-- Author: PM — looking for "real" segmentation, not stale accounts

SELECT c.customer_class,
       COUNT(DISTINCT c.customer_id) AS total_customers,
       COUNT(DISTINCT CASE WHEN o.order_date::TIMESTAMP >= DATEADD('day', -90,
                                (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
                          THEN c.customer_id END) AS active_customers
FROM   order_entry_db.order_entry.customers c
LEFT   JOIN order_entry_db.order_entry.orders o
       ON   o.customer_id = c.customer_id AND o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY active_customers DESC
;
