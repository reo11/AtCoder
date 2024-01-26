import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 前からDP
# あり得る最大と最小のA個数を持っておく
# 最後に後ろからたどっていけば行けるはず

INF = 2**30
dp = [[[INF, 0] for _ in range(2)] for _ in range(2 * n)]
dp[0][0] = [1, 1]
dp[0][1] = [0, 0]

# O(2n) => O(10^6)
for i in range(1, 2 * n):
    if a[i - 1] <= a[i]:
        dp[i][0][0] = min(dp[i][0][0], dp[i - 1][0][0] + 1)
        dp[i][0][1] = max(dp[i][0][1], dp[i - 1][0][1] + 1)
    if b[i - 1] <= a[i]:
        dp[i][0][0] = min(dp[i][0][0], dp[i - 1][1][0] + 1)
        dp[i][0][1] = max(dp[i][0][1], dp[i - 1][1][1] + 1)
    if a[i - 1] <= b[i]:
        dp[i][1][0] = min(dp[i][1][0], dp[i - 1][0][0])
        dp[i][1][1] = max(dp[i][1][1], dp[i - 1][0][1])
    if b[i - 1] <= b[i]:
        dp[i][1][0] = min(dp[i][1][0], dp[i - 1][1][0])
        dp[i][1][1] = max(dp[i][1][1], dp[i - 1][1][1])

# pprint(dp)
# 後ろから復元

ans = []
cnt_A = n
pre = -1
# O(2n) => O(10^6)
for i in reversed(range(2 * n)):
    f = False
    for j in range(2):
        if j == 0:
            if pre == 0 and a[i] > a[i + 1]:
                continue
            if pre == 1 and a[i] > b[i + 1]:
                continue
        else:
            if pre == 0 and b[i] > a[i + 1]:
                continue
            if pre == 1 and b[i] > b[i + 1]:
                continue
        if dp[i][j][0] <= cnt_A <= dp[i][j][1]:
            if not j:
                c = "A"
                pre = 0
                cnt_A -= 1
            else:
                c = "B"
                pre = 1
            ans.append(c)
            f = True
            break
    if not f:
        print(-1)
        exit()

print("".join(reversed(ans)))
