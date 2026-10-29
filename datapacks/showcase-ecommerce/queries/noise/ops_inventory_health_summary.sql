-- Inventory health: how many (product, wh) pairs in each state?
SELECT
    SUM(CASE WHEN quantity_on_hand = 0 THEN 1 ELSE 0 END) AS oos_pairs,
    SUM(CASE WHEN quantity_on_hand BETWEEN 1 AND restock_level - 1 THEN 1 ELSE 0 END) AS low,
    SUM(CASE WHEN quantity_on_hand >= restock_level THEN 1 ELSE 0 END) AS healthy,
    SUM(CASE WHEN quantity_on_hand > max_stock_level THEN 1 ELSE 0 END) AS overstocked
FROM order_entry_db.order_entry.inventories;
