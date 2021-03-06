x = 1
y = 2
z= x + y
print("this is test : " , z )



def add_numbers(x, y):
    return x + y

a = add_numbers(1, 2)
print(a)



def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z


print('test 1 : call the function ')
print(add_numbers(1, 2))

print('test 2 : call the function ')
print(add_numbers(1, 2, 3))




# ========================= Multi-line statement =================
# ====== use \ =======

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print("------- start -------")
print("result 1 : " , a)


# ======== use () ======
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9 +10)

print("result 2 : " , a)
print("-------- END --------")




# ======== use [] =======

colors = ['red',
          'blue',
          'green']

print(colors)

a = 1; b = 2; c = 3
print(a)
print(b)
print(c)

# ============================ use type to get the var type ================




def greet(name):
    #this is comment
	print("Hello, " + name + ". Good morning!")


greet ('myName')

print(greet.__doc__)



# ========================== class =============================

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)



# ============================ class example =========================

print(' ============= this is the other class example ===========')


# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()



# ===============================

for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        # Note use of 'end' on previous line
        print(repr(x*x*x).rjust(4))
        print('xxxxx')
print('test')