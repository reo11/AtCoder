import math

x = int(input())

i = 1
while True:
    if i * (i + 1) / 2 >= x:
        print(i)
        break
    i += 1
