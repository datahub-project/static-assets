-- Daily counts last 7 days — spot a sudden drop or gap
SELECT TO_DATE(order_date::TIMESTAMP) AS day, COUNT(*) AS orders
FROM   order_entry_db.order_entry.orders
WHERE  order_date::TIMESTAMP >= DATEADD('day', -7,
           (SELECT MAX(order_date::TIMESTAMP) FROM order_entry_db.order_entry.orders))
GROUP  BY 1
ORDER  BY 1 DESC;
