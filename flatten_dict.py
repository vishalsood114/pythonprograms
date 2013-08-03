def flatten_dict(x,prefix=None):
    y = {}
    for k,v in x.items():
        if prefix is None:
            key = k
        else:
            key = prefix + "." + k
        #print k,v
        if isinstance(v, dict):
            y.update(flatten_dict(v,prefix=key))
        else:
            y[key]=v
    
    return y

print flatten_dict ({'a': 1, 'b': {'x': 2, 'y': 3, 'z': {'p': 5}}, 'c': 4})
