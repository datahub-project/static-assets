-- Quick check: customer emails are supposed to be unique per the docs.
-- Are they actually? Running before the export to the new CRM.
-- Author: Julia Novak

select   cust_email,
         count(*) as customer_rows,
         min(customer_id) as first_seen_id,
         max(customer_id) as latest_seen_id
from     order_entry_db.order_entry.customers
where    cust_email is not null
group by 1
having   count(*) > 1
order by customer_rows desc, cust_email
;
