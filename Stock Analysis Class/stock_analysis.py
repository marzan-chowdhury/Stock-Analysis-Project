import yfinance as yf
import datetime as dt 
from pandas_datareader import data

class Stock: 

    def __init__(self, stock_ticker):
        self.stock_ticker =  stock_ticker

    def ticker_data(self, start, end): 
        
        # Return the stock information with the provided dates given 

        start_date = start
        end_date = end

        user_ticker_symbol = self.stock_ticker

        df = data.DataReader(user_ticker_symbol, 'yahoo', start_date, end_date)
        #return df.head(15)
        return df

    def present_stock_data(self, start, end): 

        # Present the stock data in a DataFrame 

        stock_data = self.ticker_data(start, end)
        return stock_data.head(15) 

    def start_date(self, start_year, start_month, start_day): 
        
        #Return the date in a format that is accepted by python 

        start_year = start_year
        start_month = start_month 
        start_day = start_day
        
        start_date = dt.datetime(start_year, start_month, start_day)

        return start_date
    
    def end_date(self, end_year, end_month, end_day): 

        #Return the date in a format that is accepted by python 

        end_year = end_year
        end_month = end_month 
        end_day = end_day

        end_date = dt.datetime(end_year, end_month, end_day)

        return end_date 


symbols = ["MSFT","INTC", "AMZN", "EBAY", "AAPL", "GOOG", "FB", "TSLA", "GE"]
stock_list = Stock(symbols)
#start = dt.datetime(2021,2,18)
#end = dt.datetime(2021,3,19) 
start = stock_list.start_date(2021,2,18)
end = stock_list.end_date(2021,3,5)
#print(stock_list.ticker_data(start, end))
print(stock_list.present_stock_data(start, end))


