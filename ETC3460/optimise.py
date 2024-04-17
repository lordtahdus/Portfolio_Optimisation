import yfinance as yf
import numpy as np
import pandas as pd
import itertools
import csv

from typing import List
from gekko import GEKKO


stock_returns = pd.read_csv('ETC3460\stock_log_returns.csv', index_col='Date')
# 6 industries with 3 stocks each
industries = {
    'Financials': ['SUN', 'WBC', 'CBA'],
    'Real Estate': ['BWP', 'GPT', 'MGR'],
    'Information Technology': ['CPU', 'XRO', 'WTC'],
    'Energy': ['STO', 'VEA', 'WDS'],
    'Health Care': ['SHL', 'FPH', 'CSL'],
    'Consumer Staples': ['TWE', 'GNC', 'WOW']
}   
combinations = list(itertools.product(*industries.values()))

# industries = {
#     'Financials': ['SUN', 'WBC'],
#     'Real Estate': ['BWP']
# }

# Generate all combinations of selecting one stock from each industry



# mean = np.array(stock_returns.mean()) # vector of means of returns
# varcov = np.array(stock_returns.cov()) # Var-cov matrix

# print(mean)
# print(varcov)


'''
Testing
'''

# selected_stocks = ['SUN', 'BWP']

# mean = np.array(stock_returns[selected_stocks].mean())
# varcov = np.array(stock_returns[selected_stocks].cov())

# m = GEKKO(remote=False)
# # Variables (in matrix form)
# b = m.Array(m.Var, len(mean), value=0.1, lb=0.1, ub=1)
# # Constraint (in matrix form)
# m.Equation(np.sum(b) == 1)

# # Return per risk: Expected log returns / Variance log returns
# # obj = b*mean*(b*varcov*b).T
# obj = np.dot(b, mean) * (b.T @ varcov @ b)**(-1)

# m.Minimize(-obj)
# m.solve(disp=False)

# b_hat = np.array([b_i.value[0] for b_i in b])
# obj_value = np.dot(b_hat, mean) * (b_hat.T @ varcov @ b_hat)**(-1)

# print("Optimized b:", list(b_hat))
# print("Optimized Objective Value:", obj_value)
# print('Optimized Returns:', np.dot(b_hat, mean))
# print('Optimized Risk:', (b_hat.T @ varcov @ b_hat))



"""
Real stuffs
"""

results = []

# Loop through each combination and optimize
for combination in combinations:
    # Extract stocks from this combination
    selected_stocks = list(combination)
    # Calculate mean and varcov matrix for selected stocks
    mean = np.array(stock_returns[selected_stocks].mean())
    varcov = np.array(stock_returns[selected_stocks].cov())

    # Optimization with GEKKO
    m = GEKKO(remote=False)
    b = m.Array(m.Var, len(mean), value=0.1, lb=0.1, ub=1)
    m.Equation(np.sum(b) == 1)
    obj = np.dot(b, mean) * (b.T @ varcov @ b)**(-1)
    m.Minimize(-obj)
    m.solve(disp=False)
    
    # Retrieve optimized weights
    b_hat = np.array([b_i.value[0] for b_i in b])
    # Calculate objective value
    obj_value = np.dot(b_hat, mean) * (b_hat.T @ varcov @ b_hat)**(-1)

    results.append({
        'Combination': combination,
        'Optimized_b': list(b_hat),
        "Optimized_Objective": obj_value,
        'Optimized_Returns': np.dot(b_hat, mean),
        'Minimum_Variance': (b_hat.T @ varcov @ b_hat)
    })

# Write results to a file
# with open('portfolio_optimization_results.txt', 'w') as f:
#     for result in results:
#         f.write(f"Combination: {result['Combination']}\n")
#         f.write(f"Optimized_b: {result['Optimized_b']}\n")
#         f.write(f"Optimized Objective: {result['Optimized_Objective']}\n")
#         f.write(f"Optimized Returns: {result['Optimized_Returns']}\n")
#         f.write(f"Minimum Variance: {result['Minimum_Variance']}\n\n")


# Write results to a CSV file
with open('ETC3460/portfolio_optimization_results.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'Combination', 'Optimized_b', 'Optimized_Objective', 
        'Optimized_Returns', 'Minimum_Variance'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for result in results:
        writer.writerow({
            'Combination': result['Combination'],
            'Optimized_b': result['Optimized_b'],
            'Optimized_Objective': result['Optimized_Objective'],
            'Optimized_Returns': result['Optimized_Returns'],
            'Minimum_Variance': result['Minimum_Variance']
        })