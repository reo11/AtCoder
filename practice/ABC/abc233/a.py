import math

x, y = map(int, input().split())

if (y - x) / 10 <= 0:
    print(0)
else:
    print(math.ceil((y - x) / 10))
