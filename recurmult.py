import sys

def recurmult(x,n):
    if n == 0:
        return 0
    else:
        return (x + recurmult(x,n-1))

print recurmult(4,5)
