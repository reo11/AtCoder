from collections import defaultdict
x = defaultdict(int)
y = defaultdict(int)
ans_x = 0
ans_y = 0

for _ in range(3):
    x_, y_ = map(int, input().split())
    x[x_] += 1
    y[y_] += 1

for x_, count in x.items():
    if count == 1:
        ans_x = x_

for y_, count in y.items():
    if count == 1:
        ans_y = y_


print(ans_x, ans_y)