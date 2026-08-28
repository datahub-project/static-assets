-- Pulling the full order history for customer 963 (Laure Schruurs).
-- CX got a complaint about a missed delivery — need to confirm what she's
-- ordered recently and whether any are still open.
-- Author: Sarah Chen — won't need this query again after this ticket.

SELECT o.order_id,
       o.order_date,
       o.order_status,
       o.order_total,
       o.delivery_type,
       o.cost_of_delivery,
       w.warehouse_name,
       p.promotion_name
FROM   order_entry_db.order_entry.orders     o
LEFT   JOIN order_entry_db.order_entry.warehouses w  USING (warehouse_id)
LEFT   JOIN order_entry_db.order_entry.promotions p  USING (promotion_id)
WHERE  o.customer_id = 963
ORDER  BY o.order_date::TIMESTAMP DESC
;
