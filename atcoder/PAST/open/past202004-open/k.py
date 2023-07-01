n = int(input())
s = input()

c = list(map(int, input().split()))
d = list(map(int, input().split()))

# dp
dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
# dp[i][j] := sのi文字目までで左にある未処理の(の数にするのにかかる最小コスト
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(n + 1):
        if s[i - 1] == "(":
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + d[i - 1])
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            if j + 1 < n + 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + c[i - 1])
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + d[i - 1])
            if j + 1 < n + 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + c[i - 1])
print(dp[-1][0])
