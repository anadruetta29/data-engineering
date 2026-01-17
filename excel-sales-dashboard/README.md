# Excel Sales Dashboard 

The objective of this folder is to build an Excel sales dashboard from a raw dataset, applying data
cleaning with Power Query and performing analysis through pivot tables and advanced functions.

## Original Dataset 

I downloaded a dataset from Kaggle about sales, type of payments, products and clients. 

## Power Query

The raw data is transformed using Power Query to ensure accuracy and consistency. 
The cleaning process includes:
- Removing unnecessary columns to optimize performance.
- Correcting data types (ensuring numbers are treated as such, not text).
- Normalizing dates for consistent time-series analysis.
- Text sanitization (removing extra spaces, fixing capitalization).
- Renaming columns to follow a professional naming convention.
- Creating calculated columns where necessary, such as: Total Sales = [Price] * [Quantity]

## Analysis 

Using the cleaned dataset, I generated Pivot Tables to analyze Total Sales, Monthly Sales, and
Product Performance.

## Dashboard 

Lastly, I built a Dashboard with two main charts: Monthly Sales and Product Performance. 
It also features KPIs for Total Sales and the Total Number of Sales.