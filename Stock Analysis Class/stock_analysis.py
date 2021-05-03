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
        df_pivot = df.pivot('Date','Symbol','Close').reset_index()
        df_pivot.head()

        return df_pivot

    def correlation_data(self): 

        df_pivot = self.clean_data()
        corr_df = df_pivot.corr(method='pearson')

        corr_df.head().reset_index()
        corr_df.head()
        return corr_df
#------------------------------------------------------------------------------
    def flatten_list(self, _2d_list):
        flat_list = []
        # Iterate through the outer list
        for element in _2d_list:
            if type(element) is list:
                # If the element is of type list, iterate through the sublist
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list
#------------------------------------------------------------------------------
# -------------------------Portfolio Optimization Class---------------------------------- 
    def quarterly_mean(self): 

        simple_rate_of_return = self.simple_rate_of_return()
        quarterly_mean = simple_rate_of_return.mean()

        return quarterly_mean

    def expected_5_year_return(self): 
        #get the stocks
        stock_list = self.stock_ticker
        # #get the 5 year data for the stocks 
        # stock_five_year_data = self.stock_five_year_data(stock_list)
        # #get the yeraly returns of the stocks in the portfolio
        # yearly_returns = self.yearly_stock_return(stock_list)
        #calculate the mean for each stock (mean is representing the expected return) and store this in a list
        mean_in_portfolio = self.expected_return(stock_list)
        #we now have a list of expected returns which will be used to calculate the portfolio expected return
        print("mean in the portfolio: ", mean_in_portfolio)
        return mean_in_portfolio
        #print("yearly returns: ", yearly_returns)
        
    def expected_return(self, stock): 
        
        #expected return can be calculated from using the mean 
        yearly_returns = self.yearly_stock_return(stock)
        #using the mean method, we can calculate the mean in the datafram by specifying which column to use
        mean = yearly_returns.mean(axis=0)
        print("Yearly mean: ", mean)
        return mean
    
    def yearly_stock_return(self, ticker_symbol): 
        
        #over a 5 year period: 

        stock_five_year_data = self.stock_five_year_data(ticker_symbol)
        #stock_five_year_returns = stock_five_year_data['Adj Close'].pct_change()
        #get the annual return of the stock over the previous 5 years
        stock_five_year_returns = stock_five_year_data.resample('Y').ffill().pct_change() 


        #print("Yearly Returns: ", stock_five_year_returns)
        return stock_five_year_returns

    def covariance_stocks_simple_returns(self): 
        #get the simple rate of return 
        simple_rate_return = self.simple_rate_of_return()
        covariance = simple_rate_return.cov()
        return covariance   
    
    def simple_rate_of_return(self): 

        list_of_stocks = self.stock_ticker
        stock_five_year_data = self.stock_five_year_data(list_of_stocks)
        stock_data_adj_close = stock_five_year_data
        #refine the df to get the quarterly stock data over the previous 5 years  
        stock_data_adj_close  = stock_data_adj_close.resample('Q').last()

        simple_rate_of_return = stock_data_adj_close.pct_change()

        return simple_rate_of_return
#-----------------------------------------------------------------------------------------------------------

    def list_of_stocks_data(self, stocks_list): 
        
        # Return the stock information with the provided dates given 

        start_date = self.start_date
        end_date = self.end_date

        df = data.DataReader(stocks_list, 'yahoo', start_date, end_date)
        #cols = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close')
        #df.reindex(columns=cols)
        #return df.head(15)
        return df

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