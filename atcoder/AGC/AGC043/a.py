from collections import deque

h, w = map(int, input().split())
s = [[i for i in list(str(input()))] for i in range(h)]
INF = 10**9
dp = [[INF for _ in range(w)] for _ in range(h)]


if s[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0
que = deque()
que.append((0, 0))
is_checked = [[False for _ in range(w)] for _ in range(h)]
while len(que) > 0:
    y, x = que.popleft()
    if y + 1 < h:
        if s[y][x] != s[y + 1][x]:
            dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + 1)
        else:
            dp[y + 1][x] = min(dp[y + 1][x], dp[y][x])
        if not is_checked[y + 1][x]:
            que.append((y + 1, x))
            is_checked[y + 1][x] = True
    if x + 1 < w:
        if s[y][x] != s[y][x + 1]:
            dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + 1)
        else:
            dp[y][x + 1] = min(dp[y][x + 1], dp[y][x])
        if not is_checked[y][x + 1]:
            que.append((y, x + 1))
            is_checked[y][x + 1] = True
if s[h - 1][w - 1] == "#":
    dp[h - 1][w - 1] += 1
print(dp[h - 1][w - 1] // 2)
