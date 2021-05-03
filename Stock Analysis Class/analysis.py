from stock_analysis import Stock
from datetime import datetime, timedelta
import datetime as dt
import dateutil.relativedelta
from pandas_datareader import data
import yfinance as yf
import numpy as np
import math

class Analysis(Stock): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)

#-----------------------------------------------------------------

#--------does the same as the simple_rate_return function---------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
    def simple_daily_rate_return(self): 
        starting_price = self.stock_prices
        todays_date = datetime.now() - timedelta(1)#.strftime("%Y-%m-%d")
        todays_date = todays_date.strftime("%Y-%m-%d")
        #print("Current Date: ", current_date)
        recent_df = self.todays_data(todays_date) 
        #print("Current dataframe: ", recent_df) 
        todays_closing_price = recent_df['Close']
        #df = recent_df['Adj Close'].to_frame().reset_index()

        #todays_closing_price = df.loc[:,'Adj Close']
        todays_closing_price = recent_df.loc[:,'Adj Close']
        #print("Todays closing price: ", todays_closing_price)
        test = todays_closing_price.iloc[-1]
        todays_closing_price = test
        #print("test: ", test)
        #print(df)
        #print("Todays closing price is: ", todays_closing_price)
        #print(starting_price)
        simple_rate_return_1 = ((todays_closing_price - starting_price) / starting_price) * 100
        #print("returns  = ", simple_rate_return_1)
        return simple_rate_return_1
#-----------------------------------------------------------------------------------------------------#

    # def simple_rate_return(self): 
        
    #     #get the price the stock was bought at
    #     stock_prices = self.stock_prices
    #     todays_date = datetime.now() - timedelta(1)#.strftime("%Y-%m-%d")
    #     todays_date = todays_date.strftime("%Y-%m-%d")
    #     recent_df = self.todays_data(todays_date) 
    #     todays_closing_price = recent_df['Close']

    #     todays_closing_price = recent_df.loc[:,'Adj Close']
    #     #print("Todays closing price: ", todays_closing_price)
    #     test = todays_closing_price.iloc[-1]
    #     todays_closing_price = test
    #     #print("test: ", test)
    #     #print(df)
    #     #print("Todays closing price is: ", todays_closing_price)
    #     #print(stock_prices)
    #     simple_rate_return_1 = ((todays_closing_price - stock_prices) / stock_prices) * 100
    #     #print("returns  = ", simple_rate_return_1)
    #     return simple_rate_return_1

#get the expected return of one stock
#based on the 5 year annual return history
    def expected_return(self, stock): 
        
        #expected return can be calculated from using the mean 
        yearly_returns = self.yearly_stock_return(stock)
        #using the mean method, we can calculate the mean in the datafram by specifying which column to use
        mean = yearly_returns.mean(axis=0)
        print("Yearly mean: ", mean)
        return mean
    
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
#------------------------------------------------------------------------------------------------------------------------------#
# This function will return the expected return of the portfolio                                                               #                               
# The expcetd return is based off using the annual return of the stock                                                         #
# we get the last 5 years annual return and multiply it by the weight the asset holds in the portfolio                         #
#------------------------------------------------------------------------------------------------------------------------------#  
    def expected_portfolio_return(self): 
        
        expected_portfolio_return = 0 
        #get the weight of each asset in the portfolio 
        weights_of_assets = self.weights_of_portfolio()
        #get the expected return of each asset in the portfolio 
        assets_expected_return = self.expected_5_year_return()

        #loop through both lists together (using zip)
        #multiply each weight against the expected return 
        for i, j in zip(assets_expected_return, weights_of_assets):
            expected_portfolio_return += i * j 
        expected_portfolio_return = str(round(expected_portfolio_return, 2)) + '%'
        print("The expected returns for the portfolio is: ", expected_portfolio_return)
#------------------------------------------------------------------------------------------------------------------------------#
# This function will return the expected return of the portfolio using the quarterly price changes over the last 5 years       #                               
# we get the last 5 years of quarterly price changes and multiply it by the weight the asset holds in the portfolio            #
# This will return the quarterly portfolio return                                                                              #
#------------------------------------------------------------------------------------------------------------------------------#  
    def expected_quarterly_portfolio_return(self): 
        weights_in_portfolio = self.weights_of_portfolio()
        expected_ror = self.expected_return_ror()
        expected_ror = expected_ror.values.tolist()
        quarterly_portfolio_return = 0
        for i,j in zip(expected_ror, weights_in_portfolio): 
            quarterly_portfolio_return += i * j 
        print(quarterly_portfolio_return)
        return quarterly_portfolio_return * 100

#------------------------------------------------------------------------------------------------------------------------------#
# This function will return the exp[ected return of each stock in the portfolio                                                #                               
# The expcetd return is based off using the simple rate of return                                                              #
# The simple rate of return uses the last 5 year data of the stock and calculates the percentage change in prices qurterly     #                                                     
#------------------------------------------------------------------------------------------------------------------------------#
    def expected_return_ror(self): 
        simple_rate_of_return = self.simple_rate_of_return()
        expected_ror = simple_rate_of_return.mean()
        #print("eRoR: ", expected_ror)
        return expected_ror
#------------------------------------------------------------------------------------------------------------------------------#
# This function will return the portfolio return                                                                               #
# The portfolio return is based on the the current price of the stocks in the portfolio against the prices they were bought at #
# The prices that the stock were bought at are provided in the constructor                                                     #
#------------------------------------------------------------------------------------------------------------------------------#
    def portfolio_return(self):
        
        portfolio_prices = self.stock_prices
        simple_return_assets = self.simple_daily_rate_return()#self.simple_rate_return()
        simple_return_assets = simple_return_assets.values.tolist()
        print("simple return: ", simple_return_assets)
        wieghts_of_assets = self.weights_of_portfolio()

        portfolio_return = 0 

        for i, j in zip(simple_return_assets, wieghts_of_assets):
            #print("returns: ", i)
            #for j in wieghts_of_assets: 
                #print("weights: ", j)
            portfolio_return += i * j 
                
        
        print("Portfolio return (right now): ", portfolio_return)
        return portfolio_return
        

    def weights_of_portfolio(self): 

        list_of_stocks = self.stock_ticker 
        list_of_stock_prices = self.stock_prices 

        number_of_stocks = 0 
        for stock in list_of_stocks:
            number_of_stocks += 1 
        print("Number of stock in portfolio: ", number_of_stocks)

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
    
    def yearly_stock_return(self, ticker_symbol): 
        
        #over a 5 year period: 

        stock_five_year_data = self.stock_five_year_data(ticker_symbol)
        #stock_five_year_returns = stock_five_year_data['Adj Close'].pct_change()
        #get the annual return of the stock over the previous 5 years
        stock_five_year_returns = stock_five_year_data.resample('Y').ffill().pct_change() 


        #print("Yearly Returns: ", stock_five_year_returns)
        return stock_five_year_returns

    
    def variance_of_individual_stock(self, ticker_symbol): 
        
        stock_five_year_data = self.stock_five_year_data(ticker_symbol)
        #stock_five_year_returns = stock_five_year_data['Adj Close'].pct_change()
        #get the annual return of the stock over the previous 5 years
        stock_five_year_returns = stock_five_year_data.resample('Y').ffill().pct_change()

        stock_return_list = stock_five_year_returns.values.tolist()
        #pop the first element of the list as it is recorded as 'Nan' which will output the wrong data
        stock_return_list.pop(0)
        print("list: ", stock_return_list)
        variance_of_stock = np.var(stock_return_list)

        print("Data: ", stock_five_year_data)
        print("Change: ", stock_five_year_returns)
        print("Variance: ", variance_of_stock)

        return variance_of_stock

    def standard_deviation_stock(self, ticker_symbol): 
        
        stock_five_year_data = self.stock_five_year_data(ticker_symbol)
        #stock_five_year_returns = stock_five_year_data['Adj Close'].pct_change()
        #get the annual return of the stock over the previous 5 years
        stock_five_year_returns = stock_five_year_data.resample('Y').ffill().pct_change()

        stock_return_list = stock_five_year_returns.values.tolist()
        #pop the first element of the list as it is recorded as 'Nan' which will output the wrong data
        stock_return_list.pop(0)
        #standard deviation of the stock based on the 5 year annual return
        std_stock = np.std(stock_return_list)

        print("STD Stock: ", std_stock)

        return std_stock
    
    def standard_deviation_portfolio(self): 

        #get the weights of the portfolio
        weights_in_portfolio = self.weights_of_portfolio()
        #print(weights_in_portfolio)

        #get the standard deviations of each stock in the portfolio: 

        #get list of stocks in the portfolio 
        stock_list = self.stock_ticker
        #create an empty list to store the std of each stock in the portfolio 
        std_in_portfolio = []
        #loop through each stock in the portfolio to get the individual std 
        for i in stock_list: 
            std_in_portfolio.append(self.standard_deviation_stock(i))
        # print("**************")
        # print("STD in portfolio: ", std_in_portfolio)
        # print("**********")
        # print(weights_in_portfolio)
        
        #create empty list to store the squared weights and squared standard deviations
        squared_weights = []
        squared_deviation = []
        #loop through the wights list and standard deviation list of the portfolio
        for i in weights_in_portfolio: 
            square = i ** 2
            squared_weights.append(square)
        #print("squared weights: ", squared_weights)
        for i in std_in_portfolio:
            square_std = i ** 2
            squared_deviation.append(square_std)
        #print("squared std: ", squared_deviation)

        #get the correlation of the stocks in the portfolio
        stocks_correlation = self.correlation_coefficient()
        #print(stocks_correlation)
        stocks_correlation = stocks_correlation.values.tolist() 
        #flatten the nested list into a single list
        flat_list = self.flatten_list(stocks_correlation)
        #get the average correlation of the portfolio 
        sum_flat_list = 0 
        length_flat_list = len(flat_list)
        for i in flat_list:
            sum_flat_list += i
        average_correlation = sum_flat_list / length_flat_list
        #print("average correlation: ", average_correlation)

        #standard deviation formula of a portfolio 
        #get all the weights multiplied against each other 
        weights_multiplied = 1 
        for i in weights_in_portfolio: 
            weights_multiplied = weights_multiplied * i 
        print("all weights multiplied", weights_multiplied)
        #get all std multiplied against each other 
        std_multiplied = 1 
        for j in std_in_portfolio: 
            std_multiplied = std_multiplied * j
        print("all std multiplied", std_multiplied)

        #this is part of the std portfolio formula 
        # 2 multiplied by the weights multiplied by the stand deviation multiplied by correlation 
        weights_std_correlation_data = 2 * weights_multiplied * std_multiplied
        #print(weights_multiplied)
        #beginning part of the std portfolio formula 
        #multiply each std squared against its corresponding weights squared 
        sum_weights_std_squared = 0
        for i, j in zip(squared_weights, squared_deviation):
            sum_weights_std_squared += i * j 

        #print("sum of weights and std combined: ", sum_weights_std_squared)

        variance_portfolio = sum_weights_std_squared + weights_std_correlation_data
        print("variance portfolio: ", variance_portfolio)
        #square root variance to get std
        standard_deviation_portfolio = math.sqrt(variance_portfolio)
        print("std of portfolio: ", standard_deviation_portfolio)

        return standard_deviation_portfolio
    
    def variance_of_portfolio(self): 

        standard_deviation_portfolio = self.standard_deviation_portfolio()
        variance_of_portfolio = standard_deviation_portfolio ** 2

        return variance_of_portfolio       

    def correlation_coefficient(self): 
        
        stock_list = self.stock_ticker
        stock_one_year_data = self.stock_one_year_data(stock_list)
        portfolio = stock_one_year_data['Adj Close']

        corr_matrtix = portfolio.corr()
        print(corr_matrtix)
        return corr_matrtix

    def covariance_stocks_yearly_returns(self): 
        list_of_stocks = self.stock_ticker
        annual_returns = self.yearly_stock_return(list_of_stocks)
        covariance = annual_returns.cov()
        return covariance   
    
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
    
    def quarterly_mean(self): 

        simple_rate_of_return = self.simple_rate_of_return()
        quarterly_mean = simple_rate_of_return.mean()

        return quarterly_mean

    def stock_daily_returns(self): 
        stock_list = self.stock_ticker
        stock_data = self.ticker_data()
        stock_daily_returns = stock_data['Adj Close'].pct_change()

        return stock_daily_returns
    
    def stock_daily_std(self):

        stock_daily_returns = self.stock_daily_returns()
        stock_daily_std = stock_daily_returns.std()

        return stock_daily_std
    
    def stock_daily_var(self):

        stock_daily_returns = self.stock_daily_returns()
        stock_daily_var = stock_daily_returns.var()

        return stock_daily_var


    def sharpe_ratio(self): 
        weights_in_portfolio = self.weights_of_portfolio()
        portfolio_weight = np.array(weights_in_portfolio)
        covariance = self.covariance_stocks_simple_returns()
 
        #get the expected quarterly returns
        quarterly_portfolio_return = self.expected_quarterly_portfolio_return()
        portfolio_std = np.sqrt(np.dot(portfolio_weight.T, np.dot(covariance, portfolio_weight)))
        #get the decimal value instead of percentage
        quarterly_portfolio_return = quarterly_portfolio_return / 100
        #sharpe ratio = portfolio return - risk-free rate of return / portfolio std
        #current risk free rate of return = 0.168 
        #risk of return rate  = ( (1 + 10 year bond rate) / (1 + inflation rate) ) - 1
        #risk of return rate  = ( (1 + 1.63) / (1 + 1.25) ) - 1
        sharpe_ratio = (quarterly_portfolio_return - 0.168) / portfolio_std
        print("sharpe ratio: ", sharpe_ratio)
        return sharpe_ratio 


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

    
    def five_year_annual_returns(self): 
        
        current_stock = self.stock_ticker
        #get weekly data of the stock 
        stock_data = self.stock_five_year_data(current_stock)
        #store the opening prices of the stock
        open_prices = stock_data.loc[:,'Open']
        #store the closing prices of the stock
        closing_prices = stock_data.loc[:,'Close']

        #get the first open price of last week(represents the opeing price of last week)
        opening_weekly_price = open_prices.iloc[0]
        #get the clsoing price of today 
        closing_weekly_price = closing_prices.iloc[-1]

        #calculate the weekly return from the opeining price of last week to the closing price of today 
        five_year_change = ((closing_weekly_price - opening_weekly_price) / opening_weekly_price) * 100
        print("5 Year return: ", five_year_change)
    



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
#list_stocks = ['AMZN','GOOG', 'TSLA', 'AAPL', 'UBER', 'NFLX', 'SQ', 'AMD', 'PLTR', 'NVDA']
#prices_of_stocks = [500, 100, 600, 450, 600, 750, 650, 330, 540, 100]
prices_of_stocks = [800, 200]
#x = Analysis('TSLA', start, end, 'MARZAN')
x = Analysis(list_stocks, prices_of_stocks, start, end)
#using the parent methods to test if it works
#print(x.ticker_data())
# x.talk()
# print("***************************")
# print(x.get_start_date())
# print("***************************")
# print(x.ticker_data())
# print("***************************")

#simp_return = x.simple_rate_return(prices_of_stocks)

# simp_return = x.simple_daily_rate_return()
# print("Returns: ", simp_return)
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

# print("***************************")
# print("Portfolio returns")
# x.portfolio_return()

# print("***************************")
# print("Varianmce of tesla")
# x.variance_of_individual_stock('TSLA')

# print("***************************")
# print("yearly stock return of tesla")
# x.yearly_stock_return('TSLA')

# print("***************************")
# print("STD of tesla")
# x.standard_deviation_stock('TSLA')

# print("***************************")
# print("Correlation of portfolio")
# x.correlation_of_stocks()

# print("***************************")
# print("Correlation of stocks")
# correlation_stocks = x.correlation_data()
# print(correlation_stocks)
# print("***************************")
# print("***************************")
# print("***************************")
# x.expected_5_year_return()
# print("***************************")
# x.expected_portfolio_return()
# print("***************************")
# x.expected_return_ror()
# print("***************************")
# x.expected_quarterly_portfolio_return()
x.sharpe_ratio()
# x.variance_of_individual_stock('TSLA')

# x.testing_covariance()
#x.covariance_stocks_yearly_returns()
# test = x.correlation_coefficient()
# y = test.values.tolist()
# print(y)
#x.correlation_coefficient()


# print("***************************")
# x.standard_deviation_portfolio()


# start = x.get_start_date()
# end = x.get_end_date()

# x.present_stock_data()


