-- Monthly GMV with prior-year comparison
-- Author: Ian Chen (Director of Data) — adapted for the exec dashboard
--
-- Adds a prior-year column + YoY % so we can show momentum on the monthly slide.
-- Same canonical GMV definition; just a wider shape.

WITH monthly_gmv AS (
    SELECT DATE_TRUNC('month', order_date::TIMESTAMP)::DATE AS order_month,
           SUM(order_total)                                  AS gmv
    FROM   order_entry_db.order_entry.orders
    WHERE  order_status NOT IN (3, 4)
    GROUP  BY 1
),
window_bounds AS (
    SELECT MAX(order_month)                                       AS latest_month,
           DATEADD('month', -11, MAX(order_month))                AS earliest_in_window,
           DATEADD('year',  -1,  DATEADD('month', -11, MAX(order_month))) AS earliest_prior_year
    FROM   monthly_gmv
)
SELECT cur.order_month,
       cur.gmv                                              AS gmv_current,
       prv.gmv                                              AS gmv_prior_year,
       cur.gmv - prv.gmv                                    AS yoy_abs_delta,
       (cur.gmv - prv.gmv) / NULLIF(prv.gmv, 0) * 100.0     AS yoy_pct_change
FROM   monthly_gmv cur
JOIN   window_bounds w
  ON   cur.order_month BETWEEN w.earliest_in_window AND w.latest_month
LEFT   JOIN monthly_gmv prv
  ON   prv.order_month = DATEADD('year', -1, cur.order_month)
ORDER  BY cur.order_month
;
