-- Net revenue by month — per the Metrics Reference, sum line-item revenue
-- where return_date IS NULL (i.e. keep only the non-returned value).
-- Author: BID / James

SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS order_month,
       SUM(CASE WHEN oi.return_date IS NULL
                THEN oi.unit_price * oi.quantity
                ELSE 0 END) AS net_revenue,
       SUM(oi.unit_price * oi.quantity) AS gross_revenue
FROM   order_entry_db.order_entry.order_items oi
JOIN   order_entry_db.order_entry.orders      o  USING (order_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY 1
;
