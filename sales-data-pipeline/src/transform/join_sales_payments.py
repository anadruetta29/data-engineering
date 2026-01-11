def transform_data(sales, payments):
    df = sales.merge(payments, on="sale_id")
    df = df[df["status"] == "PAID"]
    df["total_amount"] = df["quantity"] * df["price"]
    return df
