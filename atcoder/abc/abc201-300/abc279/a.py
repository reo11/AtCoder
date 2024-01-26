s = list(input())

ans = 0

for si in s:
    if si == "v":
        ans += 1
    else:
        ans += 2
print(ans)
