import numpy as np
import yfinance as yf
from scipy.stats import norm


def download_data(stock, start_date, end_date):
    df = yf.download(stock, start_date, end_date)
    df = df[['Adj Close']]
    df['returns'] = df['Adj Close'].pct_change()
    return df


def calculate_var_n(stock_data, position, c, n):
    df = stock_data
    mu = np.mean(df['returns'])
    sigma = np.std(df['returns'])
    var = position * (mu * n - sigma * np.sqrt(n) * norm.ppf(1-c))
    return var


stock = download_data('META', '2022-04-02', '2024-03-01')

Var = calculate_var_n(stock, 100000, 0.99, 1)
