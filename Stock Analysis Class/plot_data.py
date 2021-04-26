from analysis import Analysis
import numpy as np 
import pandas as pd
from datetime import datetime, timedelta
import datetime as dt
import dateutil.relativedelta 
from pandas_datareader import data 
from datetime import datetime 

import matplotlib.pyplot as plt 
import seaborn


class Visualize(Analysis): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)
    
    def quarterly_data(self): 

        stock_data = self.ticker_data()
        stock_data_adj_close = stock_data['Adj Close']
        quarterly_data = stock_data_adj_close.resample('Q').last()
        return quarterly_data.head()
    
    def quarterly_simple_rate_return(self): 
        
        quarterly_data = self.quarterly_data()
        quarterly_change = quarterly_data.pct_change()

        return quarterly_change.head()
    
    def stock_performance(self): 


        stock_data = self.todays_data_copy()
        print(stock_data)
        stock_data_adj_close = stock_data['Adj Close']
        performance = stock_data_adj_close
        
        performance.plot(grid = True, figsize=(15,10), title = "Stock Performance").axhline(y = 1, color = "black", lw = 2)
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()
        return performance.tail(1)
    
    def expected_rate_return(self): 
        #based on quarterly price of the assets whereas before we used the yearly returns

        simple_rate_return = self.quarterly_simple_rate_return()
        #simple_rate_return = self.expected_return()
        expected_rate_return = simple_rate_return.mean()
        print("Expected RoR: ", expected_rate_return)

        symbols = expected_rate_return.index
        plt.bar(x = symbols,height = expected_rate_return)
        plt.tight_layout()
        plt.xticks(rotation='vertical')
        plt.xlabel('Stock')
        plt.ylabel('Expected Rate Of Return')
        plt.title('Expected Rate Of Return (Quarterly)')
        plt.show()
        
    def present_variance(self): 
        stock_list = self.stock_ticker
        stock_variance = []
        for i in stock_list: 
            print("Stock: ", i)
            stock_variance.append(self.variance_of_individual_stock(i))
        print("Variance of each stock in portfolio: ", stock_variance)
        plt.bar(x = stock_list ,height = stock_variance)
        plt.xticks(rotation='vertical')
        plt.xlabel('Stock')
        plt.ylabel('Variance Of The Mean Rate Of Return')
        plt.title('Variance Of each stock in the portfolio')
        plt.tight_layout()
        plt.show()
    
    def present_std_stock(self): 
        stock_list = self.stock_ticker
        stock_std = []
        for i in stock_list: 
            print("Stock: ", i)
            stock_std.append(self.standard_deviation_stock(i))
        print("STD of each stock in portfolio: ", stock_std)
        plt.bar(x = stock_list ,height = stock_std)
        plt.xticks(rotation='vertical')
        plt.xlabel('Stock')
        plt.ylabel('Standard Deviation')
        plt.title('Standar Deviation Of each stock in the portfolio')
        plt.tight_layout()
        plt.show()

    def covariance_matrix(self): 

        corr_df = self.correlation_data()
        plt.figure(figsize=(13, 8))
        seaborn.heatmap(corr_df, annot=True, cmap='RdYlGn')
        plt.title('CO-Variance (Correlation between stocks)')
        plt.show()

#symbols_list = ['V', 'SQ', 'TSLA', 'BTC', 'PYPL']
#'2222.SR' --> ARAMCO OIL COMPANY
#symbols_list = ['TSLA', 'AAPL', 'OXY']
start = '2019-04-07'
end = '2021-04-23'
#prices_of_stocks = [500, 100, 350]
symbols_list = ['AMZN','GOOG', 'TSLA', 'AAPL', 'UBER', 'NFLX', 'SQ', 'AMD', 'PLTR', 'NVDA']
prices_of_stocks = [500, 100, 600, 450, 600, 750, 650, 330, 540, 100]
x = Visualize(symbols_list, prices_of_stocks, start, end)


x.covariance_matrix()
#x.quarterly_data()
#print(x.quarterly_simple_rate_return())
#print(x.stock_performance())
# x.expected_rate_return()
# x.present_variance()
x.present_std_stock()
