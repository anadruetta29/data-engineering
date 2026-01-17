# SQL Data Warehouse – Sales Analytics

## Project Overview
This project implements a sales data warehouse using PostgreSQL and a star schema design.  
The goal is to perform analytical queries on sales data using advanced SQL features.

## Data Model
The warehouse follows a **star schema** with the following tables:

### Fact Table
- **fact_sales**
  - Stores transactional sales data
  - Measures: total_amount, quantity
  - Foreign keys to dimensions

### Dimension Tables
- **users** (customer dimension)
- **products** (product dimension)
- **time** (time dimension)

## Technologies Used
- PostgreSQL
- SQL (CTEs, JOINs, Window Functions)
- Star Schema modeling

## Example Analytical Queries

    1. Basic Queries (basic.sql)
- Retrieve all sales with their total amount and date.
- List all products along with their category and price.
- Calculate the total revenue (sum of total_amount).
- Get total sales broken down by payment method.
- List all active users (is_active = true).

  2. JOINs (joins.sql)
- Total sales per product (Product Name + Total Sold).
- Total sales per user country.
- Sales volume by month and year.
- Total amount spent by each user.
- Number of sales per product category.

  3. CTEs – Common Table Expressions (ctes.sql)
- Calculate monthly sales using a CTE.
- Identify the month with the highest sales volume.
- Calculate total spend per user and filter those exceeding a specific threshold.
- Analyze sales per product using an intermediate CTE.
- Isolate approved sales (payment_status = 'approved') in a CTE for further analysis.

  4. Window Functions (window_functions.sql)
- Product ranking based on total sales (RANK).
- User ranking based on total spending.
- Running total of sales per month (SUM() OVER).
- Assign a row number to each transaction per user (ROW_NUMBER).
- Compare each sale against the monthly average (AVG() OVER).

## Key Learnings
- Star schema data modeling
- Advanced SQL querying
- Common Table Expressions (CTEs)
- Window functions for analytical use cases
- Performance-oriented querying