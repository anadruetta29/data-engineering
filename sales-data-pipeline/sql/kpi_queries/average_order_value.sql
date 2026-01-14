-- Average Order Value (AOV)
-- Calculates the average revenue per successful sale

SELECT
    ROUND(AVG(total_amount), 2) AS average_order_value
FROM fact_sales
WHERE payment_status = 'PAID';
