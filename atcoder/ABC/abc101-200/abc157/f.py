from pylab import *
import random
from math import sqrt
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
xyc = [[i for i in list(map(int, input().split()))] for i in range(n)]

def dis(X, Y, x, y):
    return sqrt((X-x)**2 + (Y-y)**2)

def cost(X, Y, k):
    global xyc
    t = []
    for x, y, c in xyc:
        t.append(c * dis(X, Y, x, y))
    t.sort()
    return t[k-1]


