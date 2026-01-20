from pathlib import Path
from utils import load_csv_to_staging

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def extract_users():
    load_csv_to_staging(
        RAW_DATA_DIR / "users.csv",
        "staging.dim_users"
    )


def extract_products():
    load_csv_to_staging(
        RAW_DATA_DIR / "products.csv",
        "staging.dim_products"
    )


def extract_dates():
    load_csv_to_staging(
        RAW_DATA_DIR / "dates.csv",
        "staging.dim_date"
    )


def extract_sales():
    load_csv_to_staging(
        RAW_DATA_DIR / "sales.csv",
        "staging.dim_sales"
    )


def main():
    print("EXTRACT → STAGING")

    extract_sales()
    extract_dates()
    extract_users()
    extract_products()

    print("Extract finished!")


if __name__ == "__main__":
    main()
