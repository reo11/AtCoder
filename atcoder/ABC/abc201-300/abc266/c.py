import numpy as np
points = []

for _ in range(4):
    x, y = map(int, input().split())
    points.append(np.array([x, y]))

flag = True
# 外積のΘは反時計回りなので、全ての角の外積を求めれば良い
# 180を超えるとマイナスになるので外積の正負をチェック
for i in range(4):
    j = (i + 1) % 4
    k = (j + 1) % 4
    vec_a = points[j] - points[i]
    vec_b = points[k] - points[j]
    if np.cross(vec_a, vec_b) < 0:
        flag = False

if flag:
    print("Yes")
else:
    print("No")