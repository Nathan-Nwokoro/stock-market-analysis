# Exploratory Data Analysis Findings

This report summarises the first exploratory analysis of Apple, Microsoft, NVIDIA, Amazon, the S&P 500, and the FTSE 100 using daily market data from 2010-01-04 to 2025-12-31.

## What grew the most?

NVIDIA grew the most by a very large margin.

Its total return was approximately 43,906%, meaning the final closing price was about 440 times higher than the starting closing price in the dataset. This was much higher than the next strongest assets, Apple and Amazon.

Total return ranking:

| Asset | Total return |
| --- | ---: |
| NVIDIA | 43,906% |
| Apple | 4,136% |
| Amazon | 3,348% |
| Microsoft | 1,991% |
| S&P 500 | 504% |
| FTSE 100 | 81% |

## What was the riskiest?

NVIDIA was also the riskiest asset based on annualized volatility.

Volatility measures how much daily returns move up and down. NVIDIA had annualized volatility of approximately 45.7%, which was higher than every other asset in the analysis. This means NVIDIA had the largest price swings and was less stable day to day.

Volatility ranking:

| Asset | Annualized volatility |
| --- | ---: |
| NVIDIA | 45.7% |
| Amazon | 32.8% |
| Apple | 28.2% |
| Microsoft | 25.5% |
| S&P 500 | 17.3% |
| FTSE 100 | 15.5% |

## Which asset had the worst drawdown?

NVIDIA had the worst maximum drawdown.

Its maximum drawdown was approximately -66.3%. This means that, at its worst point, NVIDIA fell about 66% from a previous high before recovering. Amazon also had a large drawdown of about -56.1%, but NVIDIA's was the largest.

Maximum drawdown ranking:

| Asset | Maximum drawdown |
| --- | ---: |
| NVIDIA | -66.3% |
| Amazon | -56.1% |
| Apple | -43.8% |
| Microsoft | -37.1% |
| FTSE 100 | -36.6% |
| S&P 500 | -33.9% |

## Which stocks moved together?

The assets that moved together most strongly were Microsoft and the S&P 500.

Their daily return correlation was approximately 0.75. This means Microsoft often moved in the same direction as the wider US stock market. Apple and the S&P 500 also had a strong correlation of about 0.69.

Strongest correlations:

| Pair | Correlation |
| --- | ---: |
| Microsoft and S&P 500 | 0.75 |
| Apple and S&P 500 | 0.69 |
| NVIDIA and S&P 500 | 0.63 |
| Amazon and S&P 500 | 0.61 |
| Apple and Microsoft | 0.58 |
| Amazon and Microsoft | 0.57 |

The FTSE 100 had weaker correlations with the individual US technology stocks. This makes sense because the FTSE 100 represents the UK market, while Apple, Microsoft, NVIDIA, and Amazon are US technology companies.

## Was higher return linked to higher risk?

Yes, in this dataset higher return was generally linked to higher risk, but the relationship was not perfect.

NVIDIA had both the highest total return and the highest volatility. This shows a clear risk-return tradeoff: investors were rewarded with very high long-term growth, but they also had to accept much larger price swings and a deeper drawdown.

Amazon and Apple also had high returns and higher volatility than the market indices. The S&P 500 and FTSE 100 had lower returns, but they were also less volatile.

However, risk and return did not move in a perfectly straight line. For example, Microsoft had lower total return than Apple and Amazon, but it had a strong Sharpe ratio, meaning its return was attractive compared with the level of volatility it took.

Overall, the first EDA suggests that the highest-growth assets were also among the riskiest, especially NVIDIA.
