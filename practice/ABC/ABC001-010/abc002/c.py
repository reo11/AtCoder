from math import sqrt
xy = list(map(int, input().split()))

def dis(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

a = dis(xy[0], xy[1], xy[2], xy[3])
b = dis(xy[2], xy[3], xy[4], xy[5])
c = dis(xy[4], xy[5], xy[0], xy[1])

s = (a+b+c) / 2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)