# A - ゲーム
# from pprint import pprint
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = 0

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# どちらかの山札が0とした場合、結果は一意に定まる
dp[1][0] = a[n-1]
for i in range(2, n+1):
    dp[i][0] = dp[i-2][0] + a[-i]

dp[0][1] = b[m-1]
for i in range(2, m+1):
    dp[0][i] = dp[0][i-2] + b[-i]

# 自分が取る/取らされるスコアの中で小さいものを除外する
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i][0] + dp[i-1][0] + dp[0][j] + dp[0][j-1] - min(dp[i-1][j], dp[i][j-1])
# pprint(dp)
print(dp[n][m])