""" function that computes the sum of any function passed as
    a parameter
    """

def sigma(f,a,b):
    return sum(f(x) for x in range(a,b))

def square(x):
    return x*x
def cube(x):
    return x*x*x


print sigma(square, 1,10)
print sigma(cube,1,10)
print sigma(lambda x:x**0.5, 0,10)
print sigma(lambda x:1.0/x,1,100)
