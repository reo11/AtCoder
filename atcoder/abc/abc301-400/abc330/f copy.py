from collections import defaultdict

INF = float("inf")
n, k = map(int, input().split())
xy = []
min_max_x = [INF, -INF]
min_max_y = [INF, -INF]
dxy = [(0, 1), (1, 2), (2, 3), (3, 0)]

counter = defaultdict(lambda: defaultdict(lambda: 0))

for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
    counter["x"][x] += 1
    counter["y"][y] += 1
    min_max_x[0] = min(min_max_x[0], x)
    min_max_x[1] = max(min_max_x[1], x)
    min_max_y[0] = min(min_max_y[0], y)
    min_max_y[1] = max(min_max_y[1], y)

# k = 0で生成できる正方形を初期値とする
ans = max((min_max_x[1] - min_max_x[0]), (min_max_y[1] - min_max_y[0]))
positions = [min_max_x[0], min_max_y[1], min_max_x[0] + ans, min_max_y[1] + ans]

while k > 0:
    # dxyiのうち最もコスト消費が少なく小さくできるものを選択しつづける
    if positions[0] == positions[2]:
        break
    next_dxy = [INF, -1]  # (cost, dx, dy)
    for i, (dx, dy) in enumerate(dxy):
        cost = 0
        if dx % 2 == 0:
            cost += counter["x"][positions[dx]]
        else:
            cost += counter["y"][positions[dx]]
        if dy % 2 == 0:
            cost += counter["x"][positions[dy]]
        else:
            cost += counter["y"][positions[dy]]
        if cost < next_dxy[0]:
            next_dxy = (cost, i)
    if i == -1:
        break
    if k - cost < 0:
        break
    if i == 0:
        k -= counter["x"][positions[0]]
        counter["x"][positions[0] + 1] += counter["x"][positions[0]]
        counter["x"][positions[0]] = 0
        k -= counter["y"][positions[1]]
        counter["y"][positions[1] + 1] += counter["y"][positions[1]]
        counter["y"][positions[1]] = 0
        positions[0] += 1
        positions[1] += 1
    elif i == 1:
        k -= counter["y"][positions[1]]
        counter["y"][positions[1] + 1] += counter["y"][positions[1]]
        counter["y"][positions[1]] = 0
        k -= counter["x"][positions[2]]
        counter["x"][positions[2] - 1] += counter["x"][positions[2]]
        counter["x"][positions[2]] = 0
        positions[1] += 1
        positions[2] -= 1
    elif i == 2:
        k -= counter["x"][positions[2]]
        counter["x"][positions[2] - 1] += counter["x"][positions[2]]
        counter["x"][positions[2]] = 0
        k -= counter["y"][positions[3]]
        counter["y"][positions[3] - 1] += counter["y"][positions[3]]
        counter["y"][positions[3]] = 0
        positions[2] -= 1
        positions[3] -= 1
    else:
        k -= counter["y"][positions[3]]
        counter["y"][positions[3] - 1] += counter["y"][positions[3]]
        counter["y"][positions[3]] = 0
        k -= counter["x"][positions[0]]
        counter["x"][positions[0] + 1] += counter["x"][positions[0]]
        counter["x"][positions[0]] = 0
        positions[3] -= 1
        positions[0] += 1
print(positions[2] - positions[0])
