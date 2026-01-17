CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE time (
    time_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);

CREATE INDEX idx_fact_sales_product
ON fact_sales(product_id);

CREATE INDEX idx_time_date
ON time(date);

CREATE INDEX idx_time_date
ON time(date);

