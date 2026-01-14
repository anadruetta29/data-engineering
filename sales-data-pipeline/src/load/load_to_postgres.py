from sqlalchemy import create_engine, text
import pandas as pd

DB_URL = "postgresql://user:password@localhost:5432/sales_dw"

def load_to_postgres(df: pd.DataFrame, table_name: str):

    if df.empty:
        print("No data to load.")
        return

    engine = create_engine(DB_URL)

    sale_dates = df["sale_date"].dt.date.unique().tolist()

    with engine.begin() as connection:

        delete_query = text(f"""
            DELETE FROM {table_name}
            WHERE sale_date = ANY(:sale_dates)
        """)

        connection.execute(
            delete_query,
            {"sale_dates": sale_dates}
        )

        df.to_sql(
            table_name,
            connection,
            if_exists="append",
            index=False
        )

    print(f"Loaded {len(df)} records into {table_name}")
