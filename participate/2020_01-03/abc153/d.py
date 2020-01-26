from math import floor
import sys
sys.setrecursionlimit(20000000)

h = int(input())

def f(n):
    if n == 1:
        return 1
    else:
        return f(floor(n/2)) * 2 + 1

print(f(h))