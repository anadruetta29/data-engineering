WITH monthly_sales AS (
    SELECT
        t.year,
        t.month,
        SUM(f.total_amount) AS total_sales
    FROM fact_sales f
    JOIN time t ON f.time_id = t.time_id
    GROUP BY t.year, t.month
)
SELECT *
FROM monthly_sales
ORDER BY year, month;


WITH monthly_sales AS (
    SELECT
        t.year,
        t.month,
        SUM(f.total_amount) AS total_sales
    FROM fact_sales f
    JOIN time t ON f.time_id = t.time_id
    GROUP BY t.year, t.month
)
SELECT *
FROM monthly_sales
ORDER BY total_sales DESC
LIMIT 1;


WITH user_spending AS (
    SELECT
        u.user_id,
        u.email,
        SUM(f.total_amount) AS total_spent
    FROM fact_sales f
    JOIN users u ON f.user_id = u.user_id
    GROUP BY u.user_id, u.email
)
SELECT *
FROM user_spending
WHERE total_spent > 1000
ORDER BY total_spent DESC;


WITH product_sales AS (
    SELECT
        p.product_id,
        p.product_name,
        SUM(f.quantity) AS total_quantity_sold,
        SUM(f.total_amount) AS total_sales_amount
    FROM fact_sales f
    JOIN products p ON f.product_id = p.product_id
    GROUP BY p.product_id, p.product_name
)
SELECT *
FROM product_sales
ORDER BY total_sales_amount DESC;


WITH approved_sales AS (
    SELECT *
    FROM fact_sales
    WHERE payment_status = 'approved'
)
SELECT *
FROM approved_sales
JOIN products p ON approved_sales.product_id = p.product_id
JOIN users u ON approved_sales.user_id = u.user_id
JOIN time t ON approved_sales.time_id = t.time_id
ORDER BY approved_sales.total_amount DESC;