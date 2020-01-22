n, m = map(int, input().split())
abc = []
for i in range(m):
    a, b = map(int, input().split())
    c_ = list(map(int, input().split()))
    c = 0
    for v in c_:
        c += 2**(v-1)
    abc.append([a, b, c])

INF = 10**9
dp = [[INF for _ in range(1 << n)]for _ in range((m+1))]

for i in range(m):
    dp[i][0] = 0

for i in range(m):
    for j in range(1 << n):
        s = j | abc[i][2]
        dp[i+1][s] = min(dp[i+1][s], dp[i][j] + abc[i][0])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])
