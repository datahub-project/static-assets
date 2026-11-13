-- Attachment rate w/ YoY
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
           COUNT(promotion_id) * 100.0 / NULLIF(COUNT(*), 0) AS attachment_rate
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT cur.order_month, cur.attachment_rate AS current_rate, prv.attachment_rate AS prior_year_rate,
       cur.attachment_rate - prv.attachment_rate AS yoy_pp_delta
FROM   monthly cur LEFT JOIN monthly prv ON prv.order_month = DATEADD('year', -1, cur.order_month)
ORDER  BY cur.order_month;
