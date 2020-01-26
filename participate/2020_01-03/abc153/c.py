n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

ans = 0
for i in range(n - k):
    ans += h[i]
print(ans)