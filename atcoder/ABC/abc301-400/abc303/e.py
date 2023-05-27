from collections import defaultdict, deque

n = int(input())
edges = defaultdict(lambda: set())
for i in range(n - 1):
    u, v = map(int, input().split())
    edges[u].add(v)
    edges[v].add(u)

q = deque([])
for edge, vs in edges.items():
    if len(vs) == 1:
        q.append(edge)

def delete_edge(u, v):
    edges[u].discard(v)
    edges[v].discard(u)

ans = []
# 次数から端を探して、その連結成分を星の中心と考えると良い
while True:
    # print(ans, q, edges)
    if len(q) > 0:
        v = q.popleft()
    else:
        count_multi_edge = 0
        for edge, vs in edges.items():
            if len(vs) == 1:
                q.append(edge)
            elif len(vs) > 1:
                count_multi_edge += 1

        if count_multi_edge == 0:
            break
        if len(q) == 0:
            break
        else:
            v = q.popleft()
    if len(edges[v]) == 0:
        continue
    center = list(edges[v])[0]
    center_edges = []
    for edge in edges[center]:
        center_edges.append(edge)
    if len(center_edges) <= 1:
        continue
    ans.append(len(center_edges))
    # 星の頂点として使用した分削除
    for u in center_edges:
        delete_edge(u, center)
        next_us = list(edges[u])
        for next_u in next_us:
            if len(edges[next_u]) <= 2:
                delete_edge(u, next_u)

ans.sort()
print(*ans, sep=" ")