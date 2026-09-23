-- Show the violating rows with the address detail
select o.order_id, o.order_date, o.delivery_type, a.address_line1, a.town_city
from order_entry_db.order_entry.orders o
join order_entry_db.order_entry.addresses a on o.delivery_address_id = a.address_id
where o.delivery_type = 'In-Store Pickup'
order by o.order_date desc limit 50;
