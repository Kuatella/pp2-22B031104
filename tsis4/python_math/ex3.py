import math

def area_of_poligon(sides, sideLength):
    area = sides/4 * sideLength**2 * math.tan(math.radians(180/sides))
    return math.ceil(area)

n = int(input())
l = int(input())

print(area_of_poligon(n, l))