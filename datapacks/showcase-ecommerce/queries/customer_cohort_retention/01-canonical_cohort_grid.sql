-- Cohort retention — first-order month × months-since-first-order
-- Author: David Kim
-- Cohort = customers who placed their first order in a given month.
-- Cell = how many of those customers ordered again in month_offset N.

WITH first_order AS (
    SELECT customer_id, MIN(order_date::TIMESTAMP) AS first_order_at
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
),
labelled AS (
    SELECT fo.customer_id,
           DATE_TRUNC('month', fo.first_order_at)                                    AS cohort_month,
           DATE_TRUNC('month', o.order_date::TIMESTAMP)                              AS active_month,
           MONTHS_BETWEEN(DATE_TRUNC('month', o.order_date::TIMESTAMP), DATE_TRUNC('month', fo.first_order_at)) AS month_offset
    FROM   first_order fo
    JOIN   order_entry_db.order_entry.orders o
           ON o.customer_id = fo.customer_id AND o.order_status NOT IN (3, 4)
)
SELECT cohort_month::DATE        AS cohort_month_d,
       month_offset,
       COUNT(DISTINCT customer_id) AS active_customers
FROM   labelled
GROUP  BY 1, 2
ORDER  BY 1, 2
;
