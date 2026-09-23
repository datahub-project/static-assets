-- Retention grid as percentages (vs the cohort size at m0)
-- Author: David Kim

WITH first_order AS (
    SELECT customer_id, MIN(order_date::TIMESTAMP) AS first_order_at
    FROM   order_entry_db.order_entry.orders WHERE order_status NOT IN (3, 4) GROUP BY 1
),
labelled AS (
    SELECT fo.customer_id,
           DATE_TRUNC('month', fo.first_order_at) AS cohort_month,
           MONTHS_BETWEEN(DATE_TRUNC('month', o.order_date::TIMESTAMP), DATE_TRUNC('month', fo.first_order_at)) AS month_offset
    FROM first_order fo
    JOIN order_entry_db.order_entry.orders o ON o.customer_id = fo.customer_id AND o.order_status NOT IN (3, 4)
),
grid AS (
    SELECT cohort_month, month_offset, COUNT(DISTINCT customer_id) AS active_customers
    FROM labelled GROUP BY 1, 2
),
cohort_size AS (
    SELECT cohort_month, active_customers AS cohort_size FROM grid WHERE month_offset = 0
)
SELECT g.cohort_month::DATE, g.month_offset, g.active_customers,
       g.active_customers * 100.0 / cs.cohort_size AS retention_pct
FROM   grid g JOIN cohort_size cs USING (cohort_month)
ORDER  BY g.cohort_month, g.month_offset
;
