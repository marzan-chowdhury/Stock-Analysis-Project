import pandas as pd
import matplotlib.pyplot as plt

from pandas_datareader import data
import datetime as dt

start_date = pd.to_datetime('2021-2-18')
end_date = pd.to_datetime('2021-3-12') 
user_ticker_symbol = 'TSLA'
df = data.DataReader(user_ticker_symbol, 'yahoo', start_date, end_date)
df.to_csv (r'C:\University\Level 6\Project Planning\Project Code\Stock Analysis Class\export_dataframe.csv', index = True, header=True)
df = pd.read_csv("C:\\University\\Level 6\\Project Planning\\Project Code\\Stock Analysis Class\\export_dataframe.csv")

#df = pd.read_csv("alphabet_stock_data.csv")
# df = data.DataReader(user_ticker_symbol, 'yahoo')
# start_date = pd.to_datetime('2020-4-1')
# end_date = pd.to_datetime('2020-9-30')                         

df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')

#closing price chart 
top_plt = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=4)
top_plt.plot(stock_data.index, stock_data["Close"])
plt.title('Historical stock prices of Tesla Inc. [01-04-2020 to 30-09-2020]')

#volume chart 
bottom_plt = plt.subplot2grid((5,4), (3,0), rowspan=3, colspan=4)
bottom_plt.bar(stock_data.index, stock_data['Volume'], width=0.1)
plt.title('Tesla Trading Volume', y=-0.60)
axes = plt.gca()
axes.set_xlim([start_date,end_date])
axes.set_ylim([0,100000000])
plt.gcf().set_size_inches(12,8)
plt.tight_layout()
plt.show()