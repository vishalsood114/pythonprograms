def mysum(x):
    sum  = x[0]
    for i in x[1:]:
        sum = sum + i

    return sum

print mysum([1,2,3,4,5])
print mysum(range(10))
print mysum(['hello','world','vishal'])

