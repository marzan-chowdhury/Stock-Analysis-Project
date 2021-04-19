import yfinance as yf
import datetime as dt 
from pandas_datareader import data
import matplotlib.pyplot as plt

class Stock: 


    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        self.stock_ticker =  stock_ticker
        self.stock_prices = stock_prices
        self.start_date = start_date
        self.end_date = end_date
    
    def get_stock(self): 
        return self.stock_ticker
    
    def get_start_date(self): 
        return self.start_date 

    def get_end_date(self): 
        return self.end_date 

    def ticker_data(self): 
        
        # Return the stock information with the provided dates given 

        start_date = self.start_date
        end_date = self.end_date

        user_ticker_symbol = self.stock_ticker

        df = data.DataReader(user_ticker_symbol, 'yahoo', start_date, end_date)
        #cols = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close')
        #df.reindex(columns=cols)
        #return df.head(15)
        return df

    def list_of_stocks_data(self, stocks_list): 
        
        # Return the stock information with the provided dates given 

        start_date = self.start_date
        end_date = self.end_date

        df = data.DataReader(stocks_list, 'yahoo', start_date, end_date)
        #cols = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close')
        #df.reindex(columns=cols)
        #return df.head(15)
        return df

    def example(self, start, end): 

        # Remove this method as this is displayinhg the info in a graph
        # Most likely be used in another class 
        stock_data = self.ticker_data(start, end)
        closing_price = stock_data['Adj Close']
        closing_price.plot()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Adjusted Closing Price')
        plt.show()

    def present_stock_data(self): 

        # Present the stock data in a DataFrame 
        start = self.start_date
        end = self.end_date
        stock_data = self.ticker_data()
        return stock_data.head(15) 

    def set_start_date(self, start_year, start_month, start_day): 
        
        #Return the date in a format that is accepted by python 

        start_year = start_year
        start_month = start_month 
        start_day = start_day
        
        self.start_date = dt.datetime(start_year, start_month, start_day)

        #return start_date
    
    def set_end_date(self, end_year, end_month, end_day): 

        #Return the date in a format that is accepted by python 

        end_year = end_year
        end_month = end_month 
        end_day = end_day

        self.end_date = dt.datetime(end_year, end_month, end_day)
        #return end_date 
    
    def convert_start_date(self): 

        start_date_obj = dt.datetime.strptime(self.start_date, '%d/%m/%y')
        return start_date_obj

    def convert_end_date(self): 

        end_date_obj = dt.datetime.strptime(self.end_date, '%d/%m/%y')
        return end_date_obj
        
# symbol = ["GME", "TSLA", "MSFT"]
# stock_list = Stock(symbol, "22/01/2020", "29/03/2021")
# print(stock_list.get_start_date())
# print(stock_list.ticker_data())

#symbols = "GME"
# #symbols = ["GME", "TSLA", "MSFT"]
# symbols = ["TSLA"]
# stock_list = Stock(symbols)
# #start = dt.datetime(2021,2,18)
# #end = dt.datetime(2021,3,19) 
# # start = stock_list.start_date(2021,2,18)
# # end = stock_list.end_date(2021,3,11)

# stock_list.set_start_date(2021,3,19)
# stock_list.set_end_date(2021,3,22)
# start = stock_list.get_start_date()
# end = stock_list.get_end_date()

# #print(stock_list.ticker_data(start, end))
# #print(stock_list.present_stock_data(start, end))
# print(stock_list.present_stock_data(start, end)) #Remove this line of code as it isnt needed for this part and uncomment line 75