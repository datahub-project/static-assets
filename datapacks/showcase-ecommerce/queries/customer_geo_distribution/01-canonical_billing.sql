-- Customer base by country (via their saved addresses)
-- Author: PM
-- Note: customers.country_id is unreliable in this env (values don't FK to countries),
-- so resolving country through the customer's addresses is the safer path.

SELECT co.country_name,
       co.country_code,
       COUNT(DISTINCT a.customer_id) AS customers
FROM   order_entry_db.order_entry.addresses a
JOIN   order_entry_db.order_entry.countries co ON co.country_id = a.country_id
GROUP  BY 1, 2
ORDER  BY customers DESC
;
