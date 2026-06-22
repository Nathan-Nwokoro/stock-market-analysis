import yfinance as yf

tickers = [
    "AAPL",   # Apple
    "MSFT",   # Microsoft
    "NVDA",   # NVIDIA
    "AMZN",   # Amazon
    "^GSPC",  # S&P 500
    "^FTSE"   # FTSE 100
]

data = yf.download(
    tickers,
    start="2010-01-01",
    end="2026-01-01"
)

data.to_csv("data/stock_data.csv")