## Source 1 – Sales
Format: CSV

Frequency: Daily

Fields: sale_id, product_id, user_id, quantity, price, sale_date, country

## Source 2 – Payments
Format: JSON via API

Frequency: Daily

Fields: payment_id, sale_id, status, payment_method, amount, payment_date

## Source 3 – User Table
Format: SQL Script

Frequency: Daily

Fields: user_id, email, country, signup_date, is_active