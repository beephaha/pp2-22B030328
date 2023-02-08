import math

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def dist(self, point):
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
pt1 = point(2, 3)
pt2 = point(4, 6)

print(point.show())
    