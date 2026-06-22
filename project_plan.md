# Stock Market Data Analysis Project Plan

## Working Title

Understanding Stock Market Risk, Returns, and Prediction

## Objective

Analyse several years of stock market data using mathematics, statistics, programming, and visualisation. The project should demonstrate data analyst skills through a clear, evidence-based study of financial market risk and return.

## Stage 1: Data Collection

Goals:

- Download historical daily prices.
- Download trading volume.
- Include individual stocks and benchmark indices.
- Store raw data as CSV files first.
- Later, optionally store processed data in a SQL database.

Skills:

- APIs
- Data acquisition
- Data storage
- Python scripting

Initial assets:

- Apple
- Microsoft
- NVIDIA
- Amazon
- S&P 500
- FTSE 100

## Stage 2: Exploratory Data Analysis

Questions:

- Which stock grew the most?
- Which stock had the largest crashes?
- Which stock was most volatile?
- How do prices and returns compare across assets?

Visualisations:

- Price charts
- Daily return histograms
- Boxplots
- Correlation heatmaps

Skills:

- Pandas
- NumPy
- Matplotlib or Plotly
- Statistical summaries

## Stage 3: Risk Analysis

Metrics:

- Daily returns
- Volatility
- Sharpe ratio
- Correlations
- Maximum drawdown

Mathematical ideas:

- Probability
- Standard deviation
- Risk measurement
- Risk-adjusted return

## Stage 4: Portfolio Analysis

Question:

If an investor had GBP 10,000, how could it be split across stocks?

Analyse:

- Portfolio return
- Portfolio risk
- Diversification effects
- Different portfolio weights

Skills:

- Linear algebra
- Optimisation
- Statistics

## Stage 5: Machine Learning

Optional prediction task:

- Predict whether a stock rises or falls the next day.

Possible models:

- Logistic regression
- Random forest
- XGBoost

Important principle:

Evaluate models honestly. A realistic result such as 56% accuracy with clear limitations is more credible than claiming a perfect stock predictor.

## Stage 6: Dashboard

Possible tools:

- Streamlit
- Power BI
- Tableau

Dashboard features:

- Stock comparison
- Interactive price charts
- Risk metrics
- Correlation view
- Portfolio simulator

## Stage 7: Final Report

Suggested sections:

- Introduction
- Objectives
- Methodology
- Data collection
- Exploratory analysis
- Risk analysis
- Portfolio analysis
- Machine learning results, if included
- Key findings
- Limitations
- Conclusion
- What was learned

## CV Description

Stock Market Risk and Portfolio Analytics Platform

- Collected and analysed historical financial market data using Python and SQL.
- Calculated volatility, correlations, Sharpe ratios, drawdowns, and portfolio risk metrics.
- Built machine learning models to predict stock price direction.
- Developed an interactive dashboard for visualising market performance and risk.
- Produced a professional report communicating data-driven investment insights.

## Git Workflow

Start by working on the main branch and making frequent commits.

Useful commit examples:

- Initial project setup
- Added data collection script
- Implemented daily return calculations
- Added volatility and Sharpe ratio metrics
- Built portfolio analysis module
- Created dashboard prototype
- Added final project report

Branches can be added later for larger features such as:

- dashboard
- machine-learning
- sql-database
