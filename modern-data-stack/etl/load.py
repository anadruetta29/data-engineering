from utils import get_connection

def load_fact_sales():
    sql = """
    INSERT INTO warehouse.fact_sales (
        sale_id,
        user_sk,
        product_sk,
        date_sk,
        quantity,
        total_amount,
        payment_status,
        payment_method
    )
    SELECT
        s.sale_id,
        du.user_sk,
        dp.product_sk,
        dd.date_sk,
        s.quantity,
        s.total_amount,
        s.payment_status,
        s.payment_method
    FROM staging.dim_sales s
    JOIN warehouse.dim_users du ON s.user_id = du.user_id
    JOIN warehouse.dim_products dp ON s.product_id = dp.product_id
    JOIN warehouse.dim_date dd 
    ON dd.full_date = TO_DATE(CAST(s.time_id AS TEXT), 'YYYYMMDD')
    ON CONFLICT (sale_id) DO NOTHING;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
        print("fact_sales loaded successfully!")
    except Exception as e:
        print(f"Error loading fact_sales: {e}")

def main():
    print("LOAD → FACT TABLE")
    load_fact_sales()
    print("Load finished!")

if __name__ == "__main__":
    main()