from utils import get_connection


def load_dim_date():
    sql = """
    INSERT INTO warehouse.dim_date (
        full_date,
        year,
        month_number,
        month,
        year_month
    )
    SELECT DISTINCT
        TO_DATE(
            regexp_replace(
                lower(
                    regexp_replace(date, '^[a-záéíóúñ]+,\\s*', '')
                ),
                '(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)',
                CASE
                    WHEN regexp_match(lower(date), 'enero') IS NOT NULL THEN 'january'
                    WHEN regexp_match(lower(date), 'febrero') IS NOT NULL THEN 'february'
                    WHEN regexp_match(lower(date), 'marzo') IS NOT NULL THEN 'march'
                    WHEN regexp_match(lower(date), 'abril') IS NOT NULL THEN 'april'
                    WHEN regexp_match(lower(date), 'mayo') IS NOT NULL THEN 'may'
                    WHEN regexp_match(lower(date), 'junio') IS NOT NULL THEN 'june'
                    WHEN regexp_match(lower(date), 'julio') IS NOT NULL THEN 'july'
                    WHEN regexp_match(lower(date), 'agosto') IS NOT NULL THEN 'august'
                    WHEN regexp_match(lower(date), 'septiembre') IS NOT NULL THEN 'september'
                    WHEN regexp_match(lower(date), 'octubre') IS NOT NULL THEN 'october'
                    WHEN regexp_match(lower(date), 'noviembre') IS NOT NULL THEN 'november'
                    WHEN regexp_match(lower(date), 'diciembre') IS NOT NULL THEN 'december'
                END
            ),
            'DD "de" Month "de" YYYY'
        ) AS full_date,
        year,
        monthnumber AS month_number,
        month,
        yearmonth AS year_month
    FROM staging.dim_date
    ON CONFLICT (full_date) DO NOTHING;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

    print("dim_date loaded")

def load_dim_users():
    sql = """
    TRUNCATE TABLE warehouse.dim_users CASCADE;

    INSERT INTO warehouse.dim_users (
        user_id,
        email,
        country,
        signup_date,
        is_active
    )
    SELECT
        user_id,
        email,
        country,
        TO_DATE(
            regexp_replace(
                lower(
                    regexp_replace(signup_date, '^[a-záéíóúñ]+,\\s*', '')
                ),
                '(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)',
                CASE
                    WHEN regexp_match(lower(signup_date), 'enero') IS NOT NULL THEN 'january'
                    WHEN regexp_match(lower(signup_date), 'febrero') IS NOT NULL THEN 'february'
                    WHEN regexp_match(lower(signup_date), 'marzo') IS NOT NULL THEN 'march'
                    WHEN regexp_match(lower(signup_date), 'abril') IS NOT NULL THEN 'april'
                    WHEN regexp_match(lower(signup_date), 'mayo') IS NOT NULL THEN 'may'
                    WHEN regexp_match(lower(signup_date), 'junio') IS NOT NULL THEN 'june'
                    WHEN regexp_match(lower(signup_date), 'julio') IS NOT NULL THEN 'july'
                    WHEN regexp_match(lower(signup_date), 'agosto') IS NOT NULL THEN 'august'
                    WHEN regexp_match(lower(signup_date), 'septiembre') IS NOT NULL THEN 'september'
                    WHEN regexp_match(lower(signup_date), 'octubre') IS NOT NULL THEN 'october'
                    WHEN regexp_match(lower(signup_date), 'noviembre') IS NOT NULL THEN 'november'
                    WHEN regexp_match(lower(signup_date), 'diciembre') IS NOT NULL THEN 'december'
                END
            ),
            'DD "de" Month "de" YYYY'
        ),
        is_active
    FROM staging.dim_users;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

    print("dim_users loaded")



def load_dim_products():
    sql = """
    INSERT INTO warehouse.dim_products (
        product_id,
        product_name,
        category,
        price
    )
    SELECT DISTINCT
        product_id,
        product_name,
        category,
        price
    FROM staging.dim_products
    ON CONFLICT (product_id) DO UPDATE
    SET
        product_name = EXCLUDED.product_name,
        category = EXCLUDED.category,
        price = EXCLUDED.price;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

    print("dim_products loaded")


def main():
    print("TRANSFORM → DIMENSIONS")

    load_dim_date()
    load_dim_users()
    load_dim_products()

    print("Transform finished!")


if __name__ == "__main__":
    main()
