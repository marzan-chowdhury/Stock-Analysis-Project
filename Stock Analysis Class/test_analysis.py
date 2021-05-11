import unittest
from analysis import Analysis 

class TestAnalysis(unittest.TestCase): 
#inheriting fron unittest.Testcase is going to give accesss to a lof of tetsing capabilities 
    def setUp(self): 
        self.stock_one = Analysis('TSLA', 500, '2021-04-07', '2021-04-08')
    
    def tearDown(self):
        print('tearDown')

    def test_standard_deviation_of_a_stock(self):
        actual_std = self.stock_one.standard_deviation_stock('TSLA')
        expected_std = 2.9052249057260178
        self.assertEqual(actual_std,expected_std)
    
    def test_daily_return_stock(self):
        actual_daily_returns = self.stock_one.daily_return()
        expected_daily_returns = 0.94
        self.assertEqual(actual_daily_returns,expected_daily_returns)
    
    def test_weekly_return_stock(self):
        actual_weekly_returns = self.stock_one.weekly_return()
        expected_weekly_returns = -4.51
        self.assertEqual(actual_weekly_returns,expected_weekly_returns)
    
    def test_monthly_return_stock(self):
        actual_monthly_returns = self.stock_one.monthly_return()
        expected_monthly_returns = -0.78
        self.assertEqual(actual_monthly_returns,expected_monthly_returns)
    
    def test_six_month_return_stock(self):
        actual_six_month_returns = self.stock_one.six_month_return()
        expected_six_month_returns = 52.98
        self.assertEqual(actual_six_month_returns,expected_six_month_returns)
    
    def test_one_year_return_stock(self):
        actual_one_year_returns = self.stock_one.one_year_return()
        expected_one_year_returns = 310.09
        self.assertEqual(actual_one_year_returns,expected_one_year_returns)

    def test_year_to_date_return_stock(self):
        actual_ytd_returns = self.stock_one.ytd_return()
        expected_ytd_returns = -6.48
        self.assertEqual(actual_ytd_returns,expected_ytd_returns)
    
    def test_five_year_return_stock(self):
        actual_five_year_returns = self.stock_one.five_year_annual_returns()
        expected_five_year_returns = 1518.61
        self.assertEqual(actual_five_year_returns,expected_five_year_returns)

    def test_simple_daily_return(self):
        actual_returns = self.stock_one.simple_daily_rate_return()
        expected_returns = 34.416
        self.assertEqual(actual_returns,expected_returns)

if __name__ == '__main__':
    unittest.main()