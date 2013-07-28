def myreverse(x):
    result = []
    for i in range(len(x)):
        result.append(x[-1-i])

    return result

print myreverse(range(1,5))
