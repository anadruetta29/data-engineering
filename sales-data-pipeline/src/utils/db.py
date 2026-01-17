from sqlalchemy import create_engine, text
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

DB_URL = "postgresql://postgres:admin@localhost:5432/sales_dw"

engine = create_engine(DB_URL)

with engine.connect() as conn:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema_sql = file.read()

    conn.execute(text(schema_sql))
    conn.commit()

print("Schema created successfully")
