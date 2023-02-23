def squares(a, b):
    x = 1
    
    while x**2 < a:
        x += 1
        continue
    
    while x**2 <= b:
        yield x**2
        x += 1

a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)
