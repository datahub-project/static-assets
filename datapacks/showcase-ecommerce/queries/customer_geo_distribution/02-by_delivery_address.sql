-- Geographic distribution by delivery-address country (not billing)
-- Author: Sarah Chen
-- Different question — captures where ORDERS go, not where the buyer is registered.

SELECT co.country_name,
       COUNT(DISTINCT o.order_id) AS orders,
       SUM(o.order_total)         AS revenue,
       COUNT(DISTINCT o.customer_id) AS distinct_customers
FROM   order_entry_db.order_entry.orders    o
JOIN   order_entry_db.order_entry.addresses a  ON o.delivery_address_id = a.address_id
JOIN   order_entry_db.order_entry.countries co USING (country_id)
WHERE  o.order_status NOT IN (3, 4)
GROUP  BY 1
ORDER  BY revenue DESC
;
