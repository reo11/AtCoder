n, s, m, l = map(int, input().split())
INF = float("inf")
ans = INF
for i in range(20):
    for j in range(20):
        for k in range(20):
            if (i * 6) + (j * 8) + (12 * k) >= n:
                ans = min(ans, i * s + j * m + k * l)
print(ans)
