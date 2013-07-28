def myabs(x):
    if x < 0:
       return x * (-1)
    else:
       return x

print myabs(2)
print myabs (-2)

def minimum(x,y):
    if x > y:
       return y
    else:
       return x

print minimum(2,5)
print minimum(20,5)

def minimum3(x,y,z):
    return minimum(minimum(x,y),z)


print minimum3(3,5,2)
