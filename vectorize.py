def vectorize(f,value=None):
    def g(n):
        value=[]
        for i in n:
            value.append(f(i))
        return value
    return g

@vectorize
def square(x): return x*x

print square([1,2,3,4])
print square([1,2,3,4])

g=vectorize(len)
print g(["hello", "python"])
