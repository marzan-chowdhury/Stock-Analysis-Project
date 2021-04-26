import yfinance as yf
import datetime as dt 
from pandas_datareader import data
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from datetime import datetime, timedelta
import dateutil.relativedelta

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
    def stock_one_day_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%Y-%m-%d")
        
        today = datetime.now().strftime("%d/%m/%Y")
        #print("Todays date: ", today)
        yesterday = datetime.now() - timedelta(1)
        # yesterday = today - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        #print("yesterdays date:", yesterday) 
        df = data.DataReader(ticker_symbol, 'yahoo', yesterday, todays_date)
        return df

    def stock_one_day_2_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Todays date: ", today)
        yesterday = datetime.now() - timedelta(1)
        # yesterday = today - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Yesterday date:", yesterday) 
        df = data.DataReader(ticker_symbol, 'yahoo', yesterday, todays_date)
        return df
    
    def stock_one_week_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Todays date: ", today)
        last_week = datetime.now() - timedelta(7)
        # yesterday = today - datetime.timedelta(days=1)
        last_week = last_week.strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Last week date:", last_week) 
        df = data.DataReader(ticker_symbol, 'yahoo', last_week, today)
        return df
    
    def stock_one_month_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Todays date: ", today)
        last_month = datetime.now() - timedelta(31)
        # yesterday = today - datetime.timedelta(days=1)
        last_month = last_month.strftime("%Y-%m-%d")#("%d/%m/%Y")
        #print("Last month date:", last_month) 
        df = data.DataReader(ticker_symbol, 'yahoo', last_month, todays_date)
        return df
    
    def stock_six_month_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now()
        six_months_ago = today - dateutil.relativedelta.relativedelta(months=6)

        #print("Todays date: ", today)
        #print("Six moths ago month: ", six_months_ago)

        df = data.DataReader(ticker_symbol, 'yahoo', six_months_ago, todays_date)
        return df
    
    def stock_ytd_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        today = datetime.now()
        current_year = today.year
        #print("This year is: ", today.year)

        ytd_start = dt.datetime(current_year, 1, 1)
        ytd_start = ytd_start.strftime("%d/%m/%Y")
        #print("YTD STARTS: ", ytd_start)

        df = data.DataReader(ticker_symbol, 'yahoo', ytd_start, todays_date)
        return df

    def stock_one_year_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now()
        one_year_ago = today - dateutil.relativedelta.relativedelta(months=12)

        #print("Todays date: ", today)
        #print("One Year Ago: ", one_year_ago)

        df = data.DataReader(ticker_symbol, 'yahoo', one_year_ago, todays_date)
        return df
    
    def stock_five_year_data(self, ticker_symbol): 

        todays_date = datetime.now().strftime("%d/%m/%Y")
        today = datetime.now()
        five_years_ago = today - dateutil.relativedelta.relativedelta(years=5)

        df = data.DataReader(ticker_symbol, 'yahoo', five_years_ago, todays_date)
        #only return the closing price of the stock 
        df = df.loc[:,'Adj Close']
        return df

    def todays_data(self, end_date): 
        # Return the stock information with the provided dates given

        user_ticker_symbol = self.stock_ticker
        todays_date = datetime.now().strftime("%d/%m/%Y")
        today = datetime.now()
        five_years_ago = today - dateutil.relativedelta.relativedelta(years=5)
        print("end date: ", end_date)
        df = data.DataReader(user_ticker_symbol, 'yahoo', five_years_ago, todays_date)
        print("Dataframe:" ,df)
        return df
    
    def todays_data_copy(self): 
        # Return the stock information with the provided dates given

        user_ticker_symbol = self.stock_ticker
        todays_date = datetime.now().strftime("%d/%m/%Y")
        today = datetime.now()
        five_years_ago = today - dateutil.relativedelta.relativedelta(years=5)
        df = data.DataReader(user_ticker_symbol, 'yahoo', five_years_ago, todays_date)
        print("Dataframe:" ,df)
        return df

    
    # def todays_data(self, end_date): 
    #     # Return the stock information with the provided dates given
    #     user_ticker_symbol = self.stock_ticker
    #     #print("end date: ", end_date)
    #     df = data.DataReader(user_ticker_symbol, 'yahoo', end_date)
    #     #print("Dataframe:" ,df)
    #     return df
#------------------------------------------------------------------------------
# -------------------------Co-variance matrix----------------------------------    
    def ticker_symbols(self): 
        #array to store prices
        symbols = []
        symbols_list = self.stock_ticker
        #print("stock list: ", symbols_list)
        start = self.start_date
        for ticker in symbols_list:     
            #r = web.DataReader(ticker, 'yahoo', start)  
            stock_dataframe =  data.DataReader(ticker, 'yahoo', start)
            #stock_dataframe = self.ticker_data_1()
            stock_dataframe['Symbol'] = ticker    
            symbols.append(stock_dataframe)
        return symbols

    def clean_data(self): 
        
        symbols = self.ticker_symbols()
        df = pd.concat(symbols)
        df = df.reset_index()
        df = df[['Date', 'Close', 'Symbol']]
        #df.head()
        df_pivot = df.pivot('Date','Symbol','Close').reset_index()
        print("****************************")
        df_pivot.head()

        return df_pivot

    def correlation_data(self): 

        df_pivot = self.clean_data()
        corr_df = df_pivot.corr(method='pearson')

        corr_df.head().reset_index()
        corr_df.head()
        # print("corr_df")
        # print(corr_df)
        return corr_df
#------------------------------------------------------------------------------

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