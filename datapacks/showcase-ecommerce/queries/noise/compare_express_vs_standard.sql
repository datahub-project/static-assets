-- Express vs Standard vs Overnight comparison
select delivery_type, count(*) as orders, avg(order_total) as aov, avg(cost_of_delivery) as avg_shipping
from order_entry_db.order_entry.orders
where delivery_type in ('Express', 'Standard', 'Overnight')
group by 1;
