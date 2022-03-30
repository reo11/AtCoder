n, k = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for v in h:
    if k <= v:
        ans += 1
print(ans)