import pandas as pd

#################### example 1 ####################
numbers = {1,2,3,4,5}
ser = pd.Series(list(numbers))

print(ser.size)

##################  example 2 ###################
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))

