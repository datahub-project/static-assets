-- DQ check: any orders attributed to a promo, but with order_date outside the window?
-- Author: Julia (DQE)

SELECT COUNT(*) AS misattributed_orders,
       COUNT(DISTINCT o.promotion_id) AS promos_affected
FROM   order_entry_db.order_entry.orders o
JOIN   order_entry_db.order_entry.promotions p USING (promotion_id)
WHERE  o.order_date::TIMESTAMP NOT BETWEEN p.promotion_start_date::TIMESTAMP
                                        AND COALESCE(p.promotion_end_date::TIMESTAMP, '9999-12-31'::TIMESTAMP);
