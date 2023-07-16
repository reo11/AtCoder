MOD = 10 ** 9 + 7
l, r = map(int, input().split())

# bit DP
# 10^18 -> 2^60くらい
# rからlを引く


def solve(num):
    if num == 1 or num == 0:
        return 0
    b = str(bin(num)[2:])
    n = len(b)
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    if n > 2:
        dp[2] = 2
    for i in range(3, n):
        if b[-i] == "1":
            dp[i] += sum(dp[:i])
            dp[i] %= MOD
    print(dp)
    return dp[-1]


r_a = solve(r)
l_a = solve(l - 1)

ans = r_a - l_a
print(ans)
