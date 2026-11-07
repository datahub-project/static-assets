-- Top products by return rate (not raw count)
-- Author: Sarah Chen — raw count favours high-volume SKUs; this is normalised

WITH stats AS (
    SELECT p.product_id,
           p.product_name,
           COUNT(*)              AS dispatched,
           COUNT(oi.return_date) AS returned
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.products    p USING (product_id)
    WHERE  oi.dispatch_date IS NOT NULL
    GROUP  BY 1, 2
)
SELECT product_id, product_name, dispatched, returned,
       returned * 100.0 / NULLIF(dispatched, 0) AS return_rate_pct
FROM   stats
WHERE  dispatched >= 10              -- need volume floor for a meaningful rate
ORDER  BY return_rate_pct DESC
LIMIT  25
;
