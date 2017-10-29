x = 1
y = 2
z= x + y
print("this is test : " , z )

x


def add_numbers(x, y):
    return x + y

a = add_numbers(1, 2)
print(a)



def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))