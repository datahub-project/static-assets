-- Most-returned products via mart
select product_id, product_name, count(*) as returns
from order_entry_db.analytics.order_details
where return_date is not null
group by 1, 2 order by returns desc limit 25;
