
# Project 1 - Alpha Vantage API Test
# Retrieve Apple's daily stock market data

import os
import requests
import pandas as pd
from pathlib import Path

# 1. Retrieve API key securely from environment variable
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Configure the environment variable.")

# 2. Define API request
url = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "outputsize": "compact",
    "apikey": API_KEY
}

# 3. Connect to Alpha Vantage
print("Connecting to Alpha Vantage...")

response = requests.get(url, params=parameters, timeout=30)
response.raise_for_status()

data = response.json()

# 4. Check for API errors or messages
if "Error Message" in data:
    raise ValueError(data["Error Message"])

if "Note" in data or "Information" in data:
    raise RuntimeError(
        data.get("Note") or data.get("Information")
    )

# 5. Extract daily stock prices
if "Time Series (Daily)" not in data:
    raise ValueError(f"Unexpected API response: {data}")

stock_data = data["Time Series (Daily)"]

df = pd.DataFrame.from_dict(stock_data, orient="index")

# 6. Clean column names
df.columns = [
    column.split(". ", 1)[1]
    for column in df.columns
]

# 7. Convert values into numeric data
df = df.apply(pd.to_numeric)

# 8. Format dates and sort chronologically
df.index = pd.to_datetime(df.index)
df.index.name = "Date"

df = df.sort_index()

# 9. Save CSV file
project_folder = Path(__file__).resolve().parent.parent
output_folder = project_folder / "data" / "raw"

output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "aapl_sample.csv"

df.to_csv(output_file)

# 10. Display results
print("\nApple stock data downloaded successfully!")
print("\nFirst five records:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSaved file:", output_file)
print("\nNumber of records:", len(df))
