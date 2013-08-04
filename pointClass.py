class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    
    def __mul__(self,value):
        return Point(self.x * value, self.y * value)
    
    def __repr__(self):
            return "Point(%d, %d)" % (self.x, self.y)

p1 = Point(1, 3)
p2 = Point(4, 4)
print p1 + p2

print Point(1, 2) * 5
