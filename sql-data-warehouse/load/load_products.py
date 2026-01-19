import pandas as pd
from pathlib import Path
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "sales_dw",
    "user": "postgres",
    "password": "admin"
}

CSV_PATH = Path(__file__).parent.parent / "data" / "products.csv"

df = pd.read_csv(CSV_PATH)

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

insert_query = """
INSERT INTO products (product_id, product_name, category, price)
VALUES (%s, %s, %s, %s)
ON CONFLICT (product_id) DO NOTHING;
"""

for _, row in df.iterrows():
    cursor.execute(
        insert_query,
        (
            row["product_id"],
            row["product_name"],
            row["category"],
            row["price"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Products data loaded successfully")
