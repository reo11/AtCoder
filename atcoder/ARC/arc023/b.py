r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]

ans = 0
for i in range(r):
    for j in range(c):
        if (i + j) % 2 == d % 2 and (i + j) <= d:
            ans = max(ans, a[i][j])
print(ans)
