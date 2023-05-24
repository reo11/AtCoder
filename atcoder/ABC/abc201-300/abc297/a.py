n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = -1
for i in range(n - 1):
    if t[i + 1] - t[i] <= d:
        ans = t[i + 1]
        break
print(ans)
