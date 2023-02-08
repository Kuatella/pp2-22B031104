# 3
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Ractangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width



sh = Ractangle(5,4)
print(sh.area())