from extract.extract_sales import extract_sales
from extract.extract_payments import extract_payments
from transform.clean_sales import clean_sales
from transform.clean_payments import clean_payments
from transform.join_sales_payments import join_sales_payments
from load.load_fact_sales import load_fact_sales
from load.load_payments_raw import load_payments_raw

def run_pipeline():
    sales = extract_sales()
    payments = extract_payments()

    sales_clean = clean_sales(sales)
    payments_clean = clean_payments(payments)

    fact_sales = join_sales_payments(sales_clean, payments_clean)

    load_fact_sales(fact_sales, "fact_sales")
    load_payments_raw(payments)

if __name__ == "__main__":
    run_pipeline()
