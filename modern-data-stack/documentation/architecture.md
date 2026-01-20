# Architecture – Modern Data Stack Project

## Overview
This project builds a modern ETL pipeline to extract, transform, and load sales data from CSV files 
into a PostgreSQL warehouse, ready for Power BI dashboards.

## Data Sources
- users.csv, products.csv, sales.csv, dates.csv

## ETL Pipeline
1. Extract: Load CSVs into staging tables.
2. Transform: Clean, deduplicate, create surrogate keys.
3. Load: Populate fact_sales table and dimension tables.

## Data Warehouse Model
- dim_date(date_sk, full_date, year, month)
- dim_users(user_sk, user_name)
- dim_products(product_sk, product_name, category)
- fact_sales(sale_id, user_sk, product_sk, date_sk, quantity, total_amount)

## Relationships
- fact_sales.user_sk → dim_users.user_sk
- fact_sales.product_sk → dim_products.product_sk
- fact_sales.date_sk → dim_date.date_sk

## Tools & Technologies
- Python 3, Pandas, PostgreSQL, Power BI

## Notes
- Date keys are aligned using YYYYMMDD format.
