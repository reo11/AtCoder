import math
h = int(input())
w = int(input())
n = int(input())

a = max(h, w)
print(math.ceil(n / a))