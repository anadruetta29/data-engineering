import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
SALES_FILE = RAW_PATH / "sales.csv"

def extract_sales():
    if not SALES_FILE.exists():
        raise FileNotFoundError("sales.csv not found")

    return pd.read_csv(SALES_FILE)
