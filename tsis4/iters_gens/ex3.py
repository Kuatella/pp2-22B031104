def threeUndfour(n):
    a = 12

    while a <= n:
        yield a
        a += 12

x = int(input())

for i in threeUndfour(x):
    print(i)