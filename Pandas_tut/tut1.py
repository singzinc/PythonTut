import pandas as pd

##################################################
#The Series Data Structure

#################### example 1 ####################
numbers = {1,2,3,4,5}
ser = pd.Series(list(numbers))
print(ser)
print("size of the list" , ser.size)

##################  example 2 ###################
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))


##################  example 3 ###################
numbers = [1, 2, None]
pd.Series(numbers)
print(pd.Series(numbers))