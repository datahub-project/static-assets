-- Products out of stock across all warehouses
-- Author: Ben Porter (Data Engineer) — supports the OOS Slack alert
--
-- "Out of stock everywhere" = SUM(qty_on_hand) over all warehouses is 0.
-- Note: negative quantities can occasionally appear due to CDC race conditions
-- (see the Inventory Staleness runbook). Clamp to 0 so they don't artificially
-- mask a true OOS situation.

SELECT p.product_id,
       p.product_name,
       p.product_status,
       SUM(GREATEST(i.quantity_on_hand, 0)) AS total_stock
FROM   order_entry_db.order_entry.products    p
JOIN   order_entry_db.order_entry.inventories i USING (product_id)
GROUP  BY 1, 2, 3
HAVING SUM(GREATEST(i.quantity_on_hand, 0)) = 0
ORDER  BY p.product_name
;
