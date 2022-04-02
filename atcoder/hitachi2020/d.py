import sys

input = sys.stdin.readline

n, t = map(int, input().split())
ab = []
a0 = []
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        a0.append(b)
    else:
        ab.append([(a / (b + 1)), a, b])
a0.sort()
ab.sort(reverse=True)

INF = 10 ** 12
N = 40
m = len(ab)
dp = [[INF for _ in range(N)] for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    a, b = ab[i - 1][1], ab[i - 1][2]
    dp[i][0] = 0
    for j in range(1, N):
        tmp = 1 + dp[i - 1][j - 1]
        dp[i][j] = min(dp[i - 1][j], tmp + (a * tmp + b))
ans = 0
for i in range(N):
    time = dp[-1][i]
    ans_tmp = i
    if time <= t:
        for v in a0:
            time += 1 + v
            if time <= t:
                ans_tmp += 1
            else:
                break
        ans = max(ans, ans_tmp)

print(ans)
