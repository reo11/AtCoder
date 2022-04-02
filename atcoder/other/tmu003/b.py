# I - イウィ
s = input()
n = len(s)

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for l in range(1, n + 1):
    for i in range(n - l + 1):
        e = i + l - 1
        for j in range(i + 1, e):
            dp[i][e] = max(dp[i][e], dp[i][j] + dp[j + 1][e])
        if s[i] == "i" and s[e] == "i":
            for j in range(i + 1, e):
                if s[j] == "w":
                    fail = False
                    len_ = (j - 1) - (i + 1) + 1
                    if len_ and not (len_ >= 3 and dp[i + 1][j - 1] == len_):
                        fail = True
                    len_ = (e - 1) - (j + 1) + 1
                    if len_ and not (len_ >= 3 and dp[j + 1][e - 1] == len_):
                        fail = True
                    if not fail:
                        dp[i][e] = e - i + 1
                        break
print(dp[0][n - 1] // 3)
