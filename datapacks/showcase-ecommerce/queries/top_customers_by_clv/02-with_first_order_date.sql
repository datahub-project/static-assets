-- Top CLV customers, with tenure
-- Author: David Kim — adds first_order_date to compute "revenue per year on platform"

WITH cust AS (
    SELECT customer_id,
           SUM(order_total)              AS lifetime_revenue,
           COUNT(DISTINCT order_id)      AS lifetime_orders,
           MIN(order_date::TIMESTAMP)    AS first_order_at,
           MAX(order_date::TIMESTAMP)    AS most_recent_order
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
)
SELECT c.customer_id,
       cu.cust_first_name || ' ' || cu.cust_last_name AS customer_name,
       cu.customer_class,
       c.lifetime_revenue,
       c.lifetime_orders,
       c.first_order_at,
       c.most_recent_order,
       DATEDIFF('day', c.first_order_at, c.most_recent_order) AS days_on_platform,
       c.lifetime_revenue
           / NULLIF(DATEDIFF('day', c.first_order_at, c.most_recent_order), 0) * 365
                                                       AS annualised_revenue
FROM   cust c
JOIN   order_entry_db.order_entry.customers cu USING (customer_id)
ORDER  BY c.lifetime_revenue DESC
LIMIT  10
;
