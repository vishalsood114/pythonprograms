def unique(values,key=None):
    # if key is None:
    # key = lambda x:x
    d={}
    for v in values:
        if key is None:
            d[v] = v
        else:
            d[key(v)] = v

    return d.values()
        

print unique([1,2,1,3,2,5])
print unique(["Python", "perl", "python", "java", "perl"])

print unique(["python", "perl", "java", "jython"], key=lambda s:s.lower())
