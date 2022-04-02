from heapq import heappop, heappush

H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == "S":
            sx, sy = j, i
        elif s[i][j] == "G":
            gx, gy = j, i

left, right = 0, T
while left < right - 1:
    mid = (left + right) // 2
    w = [[float("inf")] * W for _ in range(H)]
    w[sy][sx] = 0

    queue = [(0, sx, sy)]
    while queue:
        cost, x, y = heappop(queue)
        if w[y][x] < cost:
            continue

        for x_, y_ in zip([x + 1, x - 1, x, x], [y, y, y + 1, y - 1]):
            if 0 <= x_ <= W - 1 and 0 <= y_ <= H - 1:
                t = 0
                if s[y_][x_] == "#":
                    t = mid
                elif s[y_][x_] == ".":
                    t = 1

                if cost + t < w[y_][x_]:
                    w[y_][x_] = cost + t
                    heappush(queue, (cost + t, x_, y_))

    if w[gy][gx] < T:
        left = mid
    else:
        right = mid

print(left)
