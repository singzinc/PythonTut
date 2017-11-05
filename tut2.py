x = 'test'
print ("We're on time %d" , x)

# =================== looping example =====================

for x in range(0, 5):
    print ("We're on time %d" % (x))
    print ("test : " , x)

# ========================

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print (x)


# =========================== for else ========

for x in range(3):
    print (x)
else:
    print ('Final x = %d' % (x))
