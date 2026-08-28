-- attempted: order_date → dispatch → delivery funnel by week
-- got distracted by the fact that estimated_delivery is sometimes BEFORE dispatch_date
-- which breaks the funnel logic. parking this for now.

SELECT TO_DATE(order_date::TIMESTAMP) AS day,
       COUNT(*) AS orders
       -- , next: count items dispatched within 2 days
       -- , next: count items "delivered" (estimated_delivery passed)
FROM order_entry_db.order_entry.orders
GROUP BY 1 ORDER BY 1 DESC LIMIT 30;
