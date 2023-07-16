h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
min_a = float("inf")
for a_i in a:
    min_a = min(min_a, min(a_i))
ans = 0
for i in range(h):
    for j in range(w):
        ans += a[i][j] - min_a
print(ans)
