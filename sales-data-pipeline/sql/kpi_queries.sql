SELECT country, SUM(total_amount)
FROM fact_sales
GROUP BY country;
