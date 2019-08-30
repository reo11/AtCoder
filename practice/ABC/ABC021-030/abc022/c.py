import numpy as np
import scipy.sparse.csgraph as cs

N, M = map(int, input().split())
INF = 10**9
G = np.array([[INF]*N for i in range(N)])
H = []
for _ in range(M):
    u, v, l = map(int, input().split())
    if u == 1:
        H.append((v-1, l))
    else:
        G[u-1][v-1] = l
        G[v-1][u-1] = l

G = cs.floyd_warshall(G)

ans = INF
for i, h1 in enumerate(H[:len(H)-1]):
    for h2 in H[i+1:]:
        ans = min(ans, G[h1[0]][h2[0]]+h1[1]+h2[1])

if ans == INF:
    print(-1)
else:
    print(int(ans))
