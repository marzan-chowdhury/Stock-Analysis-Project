import sys
sys.path.append("C:/University/Level 6/Project Planning/Project Code/Stock Analysis Class")
from stock_analysis import Stock

from pandas_datareader import data
import pandas as pd 
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style 
import yfinance as yf
import datetime as dt 
from datetime import datetime, timedelta
import dateutil.relativedelta
import math
style.use('ggplot')

class Prediction(Stock): 

  def __init__(self, stock_ticker, stock_prices, start_date, end_date):
    super().__init__(stock_ticker, stock_prices, start_date, end_date)
  
  def get_stock_data(self):  
    user_ticker_symbol = self.stock_ticker
    stock_data = self.stock_five_year_data(user_ticker_symbol)
    return stock_data
  
  def percentage_change(self): 

    stock_data = self.get_stock_data()
    #get the percentage change of the stocks
    returns = stock_data.pct_change()
    return returns
  
  def get_latest_price(self): 

    stock_data = self.get_stock_data()
    #convert dataframe to a list
    stock_data = stock_data.values.tolist()
    #get the last price of the stock
    last_price = stock_data[-1]
    final_price = 0
    for i in last_price:
      final_price += i
    return final_price
  
  def simulations(self): 
    num_simulations = 100
    #how many days into the future we are going int
    num_days = 1260 #252 trading days 
    return num_simulations, num_days

  def monte_carlo_sim(self):

    #get the number of simulations, days
    num_simulations, num_days = self.simulations()
    #create a dataframe for our simulations 
    simulation_df = pd.DataFrame() 
    #get the returns (percentage change of the stock data)
    returns = self.percentage_change()
    #get the last price of the stock data 
    last_price = self.get_latest_price()

    #create a for loop for the number of simulations we want to create 
    for x in range(num_simulations): 
      #create a count
      count = 0
      #exctract monte carlo simulation 
      daily_vol = returns.std() 

      #list to append all the prices for the year 
      price_series = []
      #randomise the price of the stock
      price = last_price * (1 + np.random.normal(0,daily_vol))
      #add the random stock prices to our empty list
      price_series.append(price)
      #loop through the number of days 
      for y in range(num_days):
        if count == 1260: #number of days
          break 
        #multiply our random prices and then append them to the list 
        price = price_series[count] * (1 + np.random.normal(0,daily_vol))
        price_series.append(price)
        count += 1 

      simulation_df[x] = price_series
    return simulation_df

  def plot_monte_carlo_sim(self): 

    ticker_symbol = self.stock_ticker
    #get our simulation dataframe
    simulation_df = self.monte_carlo_sim()

    #get the last price 
    last_price = self.get_latest_price()

    fig = plt.figure() 
    fig.suptitle('Monte Carlo Simulation of '+ str(ticker_symbol))
    plt.plot(simulation_df)
    plt.axhline(y = last_price, color = 'b', linestyle = '-')
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.show() 





start = '2015-04-07'
end = '2021-04-08'
prices_of_stocks = [800]
list_stocks = ['TSLA']
x = Prediction(list_stocks, prices_of_stocks, start, end)
x.plot_monte_carlo_sim()



#x.percentage_change()
# x.get_latest_price()
# x.monte_carlo_sim()




