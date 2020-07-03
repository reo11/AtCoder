from math import sqrt
x = [0, 0, 0]
y = [0, 0, 0]
x[0], y[0], r = map(int, input().split())
x[1], y[1], x[2], y[2] = map(int, input().split())

def dist(x1, x2, y1, y2):
   return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def check1(x, y, r):
   # 円が四角に完全に含まれるか
   res1 = x[1] <= x[0] - r
   res2 = x[0] + r <= x[2]
   res3 = y[1] <= y[0] - r
   res4 = y[0] + r <= y[2]
   return res1 and res2 and res3 and res4

def check2(x, y, r):
   # 四角が円に完全に含まれるか
   res1 = dist(x[0], x[1], y[0], y[1]) <= r
   res2 = dist(x[0], x[1], y[0], y[2]) <= r
   res3 = dist(x[0], x[2], y[0], y[1]) <= r
   res4 = dist(x[0], x[2], y[0], y[2]) <= r
   return res1 and res2 and res3 and res4

print(["YES", "NO"][check1(x, y, r)])
print(["YES", "NO"][check2(x, y, r)])