-- Monthly promotion attachment rate (% of orders using a promo)
-- Author: BID

SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
       COUNT(*) AS orders,
       COUNT(promotion_id) AS promoted_orders,
       COUNT(promotion_id) * 100.0 / NULLIF(COUNT(*), 0) AS attachment_rate_pct
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY 1;
