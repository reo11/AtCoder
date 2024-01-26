import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
uvbc = []

for _ in range(m):
    u, v, b, c = map(int, input().split())
    uvbc.append((u, v, b, c))
