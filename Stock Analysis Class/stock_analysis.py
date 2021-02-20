import yfinance as yf
import datetime as dt 
from pandas_datareader import data

class Stock: 

    def __init__(self, stock_ticker):
        self.stock_ticker =  stock_ticker

    # def get_ticker(self): 
    #     user_ticker_symbol = self.stock_ticker
    #     ticker_symbol = yf.Ticker(user_ticker_symbol)
    #     return ticker_symbol

    def ticker_data(self, start, end): 
        
        #start_date = dt.datetime(start)
        #end_date = dt.datetime(end)

        start_date = start
        end_date = end

        user_ticker_symbol = self.stock_ticker
        ticker_symbol = yf.Ticker(user_ticker_symbol)

        df = data.DataReader(user_ticker_symbol, 'yahoo', start_date, end_date)
        return df.head()

    def start_end_data(self, start, end): 
        start_date = dt.datetime(start)
        end_date = dt.datetime(end)

microsoft = Stock('msft')
start = dt.datetime(2021,2,18)
end = dt.datetime(2021,3,19) 
print(microsoft.ticker_data(start, end))


