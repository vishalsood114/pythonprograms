import time
import urllib

def profile(f):
    def g(n):
        t0 = time.time()
        value = f(n)
        t1 = time.time()
        print "took %f seconds" % (t1-t0)
        return value
    return g

def timepass(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i*j
    return sum

timepass = profile(timepass)

print timepass(10)

@profile
def wget(url):
    return urllib.urlopen(url).read()

x = wget("http://python.org")
