-- Invariant check: min_price should always be <= list_price.
-- Spotting any inverted entries.
-- Author: Julia (DQE)

SELECT product_id, product_name, list_price, min_price, min_price - list_price AS gap
FROM   order_entry_db.order_entry.products
WHERE  min_price > list_price
ORDER  BY gap DESC
;
