-- Zero / negative order totals — DQ check
SELECT order_id, order_date, order_status, order_total
FROM   order_entry_db.order_entry.orders
WHERE  order_total <= 0
ORDER  BY order_total LIMIT 50;
