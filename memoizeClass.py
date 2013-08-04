import functools
import sys

class memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}

    def __call__(self,n):
        if n not in self.cache:
             self.cache[n] = self.f(n)
        return self.cache[n]

@memoize
def square(x):
    print "square(%d)" % x
    return x*x

print square(2)
print square(2)
print square(2)
