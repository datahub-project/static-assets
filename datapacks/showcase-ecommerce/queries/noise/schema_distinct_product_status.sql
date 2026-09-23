-- What values appear in products.product_status?
SELECT product_status AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.products
GROUP BY 1 ORDER BY cnt DESC;
