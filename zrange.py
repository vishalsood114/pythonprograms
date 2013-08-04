class zrange:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __len__(self):
        return (self.b-self.a)

    def __getitem__ (self,i):
        if 0 <= i <= (self.b-self.a):
            return self.a + i
        else:
            return IndexError(i)

z = zrange(3,8)
print len(z)
print z[1]
print z[2]
