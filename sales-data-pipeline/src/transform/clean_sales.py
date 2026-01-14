import pandas as pd

def clean_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    df = df_sales.copy()

    df = df.drop_duplicates(subset=["sale_id"])

    df = df.dropna(subset=["price", "quantity", "user_id"])

    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    return df
