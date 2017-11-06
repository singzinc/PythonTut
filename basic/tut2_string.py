
# ====================== concat example 1 ===================

firstname = 'sing'
lastname = 'zinc '

print(firstname + ' ' + lastname)
print(firstname * 3)
print('sing' in firstname)


# ====================== concat example 2 ===================

foo = "seven"
print("She lives with " + foo + " small men")


# ====================== Concat example 3 ===================
x = 'apples'
y = 'lemons'
z = 'In the basket are %s and %s' % (x,y)

print(z)


#=============== example 2 ===================

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)


# this is incorrect example
# x = 'Chris' + 2
# print(x)


x = 'Chris' + str(2)
print(x)

