-- TODO: trying to roll up revenue by supplier_id but the supplier table
-- isn't here; supplier_id lives on order_items + products as an opaque number.
-- Need to ping data-eng about whether there's a supplier dim table.

select supplier_id, count(*) as line_items, sum(unit_price * quantity) as rev
from order_entry_db.order_entry.order_items
group by 1 order by rev desc limit 20;
-- left to do: join to a supplier table once it exists. For now this gives
-- us the IDs to ask about.
