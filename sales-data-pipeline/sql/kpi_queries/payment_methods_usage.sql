-- Payment Methods Usage
-- Ranks payment methods by number of successful transactions

SELECT
    payment_method,
    COUNT(*) AS usage_count
FROM fact_sales
WHERE payment_status = 'approved'
GROUP BY payment_method
ORDER BY usage_count DESC;
