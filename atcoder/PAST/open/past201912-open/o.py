import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = 6 * n
a = [list(map(int, input().split())) for i in range(n)]


def compression(a):
    numbers = []
    for i in range(n):
        for v in a[i]:
            numbers.append(v)
    numbers.sort()
    d = {}
    for i, k in enumerate(numbers):
        d[k] = i
    for i in range(n):
        for j in range(6):
            a[i][j] = d[a[i][j]]
    return a


# aを座圧
a = compression(a)
dp = [1 for _ in range(n + 1)]

# 出目が入力された時に、対応するダイスの番号を引けるようにしておく
dise = defaultdict(lambda: [])
for i in range(n):
    for k in range(6):
        dise[a[i][k]] = i

# dp[i] = i番目のダイスの期待値の最大値
# 最良の選択肢を選び続けるので、降順で探索すると、
# それまでに登場した最も良い期待値を持つダイスを使うことになる
dp_max = 1
for i in reversed(range(m)):
    dp[dise[j]] += dp_max / 6
    dp_max = max(dp_max, dp[dise[i]])

print(dp_max)
