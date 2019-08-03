w, h, n = map(int, input().split())
a_r = w
a_l = 0
a_u = h
a_d = 0
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        a_l = max(a_l, x)
    elif a == 2:
        a_r = min(a_r, x)
    elif a == 3:
        a_d = max(a_d, y)
    else:
        a_u = min(a_u, y)


print(max(0, a_r - a_l) * max(0, a_u - a_d))

