-- New customers per month (signup date)
-- Author: PM / Karen

SELECT DATE_TRUNC('month', customer_since::TIMESTAMP)::DATE AS signup_month,
       COUNT(*) AS new_customers
FROM   order_entry_db.order_entry.customers
GROUP  BY 1
ORDER  BY 1
;
