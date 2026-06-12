-- Net revenue via mart — line_total is pre-computed
select date_trunc('month', order_date::timestamp)::date as order_month,
       sum(case when return_date is null then line_total else 0 end) as net_revenue,
       sum(line_total) as gross_revenue
from order_entry_db.analytics.order_details
where order_status not in (3, 4)
group by 1 order by 1;
