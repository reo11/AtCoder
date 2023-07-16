MOD = 1000000007
h, w, k = map(int, input().split())

dp = [[0 for _ in range(w)] for _ in range(h + 1)]
dp[0][0] = 1

if w == 1:
    print(1)
    exit()

for y in range(1, h + 1):
    for i in range(2 ** (w - 1)):
        bin_i = str(bin(i))[2:]
        if "11" in bin_i:
            continue
        for j in range(1, w):
            if (i >> j - 1) & 1:
                dp[y][j] += dp[y - 1][j - 1]
        for j in range(w - 1):
            if (i >> j) & 1:
                dp[y][j] += dp[y - 1][j + 1]
        for j in range(w):
            f = True
            if j < w:
                f = f and not ((i >> j) & 1)
            if j - 1 >= 0:
                f = f and not ((i >> j - 1) & 1)
            if f:
                dp[y][j] += dp[y - 1][j]
        for i in range(w):
            dp[y][i] %= MOD
# print(dp)
print(dp[h][k - 1])
