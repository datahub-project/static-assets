-- Full breakdown of order 2008
SELECT o.order_id, o.order_date, o.order_total, o.order_status, o.payment_method_code,
       oi.line_item_id, p.product_name, oi.unit_price, oi.quantity,
       oi.unit_price * oi.quantity AS line_total, oi.dispatch_date, oi.return_date
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.order_items oi USING (order_id)
JOIN order_entry_db.order_entry.products p USING (product_id)
WHERE o.order_id = 2008
ORDER BY oi.line_item_id;
