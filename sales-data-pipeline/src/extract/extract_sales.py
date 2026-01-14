import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PAYMENTS_FILE = RAW_PATH / "sales.csv"

def extract_sales():
    if not PAYMENTS_FILE.exists():
        raise FileNotFoundError("sales.csv not found")

    RAW_PATH.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_PATH / "sales.csv")

    return df
