-- Back-order holds currently in flight (per Orders runbook)
SELECT COUNT(*) AS hold_orders, SUM(order_total) AS revenue_held
FROM order_entry_db.order_entry.orders
WHERE wait_till_complete_yn = 'Y' AND order_status IN (0, 1);
