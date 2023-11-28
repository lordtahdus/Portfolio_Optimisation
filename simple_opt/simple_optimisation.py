import yfinance as yf
import numpy as np
import pandas as pd
from gekko import GEKKO
from retrieve_history import *


# asx200_list = pd.read_csv('assets/ASX200_companies_list.csv')
# period = '1mo'
# interval = '1wk'

# stock_history = retrieve_history(asx200_list['Yahoo Code'], period, interval)
# mean_returns, varcov_returns = get_mean_varcov(stock_history)

# print(varcov_returns)

stock_returns = pd.read_csv('simple_opt/stock_returns.csv', index_col='Date')

mean = np.array(stock_returns.mean()) # vector of means of returns
varcov = np.array(stock_returns.cov()) # Var-cov matrix

print(mean)
print(varcov)

m = GEKKO(remote=False)

# Variables (in matrix form)
b = m.Array(m.Var, 10, value=0.1, lb=0, ub=1)

# Constraint in matrix form
m.Equation(np.sum(b) == 1)

# obj = b*mean*(b*varcov*b).T

obj = np.dot(b, mean) * (b.T @ varcov @ b)**(-1)

m.Minimize(-obj)

m.solve(disp=False)

b_hat = np.array([b_i.value[0] for b_i in b])
obj_value = np.dot(b_hat, mean) * (b_hat.T @ varcov @ b_hat)**(-1)

print("Optimized b:", b_hat)
print("Optimized Objective Value:", obj_value)