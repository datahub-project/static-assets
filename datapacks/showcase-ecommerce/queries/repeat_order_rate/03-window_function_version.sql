-- Repeat-order rate via window function on per-order data
-- Author: David Kim
--
-- Window-function take. Slightly heavier than the CTE version but easier to
-- repurpose for "Nth order metrics" later.

WITH ordered AS (
    SELECT customer_id,
           order_id,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date::TIMESTAMP) AS n
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
)
SELECT
    COUNT(DISTINCT customer_id)                          AS total_customers,
    COUNT(DISTINCT CASE WHEN n >= 2 THEN customer_id END) AS repeat_customers,
    COUNT(DISTINCT CASE WHEN n >= 2 THEN customer_id END) * 100.0
        / NULLIF(COUNT(DISTINCT customer_id), 0)         AS repeat_rate_pct
FROM   ordered
;
