import pandas as pd
from psycopg2.extras import execute_batch
from pathlib import Path
from utils import get_connection

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

def load_csv_to_staging(csv_path: Path, table_name: str, truncate: bool = True):
    df = pd.read_csv(csv_path)

    if df.empty:
        print(f"⚠️  {csv_path.name} is empty. ")
        return

    conn = get_connection()
    cursor = conn.cursor()

    if truncate:
        cursor.execute(f"TRUNCATE TABLE {table_name};")

    columns = list(df.columns)
    values = [tuple(row) for row in df.itertuples(index=False, name=None)]

    insert_sql = f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES ({', '.join(['%s'] * len(columns))})
    """

    execute_batch(cursor, insert_sql, values, page_size=1000)

    conn.commit()
    cursor.close()
    conn.close()

    print(f" {csv_path.name} → {table_name} ({len(df)} lines inserted)")


def extract_users():
    load_csv_to_staging(
        RAW_DATA_DIR / "users.csv",
        "staging.users"
    )


def extract_products():
    load_csv_to_staging(
        RAW_DATA_DIR / "products.csv",
        "staging.products"
    )


def extract_dates():
    load_csv_to_staging(
        RAW_DATA_DIR / "dates.csv",
        "staging.dates"
    )


def extract_sales():
    load_csv_to_staging(
        RAW_DATA_DIR / "sales.csv",
        "staging.sales"
    )


def main():
    print("EXTRACT → STAGING")

    extract_sales()
    extract_dates()
    extract_users()
    extract_products()

    print("Extract finished! ")


if __name__ == "__main__":
    main()
