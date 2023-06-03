# bitDP
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
INF = 10 ** 12
dp = [INF for _ in range(2**n)]
pre_dp = [INF for _ in range(2**n)]
dp[0] = 0
pre_dp[0] = 0

for _ in range(m):
    s, c = input().split()
    c = int(c)
    s = "".join(list(map(lambda x: '1' if x == 'Y' else '0', list(s))))
    s = int(s, 2)
    for i in range(2**n):
        t = i | s
        dp[t] = min(dp[t], pre_dp[t], pre_dp[i] + c)
    for i in range(2**n):
        pre_dp[i] = dp[i]
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])


