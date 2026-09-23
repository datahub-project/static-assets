-- DQ invariant — In-Store Pickup orders shouldn't carry a delivery_address_id
-- Author: Julia
SELECT COUNT(*) AS violations
FROM   order_entry_db.order_entry.orders
WHERE  delivery_type = 'In-Store Pickup'
  AND  delivery_address_id IS NOT NULL;
