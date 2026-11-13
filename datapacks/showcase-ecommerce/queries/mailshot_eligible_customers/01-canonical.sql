-- Mailshot-eligible customer count
SELECT mailshot,
       COUNT(*) AS customers
FROM   order_entry_db.order_entry.customers
GROUP  BY 1;
