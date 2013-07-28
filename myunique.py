def myunique(x):
    result = []
    for i in x:
        if i not in result:
            result.append(i)

    return result

print myunique([1,2,1,3,2,5])
