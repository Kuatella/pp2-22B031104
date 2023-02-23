def area_of_trapezoid(height, upper_base, lower_base):
    area = height * (upper_base + lower_base) / 2
    return area

h = int(input())
a = int(input())
b = int(input())

print(area_of_trapezoid(h, a, b))