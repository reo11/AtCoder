n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

ans_min = a * (n + 1)
for i in range(n + 1):
    j = ((n - i) * e - h - b * i) // (d + e) + 1
    j = max(0, j)
    ans_min = min(i * a + j * c, ans_min)
print(ans_min)
