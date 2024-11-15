import yfinance as yf
import numpy as np
import pandas as pd
from typing import List

# y = yf.Ticker("BHP.AX").history(period="1y", interval='1wk')
# y['Pct_change'] = (y['Close'] - y['Open']) / y['Open'] * 100
# print(y.drop('Open', axis=1))


# tickers = yf.Tickers('msft aapl')
# print(tickers.history(period="1y", interval='1wk'))

def retrieve_history(codes: List, period, interval) -> dict:
    stock_history = {}
    for code in codes:
        data = yf.Ticker(code).history(period, interval)
        # add return
        # data['Return'] = (data['Close'] - data['Open']) / data['Open'] * 100
        data['Return'] = (data['Close'] - data['Open']) / data['Open'] * 100
        data['Log_Return'] = np.log(data['Close'][1:] / data['Close'][:-1])
        # drop unnecessary cols
        data.drop(['Dividends', 'Stock Splits'], axis=1)
        stock_history[code] = data
    return stock_history


def get_mean_varcov(stock_history: dict):
    """
    Input orginal stock historical data
    dof = n-1
    """
    returns_data = pd.concat(
        [data['Return'] for data in stock_history.values()], 
        axis=1, keys=stock_history.keys()
    )
    mean = returns_data.mean()
    varcov = returns_data.cov()
    return mean, varcov





if __name__ == '__main__':
    # stock_history = retrieve_history(['MSFT', 'AAPL'], '1mo', '1wk')    
    # print(get_mean_varcov(stock_history))

    period = '1y'
    interval = '1wk'
    asx200_list = pd.read_csv('assets/ASX200_companies_list.csv')

    stock_history = retrieve_history(asx200_list['Yahoo Code'][[0,3]], period, interval)
    mean_returns, varcov_returns = get_mean_varcov(stock_history)

    # store the returns of stocks
    returns_data = pd.concat(
        [data['Return'] for data in stock_history.values()], 
        axis=1, keys=stock_history.keys()
    )
    returns_data.to_csv('simple_opt/stock_returns.csv')


