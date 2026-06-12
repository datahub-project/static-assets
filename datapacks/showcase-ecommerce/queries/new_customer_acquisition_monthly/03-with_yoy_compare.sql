-- Monthly signups with YoY
-- Author: Ian Chen — exec deck

WITH monthly AS (
    SELECT DATE_TRUNC('month', customer_since::TIMESTAMP)::DATE AS signup_month, COUNT(*) AS new_customers
    FROM   order_entry_db.order_entry.customers
    GROUP  BY 1
)
SELECT cur.signup_month, cur.new_customers,
       prv.new_customers                                                 AS prior_year,
       cur.new_customers - prv.new_customers                              AS yoy_delta,
       (cur.new_customers - prv.new_customers) * 100.0
           / NULLIF(prv.new_customers, 0)                                 AS yoy_pct
FROM   monthly cur
LEFT   JOIN monthly prv ON prv.signup_month = DATEADD('year', -1, cur.signup_month)
ORDER  BY cur.signup_month
;
