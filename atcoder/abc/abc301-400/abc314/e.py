import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
c = []
p = []
s = []
INF = float("inf")
for _ in range(n):
    x = list(map(int, input().split()))
    ci = x[0]
    pi = x[1]
    si = x[2:]
    c.append(ci)
    p.append(pi)
    s.append(si)

# 期待値DP
# 得点iをコストj払って達成する確率

dp = defaultdict(lambda: defaultdict(lambda: 0))
dp[0][0] = 1

# 配るDP
for i in range(m):
    for j in dp[i].keys():
        # k番目のルーレットを回す
        for k in range(n):
            ci = c[k]
            pi = p[k]
            si = s[k]
            for sij in si:
                dp[i + sij][j + ci] += dp[i][j] * (1 / pi)

ans = 0
for i in dp.keys():
    if i < m:
        continue
    for cost, p in dp[i].items():
        ans += p * cost
print(ans)