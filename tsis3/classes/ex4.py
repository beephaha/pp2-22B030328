import math

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    
    def move(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y
        
    def dist(self, point):
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
pointt1 = point(2, 3)
pointt2 = point(4, 6)
print(pointt1.dist(pointt2))
print(pointt1.show())
print(pointt2.move(3, 4))    