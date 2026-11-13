-- Negative inventory bucketed by severity
-- Author: Julia
SELECT
    CASE WHEN i.quantity_on_hand BETWEEN -10 AND -1 THEN 'minor'
         WHEN i.quantity_on_hand BETWEEN -100 AND -11 THEN 'medium'
         WHEN i.quantity_on_hand < -100 THEN 'severe'
    END AS severity,
    COUNT(*) AS anomaly_count,
    MIN(i.quantity_on_hand) AS worst_qty
FROM order_entry_db.order_entry.inventories i
WHERE i.quantity_on_hand < 0
GROUP BY 1
ORDER BY severity;
