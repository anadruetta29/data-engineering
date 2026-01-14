-- Revenue by Country
-- Calculates total revenue grouped by country

SELECT
    country,
    SUM(total_amount) AS total_revenue
FROM fact_sales
WHERE payment_status = 'PAID'
GROUP BY country
ORDER BY total_revenue DESC;
