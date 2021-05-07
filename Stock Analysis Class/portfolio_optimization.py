# import sys
# sys.path.append("C:/University/Level 6/Project Planning/Project Code/Stock Analysis Class")
from stock_analysis import Stock
import numpy as np
#-----------------------------------------------#
#portfolio optimisation and efficietn frontier  #
import cvxopt as opt                            #
from cvxopt import blas, solvers                #
#-----------------------------------------------#
from datetime import datetime, timedelta
import datetime as dt
import dateutil.relativedelta
from pandas_datareader import data
import yfinance as yf
import pandas as pd
import math
import random
import matplotlib.pyplot as plt 
import seaborn

class Optimization(Stock): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)
    
    def quarterly_mean(self): 

        simple_rate_of_return = self.simple_rate_of_return()
        quarterly_mean = simple_rate_of_return.mean()

        return quarterly_mean

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

    def weights_of_portfolio(self): 

        list_of_stocks = self.stock_ticker 
        list_of_stock_prices = self.stock_prices 

        number_of_stocks = 0 
        for stock in list_of_stocks:
            number_of_stocks += 1 

        total_weights = [] 

        total_invested = 0 
        for prices in list_of_stock_prices: 
            total_invested += prices 
        for prices in list_of_stock_prices:
            weight_asset = prices /  total_invested
            total_weights.append(weight_asset)
        
        return total_weights
    
    def my_portfolio(self): 
        
        portfolio = self.stock_ticker 
        #length of the portfolio 
        length_port = len(portfolio)
        #find the returns 
        expected_returns = self.quarterly_mean()
        expected_returns = expected_returns.values.tolist()
        sum = 0 
        for i in expected_returns:
            sum += i 
        average_returns = sum / length_port
        weights = self.weights_of_portfolio()
        stock_covariance = self.covariance_stocks_simple_returns()
        volatility = np.sqrt(np.dot(weights, np.dot(stock_covariance, weights)))
        return average_returns , volatility

    def return_portfolios(self, expected_returns, cov_matrix):

        np.random.seed(1)
        port_returns = []
        port_volatility = []
        stock_weights = []

        selected = (expected_returns.axes)[0]
        #this specifies the number of random portfolios generated  
        num_assets = len(selected) 
        num_portfolios = 100000

        for single_portfolio in range(num_portfolios):
            weights = np.random.random(num_assets)
            weights /= np.sum(weights)
            returns = np.dot(weights, expected_returns)
            risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            port_returns.append(returns)
            port_volatility.append(risk)
            stock_weights.append(weights)

            portfolio = {'Returns': port_returns,
                        'Risk': port_volatility}

        for counter,symbol in enumerate(selected):
            portfolio[symbol +' Weight'] = [Weight[counter] for Weight in stock_weights]

        df = pd.DataFrame(portfolio)

        column_order = ['Returns', 'Risk'] + [stock + ' Weight' for stock in selected]

        df = df[column_order]

        return df

    def optimal_portfolio(self, returns):
        n = returns.shape[1]
        returns = np.transpose(returns.values)

        N = 10
        mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

        # Convert to cvxopt matrices
        S = opt.matrix(np.cov(returns))
        pbar = opt.matrix(np.mean(returns, axis=1))

        # Create constraint matrices
        G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
        h = opt.matrix(0.0, (n ,1))
        A = opt.matrix(1.0, (1, n))
        b = opt.matrix(1.0)

        # Calculate efficient frontier weights using quadratic programming
        portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] for mu in mus]
        
        ## CALCULATE RISKS AND RETURNS FOR FRONTIER
        returns = [blas.dot(pbar, x) for x in portfolios]
        risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
        ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
        m1 = np.polyfit(returns, risks, 2)
        x1 = np.sqrt(m1[2] / m1[0])
        # CALCULATE THE OPTIMAL PORTFOLIO
        wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
        return np.asarray(wt), returns, risks

    def generate_random_portfolios(self): 
        #we will be using the expected returns that are generated from the quarterly changes rather than yearly 
        expected_returns = self.quarterly_mean()
        stock_covariance = self.covariance_stocks_simple_returns()

        random_portfolios = self.return_portfolios(expected_returns, stock_covariance)
        #print(random_portfolios.head())


        return random_portfolios
    
    def generate_optimal_portfolio(self): 

        stock_data_quarterly_returns = self.simple_rate_of_return()
        #remove the Nan in the datafram which is found at the zero index position as ther isnt any data to compare previously
        stock_data_quarterly_returns = stock_data_quarterly_returns[1:]
        weights, returns, risks = self.optimal_portfolio(stock_data_quarterly_returns[1:])
        #print(weights, returns, risks)

        return weights, returns, risks 

    def recommended_portfolio_plot(self): 

        stock_data_quarterly_returns = self.simple_rate_of_return()
        generate_random_portfolios = self.generate_random_portfolios()
        max_port, min_vol = self.recommended_portfolio() 
        max_returns = max_port[0]
        max_risk = max_port[1]
        min_returns = min_vol[0]
        min_risk = min_vol[1]

        return max_returns, max_risk, min_returns, min_risk

    
    def recommended_portfolio(self): 
        generate_random_portfolios = self.generate_random_portfolios()
        for i in range(10000):
            #define the risk and returns wanted for the portfolio
            if generate_random_portfolios.Risk[i] < 0.3 and generate_random_portfolios.Returns[i] > 0.15:
                max_return_portfolio = generate_random_portfolios.iloc[generate_random_portfolios['Returns'].idxmax()]
                min_volatility_portfolio = generate_random_portfolios.iloc[generate_random_portfolios['Risk'].idxmin()]
                #print(generate_random_portfolios.iloc[[i]])
        print(max_return_portfolio)
        print(min_volatility_portfolio)
        return max_return_portfolio, min_volatility_portfolio
    
    def efficient_frontier(self): 

        weights, returns, risks = self.generate_optimal_portfolio()
        random_portfolios = self.generate_random_portfolios()
        max_returns, max_risk, min_returns, min_risk = self.recommended_portfolio_plot()
        #this will plot where the investors portfolio is on the efficient frontier
        p_risks, p_returns = self.my_portfolio()
        plt.style.use('seaborn')
        random_portfolios.plot.scatter(x='Risk', y='Returns', figsize=(10,8), grid=True)

        plt.xlabel('Volatility (Std. Deviation)', fontsize = 20)
        plt.ylabel('Expected Returns', fontsize = 20)
        plt.title('Efficient Frontier', fontsize = 20)
        plt.plot(risks, returns, 'y-o')
        #the investors portfolio is marked by a red mark
        plt.plot(p_risks, p_returns, marker=(5,1,0),color='r')
        plt.plot(max_returns, max_risk, marker=(5,1,0),color='g')
        plt.plot(min_returns, min_risk, marker=(5,1,0),color='b')
        plt.show()



start = '2019-04-07'
end = '2021-04-23'
symbols_list = ['AMZN','NVDA', 'TSLA', 'AAPL']
prices_of_stocks = [5000, 11000, 25000, 4500]
x = Optimization(symbols_list, prices_of_stocks, start, end)

#x.recommended_portfolio()
# x.generate_random_portfolios()
# x.generate_optimal_portfolio()
x.efficient_frontier()
#x.my_portfolio()
#x.generate_optimal_portfolio_2()













