
# Financial Risk and Options Pricing
## Overview
This repository contains Python code for calculating the Value at Risk (VaR) and option prices using the Black-Scholes model. It leverages the yfinance library to download historical stock data and the scipy library for statistical calculations.

## Functions
### calculate_var_n
#### Calculates the Value at Risk (VaR) for a given stock position over n days with a confidence level c.
#### Parameters:

- **stock_data (DataFrame)**: DataFrame containing historical stock data with returns.
- **position (float)**: Value of the position in the stock.
- **c (float)**: Confidence level (e.g., 0.99 for 99% confidence).
- **n (int)**: Number of days.

### call_option_price
#### Calculates the price of a European call option using the Black-Scholes model.
#### Parameters:

- **S (float)**: Current stock price.
- **E (float)**: Strike price.
- **T (float)**: Time to expiration (in years).
- **rf (float)**: Risk-free interest rate.
- **sigma (float)**: Volatility of the stock.

### put_option_price
#### Calculates the price of a European put option using the Black-Scholes model.
#### Parameters:

- **S (float)**: Current stock price.
- **E (float)**: Strike price.
- **T (float)**: Time to expiration (in years).
- **rf (float)**: Risk-free interest rate.
- **sigma (float)**: Volatility of the stock.

