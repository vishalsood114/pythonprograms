import functools
import sys

indent = 0
def trace2(f):
    def g(*args):
        global indent
        #convert args into a string
        sargs = ",".join(str(a) for a in args)
        print "| " * indent + "|-- %s (%s)" % (f.__name__, sargs)
        indent += 1
        value = f(*args)
        indent -= 1
        return value
    return g

def memoize(f):
    cache = {}
    # This makes the function g look like the given function f.
    # The __name__, __doc__ etc. will be copied.
    @functools.wraps(f)
    def g(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return g

@trace2
@memoize
def fib2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


fib2(10)
