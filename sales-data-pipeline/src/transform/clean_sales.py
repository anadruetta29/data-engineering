import pandas as pd
from pathlib import Path

STAGING_PATH = Path("data/staging")
STAGING_PATH.mkdir(parents=True, exist_ok=True)

def clean_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    df = df_sales.copy()

    df = df.drop_duplicates(subset=["sale_id"])

    df = df.dropna(subset=["price", "quantity", "user_id"])

    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    output_file = STAGING_PATH / "sales_clean.csv"
    df.to_csv(output_file, index=False)

    return df
