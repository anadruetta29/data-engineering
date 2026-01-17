SELECT
    p.product_name,
    SUM(f.quantity) AS total_sold
FROM fact_sales f
JOIN products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;


SELECT
    u.country,
    SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN users u ON f.user_id = u.user_id
GROUP BY u.country
ORDER BY total_sales DESC;


SELECT
    t.year,
    t.month,
    SUM(f.total_amount) AS sales_volume
FROM fact_sales f
JOIN time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year, t.month;


SELECT
    u.user_id,
    u.email,
    SUM(f.total_amount) AS total_spent
FROM fact_sales f
JOIN users u ON f.user_id = u.user_id
GROUP BY u.user_id, u.email
ORDER BY total_spent DESC;


SELECT
    p.category,
    COUNT(f.sale_id) AS number_of_sales
FROM fact_sales f
JOIN products p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY number_of_sales DESC;


