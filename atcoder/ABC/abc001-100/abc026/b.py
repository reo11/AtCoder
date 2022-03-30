from math import pi
n = int(input())
r = []
ans = 0
for i in range(n):
    r.append(int(input()))
r.sort()
for v in r[::-1][0::2]:
    ans += v * v * pi
for v in r[::-1][1::2]:
    ans -= v * v * pi
print(ans)