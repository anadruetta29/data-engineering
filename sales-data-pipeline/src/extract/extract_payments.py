import requests
import pandas as pd

def extract_payments():
    response = requests.get("API_URL")
    return pd.DataFrame(response.json())
