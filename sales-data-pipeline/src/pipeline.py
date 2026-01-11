from extract.extract_sales import extract_sales
from extract.extract_payments import extract_payments
from transform.join_sales_payments import transform_data
from load.load_to_postgres import load_data

def run():
    sales = extract_sales()
    payments = extract_payments()
    fact_sales = transform_data(sales, payments)
    load_data(fact_sales)

if __name__ == "__main__":
    run()
