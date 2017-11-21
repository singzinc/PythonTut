import pandas_datareader as pdr
import datetime
import pandas as pd

start = datetime.datetime(2017, 1, 1)
end =  datetime.datetime(2017, 12, 31)

print(start)
print(end)

#get data from google
aapl = pdr.get_data_google('AAPL', start=datetime.datetime(2015, 10, 1), end=datetime.datetime(2017, 11, 11))

print("------------- print out full set data")
print(aapl)


print('################# get the time range ####################')
print(aapl.loc[pd.Timestamp('2017-11-01'):pd.Timestamp('2017-12-31')])

print('################# get year ####################')
print(aapl.loc['2017'])

print('################# get array range ####################')
# print(aapl[22:43])

# get data from 1 to 43
result = aapl[1:43]
print (result)

# only get the data from
result = aapl.iloc[[22,43], [0, 3, 4]]

print (result)


closeVal = aapl.Close
volumeVal = aapl.Volume
openVal = aapl.Open
highVal = aapl.High
lowVal = aapl.Low


# Print `aapl close value only`
print(openVal )
print(closeVal)
print(volumeVal)
print(highVal)
print(lowVal)

