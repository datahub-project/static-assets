-- Negative promotion budget? (DQ canary)
SELECT * FROM order_entry_db.order_entry.promotions WHERE promotion_cost < 0;
