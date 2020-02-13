from math import ceil
n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))

h = [x % (a+b) for x in h]
h.sort()

point = 0
u = []
for v in h:
    if v == 0:
        u.append(ceil((a+b)/a))
    elif v <= a:
        point += 1
    else:
        u.append(ceil(v/a))

u.sort()
for v in u:
    if k - (v - 1) >= 0:
        point += 1
        k = k - (v - 1)
    else:
        break
print(point)