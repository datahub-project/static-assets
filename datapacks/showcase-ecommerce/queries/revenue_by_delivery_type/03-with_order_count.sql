-- Revenue + count + margin contribution by delivery type
-- Author: Sarah Chen
-- Margin contribution = revenue - shipping. Doesn't include COGS — just looks
-- at how much shipping eats into top-line by delivery option.

SELECT delivery_type,
       COUNT(*)                                          AS orders,
       SUM(order_total)                                  AS revenue,
       SUM(cost_of_delivery)                             AS shipping_cost,
       SUM(order_total) - SUM(cost_of_delivery)          AS revenue_after_shipping,
       (SUM(order_total) - SUM(cost_of_delivery))
           / NULLIF(SUM(order_total), 0) * 100            AS pct_kept_after_shipping
FROM   order_entry_db.order_entry.orders
WHERE  order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
