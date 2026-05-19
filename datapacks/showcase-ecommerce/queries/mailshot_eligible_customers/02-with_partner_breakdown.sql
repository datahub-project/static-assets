-- Mailshot consent + partner consent matrix
-- Author: Karen — needed for the privacy review

SELECT mailshot,
       partner_mailshot,
       COUNT(*) AS customers,
       COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS pct_of_base
FROM   order_entry_db.order_entry.customers
GROUP  BY 1, 2
ORDER  BY 1, 2
;
