# https://atcoder.jp/contests/dp/tasks/dp_n
import sys

sys.setrecursionlimit(20000000)

n = int(input())
a = list(map(int, input().split()))
b = [0]
sum_ = 0
for i in range(n):
    sum_ += a[i]
    b.append(sum_)

INIT = -1
dp = [[INIT for _ in range(n + 1)] for _ in range(n + 1)]


def solve(left, r):
    if dp[left][r] != -1:
        return dp[left][r]

    if abs(left - r) == 0:
        return 0

    res = 10**12
    for mid in range(left, r):
        res = min(res, solve(left, mid) + solve(mid + 1, r))

    dp[left][r] = res + (b[r] - b[left - 1])
    return dp[left][r]


print(solve(1, n))
