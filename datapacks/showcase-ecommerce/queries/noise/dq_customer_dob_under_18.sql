-- Implausible DoB — under 18 or over 120
SELECT COUNT(*) AS customers_dob_under_18
FROM order_entry_db.order_entry.customers
WHERE DATEDIFF('year', dob::DATE, CURRENT_DATE) < 18 OR DATEDIFF('year', dob::DATE, CURRENT_DATE) > 120;
