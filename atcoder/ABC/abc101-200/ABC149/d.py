n, k = map(int, input().split())
r, s, p_ = list(map(int, input().split()))
p = [r, p_, s]
t = str(input())

dp = [[0 for _ in range(3)] for _ in range(n + 1)]
# 0: r, 1: p, 2: s
d = {"r": 1, "p": 2, "s": 0}
for i in range(1, n + 1):
    v_num = d[t[i - 1]]
    for j in range(3):
        # 勝てる数字
        if i < k + 1:
            if j == v_num:
                dp[i][j] = p[j]
            else:
                dp[i][j] = 0
        else:
            tmp = dp[i - k][:]
            tmp.pop(j)
            if j == v_num:
                dp[i][j] = max(tmp) + p[j]
            else:
                dp[i][j] = max(tmp)
ans = 0
for i in range(1, k + 1):
    ans += max(dp[-i])
print(ans)
