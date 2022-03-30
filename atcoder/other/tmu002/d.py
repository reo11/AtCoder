# トランプ挿入ソート
import bisect
import sys
input = sys.stdin.readline
INF = 10**10

n = int(input())
c = [0] * n

for i in range(n):
    c[i] = int(input())

dp = [INF] * (n+1)
dp[0] = -INF

for i in range(n):
    idx = bisect.bisect_right(dp, c[i])
    dp[idx] = c[i]

ans = 0
for i in range(1, len(dp)):
    if dp[i] == INF:
        break
    else:
        ans += 1
ans = n - ans
print(ans)

