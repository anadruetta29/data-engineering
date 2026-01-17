CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    email TEXT,
    country TEXT,
    signup_date DATE,
    is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id TEXT PRIMARY KEY,
    product_id TEXT,
    user_id TEXT,
    sale_date DATE,
    country TEXT,
    payment_status TEXT,
    payment_method TEXT,
    total_amount NUMERIC,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
