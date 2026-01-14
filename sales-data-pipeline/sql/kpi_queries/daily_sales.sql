-- Daily Total Sales
-- Counts the number of successful sales per day

SELECT
    sale_date,
    COUNT(DISTINCT sale_id) AS total_sales
FROM fact_sales
WHERE payment_status = 'PAID'
GROUP BY sale_date
ORDER BY sale_date;
