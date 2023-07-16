n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

ans = [[1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    ans[i][i] = 0

for i in range(m):
    for j in range(1, n):
        ans[a[i][j - 1] - 1][a[i][j] - 1] = 0
        ans[a[i][j] - 1][a[i][j - 1] - 1] = 0
out = 0
for i in range(n):
    out += sum(ans[i])
print(out // 2)
