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



'''
SIMPLE 2 PARAMETERS CASE
'''
# mean1 = mean[0]
# mean2 = mean[1]

# var1 = varcov[0][0]
# cov = varcov[1][0]
# var2 = varcov[1][1]

# m = GEKKO(remote=False)
# # Variables (in matrix form)
# b1 = m.Var(value=0.1, lb=0, ub=1)
# b2 = m.Var(value=0.1, lb=0, ub=1)
# # Constraint in matrix form
# m.Equation(b1 + b2 == 1)

# obj = (b1*mean1 + b2*mean2) / (b1**2*var1 + 2*b1*b2*cov + b2**2*var2)
# m.Minimize(-obj)
# m.solve(disp=False)

# b_hat = [b1.value[0], b2.value[0]]
# obj_value = (b1.value[0]*mean1 + b2.value[0]*mean2) / (b1.value[0]**2*var1 + 2*b1.value[0]*b2.value[0]*cov + b2.value[0]**2*var2)

# print("Optimized b:", b_hat)
# print("Optimized Objective Value:", obj_value)


'''
MATRIX FORM
'''
m = GEKKO(remote=False)
# Variables (in matrix form)
b = m.Array(m.Var, len(mean), value=0.1, lb=0, ub=1)
# Constraint (in matrix form)
m.Equation(np.sum(b) == 1)

# obj = b*mean*(b*varcov*b).T
obj = np.dot(b, mean) * (b.T @ varcov @ b)**(-1)

m.Minimize(-obj)
m.solve(disp=False)

b_hat = np.array([b_i.value[0] for b_i in b])
obj_value = np.dot(b_hat, mean) * (b_hat.T @ varcov @ b_hat)**(-1)

print("Optimized b:", b_hat)
print("Optimized Objective Value:", obj_value)
print('Optimized Returns:', np.dot(b_hat, mean))
print('Optimized Risk:', (b_hat.T @ varcov @ b_hat))
