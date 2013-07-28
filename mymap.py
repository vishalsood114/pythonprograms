def mymap(func,l):
    return [func(x) for x in l]

def square(x):
    return x*x

print mymap(square, [1,2,3,4])
