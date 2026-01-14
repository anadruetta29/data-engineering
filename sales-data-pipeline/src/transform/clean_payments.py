import pandas as pd
from pathlib import Path

STAGING_PATH = Path("data/staging")
STAGING_PATH.mkdir(parents=True, exist_ok=True)

def clean_payments(df_payments: pd.DataFrame) -> pd.DataFrame:
    df = df_payments.copy()

    df = df.drop_duplicates(subset=["payment_id"])

    df = df.dropna(subset=["status", "sale_id"])

    df["payment_date"] = pd.to_datetime(df["payment_date"])
    df["amount"] = df["amount"].astype(float)

    df = df[df["status"] == "approved"]

    output_file = STAGING_PATH / "payments_clean.csv"
    df.to_csv(output_file, index=False)

    return df
