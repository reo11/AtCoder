n, x = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
for si in s:
    if si <= x:
        ans += si
print(ans)
