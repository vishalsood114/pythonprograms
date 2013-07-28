def myzip(x,y):
    n = min (len(x),len(y))
    return [(x[i],y[i]) for i in range(n)]


print myzip([1,2,3,4],[5,6,7,8])
