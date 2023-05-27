import math
a, b = map(int, input().split())

c = a // b
if c * b == a:
    print(c)
else:
    print(c + 1)