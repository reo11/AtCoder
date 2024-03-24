n = int(input())
s = list(input())
costs = list(map(int, input().split()))

# 右端がjの時のi盤面の最小コストをdpしていく
# 同様に左端がjの時のi番目の盤面の最小コストをdp

dp1 = [[0 for _ in range(2)] for _ in range(n)]
dp2 = [[0 for _ in range(2)] for _ in range(n)]

# 右端
if s[0] == "0":
    dp1[0][1] = costs[0]
else:
    dp1[0][0] = costs[0]

for i in range(1, n):
    if s[i] == "0":
        dp1[i][0] = dp1[i - 1][1]
        dp1[i][1] = dp1[i - 1][0] + costs[i]
    else:
        dp1[i][0] = dp1[i - 1][1] + costs[i]
        dp1[i][1] = dp1[i - 1][0]

costs = costs[::-1]
s = s[::-1]

# 左端
if s[0] == "0":
    dp2[0][1] = costs[0]
else:
    dp2[0][0] = costs[0]

for i in range(1, n):
    if s[i] == "0":
        dp2[i][0] = dp2[i - 1][1]
        dp2[i][1] = dp2[i - 1][0] + costs[i]
    else:
        dp2[i][0] = dp2[i - 1][1] + costs[i]
        dp2[i][1] = dp2[i - 1][0]

ans = float("inf")

for i in range(n - 1):
    # print(i, ans, dp1[i][0] + dp2[n - i - 2][0], dp1[i][1] + dp2[n - i - 2][1])
    ans = min(ans, dp1[i][0] + dp2[n - i - 2][0], dp1[i][1] + dp2[n - i - 2][1])
print(ans)