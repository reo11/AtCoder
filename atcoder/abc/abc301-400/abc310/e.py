n = int(input())
s = list(map(int, list(input())))
ans = 0
dp = [[0] * (n + 1) for _ in range(2)]

for i in range(1, n + 1):
    s_i = s[i - 1]
    for j in range(2):
        dp[not (j and s_i)][i] += dp[j][i - 1]
    dp[s_i][i] += 1
    ans += dp[1][i]

print(ans)
