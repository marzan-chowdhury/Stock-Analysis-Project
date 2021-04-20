from stock_analysis import Stock
import numpy as np 
import pandas as pd 
# Used to grab the stock prices, with yahoo 
#import pandas_datareader as web
from pandas_datareader import data 
from datetime import datetime 
# To visualize the results 
import matplotlib.pyplot as plt 
import seaborn


class Visualize(Stock): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)

    # def ticker_data_1(self): 
    #     user_ticker_symbol = self.stock_ticker
    #     start_date = self.start_date
    #     df = data.DataReader(user_ticker_symbol, 'yahoo', start_date)
    #     return df

    def ticker_symbols(self): 
        #array to store prices
        symbols=[]
        symbols_list = self.stock_ticker
        print("stock list: ", symbols_list)
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
        df.head()
        df_pivot=df.pivot('Date','Symbol','Close').reset_index()
        print("****************************")
        df_pivot.head()

        return df_pivot

    def correlation(self): 

        df_pivot = self.clean_data()
        corr_df = df_pivot.corr(method='pearson')
        #reset symbol as index (rather than 0-X)
        corr_df.head().reset_index()
        #del corr_df.index.name
        corr_df.head(10)
        # print("corr_df")
        # print(corr_df)
        return corr_df
    
    def plot_data(self): 

        corr_df = self.correlation()
        plt.figure(figsize=(13, 8))
        seaborn.heatmap(corr_df, annot=True, cmap='RdYlGn')
        plt.show()

#symbols_list = ['V', 'SQ', 'TSLA', 'BTC', 'PYPL']
#'2222.SR' --> ARAMCO OIL COMPANY
symbols_list = ['TSLA', '2222.SR']
start = '2021-04-07'
end = '2021-04-07'
prices_of_stocks = [500, 100]
x = Visualize(symbols_list, prices_of_stocks, start, end)


x.plot_data()
