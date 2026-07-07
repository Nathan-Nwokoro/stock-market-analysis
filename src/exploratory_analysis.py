from pathlib import Path

import numpy as np
import pandas as pd


CLEAN_DATA_PATH = Path("data/clean_stock_data.csv")
REPORTS_DIR = Path("reports")
SUMMARY_PATH = REPORTS_DIR / "eda_summary.csv"
CORRELATION_PATH = REPORTS_DIR / "return_correlation.csv"
RETURNS_PATH = REPORTS_DIR / "daily_returns.csv"


def load_clean_data(path: Path = CLEAN_DATA_PATH) -> pd.DataFrame:
    """Load cleaned stock data and enforce expected date ordering."""
    data = pd.read_csv(path, parse_dates=["date"])
    return data.sort_values(["ticker", "date"]).reset_index(drop=True)


def add_return_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Add daily and cumulative return columns for each ticker."""
    enriched = data.copy()
    grouped = enriched.groupby("ticker", group_keys=False)

    enriched["daily_return"] = grouped["close"].pct_change()
    enriched["cumulative_return"] = grouped["daily_return"].transform(
        lambda returns: (1 + returns.fillna(0)).cumprod() - 1
    )

    return enriched


def calculate_max_drawdown(prices: pd.Series) -> float:
    """Calculate the largest peak-to-trough loss for a price series."""
    running_peak = prices.cummax()
    drawdown = prices / running_peak - 1
    return drawdown.min()


def build_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Create ticker-level risk and return metrics."""
    rows = []

    for ticker, ticker_data in data.groupby("ticker"):
        returns = ticker_data["daily_return"].dropna()
        first_close = ticker_data["close"].iloc[0]
        last_close = ticker_data["close"].iloc[-1]
        total_return = last_close / first_close - 1
        annualized_return = (1 + total_return) ** (252 / len(returns)) - 1
        annualized_volatility = returns.std() * np.sqrt(252)
        sharpe_ratio = (
            annualized_return / annualized_volatility
            if annualized_volatility != 0
            else np.nan
        )

        rows.append(
            {
                "ticker": ticker,
                "start_date": ticker_data["date"].min().date(),
                "end_date": ticker_data["date"].max().date(),
                "observations": len(ticker_data),
                "first_close": first_close,
                "last_close": last_close,
                "total_return": total_return,
                "annualized_return": annualized_return,
                "annualized_volatility": annualized_volatility,
                "sharpe_ratio": sharpe_ratio,
                "max_drawdown": calculate_max_drawdown(ticker_data["close"]),
                "best_daily_return": returns.max(),
                "worst_daily_return": returns.min(),
            }
        )

    return pd.DataFrame(rows).sort_values("total_return", ascending=False)


def build_return_correlation(data: pd.DataFrame) -> pd.DataFrame:
    """Create a correlation matrix using daily returns."""
    returns_wide = data.pivot(index="date", columns="ticker", values="daily_return")
    return returns_wide.corr()


def save_optional_charts(data: pd.DataFrame, correlation: pd.DataFrame) -> None:
    """Save EDA charts when matplotlib is installed."""
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("matplotlib is not installed; skipped chart output.")
        return

    charts_dir = REPORTS_DIR / "figures"
    charts_dir.mkdir(parents=True, exist_ok=True)

    price_wide = data.pivot(index="date", columns="ticker", values="close")
    normalized_prices = price_wide / price_wide.iloc[0]

    normalized_prices.plot(figsize=(12, 7), title="Growth of $1 Invested")
    plt.ylabel("Growth multiple")
    plt.tight_layout()
    plt.savefig(charts_dir / "normalized_price_growth.png")
    plt.close()

    data.boxplot(column="daily_return", by="ticker", figsize=(12, 7))
    plt.title("Daily Return Distribution")
    plt.suptitle("")
    plt.ylabel("Daily return")
    plt.tight_layout()
    plt.savefig(charts_dir / "daily_return_boxplot.png")
    plt.close()

    fig, ax = plt.subplots(figsize=(9, 7))
    heatmap = ax.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
    ax.set_yticks(range(len(correlation.index)), correlation.index)
    fig.colorbar(heatmap, ax=ax, label="Correlation")
    ax.set_title("Daily Return Correlation")
    plt.tight_layout()
    plt.savefig(charts_dir / "return_correlation_heatmap.png")
    plt.close()


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    clean_data = load_clean_data()
    analysis_data = add_return_columns(clean_data)
    summary = build_summary(analysis_data)
    correlation = build_return_correlation(analysis_data)

    analysis_data.to_csv(RETURNS_PATH, index=False)
    summary.to_csv(SUMMARY_PATH, index=False)
    correlation.to_csv(CORRELATION_PATH)
    save_optional_charts(analysis_data, correlation)

    print(f"Saved daily returns to {RETURNS_PATH}")
    print(f"Saved EDA summary to {SUMMARY_PATH}")
    print(f"Saved return correlation matrix to {CORRELATION_PATH}")
    print()
    print("Top assets by total return:")
    print(summary[["ticker", "total_return", "annualized_volatility", "sharpe_ratio"]].to_string(index=False))


if __name__ == "__main__":
    main()
