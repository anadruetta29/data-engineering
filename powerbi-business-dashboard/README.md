# Power BI Business Sales Dashboard

This project is part of a Data Engineering learning path and represents the visualization phase of a previously developed data model.

The dashboard was built in Power BI Desktop using the same star schema data model designed and implemented in earlier phases, with data imported directly from a PostgreSQL database.

## Business Objective

The objective of this dashboard is to analyze sales performance in order to:
- Monitor overall revenue and growth trends
- Evaluate year-over-year and month-over-month performance
- Identify top-performing products and categories
- Analyze sales distribution by country
- Support data-driven business decisions

## Data Model

Star schema reused from previous project phases
- Fact table: fact_sales
- Dimension tables: dim_date (calendar table created in DAX and marked as a Date table), dim_products, 
dim_users

Data imported from PostgreSQL (localhost) using Power BI’s native connector

## Key Metrics (KPIs)
- Total Sales
- Sales YTD (Year-to-Date)
- Sales YoY % (Year-over-Year growth)
- Sales MoM % (Month-over-Month growth)

## Dashboard Features
KPI cards for executive overview
Time series analysis of sales evolution
Sales breakdown by product category
Top products ranking
Sales by country

## Technologies Used
- Power BI Desktop
- PostgreSQL

## Known Issues & Learnings
During development, some time-based measures (Sales YTD, Sales YoY %, Sales MoM %) 
initially returned blank or zero values. This issue was traced to a data modeling problem and 
provided important learning outcomes:

- The time_id column in the fact_sales table was stored as an integer (YYYYMMDD) instead of a proper 
Date data type.

- Power BI time intelligence functions do not work with numeric date representations, 
even if they visually resemble dates.

- The issue was resolved by creating a calculated Date column from the integer time_id and using it
to relate the fact table to a dedicated date dimension (dim_date).

- Time intelligence functions require: a properly formatted Date column, a Date dimension marked as a 
Date table and relationships based on actual Date data types

- Year-over-Year and Month-over-Month measures correctly return blank or zero values when no 
historical data exists for the previous period, which is expected and correct behavior.

Resolving these issues ensured accurate time-based calculations and reinforced best practices in data modeling, time intelligence, and analytical design.