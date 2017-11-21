import pandas_datareader as pdr
import datetime
import pandas as pd


#get data from google
aapl2 = pdr.get_data_google('AAPL',
                          start=datetime.datetime(2017, 10, 1),
                          end=datetime.datetime(2017, 11, 11))
#print(aapl2)


print('################# get the time range ####################')
print(aapl2.loc[pd.Timestamp('2017-11-01'):pd.Timestamp('2017-12-31')])

print('################# get year ####################')
print(aapl2.loc['2017'])