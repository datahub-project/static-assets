-- Monthly fill rate broken out by warehouse
-- Author: Sarah Chen

SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS order_month,
       w.warehouse_name,
       COUNT(*)                                            AS items_ordered,
       COUNT(oi.dispatch_date)                             AS items_dispatched,
       COUNT(oi.dispatch_date) * 100.0 / NULLIF(COUNT(*), 0) AS fill_rate_pct
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
JOIN   order_entry_db.order_entry.warehouses  w  USING (warehouse_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1, 2
ORDER  BY 1, 2
;
