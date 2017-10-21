# Write a script to sum of the first n positive integers
import random
n = 20
s = 0
i = 0
a = -10
b = 10
while i <= n:
    number = random.randint(a, b)
    if number > 0:
        print(number)
        s = s + number
    i = i + 1
print("S = ", s)
