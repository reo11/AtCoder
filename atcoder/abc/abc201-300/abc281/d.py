n, k, d = map(int, input().split())
a = list(map(int, input().split()))
INF = float("inf")

# dp[i][j][k] i番目までの数を見た時にj個選択した時のmod d = kの最大値

dp = [[[-INF for _ in range(d)] for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = 0

for i in range(1, n + 1):
    ai = a[i - 1]
    for j in range(1, k + 1):
        for ii in range(d):
            dp[i][j][ii] = max(
                dp[i - 1][j][ii],  # i番目を選択しない
                dp[i - 1][j - 1][(ii - ai) % d] + ai  # i番目を選択する
            )

ans = dp[-1][-1][0]
if ans < 0:
    print(-1)
else:
    print(ans)
