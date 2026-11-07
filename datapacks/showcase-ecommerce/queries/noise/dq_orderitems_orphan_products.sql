-- Order items referencing non-existent product_id
select count(*) as line_items_with_bad_product
from order_entry_db.order_entry.order_items oi
left join order_entry_db.order_entry.products p using (product_id)
where p.product_id is null;
