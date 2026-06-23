# Project Progress Notes

## 22 June 2026

Initial project setup completed.

Work completed so far:

- Created the main project README.
- Added a structured project plan.
- Created folders for source code, data, notebooks, reports, SQL, and notes.
- Added placeholder files so the empty project folders can be tracked by Git.
- Defined the project focus as stock market risk, return, portfolio analysis, and optional prediction.
- Added a data collection script using Yahoo Finance data.
- Downloaded historical stock market data for Apple, Microsoft, NVIDIA, Amazon, the S&P 500, and the FTSE 100.
- Saved the raw stock market dataset in the data folder.
- Added a data cleaning script to convert the raw Yahoo Finance format into a cleaner table.
- Created a cleaned dataset with date, ticker, close, high, low, open, and volume columns.

Next planned step:

- Begin exploratory data analysis using the cleaned stock market dataset.

## 23 June 2026

Started exploratory data analysis.

Work completed so far:

- Added an exploratory analysis script for the cleaned stock market dataset.
- Calculated daily returns and cumulative returns for each ticker.
- Created ticker-level summary metrics including total return, annualized return, annualized volatility, Sharpe ratio, maximum drawdown, best daily return, and worst daily return.
- Created a daily return correlation matrix.
- Saved analysis outputs in the reports folder:
  - `reports/daily_returns.csv`
  - `reports/eda_summary.csv`
  - `reports/return_correlation.csv`

Initial findings:

- NVIDIA had the highest total return from 2010-01-04 to 2025-12-31.
- NVIDIA also had the highest annualized volatility, showing the clearest risk-return tradeoff in the initial asset list.
- Microsoft had a lower total return than Apple and Amazon, but a stronger Sharpe ratio than Amazon.
- The S&P 500 was most strongly correlated with Microsoft among the selected individual stocks.
- The FTSE 100 had the lowest total return and the lowest Sharpe ratio in this asset set.

Key metric explanations:

- Volatility measures how much an asset's returns move up and down over time. Higher volatility means the price changes are less steady and the investment is usually considered riskier.
- Sharpe ratio compares return against risk. A higher Sharpe ratio means the asset produced more return for each unit of volatility. In this project, it helps compare whether a stock's return was worth the amount of risk taken.
- Maximum drawdown measures the biggest fall from a previous high point to a later low point. For example, if a stock rose to GBP 100 and then dropped to GBP 60 before recovering, the maximum drawdown would be -40%. This helps show how painful the worst loss period would have been for an investor.

Next planned step:

- Install or enable Matplotlib, then generate price growth, return distribution, and correlation heatmap charts.
- Begin turning the EDA summary into written observations for the final report.
