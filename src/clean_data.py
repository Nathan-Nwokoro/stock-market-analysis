from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/stock_data.csv")
CLEAN_DATA_PATH = Path("data/clean_stock_data.csv")


def clean_stock_data(raw_data_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Convert the Yahoo Finance multi-header CSV into a tidy table."""
    raw_data = pd.read_csv(raw_data_path, header=[0, 1], index_col=0, parse_dates=True)

    clean_data = (
        raw_data.stack(level="Ticker", future_stack=True)
        .reset_index()
        .rename(
            columns={
                "Date": "date",
                "Ticker": "ticker",
                "Close": "close",
                "High": "high",
                "Low": "low",
                "Open": "open",
                "Volume": "volume",
            }
        )
    )

    # Only require date, ticker, and close because closing price is the key value
    # needed for returns, volatility, Sharpe ratio, and drawdown analysis.
    # Other columns such as open, high, low, and volume are kept for future analysis,
    # but rows are not removed just because one of those optional values is missing.
    clean_data = clean_data.dropna(subset=["date", "ticker", "close"]) 
    clean_data = clean_data.sort_values(["ticker", "date"]).reset_index(drop=True)

    return clean_data


def main() -> None:
    clean_data = clean_stock_data()
    clean_data.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Saved cleaned data to {CLEAN_DATA_PATH}")
    print(f"Rows: {len(clean_data):,}")
    print(f"Columns: {', '.join(clean_data.columns)}")


if __name__ == "__main__":
    main()
