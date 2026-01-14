-- Failed Payment Rate
-- Calculates the percentage of failed payment attempts

SELECT
    ROUND(
        100.0 * SUM(CASE WHEN status != 'PAID' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS failed_payment_percentage
FROM payments_raw;
