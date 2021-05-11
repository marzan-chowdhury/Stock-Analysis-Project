import unittest
from stock_analysis import Stock
from pandas.util.testing import assert_equal

class TestStockAnalysis(unittest.TestCase): 
#inheriting fron unittest.Testcase is going to give accesss to a lof of tetsing capabilities 

    def setUp(self): 
        print('setUp')
        portfolio_stocks = ['AAPL', 'AMZN', 'GOOG', 'FB', 'TSLA']
        portfolio_prices = [500,1000,300,200,150]
        self.stock_one = Stock('AAPL', 150, '2020-03-02', '2021-04-08')
        self.portfolio_stocks = Stock(portfolio_stocks, portfolio_prices, '2020-03-02', '2021-04-08')
    
    def tearDown(self):
        print('tearDown')


    def test_columns(self):
        df = self.stock_one.stock_one_day_data('AAPL')
        actual_columns = list(df.columns)
        expected_columns = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
        self.assertEqual(actual_columns,expected_columns)

if __name__ == '__main__':
    unittest.main()