# Multiple Gift
import math

x, y = map(int, input().split())

i = 0
while x * 2 ** i <= y:
    i += 1
print(i)
