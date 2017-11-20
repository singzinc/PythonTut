import pandas_datareader as pdr
import datetime

#get data from yahoo
aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2011, 10, 1),
                          end=datetime.datetime(2012, 1, 1))

print(aapl)

#get data from google
aapl2 = pdr.get_data_google('AAPL',
                          start=datetime.datetime(2011, 10, 1),
                          end=datetime.datetime(2012, 1, 1))
print(aapl2)

