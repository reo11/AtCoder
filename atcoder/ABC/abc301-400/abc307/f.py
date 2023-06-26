import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
n, m = map(int, input().split())
uvw = []
for _ in range(m):
    u, v, w = map(int, input().split())
    uvw.append((u, v, w))
k = int(input())
a = list(map(int, input().split()))
d = int(input())
x = list(map(int, input().split()))

def solve1():
    # 愚直解(TLE)
    ans = [-1 for _ in range(n)]
    for a_i in a:
        ans[a_i - 1] = 0
