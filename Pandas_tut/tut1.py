import pandas as pd

####################################################################################################
##################################### The Series Data Structure ####################################
####################################################################################################

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




import numpy as np
np.nan == None


############## index example 1 ##############
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s

print(s.index)


############## index example 2 ##############

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s
print(s)



####################################################################################################
##################################### The Series Data Structure ####################################
####################################################################################################


