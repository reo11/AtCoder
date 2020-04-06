from math import sqrt
n = int(input())
xy = [input().split() for _ in range(n)]
xy = [(int(x[0]), int(x[1]))for x in xy]

def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def area(n1, n2, n3):
    x1, y1 = xy[n1]
    x2, y2 = xy[n2]
    x3, y3 = xy[n3]
    a = dist(x1, y1, x2, y2)
    b = dist(x2, y2, x3, y3)
    c = dist(x1, y1, x3, y3)
    s = (a + b + c) / 2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            t = area(i, j, k)
            print(i, j, k, t)
            if (t + 0.0001) - int(t + 0.0001) < 0.0001:
                count += 1
print(count//6)
