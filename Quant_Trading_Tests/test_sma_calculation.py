repo_name = "automation-testing-portfolio"
repo_structure = {
    "Web_Automation": ["login_test.py", "page_navigation_test.py", "form_submission_test.py"],
    "API_Tests": ["api_get_test.py", "api_post_test.py"],
    "Database_Tests": ["db_validation_test.py"],
    "Quant_Trading_Tests": ["test_stock_data_fetch.py", "test_sma_calculation.py", "test_api_stock_data.py"],
    "utils": ["config.py", "helpers.py"],
    "root_files": ["README.md", "requirements.txt", ".gitignore"]
}

def create_readme():
    return """# Automation Testing Portfolio

This repository contains standalone automation scripts using Selenium, Playwright, API testing, and Quant Trading validation with Python.

## Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run a test script:
   ```
   python Web_Automation/login_test.py
   ```

## Test Cases Included
- Web Automation (Login, Navigation, Form Submission)
- API Testing (GET, POST Validation)
- Database Testing (SQL Validation)
- Quant Trading Tests (Stock Data Fetch, SMA Calculation, API Trading Data)
"""

def create_gitignore():
    return """__pycache__/
*.pyc
*.pyo
.env
.vscode/
.idea/
"""

# Generate repo structure
repo_files = {}
for folder, files in repo_structure.items():
    if folder == "root_files":
        for file in files:
            if file == "README.md":
                repo_files[file] = create_readme()
            elif file == ".gitignore":
                repo_files[file] = create_gitignore()
            else:
                repo_files[file] = ""  # Placeholder for future content
    else:
        for file in files:
            repo_files[f"{folder}/{file}"] = ""  # Placeholder for future scripts

# Adding the Quant Trading Test Scripts
repo_files["Quant_Trading_Tests/test_stock_data_fetch.py"] = """import yfinance as yf

def test_stock_data_fetch():
    \"\"\"Fetch stock data for AAPL and verify it contains expected columns.\"\"\"
    stock = yf.Ticker(\"AAPL\")
    data = stock.history(period=\"5d\")
    expected_columns = [\"Open\", \"High\", \"Low\", \"Close\", \"Volume\"]
    assert all(col in data.columns for col in expected_columns), \"Missing required columns!\"
    print(\"✅ Test Passed: Stock data contains all expected columns\")

test_stock_data_fetch()"""

repo_files["Quant_Trading_Tests/test_sma_calculation.py"] = """import pandas as pd
import yfinance as yf

def test_sma_calculation():
    \"\"\"Fetch AAPL stock data and verify SMA calculations.\"\"\"
    stock = yf.Ticker(\"AAPL\")
    data = stock.history(period=\"50d\")
    data[\"SMA_10\"] = data[\"Close\"].rolling(window=10).mean()
    assert not data[\"SMA_10\"].isna().all(), \"SMA Calculation Failed!\"
    print(\"✅ Test Passed: SMA calculated successfully\")

test_sma_calculation()"""

repo_files["Quant_Trading_Tests/test_api_stock_data.py"] = """import requests

def test_api_stock_data():
    \"\"\"Fetch stock data from a public API and verify response format.\"\"\"
    url = \"https://www.alphavantage.co/query\"
    params = {
        \"function\": \"TIME_SERIES_INTRADAY\",
        \"symbol\": \"AAPL\",
        \"interval\": \"5min\",
        \"apikey\": \"demo\"  # Replace with your own API key
    }
    response = requests.get(url, params=params)
    data = response.json()
    assert \"Time Series (5min)\" in data, \"API Response Error!\"
    print(\"✅ Test Passed: API returned valid stock data\")

test_api_stock_data()"""

repo_files
