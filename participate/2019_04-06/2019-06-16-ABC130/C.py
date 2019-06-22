w, h, x, y = map(int, input().split())

ans = 0
if x + x == w and y + y == h:
    ans = 1

print("{} {}".format(w * h / 2, ans))
