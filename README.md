# Stock Market Risk and Portfolio Analytics

This project analyses historical stock market data to understand the relationship between risk, return, diversification, and prediction in financial markets.

The aim is not to build a "get rich quick" trading bot. Instead, the project focuses on rigorous data analysis, clear visualisation, honest model evaluation, and professional communication of results.

## Project Questions

- Which stocks grew the most over the study period?
- Which stocks were the most volatile?
- How does risk relate to return?
- Which stocks move together?
- How do stocks behave during market crashes?
- Can future price direction be predicted from historical information?
- How can a portfolio be split to balance risk and return?

## Planned Data Sources

Potential data sources include:

- Yahoo Finance
- Alpha Vantage
- Stooq

Initial assets to analyse:

- Apple Inc.
- Microsoft
- NVIDIA
- Amazon
- S&P 500 benchmark
- FTSE 100 benchmark

## Key Features

- Historical market data collection
- Exploratory data analysis
- Price, return, and volume visualisations
- Volatility and drawdown analysis
- Sharpe ratio calculations
- Stock correlation analysis
- Portfolio risk and return analysis
- Optional machine learning for next-day direction prediction
- Optional Streamlit, Power BI, or Tableau dashboard
- Final professional report

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib or Plotly
- SQL
- Scikit-learn
- Streamlit, Power BI, or Tableau
- Git and GitHub

## Risk and Return

Return measures how much an investment gains or loses over a period of time.

For example, if a stock rises from GBP 100 to GBP 110, the return is:

```text
(110 - 100) / 100 = 0.10 = 10%
```

Risk measures how uncertain or volatile returns are. In this project, risk will mainly be measured using the standard deviation of returns, also known as volatility.

A stock with large price swings is considered riskier than a stock with steadier returns.

## Important Metrics

- Daily return
- Cumulative return
- Volatility
- Maximum drawdown
- Correlation
- Sharpe ratio
- Portfolio return
- Portfolio risk

## Example Insight

An example conclusion might be:

> NVIDIA achieved the highest average annual return over the study period. However, it also exhibited the highest volatility, indicating greater investment risk. Microsoft generated lower returns but delivered superior risk-adjusted performance as measured by the Sharpe ratio.

## Project Status

Current stage: project setup and planning.

Next step: build the first data collection script and download historical prices for the initial stock list.
