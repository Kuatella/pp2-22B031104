# 6

def isPrime(n):
  for i in range(2,int(n/2)+1):
    if (n%i) == 0:
      return False
  return True

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(list(filter(lambda n: isPrime(n), l)))
