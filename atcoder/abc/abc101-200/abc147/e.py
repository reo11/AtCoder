from queue import Queue

h, w = map(int, input().split())
a = [[int(i) for i in input().split()] for i in range(h)]
b = [[int(i) for i in input().split()] for i in range(h)]
ab = []
for i in range(h):
    l = []
    for j in range(w):
        l.append(abs(a[i][j] - b[i][j]))
    ab.append(l)

q = Queue()
is_checked = [[False for _ in range(w)] for _ in range(h)]
dp = [[[False for _ in range(25601)] for _ in range(w)] for _ in range(h)]

# 幅優先的な
q.put((0, 0))

while True:
    if q.empty():
        break
    else:
        (x, y) = q.get()
        v = ab[y][x]
        if x == 0 and y == 0:
            dp[y][x][12800 + v] = True
            dp[y][x][12800 - v] = True
        if x > 0:
            l = []
            for i in range(25601):
                if dp[y][x - 1][i]:
                    l.append(i)
            for i in l:
                dp[y][x][i + v] = True
                dp[y][x][i - v] = True
        if y > 0:
            l = []
            for i in range(25601):
                if dp[y - 1][x][i]:
                    l.append(i)
            for i in l:
                dp[y][x][i + v] = True
                dp[y][x][i - v] = True
        if x < w - 1:
            if not is_checked[y][x + 1]:
                q.put((x + 1, y))
                is_checked[y][x + 1] = True
        if y < h - 1:
            if not is_checked[y + 1][x]:
                q.put((x, y + 1))
                is_checked[y + 1][x] = True

v = ab[h - 1][w - 1]
l = []
for i in range(25601):
    if dp[h - 1][w - 2][i]:
        l.append(i)
for i in l:
    dp[h - 1][w - 1][i + v] = True
    dp[h - 1][w - 1][i - v] = True

l = []
for i in range(25601):
    if dp[h - 2][w - 1][i]:
        l.append(i)
for i in l:
    dp[h - 1][w - 1][i + v] = True
    dp[h - 1][w - 1][i - v] = True

ans = 10**9
for i in range(25601):
    if dp[h - 1][w - 1][i]:
        ans = min(ans, abs(12800 - i))

print(ans)
