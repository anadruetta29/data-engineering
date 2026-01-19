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


def load_payments_raw(df: pd.DataFrame):

    if df.empty:
        print("No payments to load.")
        return

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.encode('utf-8', errors='ignore').str.decode('utf-8')

    with engine.begin() as connection:
        if "payment_date" in df.columns:
            payment_dates = pd.to_datetime(df["payment_date"]).dt.date.unique().tolist()
            delete_query = text("""
                DELETE FROM payments_raw
                WHERE payment_date = ANY(:payment_dates)
            """)
            connection.execute(delete_query, {"payment_dates": payment_dates})

        df.to_sql("payments_raw", connection, if_exists="replace", index=False)

    print(f"Loaded {len(df)} records into payments_raw")

