import sys

def izip(a,b):
    a = iter(a)
    b = iter(b)
    while True:
        yield a.next(),b.next()

def main():
    z = izip("hello", "world")
    print next(z)
    print next(z)


if __name__ == "__main__":
    main()
