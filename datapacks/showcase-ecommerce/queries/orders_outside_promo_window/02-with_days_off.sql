-- Misattributed orders with days outside the window
SELECT o.order_id, p.promotion_name, o.order_date,
       p.promotion_start_date, p.promotion_end_date,
       CASE WHEN o.order_date::TIMESTAMP < p.promotion_start_date::TIMESTAMP
            THEN DATEDIFF('day', o.order_date::TIMESTAMP, p.promotion_start_date::TIMESTAMP)
            ELSE DATEDIFF('day', p.promotion_end_date::TIMESTAMP, o.order_date::TIMESTAMP)
       END AS days_outside_window
FROM order_entry_db.order_entry.orders o
JOIN order_entry_db.order_entry.promotions p USING (promotion_id)
WHERE o.order_date::TIMESTAMP NOT BETWEEN p.promotion_start_date::TIMESTAMP
                                       AND COALESCE(p.promotion_end_date::TIMESTAMP, '9999-12-31'::TIMESTAMP)
ORDER BY days_outside_window DESC LIMIT 50;
