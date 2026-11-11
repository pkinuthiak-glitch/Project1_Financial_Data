# Financial Data Analysis Project

**Author:** Paul Kinuthia Kuguru  
**Project:** Project 1 – Financial Data Analysis  
**Date:** November 2026

## 1. Project Overview

This project focuses on collecting, storing, validating, and analysing financial stock market data using Python.

The project uses Apple Inc. (AAPL) historical stock market data obtained from two financial data providers: Alpha Vantage and Yahoo Finance.

The objective is to develop practical skills in financial data collection, data quality assessment, Python programming, and exploratory financial data analysis.

## 2. Data Sources

- **Alpha Vantage API:** Historical daily Apple stock market data.
- **Yahoo Finance:** Historical Apple stock market data using the yfinance Python library.

## 3. Technologies and Libraries

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Requests
- yfinance
- Jupyter Notebook
- Git and GitHub

## 4. Project Structure

```text
Project1_Financial_Data/
│
├── data/
│   └── raw/
│       ├── aapl_sample.csv
│       └── aapl_yfinance.csv
│
├── notebooks/
│   └── environment_test.ipynb
│
├── scripts/
│   ├── alpha_vantage_test.py
│   └── yfinance_test.py
│
├── outputs/
│
├── docs/
│
├── .gitignore
├── README.md
└── environment_test.ipynb
```

## 5. Data Collection

Two Python scripts were developed to retrieve Apple stock market data.

- `alpha_vantage_test.py` retrieves historical stock data through the Alpha Vantage API.
- `yfinance_test.py` retrieves historical stock data through Yahoo Finance.

The retrieved datasets include:

- Date
- Open
- High
- Low
- Close
- Adjusted Close (where available)
- Trading Volume

## 6. Data Validation

Data quality checks were performed using Pandas.

The validation process included:

- Checking for missing values.
- Identifying duplicate dates.
- Checking for invalid High and Low prices.
- Checking for negative trading volume.
- Verifying chronological date ordering.

The Yahoo Finance dataset contained 127 records.

Validation results showed:

- Missing values: 0
- Duplicate dates: 0
- Invalid High values: 0
- Invalid Low values: 0
- Negative volume values: 0
- Dates sorted chronologically: True

## 7. API Security

The Alpha Vantage API key is stored separately as an environment variable.

Sensitive information is excluded from version control using `.gitignore`.

The actual API key is not included in this repository.

## 8. Project Objectives

1. Retrieve financial stock market data from external sources.
2. Store financial data in CSV format.
3. Apply data validation and quality checks.
4. Use Python libraries for financial data processing.
5. Prepare datasets for exploratory data analysis and visualization.

## 9. Future Development

Planned project improvements include:

- Exploratory Data Analysis (EDA).
- Stock price trend visualization.
- Daily returns calculations.
- Moving averages.
- Volatility analysis.
- Comparison of Alpha Vantage and Yahoo Finance datasets.
- Financial data dashboards.

## 10. Author

**Paul Kinuthia Kuguru**

Financial Data Analysis Project – 2026

GitHub: https://github.com/pkinuthiak-glitch