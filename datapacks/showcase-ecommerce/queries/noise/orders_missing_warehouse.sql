-- DQ check — every order should have a warehouse_id. Any with NULL?

select count(*) as orders_missing_warehouse
from order_entry_db.order_entry.orders
where warehouse_id is null
;
