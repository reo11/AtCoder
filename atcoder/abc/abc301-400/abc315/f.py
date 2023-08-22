import sys
import math
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


def dist(i, j):
    return math.sqrt((xy[i - 1][0] - xy[j - 1][0]) ** 2 + (xy[i - 1][1] - xy[j - 1][1]) ** 2)

def penalty(i):
    if i == 0:
        return 0
    else:
        return 2**(i - 1)


n = int(input())
xy = []
INF = float("inf")

for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])


dist_sum = 0
for i in range(1, n):
    dist_sum += dist(i - 1, i)

max_value = 1000
for i in range(1, 1000):
    if penalty(i) > dist_sum:
        max_value = i + 1
        break

# dp
# ペナルティが大きいので、無視する数は20以下くらい
# dp[i][j][k] = i番目までの頂点を通過した時に最後にjを訪れて無視した頂点がk個の時の最小コスト
dp = [[INF for _ in range(max_value + 1)] for _ in range(n + 1)]
# 頂点1からスタート
dp[1][0] = 0

for start in range(1, n + 1): # 次に訪れるべき頂点
    for penalty_count in range(max_value): # それまで無視した頂点数
        for skip_count in range(1, max_value): # 連続で無視する頂点数
            if start + skip_count > n:
                break
            if penalty_count + skip_count > max_value:
                break
            base = dp[start][penalty_count] + dist(start, start + skip_count) + penalty(penalty_count + skip_count - 1) - penalty(penalty_count)
            dp[start + skip_count][penalty_count + skip_count - 1] = min(dp[start + skip_count][penalty_count + skip_count - 1], base)
ans = INF
# print(dp)
for v in dp[n]:
    ans = min(ans, v)
print(ans)