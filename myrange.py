class myrange:
    def __init__(self,n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        i = self.i
        if i < self.n:
            self.i += 1
            return i

        raise StopIteration()


print myrange(4)

for i in myrange(9):
    print i,
