import sys
from collections import defaultdict
from itertools import permutations
input = sys.stdin.buffer.readline

n, m, R = map(int, input().split())
r = list(map(int, input().split()))
INF = 10**10
dist = [[INF for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

def warshall_floyd(n, d):
    # 空間計算量: O(n^2)
    # 時間計算量: O(n^3)
    # よって、n <= 10^2程度が限界
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

dist = warshall_floyd(n, dist)
ans = INF
for t in permutations(r):
    ans_t = 0
    for i in range(R-1):
        ans_t += dist[t[i]-1][t[i+1]-1]
    ans = min(ans, ans_t)
print(ans)