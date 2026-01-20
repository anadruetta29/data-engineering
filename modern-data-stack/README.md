# Modern Data Stack Project – ETL Phase

This project is part of a Data Engineering learning path, focusing on building a modern data pipeline.
The goal of this ETL phase is to extract, transform, and load data from raw CSV files into a structured 
data warehouse that can be used for analytics and dashboards.

The pipeline loads data into dimension tables and a fact table, preparing it for reporting and 
visualization in Power BI.

## ETL Pipeline Steps
1. Extract → Staging
- Load raw CSV data into staging tables.
- Staging tables mirror the raw structure of the data.
  - Files loaded: 
    users.csv → staging.dim_users
    products.csv → staging.dim_products
    sales.csv → staging.dim_sales
    dates.csv → staging.dim_date

Purpose: store raw data safely for debugging and validation. 

2. Transform → Dimensions
- Transform raw data from staging to dimension tables in the warehouse.
- Dimension tables store clean, structured, and unique records.
  - Tables created:
    dim_date → structured calendar table
    dim_users → unique users with surrogate keys
    dim_products → unique products with categories and surrogate keys

Purpose: provide reliable reference data for fact tables and reporting.

3. Load → Fact Table
- Load fact_sales with all measures and foreign keys.
  - Fact table contains:
    sale_id
    user_sk (FK → dim_users)
    product_sk (FK → dim_products)
    date_sk (FK → dim_date)
    quantity
    total_amount
    payment_status
    payment_method

  - Join logic: 
Map raw sales data to dimension keys
Ensure no missing references

## Notes:

Earlier, fact_sales was empty because the date_sk join was incorrect. 
Resolved by matching staging.dim_sales.time_id to dim_date.full_date with proper format conversion.

Also, the transform.py script will be improved in the future for better performance.  