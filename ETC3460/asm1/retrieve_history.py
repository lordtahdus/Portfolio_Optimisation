import yfinance as yf
import numpy as np
import pandas as pd
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
    today = pd.to_datetime('2024-04-16')
    comp_list = pd.read_csv('ETC3460/companies_list.csv')
    
    """============================================="""

    # start_time = today - pd.Timedelta(days = 4*7)
    end_time = today
    # start_time = str(start_time) + '+00:00'
    end_time = str(end_time) + '+00:00'

    stock_history = retrieve_history(comp_list['Yahoo Code'], period, interval, start_time, end_time)
    # store the returns of stocks
    returns_data = pd.concat(
        [data['Log_Return'] for data in stock_history.values()], 
        axis=1, keys=stock_history.keys()
    )
    returns_data.to_csv('ETC3460/stock_log_returns.csv')



