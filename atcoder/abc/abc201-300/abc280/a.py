ans = 0

h, w = map(int, input().split())
for _ in range(h):
    for si in list(input()):
        if si == "#":
            ans += 1
print(ans)
