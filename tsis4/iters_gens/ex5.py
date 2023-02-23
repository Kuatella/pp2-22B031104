def downFromN(n):
    a = n

    while a >= 0:
        yield a
        a -= 1

x = int(input())    

for i in downFromN(x):
    print(i)