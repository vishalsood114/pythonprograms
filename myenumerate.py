def myenumerate(l):
    #return [(i,l[i]) for i in range(len(l))]
    return [zip(range(len(l)), l)]
print myenumerate(['a','b','c'])
