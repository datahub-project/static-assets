-- Same set via NOT IN (note: only safe if order_items.product_id has no NULLs)
-- Author: Andrea — older codebase style

select product_id, product_name, product_status, date_added
from order_entry_db.order_entry.products
where product_id not in (
    select distinct product_id from order_entry_db.order_entry.order_items where product_id is not null
)
order by date_added desc;
