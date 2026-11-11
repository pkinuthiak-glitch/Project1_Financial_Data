
# validate_stock_data.py

import pandas as pd
from pathlib import Path

# 1. Define project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

tickers = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

quality_results = []

print("STARTING FINANCIAL DATA QUALITY CHECK")
print("=" * 50)

# 2. Inspect each stock dataset
for ticker in tickers:

    file_path = RAW_DIR / f"{ticker}.csv"

    print(f"\nChecking {ticker}...")

    if not file_path.exists():
        print(f"ERROR: {ticker}.csv was not found.")
        continue

    df = pd.read_csv(file_path)

    # Standardize column names
    df.columns = [str(col).strip() for col in df.columns]

    # 3. Convert dates
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.sort_values("Date")

    # 4. Check missing values
    missing_values = int(df.isna().sum().sum())

    # 5. Check duplicate dates
    duplicate_dates = int(df["Date"].duplicated().sum())

    # 6. Check invalid dates
    invalid_dates = int(df["Date"].isna().sum())

    # 7. Check missing trading intervals
    valid_dates = df["Date"].dropna().sort_values()
    date_gaps = valid_dates.diff().dt.days
    unusual_gaps = int((date_gaps > 4).sum())

    # 8. Check price and volume values
    price_columns = ["Open", "High", "Low", "Close"]

    for col in price_columns + ["Volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    invalid_prices = int(
        (df[price_columns] <= 0).any(axis=1).sum()
    )

    invalid_volume = int(
        (df["Volume"] < 0).sum()
    )

    # 9. Check OHLC consistency
    invalid_ohlc = int(
        (
            (df["High"] < df[["Open", "Low", "Close"]].max(axis=1))
            |
            (df["Low"] > df[["Open", "High", "Close"]].min(axis=1))
        ).sum()
    )

    # 10. Display results
    print("Rows:", len(df))
    print("Missing values:", missing_values)
    print("Duplicate dates:", duplicate_dates)
    print("Invalid dates:", invalid_dates)
    print("Unusual date gaps:", unusual_gaps)
    print("Invalid prices:", invalid_prices)
    print("Invalid volumes:", invalid_volume)
    print("OHLC inconsistencies:", invalid_ohlc)

    # 11. Store results
    quality_results.append({
        "Ticker": ticker,
        "Rows": len(df),
        "Missing_Values": missing_values,
        "Duplicate_Dates": duplicate_dates,
        "Invalid_Dates": invalid_dates,
        "Unusual_Date_Gaps": unusual_gaps,
        "Invalid_Prices": invalid_prices,
        "Invalid_Volumes": invalid_volume,
        "OHLC_Inconsistencies": invalid_ohlc
    })

# 12. Save quality report
if quality_results:

    report = pd.DataFrame(quality_results)

    report_path = OUTPUT_DIR / "data_quality_report.csv"

    report.to_csv(report_path, index=False)

    print("\n" + "=" * 50)
    print("DATA QUALITY CHECK COMPLETED")
    print(report.to_string(index=False))
    print("\nReport saved to:", report_path)
