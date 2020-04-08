k = int(input())
r = [int(input()) for _ in range(2**k)]

dp = [[0 for _ in range(k+1)] for _ in range(2**k+1)]
for i in range(2**k+1):
    dp[i][0] = 1

def p(i, j):
    return 1 / (1 + 10**((r[j-1] - r[i-1])/400))

for i in range(1, k+1):
    for j in range(1, (2**k)+1):
        bot = ((j-1) // (2**i)) * (2**i) + 1
        mid = bot + 2 ** (i - 1)
        top = bot + 2 ** i
        # print(bot, mid, top)
        if bot <= j < mid:
            for l in range(mid, top):
                dp[j][i] += p(j, l) * dp[j][i-1] * dp[l][i-1]
        else:
            for l in range(bot, mid):
                dp[j][i] += p(j, l) * dp[j][i-1] * dp[l][i-1]
ans = []
for i in range(2**k):
    ans.append('{:.10f}'.format(dp[i+1][k]))
print("\n".join(ans))


