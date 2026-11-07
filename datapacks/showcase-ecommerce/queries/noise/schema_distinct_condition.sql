-- What values appear in order_items.condition?
SELECT "condition" AS value, COUNT(*) AS cnt
FROM order_entry_db.order_entry.order_items
GROUP BY 1 ORDER BY cnt DESC;
