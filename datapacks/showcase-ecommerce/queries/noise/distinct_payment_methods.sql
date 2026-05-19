-- Just enumerating values for the form dropdown
SELECT DISTINCT payment_method_code
FROM order_entry_db.order_entry.orders
ORDER BY 1;
