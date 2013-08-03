def my_sum(*args):
    sum  = args[0]
    for i in args[1:]:
        sum = sum + i

    return sum

print my_sum(1,2,3,4,5)

