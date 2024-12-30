n, m = map(int, input().split())
h = list(map(int, input().split()))

ans = 0

for i in range(n):
    if m >= h[i]:
        ans += 1
        m -= h[i]
    else:
        break
print(ans)
