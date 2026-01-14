from extract.extract_sales import extract_sales
from extract.extract_payments import extract_payments
from transform.clean_sales import clean_sales
from transform.clean_payments import clean_payments
from transform.join_sales_payments import join_sales_payments
from load.load_to_postgres import load_to_postgres

def run_pipeline():
    sales = extract_sales()
    payments = extract_payments()

    sales_clean = clean_sales(sales)
    payments_clean = clean_payments(payments)

    fact_sales = join_sales_payments(sales_clean, payments_clean)

    load_to_postgres(fact_sales, "fact_sales")

if __name__ == "__main__":
    run_pipeline()
