https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
# -*- coding: utf-8 -*-

# 5QQMN534 22-23
# Candidate Number:
# Do not enter Name
#%% QUESTION 2: Strategy Analysis 

#%% a)  STRATEGY: 
    
"""
Load the "strategy_returns.xlsx” file in Q2_data folder . 
Save this as a DataFrame variable called strat_ret
"""


#%%  b)

"""
Calculate the skew and kurtosis on the strategy returns. 
Plot a histogram of returns and comment on the strategy returns distribution. 
Round results to four decimal places.
"""

#%% c)  

"""Calculate the daily mean, standard deviation and Sharpe Ratio. 
Assume risk free is zero.
Print results to screen. 
Format outputs to correct units. 
Round results to four decimal places.
"""


#%% d) 

"""Calculate the annual mean, standard deviation and Sharpe Ratio. 
Assume annual risk free is zero. 
Assume 252 days per year. 
Print results to screen. 
Format outputs to correct units.
Round results to four decimal places.
"""


#%% e) 

"""
Calculate the daily rolling volatility starting from day 252.
Then extract this statistic on the 2nd January each year from 2015 to 2021 
and then annualise this value.
Assume 252 days per year. 
Create a DataFrame. 
The Index as 2nd January each year 2015 to 2021 as Dates, 
daily rolling volatility on that date, third column annual volatility. 
Print DataFrame to screen. 

"""


#%% f) 
"""
Plot a well formatted displayed bar graph of the Annual Volatility from part e. 
Show the y axis range from 15% to 20%. 
"""

#%% g) 

"""
Complete an if statement to check if the average annual volatility between 2015 and 2021 from 
part e is between the lower 15% and upper 25% standard deviation thresholds as specified by mandate. 

"""

#%% S&P 500


#%% h) 

"""
Load the "SP500_returns.xlsx” file in Q2_data folder. 
Create a new DataFrame called returns_2 and match the returns of the strategy and S&P500 
returns using the dates from the strategy as the index. 
Set S&P 500 returns that are nan as zero.

"""


#%% i) 

"""
Run an OLS  regression between strategy returns and S&P500 market benchmark returns. 
State which is the dependent and independent variable in a comment. 
Save all model results to a DataFrame. 
Extract Beta, Alpha and R-Squared from regression results to variables. 
Annualise the alpha. N = 252 days. 
Calculate the correlation. 
Round result values to four decimal places and print to screen. 

"""


#%% Hedge Fund Index  HFRI 

#%% j) 

"""
Load the "hfri_index.xlsx” file in Q2_data folder. 
Calculate the HFRI simple percentage returns. 
Create an Index for your strategy daily returns rebasing to begin with 1. 
Create a new DataFrame called returns_3 and match the rebased index of the 
strategy and HFRI index using the monthly dates from the HFRI. 
Note: There should be no NaN’s in the matched DataFrame. 
Hint: If the strategy rebased dates do not match the HFRI monthly dates exactly in the index you will need to get the 
last monthly value from  the strategy rebased dates. 
"""

#%% k) Run an OLS  regression between strat and HFRI benchmark (extract Beta, Alpha and RSquared) from regression results.
# Annualise the alpha by N = 252 days and aLso Calculate correlation



#%% l) Discuss the difference in results between part i and k in a comment 
# Is the strategy meeting the mandate requirements? Maximum 300 words. 




#%%