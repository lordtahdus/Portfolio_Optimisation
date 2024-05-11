import yfinance as yf
import numpy as np
import pandas as pd
import ast
from typing import List

def retrieve_history(codes: List, period, interval, start=None, end=None) -> dict:
    stock_history = {}
    for code in codes:
        data = yf.Ticker(code).history(period, interval, start, end)
        # add return
        # data['Return'] = (data['Close'] - data['Open']) / data['Open'] * 100
        data['Return'] = (data['Close'] - data['Open']) / data['Open'] * 100
        data['Log_Return'] = np.log(data['Close'] / data['Close'].shift(1))
        # drop unnecessary cols
        data.drop(['Dividends', 'Stock Splits'], axis=1)
        stock_history[code[:-3]] = data
    return stock_history


if __name__ == '__main__':

    """============= INPUT PARAMETERS =============="""

    period = '3y'
    interval = '1d'
    start = '2021-04-16'
    end = '2024-05-11'
    comp_list = pd.read_csv('ETC3460/asm2/best_portfolio.csv')
    
    """============================================="""

    # transform to right format
    comp_list = list(
        ast.literal_eval(comp_list['Combination'][0])
    )
    yahoo_code = [code + ".AX" for code in comp_list]

    # retrieve
    stock_history = retrieve_history(yahoo_code, period, interval, start, end)
    # store the returns of stocks
    returns_data = pd.concat(
        [data['Log_Return'] for data in stock_history.values()], 
        axis=1, keys=stock_history.keys()
    )
    returns_data.to_csv('ETC3460/asm2/holdingperiod_log_returns.csv')



