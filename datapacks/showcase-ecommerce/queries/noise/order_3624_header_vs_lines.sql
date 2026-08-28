-- Header total vs line items for order 3624 (per the runbook gotcha)
SELECT o.order_total AS header_total,
       SUM(oi.unit_price * oi.quantity) AS line_sum,
       o.order_total - SUM(oi.unit_price * oi.quantity) AS gap
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.order_items oi USING (order_id)
WHERE o.order_id = 3624
GROUP BY o.order_total;
