def product(x):
    product = x[0]
    for i in x[1:]:
        product = product * i

    return product

print product(range(1,4))

def factorial(x):
    return product(range(1,x+1))

print factorial(4)
