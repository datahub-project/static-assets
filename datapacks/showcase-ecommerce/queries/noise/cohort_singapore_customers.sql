-- Singapore customer activity
select co.country_name, count(distinct a.customer_id) as customers,
       count(distinct o.order_id) as orders
from order_entry_db.order_entry.addresses a
join order_entry_db.order_entry.countries co on co.country_id = a.country_id
left join order_entry_db.order_entry.orders o on o.delivery_address_id = a.address_id
where co.country_name = 'Singapore'
group by 1;
