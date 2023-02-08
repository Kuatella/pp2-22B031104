# 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
        
    def move(self, other):
        self.x = other.x
        self.y = other.y


    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


point1 = Point(10, 4)
point2 = Point(5, 12)

point1.show()
print(point1.dist(point2))
point1.move(point2)
point2.show()