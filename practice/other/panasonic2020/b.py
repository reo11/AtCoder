from math import ceil
h, w = map(int, input().split())

if h == 1 or w == 1:
    print(1)
    exit()

if w % 2 == 0:
    ans = (w // 2) * h
else:
    ans = (w // 2) * h + (ceil(h / 2))
print(ans)