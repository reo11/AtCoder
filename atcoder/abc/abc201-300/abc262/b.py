from collections import defaultdict

n, m = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: False))

for _ in range(m):
    u, v = map(int, input().split())
    edges[u][v] = True

ans = 0
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            if edges[a][b] and edges[b][c] and edges[a][c]:
                ans += 1
print(ans)
