# 018
import numpy as np

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def angle(point1, point2):
    a = np.array([point1.x, point1.y, point1.z])
    b = np.array([point2.x, point2.y, point2.z])
    a_tmp = a - b
    b_tmp = -b
    # aとbの角度
    cos = np.inner(a_tmp, b_tmp)
    print(a, b, cos)
    if cos == 0:
        return 0
    return np.arccos(cos) * 180 / np.pi

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
chokudai = Point(x, y, 0)
ans = []
for _ in range(q):
    e = int(input())
    point = Point(0, -l / 2 * np.sin(2 * np.pi * e / t), l / 2 * (1 - np.cos(2 * np.pi * e / t)))
    ans.append(angle(chokudai, point))
print(ans)
