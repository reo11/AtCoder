from heapq import heappush, heappop
inf = float('inf')
mod = 10**9 + 7

def dijkstra(start,ad):
    global dist, cnt
    N = len(ad)
    dist = [inf] * N
    dist[start] = 0
    cnt = [0] * N
    cnt[start] = 1
    pq = [(0,start)]
    while pq:
        dist_v, v = heappop(pq)
        for nv, nw in ad[v]:
            if dist[nv] > dist_v + nw:
                dist[nv] = dist_v + nw
                heappush(pq, (dist_v + nw, nv))
            if dist[nv] == dist_v + nw:
                cnt[nv] += cnt[v]
                cnt[nv] %= mod

N = int(input())
a, b = map(int,input().split())
a -= 1
b -= 1
M = int(input())
ad = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    ad[x].append((y, 1))
    ad[y].append((x, 1))

dijkstra(a, ad)
ans = cnt[b]
print(ans)
