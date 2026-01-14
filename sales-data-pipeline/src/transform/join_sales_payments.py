def join_sales_payments(sales_clean, payments_clean):
    df = sales_clean.merge(
        payments_clean,
        on="sale_id",
        how="inner"
    )

    df["total_amount"] = df["quantity"] * df["price"]

    fact_sales = df[[
        "sale_id",
        "product_id",
        "user_id",
        "sale_date",
        "country",
        "status",
        "payment_method",
        "total_amount"
    ]].rename(columns={"status": "payment_status"})

    return fact_sales
