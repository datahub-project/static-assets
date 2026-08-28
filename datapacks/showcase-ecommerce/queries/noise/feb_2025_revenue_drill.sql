-- Feb 2025 came in soft — exec asked why. Pulling daily revenue + order counts
-- for the month to see if it was one bad week or a broader dip.
-- Anchored to Feb only, not parameterising — this is throwaway.

SELECT TO_DATE(order_date::TIMESTAMP) AS order_day,
       COUNT(*)                       AS orders,
       SUM(order_total)               AS revenue,
       AVG(order_total)               AS aov
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP BETWEEN '2025-02-01' AND '2025-02-28 23:59:59'
GROUP  BY 1
ORDER  BY 1
;
