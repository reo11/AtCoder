from math import sqrt
a, b, c = map(int, input().split())

# sqrt(a) + sqrt(b) < sqrt(c)
# 2 * sqrt(ab) < c - a - b
# 4 * a * b < (c - a - b) ** 2

if 0 >= c - a - b:
    print("No")
    exit()

if 4 * a * b < (c - a - b) ** 2:
    print("Yes")
else:
    print("No")