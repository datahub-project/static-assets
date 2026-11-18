-- AOV by month — line-item-level avg (anti)
-- Author: Karen Okonkwo
--
-- !! warning from sarah: this AVG is over order_details rows which is line-item
-- grain, so big orders get over-weighted. Result will diverge from the official
-- monthly AOV. Keeping it because the PRD asked for "avg per row" specifically
-- but the right shape is the canonical_raw version.

SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
       AVG(order_total)                                  AS aov_lineitem_weighted,
       COUNT(*)                                          AS line_item_rows
FROM   order_entry_db.analytics.order_details
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY 1
;
