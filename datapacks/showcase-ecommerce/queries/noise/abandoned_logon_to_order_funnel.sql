-- Wanted to compute logon → order conversion but logon table doesn't have
-- a session_id or order_id reference; just customer_id + logon_date.
-- Not sure how to attribute logons to subsequent orders. Punt for now.

SELECT customer_id, COUNT(*) AS logons
FROM order_entry_db.order_entry.logon
GROUP BY 1 ORDER BY logons DESC LIMIT 10;
-- continue here once data model is clear
