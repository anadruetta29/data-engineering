SELECT
    fs.sale_id,
    fs.total_amount,
    t.date
FROM fact_sales fs
JOIN time t
    ON fs.time_id = t.time_id;

SELECT
    product_name,
    category,
    price
FROM products;


SELECT
    SUM(total_amount) AS total_sales
FROM fact_sales;


SELECT
    payment_method,
    SUM(total_amount) AS total_sales
FROM fact_sales
GROUP BY payment_method
ORDER BY total_sales DESC;


SELECT
    user_id,
    email,
    country
FROM users
WHERE is_active = true;
