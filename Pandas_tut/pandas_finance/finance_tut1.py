import pandas_datareader as pdr
import datetime
import pandas as pd

#get data from yahoo
aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2011, 10, 1),
                          end=datetime.datetime(2012, 1, 1))

print(aapl)

#get data from google
aapl2 = pdr.get_data_google('AAPL',
                          start=datetime.datetime(2017, 10, 1),
                          end=datetime.datetime(2017, 11, 11))
print(aapl2)



print(aapl2.loc[pd.Timestamp('2017-11-01'):pd.Timestamp('2017-12-31')])