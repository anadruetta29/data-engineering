def clean_payments(df):
    return df[df["status"].notnull()]
