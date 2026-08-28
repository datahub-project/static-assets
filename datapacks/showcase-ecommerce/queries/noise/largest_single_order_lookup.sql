-- What's the largest single order on record?  Karen asked for the slide.
-- Author: Sarah

select o.order_id, o.order_date, o.order_total, c.cust_first_name, c.cust_last_name, c.customer_class
from order_entry_db.order_entry.orders o
join order_entry_db.order_entry.customers c using (customer_id)
order by o.order_total desc
limit 5;
