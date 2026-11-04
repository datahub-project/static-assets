-- Monthly fill rate — INNER JOIN version (anti)
-- Author: Karen Okonkwo
-- !! Sarah noted: INNER JOIN here is wrong — drops orders that are placed
-- but have NO order_items rows yet (back-order hold during the window).
-- Result reads "100% fill rate" because we filtered to only dispatched-or-not
-- items, but the denominator is missing the unfulfilled orders. Keeping as a
-- "do not adopt" example for the wiki.

SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS order_month,
       COUNT(oi.dispatch_date) * 100.0 / NULLIF(COUNT(*), 0) AS fill_rate_pct,
       COUNT(*)                                            AS items_in_window
FROM   order_entry_db.order_entry.order_items oi
INNER  JOIN order_entry_db.order_entry.orders o USING (order_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY 1
;
