import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2013, 11, 20)


print (  start , ' - ' , end)
f = web.DataReader("F", 'yahoo', start, end)
f.ix['2017-01-04']

print(f.ix['2010-01-04'])

result = web.DataReader('AAPL', 'yahoo-actions', start, end)
print(result);