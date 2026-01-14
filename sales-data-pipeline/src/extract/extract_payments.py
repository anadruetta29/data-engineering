import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data/raw"
PAYMENTS_FILE = RAW_PATH / "payments_raw.json"

def extract_payments():
    if not PAYMENTS_FILE.exists():
        raise FileNotFoundError(f"{PAYMENTS_FILE} not found")

    with open(PAYMENTS_FILE, "r") as f:
        data = json.load(f)

    payments_list = data["payments"]
    df = pd.DataFrame(payments_list)

    return df
