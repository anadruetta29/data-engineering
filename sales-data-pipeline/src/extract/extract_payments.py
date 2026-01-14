import json
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PAYMENTS_FILE = RAW_PATH / "payments_raw.json"

def extract_payments():

    if not PAYMENTS_FILE.exists():
        raise FileNotFoundError("payments_raw.json not found")

    with open(PAYMENTS_FILE, "r") as f:
        data = json.load(f)

    return pd.DataFrame(data)
