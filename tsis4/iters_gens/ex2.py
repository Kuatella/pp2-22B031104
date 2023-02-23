def showEvens(n):
    a = 0

    while a <= n:
        yield a
        a += 2

x = int(input())

for i in showEvens(x):
    print(i, end = ", ")