import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}?client_encoding=utf8"

engine = create_engine(DB_URL)


def load_to_postgres(df: pd.DataFrame, table_name: str):
    if df.empty:
        print("No data to load.")
        return

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.encode('utf-8', errors='ignore').str.decode('utf-8')

    sale_dates = df["sale_date"].dt.date.unique().tolist()

    with engine.begin() as connection:
        delete_query = text(f"""
            DELETE FROM {table_name}
            WHERE sale_date = ANY(:sale_dates)
        """)
        connection.execute(delete_query, {"sale_dates": sale_dates})

        df.to_sql(table_name, connection, if_exists="append", index=False)

    print(f"Loaded {len(df)} records into {table_name}")
