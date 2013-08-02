def iterjoin(x,y):
    for a in x:
        yield a
    for b in y:
        yield b

def main():
    x = iter([1,2,3])
    y = iter([4,5,6])
    z = iterjoin(x,y)
    print list(z)

if __name__ == "__main__":
    main()
