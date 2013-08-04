class yrange:
    def __init__(self,n):
        self.n = n

    def __len__(self):
        return self.n

y = yrange(10)
print len(y)

