MOD = 998244353
MAX = 5001

q, k = map(int, input().split())
ans = []
dp = [0 for _ in range(MAX)]
dp[0] = 1

for _ in range(q):
    sign, num = input().split()
    num = int(num)
    if sign == "+":
        for i in reversed(range(num, k + 1)):
            dp[i] += dp[i - num]
            dp[i] %= MOD
    else:
        for i in range(num, k + 1):
            dp[i] -= dp[i - num]
            dp[i] %= MOD
    dp = dp[:]
    ans.append(dp[k])
print(*ans, sep="\n")
