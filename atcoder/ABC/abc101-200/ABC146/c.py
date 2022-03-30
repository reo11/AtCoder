import math
a, b, x = map(int, input().split())

cur = 10 ** 9
dis = cur // 2
l = []
while True:
    if len(l) > 10:
        break
    cal = (a * cur) + (b * len(str(cur)))
    if cal < x:
        cur += dis
    else:
        cur -= dis
    if dis == 1:
        l.append(cur)
    dis = math.ceil(dis/2)
ans = 0
for i in l:
    cal = (a * i) + (b * len(str(i)))
    if cal <= x:
        ans = max(ans, i)
print(min(ans, 10**9))


