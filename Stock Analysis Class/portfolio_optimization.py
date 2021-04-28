from analysis import Analysis
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


class Optimization(Analysis): 

    def __init__(self, stock_ticker, stock_prices, start_date, end_date):
        super().__init__(stock_ticker, stock_prices, start_date, end_date)
    
    def return_portfolios(self, expected_returns, cov_matrix):

        np.random.seed(1)
        port_returns = []
        port_volatility = []
        stock_weights = []

        selected = (expected_returns.axes)[0]
        #this specifies the number of random portfolios generated  
        num_assets = len(selected) 
        num_portfolios = 50000

        for single_portfolio in range(num_portfolios):
            weights = np.random.random(num_assets)
            weights /= np.sum(weights)
            returns = np.dot(weights, expected_returns)
            volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            port_returns.append(returns)
            port_volatility.append(volatility)
            stock_weights.append(weights)

            portfolio = {'Returns': port_returns,
                        'Volatility': port_volatility}

        for counter,symbol in enumerate(selected):
            portfolio[symbol +' Weight'] = [Weight[counter] for Weight in stock_weights]

        df = pd.DataFrame(portfolio)

        column_order = ['Returns', 'Volatility'] + [stock + ' Weight' for stock in selected]

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
        print("quarterly returns: ", expected_returns)
        x = self.expected_5_year_return()
        print("yearly returns: ", x)
        stock_covariance = self.covariance_stocks_simple_returns()

        random_portfolios = self.return_portfolios(x, stock_covariance)
        print(random_portfolios.head().round(4))

        return random_portfolios
    
    def generate_optimal_portfolio(self): 

        stock_data_quarterly_returns = self.simple_rate_of_return()
        #remove the Nan in the datafram which is found at the zero index position as ther isnt any data to compare previously
        stock_data_quarterly_returns = stock_data_quarterly_returns[1:]
        weights, returns, risks = self.optimal_portfolio(stock_data_quarterly_returns[1:])
        #print(weights, returns, risks)

        return weights, returns, risks 
    
    # def efficient_frontier(self): 
    #     random_portfolios = self.generate_random_portfolios()
    #     weights, returns, risks = self.generate_optimal_portfolio()
    #     stock_covariance = self.covariance_stocks_simple_returns()
    #     quarterly_mean = self.quarterly_mean()
    #     stock_data_quarterly_returns = self.simple_rate_of_return()
    #     random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize = 12, figsize=(30,30))
    #     plt.margins(x=0.05, y=-0.3)
    #     plt.xlabel('Volatility (Std. Deviation)', fontsize = 20)
    #     plt.ylabel('Expected Returns', fontsize = 20)
    #     plt.title('Efficient Frontier', fontsize = 20)

    #     #How to put labels right next to the spots?
    #     single_asset_std=np.sqrt(np.diagonal(stock_covariance))
    #     plt.scatter(single_asset_std,quarterly_mean,marker='X',color='red',s=200)
    #     for i, txt in enumerate(stock_data_quarterly_returns.keys()):
    #         plt.annotate(txt, (single_asset_std[i], quarterly_mean[i]), size=14, xytext=(10,10), ha='left', textcoords='offset points')
            
    #     plt.plot(risks, returns, 'y-o')
    #     #plt.plot(risks_noGE, returns_noGE, 'g-o')
    #     plt.legend(['With TSLA', 'Without TSLA', 'Random'], fontsize = 20, loc="lower left")
        
    #     plt.show()

    def efficient_frontier(self): 

        weights, returns, risks = self.generate_optimal_portfolio()
        random_portfolios = self.generate_random_portfolios()
        plt.style.use('seaborn')
        random_portfolios.plot.scatter(x='Volatility', y='Returns', figsize=(10,8), grid=True)


        stock_covariance = self.covariance_stocks_simple_returns()
        quarterly_mean = self.quarterly_mean()
        stock_data_quarterly_returns = self.simple_rate_of_return()

        single_asset_std=np.sqrt(np.diagonal(stock_covariance))
        plt.scatter(single_asset_std,quarterly_mean,marker='X',color='red',s=200)
        for i, txt in enumerate(stock_data_quarterly_returns.keys()):
            plt.annotate(txt, (single_asset_std[i], quarterly_mean[i]), size=14, xytext=(10,10), ha='left', textcoords='offset points')

        plt.xlabel('Volatility (Std. Deviation)', fontsize = 20)
        plt.ylabel('Expected Returns', fontsize = 20)
        plt.title('Efficient Frontier', fontsize = 20)
        plt.plot(risks, returns, 'y-o')
        plt.show()



start = '2019-04-07'
end = '2021-04-23'
symbols_list = ['AMZN','GOOG', 'TSLA', 'AAPL']
prices_of_stocks = [20, 11, 25, 44]
x = Optimization(symbols_list, prices_of_stocks, start, end)

#x.generate_random_portfolios()
#x.generate_optimal_portfolio()
x.efficient_frontier()














    
# #this will calculate return, std and sharpe ratio of each portfolio
#     def calc_portfolio_perf(weights, mean_returns, cov, rf):
#         portfolio_return = self.quarterly_portfolio_return()
#         portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
#         sharpe_ratio = (portfolio_return - rf) / portfolio_std
#         return portfolio_return, portfolio_std, sharpe_ratio

# #this will generate random portfolios
#     def simulate_random_portfolios(num_portfolios, mean_returns, cov, rf, tickers):
#         results_matrix = np.zeros((len(mean_returns)+3, num_portfolios))
#         for i in range(num_portfolios):
#             weights = np.random.random(len(mean_returns))
#             weights /= np.sum(weights)
#             portfolio_return, portfolio_std, sharpe_ratio = calc_portfolio_perf(weights, mean_returns, cov, rf)
#             results_matrix[0,i] = portfolio_return
#             results_matrix[1,i] = portfolio_std
#             results_matrix[2,i] = sharpe_ratio
#             #iterate through the weight vector and add data to results array
#             for j in range(len(weights)):
#                 results_matrix[j+3,i] = weights[j]
                
#         results_df = pd.DataFrame(results_matrix.T,columns=['ret','stdev','sharpe'] + [ticker for ticker in tickers])
            
#         return results_df