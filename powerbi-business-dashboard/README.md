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
During development, some time-based measures (Sales YTD, Sales YoY %, Sales MoM %) initially 
returned blank values. This behavior was expected and helped reinforce key Power BI concepts:
- Time intelligence functions require a dedicated Date table that is properly marked as a Date table.
- Measures must use the date column from the date dimension (dim_date[Date]) rather than dates from 
the fact table.
- Time-based calculations require an active time context (e.g., year or month filters). 
Without a selected time period, Power BI returns BLANK() by design.
- Year-over-Year and Month-over-Month measures return blank values when no data exists for the 
previous period, which is correct behavior.
- Resolving these issues ensured accurate time intelligence calculations and a robust analytical model.
