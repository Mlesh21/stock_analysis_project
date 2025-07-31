import yfinance as yf
import os
tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'NVDA', 'META', 'JPM', 'NFLX', 'DIS']
if not os.path.exists("../data"):
    os.makedirs("../data")
for ticker in tickers:
    data = yf.download(ticker, start='2005-01-01', end='2025-01-01')
    data.to_csv(f'data/{ticker}.csv')