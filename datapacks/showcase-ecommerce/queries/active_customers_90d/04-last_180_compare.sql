-- 90-day vs 180-day active customer compare
-- Author: Sarah Chen — how many lapsed in the last 90?

WITH as_of AS (SELECT MAX(order_date::TIMESTAMP) AS t FROM order_entry_db.order_entry.orders)
SELECT
    COUNT(DISTINCT CASE WHEN o.order_date::TIMESTAMP >= DATEADD('day', -90, a.t)
                        THEN o.customer_id END) AS active_90d,
    COUNT(DISTINCT CASE WHEN o.order_date::TIMESTAMP >= DATEADD('day', -180, a.t)
                        THEN o.customer_id END) AS active_180d,
    COUNT(DISTINCT CASE WHEN o.order_date::TIMESTAMP BETWEEN DATEADD('day', -180, a.t)
                                                          AND DATEADD('day', -90, a.t)
                        THEN o.customer_id END) AS active_90_to_180_only
FROM order_entry_db.order_entry.orders o, as_of a
WHERE o.order_status NOT IN (3, 4)
;
