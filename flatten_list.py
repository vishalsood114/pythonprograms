def flatten_list(x):
    y = []
    for a in x:
        if isinstance (a, list):
            y.extend(flatten_list(a))
        else:
            y.append(a)
    return y


print flatten_list([[1, 2], [3, 4, [5]]])
            
