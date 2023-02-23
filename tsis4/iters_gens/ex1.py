def squareOf(N):
    a = 1

    while a**2 < N:
        yield a**2
        a = a + 1

x = squareOf(26)

for i in squareOf(26):
    print(i)