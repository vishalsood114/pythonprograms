"""Writing a trace function over another function: like a wrapper"""

def trace(f):
    def g(x,n):
        print "%s (%s, %s)" % (f.__name__,x,n)
        return f(x,n)

    return g

def exp(x,n):
    if n == 0:
        return 1
    else:
        return x*exp(x,n-1)

def add(a,b): return a+b
add2 = trace (add)

print add2(2,3)

exp = trace(exp)
exp (3,4)
        
