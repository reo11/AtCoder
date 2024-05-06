n = int(input())
# 座標変換
convert = lambda x, y: (x + y, x - y)

xy_groups = [[], []]
for _ in range(n):
    a, b = map(int, input().split())
    xy_groups[(a + b) % 2].append(convert(a, b))

ans = 0
for group_num, xys in enumerate(xy_groups):
    xs, ys = [], []
    for x, y in xys:
        xs.append(x); ys.append(y)
    xs.sort(); ys.sort()
    sum_x, sum_y = 0, 0
    for i in range(len(xys)):
        ans += (xs[i] * i - sum_x + ys[i] * i - sum_y) // 2
        sum_x += xs[i]; sum_y += ys[i]
print(ans)