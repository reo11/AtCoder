import sys
from functools import lru_cache

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

h, w, n = map(int, input().split())
dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
s = [[True for _ in range(w)] for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = False

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i - 1][j - 1]:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = 0
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        ans += dp[i][j]
print(ans)
