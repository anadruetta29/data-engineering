import pandas as pd

def clean_payments(df_payments: pd.DataFrame) -> pd.DataFrame:
    df = df_payments.copy()

    df = df.drop_duplicates(subset=["payment_id"])

    df = df.dropna(subset=["status", "sale_id"])

    df["payment_date"] = pd.to_datetime(df["payment_date"])
    df["amount"] = df["amount"].astype(float)

    df = df[df["status"] == "PAID"]

    return df
