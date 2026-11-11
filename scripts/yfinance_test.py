
import yfinance as yf
import pandas as pd
from pathlib import Path

# Download Apple stock data
ticker = "AAPL"

print("Downloading Apple stock data using Yahoo Finance...")

stock = yf.download(
    ticker,
    period="6mo",
    interval="1d",
    auto_adjust=False,
    progress=False
)

# Check whether data was retrieved
if stock.empty:
    raise ValueError("No stock data downloaded.")

# Handle possible multi-level column names
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

# Save the dataset
project_folder = Path(__file__).resolve().parent.parent
output_folder = project_folder / "data" / "raw"
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "aapl_yfinance.csv"

stock.to_csv(output_file)

# Display results
print("\nYahoo Finance download successful!")
print("\nFirst five records:")
print(stock.head())

print("\nDataset information:")
stock.info()

print("\nSaved file:", output_file)
print("Number of records:", len(stock))
