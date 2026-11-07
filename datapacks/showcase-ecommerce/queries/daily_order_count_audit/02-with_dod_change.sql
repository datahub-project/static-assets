-- Daily counts with DoD % change — flag drops >30%
WITH daily AS (
    SELECT TO_DATE(order_date::TIMESTAMP) AS day, COUNT(*) AS orders
    FROM   order_entry_db.order_entry.orders
    WHERE  order_date::TIMESTAMP >= DATEADD('day', -14,
               (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
    GROUP  BY 1
)
SELECT day, orders,
       LAG(orders) OVER (ORDER BY day) AS prior_day,
       (orders - LAG(orders) OVER (ORDER BY day)) * 100.0 / NULLIF(LAG(orders) OVER (ORDER BY day), 0) AS dod_pct,
       CASE WHEN (orders - LAG(orders) OVER (ORDER BY day)) * 100.0 / NULLIF(LAG(orders) OVER (ORDER BY day), 0) < -30 THEN 'alert'
            ELSE 'ok' END AS status
FROM daily
ORDER BY day DESC;
