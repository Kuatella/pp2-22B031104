# 1. Write a Python program with builtin function to multiply all the numbers in a list

list_1 = list(map(int, input().split()))
product_1 = 1

for i in range(len(list_1)):
    product_1 *= list_1[i]
    
print(product_1)

#__________________________________________________________________________________________________________________________________________________

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

string_1 = str(input())

uppr = 0
lowr = 0

for i in string_1:
    if i.isupper():
        uppr += 1
    elif i.islower():
        lowr += 1

print(uppr, lowr, sep = " ")

#__________________________________________________________________________________________________________________________________________________

# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isPolindrom(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        
    return True

string_2 = str(input())

if isPolindrom(string_2):
    print("Yes")
else:
    print("No")

word = input()
print(word[::-1] == word)

#__________________________________________________________________________________________________________________________________________________

# 4. Write a Python program that invoke square root function after specific milliseconds.

import time
import math

num = int(input())
mss = int(input())
root = math.sqrt(num)

time.sleep((mss/1000))

print(f"Square root of {num} after {mss} miliseconds is {root}")

#__________________________________________________________________________________________________________________________________________________

# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.

tuple_1 = (0, 1, 2, True, False, "Hhhu")
print(all(tuple_1))