-- Net revenue = GMV - returned value (computed as two subqueries)
-- Author: Sarah Chen — keep them separate so finance can audit each line

WITH gmv AS (
    SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS month, SUM(order_total) AS gmv
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
),
returned_value AS (
    SELECT DATE_TRUNC('month', o.order_date::TIMESTAMP)::DATE AS month,
           SUM(oi.unit_price * oi.quantity) AS returned_value
    FROM   order_entry_db.order_entry.order_items oi
    JOIN   order_entry_db.order_entry.orders      o USING (order_id)
    WHERE  oi.return_date IS NOT NULL AND o.order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT g.month, g.gmv, COALESCE(r.returned_value, 0) AS returned_value,
       g.gmv - COALESCE(r.returned_value, 0)         AS net_revenue
FROM   gmv g LEFT JOIN returned_value r USING (month)
ORDER  BY g.month
;
