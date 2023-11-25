n, l, r = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for ai in a:
    x1 = abs(l - ai)
    x2 = abs(r - ai)
    min_x = min(x1, x2)
    if l <= ai and ai <= r:
        min_x = 0
    for x in [abs(min_x - ai), abs(min_x + ai)]:
        if l <= x and x <= r:
            ans.append(x)
            break
print(*ans, sep=" ")
