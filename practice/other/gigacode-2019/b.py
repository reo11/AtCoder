n, x, y, z = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    a, b = ab[i]
    if (a >= x and b >= y) and a + b >= z:
        cnt += 1
print(cnt)