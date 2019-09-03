from math import ceil
a, b = map(int, input().split())
m = ceil((b-1)/(a-1))
print(m)