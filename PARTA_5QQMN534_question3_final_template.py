https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
# -*- coding: utf-8 -*-

# 5QQMN534 22-23
# Candidate Number:
# Do not enter Name

#%% QUESTION3: Backtest RSI Strategy

"""
Do not use libraries for the RSI technical indicator.
Write the mathematics for the Wilder Smoothing RSI indicator yourself.
Write the functions and mathematics for portfolio metrics
Use log returns 

"""

#%% Set dir and path


#%% Import libraries



#%% a) Download FB between 2020-01-01 and 2022-01-01 using yahoo finance library.
# Alternatively, load the FB data from the excel file provided in folder Q3_Data.


#%% b) Download SPY benchmark for same dates as above in part a using yahoo finance library.
# Alternatively, load the SPY data from the excel file provided in folder Q3_Data


#%%  c) Extract FB Adjusted Close and create a new DataFrame called close.


#%% d) Write a function to calculate Wilder’s smoothing RSI on the FB Adjusted Close (See Screenshot in slides for mathematics). Save these results to the DataFrame called close.


#%% e) Calculate the signals based off the below condition: (4 marks)
# RSI < 30 = BUY
# RSI > 70 = SELL
# *Note: 30 & 70 are the default parameters.
# N = 14 (setting default window)




#%% f) Plot RSI signal and graph adjusted stock close price in separate plots. Save graph.


#%% g)  Calculate the log returns for adjusted close for the stock and the benchmark



#%% h) Calculate the strategy returns
"""
The basic idea is that the algorithm can only set up a position in the  stock given today’s
market data (e.g., just before the close). The position then earns tomorrow’s return.
"""



#%% i) Calculate cumualtive returns for buy and hold the stock, the strategy and the benchmark
# Double check your result with various approaches.


#%% j) Plot cumulative returns from the log returns for buy and hold the stock,
# the strategy and the benchmark




#%% k) Calculate descriptive statistics on the stock, the strategy and benchmark returns.
# Save to a DataFrame.




#%% l) Optimise the RSI with the below condition ranges:

"""
Optimise the RSI with the below condition ranges: (6 marks)
rsi_buy between 0 and 30 with increment 1
rsi_sell between 70 and 100 with increment 1
n_window between 2 and 21 with increment 1


Hint: Due to computational time, test optimal parameters with increment 10 first.
Time the optimisation in seconds and minutes and print to screen.
The optimised results should generate a DataFrame showing the:
RSI Buy, RSI Sell, N Window, market returns, strategy returns and outperformance.
Note: Outperformance is Strategy Returns – Market Returns

"""


#%% m) Sort the optimised parameter results on outperformance. Save results to an excel file. 



#%% n) Extract the optimal parameters


#%% o)  Rerun the optimal parameter strategy.
# Plot the RSI and signals and cumulative return graphs.
# Re-calculate the cumulative performances using the optimal parameters.



#%% p)  Isolate the optimal strategy returns and calculate the below performance statistics on this
# strategy and the benchmark: Assume rf = 0and 252 days. Format to 2 decimal places (dp).
# Write functions and store all results in a DataFrame and save to excel.
# Do not use a library for calcualtions.

# i) Sharpe Ratio

# ii) Sortino Ratio

# iii) Compound Annual Growth Rate  (CAGR)

# iv) Annual Volatility

# v) Calmar Ratio

# vi) Maximum Drawdown

# vii) Skewness (4dp)

# viii) Kurtosis  (4dp)



#%%  q) Calculate the number of total trades, long trades and short trades for optimal strategy.
# Save as a DataFrame.

# Total Trades


# Total Longs


# Total Shorts


#%% r) Plot a histogram optimal strategy returns vs benchmark returns


#%%