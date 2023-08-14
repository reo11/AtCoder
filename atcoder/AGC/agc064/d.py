from collections import defaultdict

MOD = 998244353
colors = {
    "R": 0,
    "B": 1,
}

n = int(input())
s = list(input())
counter = defaultdict(lambda: 0)
for si in s:
    if si == "R":
        counter["R"] += 1
    else:
        counter["B"] += 1

# DPに見える
# dp[i][j][k] = i番目に今までBをj個使っている時にkを使った時の場合の数
dp = [[[0 for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1
dp[0][0][1] = 1

# i番目の色
for i in range(1, n + 1):
    # それまでにj個Bを使っている
    for j in range(i):
        b_count = counter["B"] - j # 使えるBの数
        r_count = n - i - b_count  # 使えるRの数
        if i == n:
            print("print", i, j, r_count, b_count)
        if r_count < 0 or b_count < 0:
            # いずれかがマイナスの場合、そもそもその状況はありえない
            continue
        print(i, j, r_count, b_count)
        if r_count >= 0:
            dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]
            dp[i][j][0] %= MOD
        if b_count >= 0:
            dp[i][j][1] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]
            dp[i][j][1] %= MOD

# print(counter)
print(dp)
print(dp[n][counter["B"] - 1][1])
