x, y, z = map(int, input().split())
s = input()
n = len(s)
# DPをする
# dp[i][j]: jの状態でi文字目まで出力するためにかかる最短時間
# 状態は、caps_lockがオフかオンかの2通り
dp = [[float("inf") for _ in range(2)] for _ in range(n + 1)]
dp[0][0] = 0
dp[0][1] = z

for i in range(1, n + 1):
    c_i = s[i - 1]
    if c_i == "A":
        # offの遷移
        dp[i][0] = min(dp[i - 1][0] + y, dp[i - 1][1] + z + x)
        # onの遷移
        dp[i][1] = min(dp[i - 1][1] + x, dp[i - 1][0] + z + y)
    else:
        # offの遷移
        dp[i][0] = min(dp[i - 1][0] + x, dp[i - 1][1] + z + y)
        # onの遷移
        dp[i][1] = min(dp[i - 1][1] + y, dp[i - 1][0] + z + x)
print(min(dp[n]))