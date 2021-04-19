from stock_analysis import Stock
from datetime import datetime, timedelta
import datetime as dt
import dateutil.relativedelta
from pandas_datareader import data
import yfinance as yf

class Analysis(Stock): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date, name):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)
        self.name = name

    def talk(self):
        print(self.name, "its working")
    
    def stock_one_day_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%Y-%m-%d")
        
        today = datetime.now().strftime("%d/%m/%Y")
        print("Todays date: ", today)
        yesterday = datetime.now() - timedelta(1)
        # yesterday = today - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        print("yesterdays date:", yesterday) 
        df = data.DataReader(ticker_symbol, 'yahoo', yesterday, todays_date)
        return df

    def stock_one_day_2_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Todays date: ", today)
        yesterday = datetime.now() - timedelta(1)
        # yesterday = today - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Yesterday date:", yesterday) 
        df = data.DataReader(ticker_symbol, 'yahoo', yesterday, todays_date)
        return df
    
    def stock_one_week_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Todays date: ", today)
        last_week = datetime.now() - timedelta(7)
        # yesterday = today - datetime.timedelta(days=1)
        last_week = last_week.strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Last week date:", last_week) 
        df = data.DataReader(ticker_symbol, 'yahoo', last_week, today)
        return df
    
    def stock_one_month_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now().strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Todays date: ", today)
        last_month = datetime.now() - timedelta(31)
        # yesterday = today - datetime.timedelta(days=1)
        last_month = last_month.strftime("%Y-%m-%d")#("%d/%m/%Y")
        print("Last month date:", last_month) 
        df = data.DataReader(ticker_symbol, 'yahoo', last_month, todays_date)
        return df
    
    def stock_six_month_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now()
        six_months_ago = today - dateutil.relativedelta.relativedelta(months=6)

        print("Todays date: ", today)
        print("Six moths ago month: ", six_months_ago)

        df = data.DataReader(ticker_symbol, 'yahoo', six_months_ago, todays_date)
        return df
    
    def stock_ytd_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        today = datetime.now()
        current_year = today.year
        print("This year is: ", today.year)

        ytd_start = dt.datetime(current_year, 1, 1)
        ytd_start = ytd_start.strftime("%d/%m/%Y")
        print("YTD STARTS: ", ytd_start)

        df = data.DataReader(ticker_symbol, 'yahoo', ytd_start, todays_date)
        return df

    def stock_one_year_data(self, ticker_symbol):     

        todays_date = datetime.now().strftime("%d/%m/%Y")
        
        today = datetime.now()
        one_year_ago = today - dateutil.relativedelta.relativedelta(months=12)

        print("Todays date: ", today)
        print("One Year Ago: ", one_year_ago)

        df = data.DataReader(ticker_symbol, 'yahoo', one_year_ago, todays_date)
        return df
    
    def todays_data(self, end_date): 
        # Return the stock information with the provided dates given
        user_ticker_symbol = self.stock_ticker
        print("end date: ", end_date)
        df = data.DataReader(user_ticker_symbol, 'yahoo', end_date)
        print("Dataframe:" ,df)
        return df

    def simple_rate_return_1(self, starting_price): 
  
        todays_date = datetime.now() - timedelta(3)#.strftime("%Y-%m-%d")
        todays_date = todays_date.strftime("%Y-%m-%d")
        #print("Current Date: ", current_date)
        recent_df = self.todays_data(todays_date) 
        #print("Current dataframe: ", recent_df) 
        todays_closing_price = recent_df['Close']
        #df = recent_df['Adj Close'].to_frame().reset_index()

        #todays_closing_price = df.loc[:,'Adj Close']
        todays_closing_price = recent_df.loc[:,'Adj Close']
        print("Todays closing price: ", todays_closing_price)
        test = todays_closing_price.iloc[-1]
        todays_closing_price = test
        print("test: ", test)
        #print(df)
        print("Todays closing price is: ", todays_closing_price)
        print(starting_price)
        simple_rate_return_1 = ((todays_closing_price - starting_price) / starting_price) * 100
        print("returns  = ", simple_rate_return_1)
        return simple_rate_return_1

    def simple_rate_return(self): 
        
        stock_prices = self.stock_prices
        todays_date = datetime.now() - timedelta(3)#.strftime("%Y-%m-%d")
        todays_date = todays_date.strftime("%Y-%m-%d")
        #print("Current Date: ", current_date)
        recent_df = self.todays_data(todays_date) 
        #print("Current dataframe: ", recent_df) 
        todays_closing_price = recent_df['Close']
        #df = recent_df['Adj Close'].to_frame().reset_index()

        #todays_closing_price = df.loc[:,'Adj Close']
        todays_closing_price = recent_df.loc[:,'Adj Close']
        print("Todays closing price: ", todays_closing_price)
        test = todays_closing_price.iloc[-1]
        todays_closing_price = test
        print("test: ", test)
        #print(df)
        print("Todays closing price is: ", todays_closing_price)
        print(stock_prices)
        simple_rate_return_1 = ((todays_closing_price - stock_prices) / stock_prices) * 100
        print("returns  = ", simple_rate_return_1)
        return simple_rate_return_1

    def portfolio_simple_rate_return(self):
        
        portfolio_prices = self.stock_prices
        simple_return_assets = self.simple_rate_return_1(portfolio_prices)
        simple_return_assets = simple_return_assets.values.tolist()
        print("simple return: ", simple_return_assets)
        wieghts_of_assets = self.weights_of_portfolio()

        portfolio_return = 0 

        for i, j in zip(simple_return_assets, wieghts_of_assets):
            #print("returns: ", i)
            #for j in wieghts_of_assets: 
                #print("weights: ", j)
            portfolio_return += i * j 
                
        
        print("Portfolio return: ", portfolio_return)
        

    def weights_of_portfolio(self): 

        list_of_stocks = self.stock_ticker 
        list_of_stock_prices = self.stock_prices 

        number_of_stocks = 0 
        for stock in list_of_stocks:
            number_of_stocks += 1 
        print("Number of stokc in portfolio: ", number_of_stocks)

        total_weights = [] 

        total_invested = 0 
        for prices in list_of_stock_prices: 
            total_invested += prices 
        print("Total invested: ", total_invested)
        for prices in list_of_stock_prices:
            weight_asset = prices /  total_invested
            total_weights.append(weight_asset)
        print("Weights of assets: ", total_weights)
        
        return total_weights

    def daily_return(self): 

        current_stock = self.stock_ticker
        stock_data = self.stock_one_day_data(current_stock)
        print(stock_data)
        daily_returns = stock_data.loc[:,'Close']
        print(daily_returns)
        # test = daily_returns.iloc[-1]
        # test2 = daily_returns.iloc[-2]
        # todays_closing_price = test
        # yesterday_closing_price = test2
        x = daily_returns.pct_change() * 100
        print("Daily Returns: ", x)

    def daily_return_2(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_one_day_2_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_daily_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_daily_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        daily_per_change = ((closing_daily_price - opening_daily_price) / opening_daily_price) * 100
        print("Daily return: ", daily_per_change)

        # x = closing_prices.pct_change() * 100
        # print("Daily Returns: ", x)
    
    def weekly_return(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_one_week_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        weekly_per_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("Weekly return: ", weekly_per_change)

        x = closing_prices.pct_change() * 100
        #print("Daily Returns: ", x)
    
    def monthly_return(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_one_month_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        weekly_per_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("Monthly return: ", weekly_per_change)

        #x = closing_prices.pct_change() * 100
        #print("Daily Returns: ", x)

    def six_month_return(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_six_month_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        six_month_per_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("6 Months return: ", six_month_per_change)

        #x = closing_prices.pct_change() * 100
        #print("Daily Returns: ", x)

    def ytd_return(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_ytd_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        yearly_per_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("YTD return: ", yearly_per_change)

        #x = closing_prices.pct_change() * 100
        #print("Daily Returns: ", x)

    def one_year_return(self): 

        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_one_year_data(current_stock)
        print(stock_data)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        yearly_per_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("YTD return: ", yearly_per_change)

        #x = closing_prices.pct_change() * 100
        #print("Daily Returns: ", x)
    



#testing inheritance
# stocks = ['TSLA']

# symbol = ["GME", "TSLA", "MSFT"]
# stock_list = Stock('TSLA', "29/03/2021", "29/03/2021")


# object_0 =  Analysis('TSLA', "14/04/2021", "14/04/2021", 'marzan')
# object_1 =  Analysis('AAPL', "14/04/2021", "14/04/2021", 'marzan')
# object_2 =  Analysis('MSFT', "14/04/2021", "14/04/2021", 'marzan')


# empty_list = [object_0, object_1, object_2]

# for obj in empty_list:
#      print(obj.stock_ticker)
start = '2021-04-07'
end = '2021-04-08'
# start = '07/04/2021'
# end = '08/04/2021'
#works with a list of stocks!
list_stocks = ['TSLA', 'AAPL']
prices_of_stocks = [500, 100]
#x = Analysis('TSLA', start, end, 'MARZAN')
x = Analysis(list_stocks, prices_of_stocks, start, end, 'MARZAN')
#using the parent methods to test if it works
#print(x.ticker_data())
# x.talk()
# print("***************************")
# print(x.get_start_date())
# print("***************************")
# print(x.ticker_data())
# print("***************************")

# simp_return = x.simple_rate_return(prices_of_stocks)

simp_return = x.simple_rate_return()
print("Returns: ", simp_return)
# print("***************************")

# x.daily_return_2()
# print("***************************")
# x.weekly_return()
# print("***************************")
# x.monthly_return()
# print("***************************")
# x.six_month_return()
# print("***************************")
# x.one_year_return()
# print("***************************")
# x.ytd_return()
# print("***************************")
# x.weights_of_portfolio()

print("***************************")
x.portfolio_simple_rate_return()



# start = x.get_start_date()
# end = x.get_end_date()

# x.present_stock_data()


