n, m = map(int, input().split())
INF = 10 ** 10
ab = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    ab[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    ab[a - 1][b - 1] = 1
    ab[b - 1][a - 1] = 1

# warshall_floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            ab[i][j] = min(ab[i][j], ab[i][k] + ab[k][j])

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if ab[i][j] == 2:
            count += 1
    print(count)
