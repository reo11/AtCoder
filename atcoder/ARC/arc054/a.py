l, x, y, s, d = map(int, input().split())
s = l + s
d1 = d
d2 = l + d
d3 = 2 * l + d

v1 = (x + y) # 右
v2 = -(x - y) # 左

ans = 10**9
for d in [d1, d2, d3]:
   if s < d:
      ans = min(ans, (d - s) / v1)
   elif s > d:
      if v2 > 0:
         ans = min(ans, (s - d) / v2)
   else:
      ans = 0
print(ans)

