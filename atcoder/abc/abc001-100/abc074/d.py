import sys

input = sys.stdin.buffer.readline

n = int(input())
INF = 10**12
d = [[INF for _ in range(n)] for _ in range(n)]
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        d[i][j] = a[i][j]


def warshall_floyd(n, d):
    # 空間計算量: O(n^2)
    # 時間計算量: O(n^3)
    # よって、n <= 10^2程度が限界
    dp = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = d[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp


ans = 0
dist = warshall_floyd(n, d)
print(d, dist)
for i in range(n):
    for j in range(i + 1, n):
        if d[i][j] == dist[i][j]:
            ans += d[i][j]
        else:
            print(-1)
            exit()
print(ans)
