from collections import deque
n, d = map(int, input().split())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

is_x = [False for _ in range(n)]
is_x[0] = True
q = deque([0])

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

while len(q) > 0:
    now = q.popleft()
    for i in range(n):
        if i == now:
            continue
        if is_x[i] == False:
            if dist(xy[now][0], xy[now][1], xy[i][0], xy[i][1]) <= d:
                is_x[i] = True
                q.append(i)

ans = []
for i in range(n):
    if is_x[i]:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")