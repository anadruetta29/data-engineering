import pandas as pd
from psycopg2.extras import execute_batch
from pathlib import Path
from utils.db import get_connection


def load_csv_to_staging(
    csv_path: Path,
    table_name: str,
    truncate: bool = True
):
    df = pd.read_csv(csv_path)

    if df.empty:
        print(f"⚠{csv_path.name} is empty")
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

    print(f"{csv_path.name} → {table_name} ({len(df)} rows)")
