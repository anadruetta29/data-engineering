SELECT
    p.product_id,
    p.product_name,
    SUM(f.total_amount) AS total_sales,
    RANK() OVER (ORDER BY SUM(f.total_amount) DESC) AS sales_rank
FROM fact_sales f
JOIN products p ON f.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY sales_rank;


SELECT
    u.user_id,
    u.email,
    SUM(f.total_amount) AS total_spent,
    RANK() OVER (ORDER BY SUM(f.total_amount) DESC) AS spending_rank
FROM fact_sales f
JOIN users u ON f.user_id = u.user_id
GROUP BY u.user_id, u.email
ORDER BY spending_rank;


SELECT
    t.year,
    t.month,
    SUM(f.total_amount) AS monthly_sales,
    SUM(SUM(f.total_amount)) OVER (ORDER BY t.year, t.month) AS running_total
FROM fact_sales f
JOIN time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year, t.month;


SELECT
    f.sale_id,
    f.user_id,
    u.email,
    f.product_id,
    f.total_amount,
    ROW_NUMBER() OVER (PARTITION BY f.user_id ORDER BY f.time_id) AS transaction_number
FROM fact_sales f
JOIN users u ON f.user_id = u.user_id
ORDER BY f.user_id, transaction_number;


SELECT
    f.sale_id,
    f.user_id,
    u.email,
    f.product_id,
    f.total_amount,
    AVG(f.total_amount) OVER (PARTITION BY t.year, t.month) AS monthly_avg,
    f.total_amount - AVG(f.total_amount) OVER (PARTITION BY t.year, t.month) AS diff_from_avg
FROM fact_sales f
JOIN users u ON f.user_id = u.user_id
JOIN time t ON f.time_id = t.time_id
ORDER BY t.year, t.month, f.sale_id;