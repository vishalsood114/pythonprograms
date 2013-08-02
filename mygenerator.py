def mygenerator(n):
    i = 0
    while i < n:
        yield i
        i= i+1

print mygenerator(6)

#for i in mygenerator(10):
#    print i,

g = mygenerator(5)
print g.next()
print g.next()
print g.next()
    
    
