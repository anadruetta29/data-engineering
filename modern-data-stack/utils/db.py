import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="sales_dw",
        user="postgres",
        password="admin"
    )