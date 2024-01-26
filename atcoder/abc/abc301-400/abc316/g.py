import sys
from collections import defaultdict, deque

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

h, w = map(int, input().split())
a = []

for i in range(h):
    ai = list(input())
    a.append(ai)
